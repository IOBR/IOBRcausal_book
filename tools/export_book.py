"""Export the maintained Quarto chapters as directly readable GitHub Markdown.

QMD remains the editable source. This exporter rewrites chapter/resource links,
removes layout-only div markers and adds contents/previous/next navigation.
"""
from pathlib import Path
from urllib.parse import urlsplit, unquote
import argparse
import os
import re

ROOT = Path(__file__).resolve().parents[1]
BOOK = ROOT
GITHUB = BOOK / "github"


def chapter_title(source):
    match = re.search(r"^title:\s*(.+)$", source.read_text(encoding="utf-8"), re.M)
    if not match:
        raise ValueError(f"Missing title: {source}")
    return match.group(1).strip().strip('"\'')


def export_book(sources, check=False):
    config = (BOOK / "_quarto.yml").read_text(encoding="utf-8")
    chapters = re.findall(r"^\s*-\s+([^\s#]+\.qmd)\s*$", config, re.M)
    titles = {name: chapter_title(BOOK / name) for name in chapters}
    asset_targets = {(BOOK / "assets" / name).resolve(): (ROOT / path).resolve()
                     for name, path in sources.items()}
    outputs = {}

    for index, name in enumerate(chapters):
        source = BOOK / name
        destination = GITHUB / Path(name).with_suffix(".md")
        body = source.read_text(encoding="utf-8")
        body = re.sub(r"\A---\s*\n.*?\n---\s*\n", "", body, count=1, flags=re.S)
        body = re.sub(r"^:::.*\n?", "", body, flags=re.M)
        lines = []
        in_code = False
        for line in body.splitlines():
            if line.startswith("```"):
                in_code = not in_code
            if not in_code and re.match(r"^# (?!#)", line):
                line = "#" + line
            lines.append(line)
        body = "\n".join(lines)

        def rewrite(match):
            target = match.group(2)
            url = urlsplit(target)
            if url.scheme or url.netloc or not url.path:
                return match.group(0)
            resolved = (source.parent / unquote(url.path)).resolve()
            if resolved.suffix == ".qmd":
                resolved = GITHUB / resolved.relative_to(BOOK).with_suffix(".md")
            else:
                resolved = asset_targets.get(resolved, resolved)
            relative = Path(os.path.relpath(resolved, destination.parent)).as_posix()
            suffix = ("?" + url.query if url.query else "") + ("#" + url.fragment if url.fragment else "")
            return match.group(1) + relative + suffix + match.group(3)

        body = re.sub(r"(!?\[[^\]]*\]\()([^\n)]+)(\))", rewrite, body)
        navigation = ["[Book contents](" + Path(os.path.relpath(BOOK / "README.md", destination.parent)).as_posix() + ")"]
        for other, label in ((index - 1, "Previous"), (index + 1, "Next")):
            if 0 <= other < len(chapters):
                path = GITHUB / Path(chapters[other]).with_suffix(".md")
                href = Path(os.path.relpath(path, destination.parent)).as_posix()
                navigation.append(f"[{label}: {titles[chapters[other]]}]({href})")
        nav = " · ".join(navigation)
        text = (f"<!-- Generated from {name}. Edit the QMD source and rebuild. -->\n\n"
                f"# {titles[name]}\n\n{nav}\n\n{body.strip()}\n\n---\n\n{nav}\n")
        outputs[destination] = text

    contents = ["# IOBRcausal Book", "",
                "Practical English tutorials for installing IOBRcausal, running an analysis and reading the results.", "",
                "- Online tutorial: [IOBRcausal Book](https://iobr.github.io/IOBRcausal_book/)",
                "- Tutorial source: [IOBRcausal_book](https://github.com/IOBR/IOBRcausal_book)",
                "- Read on GitHub: [Contents](github/index.md)",
                "- R package and Skill: [IOBRcausal](https://github.com/IOBR/IOBRcausal)",
                "- Report issues: [IOBRcausal issues](https://github.com/IOBR/IOBRcausal/issues)", "",
                "**Start here:** [Install](github/installation.md) · [First analysis](github/quick-start.md) · "
                "[Use your data](github/data-preparation.md) · [Read saved results](github/workflows/saved-results.md)", "",
                "Use the chapter links above without installing any documentation tools.", "",
                "For contributors: see [MAINTAINING.md](MAINTAINING.md) to build and publish the Book.", ""]
    outputs[BOOK / "README.md"] = "\n".join(contents)
    contents = ["## All chapters", ""]
    for line in config.splitlines():
        part = re.match(r"\s*-\s+part:\s*(.+)$", line)
        chapter = re.match(r"\s*-\s+([^\s#]+\.qmd)\s*$", line)
        if part:
            contents.extend(["", "## " + part.group(1), ""])
        elif line.strip() == "appendices:":
            contents.extend(["", "## Appendix", ""])
        elif chapter:
            name = chapter.group(1)
            contents.append(f"- [{titles[name]}](github/{Path(name).with_suffix('.md').as_posix()})")
        elif line.strip() == "lang: en":
            break
    # The full contents live with the introductory chapter, keeping README short.
    contents_text = "\n".join(contents).replace(
        "](github/", "](")
    outputs[GITHUB / "index.md"] += "\n" + contents_text + "\n"
    stale = []
    for path, text in outputs.items():
        if check:
            if not path.is_file() or path.read_text(encoding="utf-8") != text:
                stale.append(path.relative_to(ROOT).as_posix())
        else:
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_text(text, encoding="utf-8")
    if stale:
        raise SystemExit("GitHub Book is missing or stale: " + ", ".join(stale))
    print(f"GitHub Book: {len(chapters)} readable chapters and a contents page {'checked' if check else 'exported'}.")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true")
    options = parser.parse_args()
    from prepare_book import resource_sources
    export_book(resource_sources(), check=options.check)
