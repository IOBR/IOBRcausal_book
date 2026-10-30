"""Check bundled tutorial resources and refresh the GitHub reading edition.

This standalone Book never needs a package checkout, an R session or a network
download to build. Resource provenance is recorded in SOURCE_MANIFEST.json.
"""
from pathlib import Path
import hashlib
import json

ROOT = Path(__file__).resolve().parents[1]


def resource_sources():
    manifest = json.loads((ROOT / "SOURCE_MANIFEST.json").read_text(encoding="utf-8"))
    return {item["copy"]: item["source"] for item in manifest["resources"]}


def main():
    manifest = json.loads((ROOT / "SOURCE_MANIFEST.json").read_text(encoding="utf-8"))
    for item in manifest["resources"]:
        source = ROOT / item["source"]
        if not source.is_file() or hashlib.sha256(source.read_bytes()).hexdigest() != item["sha256"]:
            raise SystemExit("Missing or changed tutorial resource: " + item["source"])
    print(f"Book resources: {len(manifest['resources'])} bundled files verified.")
    from export_book import export_book
    export_book(resource_sources())


if __name__ == "__main__":
    main()
