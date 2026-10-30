"""Validate the rendered English Book using the Python standard library."""
from pathlib import Path
from html.parser import HTMLParser
from urllib.parse import unquote, urlsplit
import csv
import hashlib
import json
import re

ROOT = Path(__file__).resolve().parents[1]
BOOK = ROOT
OUTPUT = BOOK / "_book"


class Page(HTMLParser):
    def __init__(self, text):
        super().__init__(convert_charrefs=True)
        self.ids = set()
        self.links = []
        self.feed(text)

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if attrs.get("id"):
            self.ids.add(attrs["id"])
        key = "href" if tag in {"a", "link"} else "src"
        if tag in {"a", "link", "img", "script", "source", "iframe"} and attrs.get(key):
            self.links.append(attrs[key])


def main():
    errors = []
    from export_book import export_book
    from prepare_book import resource_sources
    export_book(resource_sources(), check=True)
    pages = {}
    qmds = sorted(BOOK.rglob("*.qmd"))
    navigation = re.findall(r"^\s*-\s+([^\s#]+\.qmd)\s*$",
                            (BOOK / "_quarto.yml").read_text(encoding="utf-8"), re.M)
    source_names = {p.relative_to(BOOK).as_posix() for p in qmds}
    if set(navigation) != source_names or len(navigation) != len(source_names):
        errors.append("Chapter navigation does not match all Book source pages.")
    for source in qmds:
        text = source.read_text(encoding="utf-8")
        if re.search(r"[\u3400-\u9fff]", text):
            errors.append(f"Non-English text in {source.relative_to(BOOK)}")
        if re.search(r"^```\{(?:r|python)", text, re.M):
            errors.append(f"Executable code fence in {source.relative_to(BOOK)}")
        target = OUTPUT / source.relative_to(BOOK).with_suffix(".html")
        if not target.is_file():
            errors.append(f"Missing rendered page: {target.relative_to(BOOK)}")
        else:
            rendered = target.read_text(encoding="utf-8")
            if re.search(r"[\u3400-\u9fff]", rendered):
                errors.append(f"Non-English text in rendered {target.relative_to(OUTPUT)}")
            pages[target.resolve()] = Page(rendered)
    local_links = 0
    for path, page in list(pages.items()):
        for href in page.links:
            url = urlsplit(href)
            if url.scheme or url.netloc:
                continue
            destination = (OUTPUT / unquote(url.path).lstrip("/") if url.path.startswith("/")
                           else path.parent / unquote(url.path)) if url.path else path
            if destination.is_dir():
                destination = destination / "index.html"
            destination = destination.resolve()
            if not destination.is_file():
                errors.append(f"Broken local link: {path.relative_to(OUTPUT)} -> {href}")
                continue
            local_links += 1
            if url.fragment and destination.suffix == ".html":
                if destination not in pages:
                    pages[destination] = Page(destination.read_text(encoding="utf-8"))
                fragment = unquote(url.fragment)
                if fragment != "top" and fragment not in pages[destination].ids:
                    errors.append(f"Broken anchor: {path.relative_to(OUTPUT)} -> {href}")
    provenance = json.loads((ROOT / "SOURCE_MANIFEST.json").read_text(encoding="utf-8"))
    manifest = provenance["resources"]
    image_count = 0
    for record in manifest:
        source = ROOT / record["source"]
        for target in (BOOK / "assets" / record["copy"], OUTPUT / "assets" / record["copy"]):
            if not target.is_file() or hashlib.sha256(target.read_bytes()).hexdigest() != record["sha256"]:
                errors.append(f"Missing or changed resource: {target}")
        if hashlib.sha256(source.read_bytes()).hexdigest() != record["sha256"]:
            errors.append(f"Changed original resource: {source}")
        image_count += source.suffix == ".png"
    with (BOOK / "MIGRATION.csv").open(encoding="utf-8", newline="") as stream:
        migrations = list(csv.DictReader(stream))
    mapped_articles = {row["source"] for row in migrations if row["source"].endswith(".Rmd")}
    current_articles = set(provenance["original_articles"])
    if mapped_articles != current_articles:
        errors.append("Migration coverage does not match the complete article set.")
    for row in migrations:
        for target in row["book_pages"].split(";"):
            if not (BOOK / target).is_file():
                errors.append(f"Missing migration destination: {target}")
    markdown_pages = [BOOK / "README.md", *sorted((BOOK / "github").rglob("*.md"))]
    markdown_links = 0
    for page in markdown_pages:
        text = page.read_text(encoding="utf-8")
        if re.search(r"[\u3400-\u9fff]", text):
            errors.append(f"Non-English GitHub chapter: {page.relative_to(ROOT)}")
        for target in re.findall(r"!?\[[^\]]*\]\(([^\n)]+)\)", text):
            url = urlsplit(target)
            if url.scheme or url.netloc:
                continue
            destination = (page.parent / unquote(url.path)).resolve() if url.path else page
            if not destination.is_file():
                errors.append(f"Broken GitHub chapter link: {page.relative_to(ROOT)} -> {target}")
            else:
                markdown_links += 1
                if url.fragment and destination.suffix == ".md":
                    headings = re.findall(r"^#{1,6}\s+(.+)$", destination.read_text(encoding="utf-8"), re.M)
                    anchors = {re.sub(r"[^\w\s-]", "", heading.lower()).replace(" ", "-") for heading in headings}
                    if unquote(url.fragment) not in anchors:
                        errors.append(f"Broken GitHub chapter anchor: {page.relative_to(ROOT)} -> {target}")
    print(json.dumps({"pages": len(qmds), "local_links_checked": local_links,
                      "github_markdown_pages": len(markdown_pages),
                      "github_markdown_links_checked": markdown_links,
                      "original_pngs": image_count, "articles_mapped": len(mapped_articles),
                      "errors": errors}, indent=2))
    if errors:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
