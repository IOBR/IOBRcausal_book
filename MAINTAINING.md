# Maintaining the IOBRcausal Book

This repository contains the English tutorial. The R package and its Skill stay
in [IOBRcausal](https://github.com/IOBR/IOBRcausal). Like
[IOBRpy_book](https://github.com/IOBR/IOBRpy_book), it keeps tutorial chapters,
figures and publishing together in a separate repository.

## Build locally

Install Quarto 1.7.32 and Python 3.9 or later, then run from this directory:

```bash
quarto render . --no-execute
python tools/check_book.py
quarto preview . --no-browser
```

The output is `_book/index.html`. R, the IOBRcausal package, patient data and
access to the package repository are not required to build the documentation.
The displayed R examples use ordinary code fences and are never executed by
the documentation build. Running an analysis requires installing IOBRcausal.

## Edit a chapter

Edit the `.qmd` sources, then render the Book. The pre-render step verifies
bundled assets and refreshes `README.md` and the `github/` reading edition.
Commit the generated Markdown with its source changes. To refresh only the
GitHub edition, run `python tools/prepare_book.py`.

Keep the first task and expected output clear. Put detailed parameter lists in
the reference section. Preserve the eight method introductions, endpoint and
effect-scale distinctions, historical figure context and validation limits.

## Resources and provenance

`assets/` holds the original six PNGs, synthetic teaching data, downloadable
scripts and the method-support snapshot. `SOURCE_MANIFEST.json` records their
package paths, original SHA256, package version and source commit. The build
checks every file and the rendered copies. To update an asset, review the
upstream change and update its manifest entry in the same commit.

`MIGRATION.csv` maps the original 24 package articles and README sections to
their Book chapters. This inventory is checked locally without downloading
the package or its articles.

## Publish

The Book workflow builds and checks every push to `main`. Pull requests build
without deploying. Configure Settings -> Pages -> Source as **GitHub Actions**
once; successful main-branch builds then deploy the reviewed Book automatically.
The workflow can also be started manually from Actions.

The intended site is `https://iobr.github.io/IOBRcausal_book/`. Add an online
tutorial link to the reader-facing README only after that URL is verified.
An uploaded artifact is not a deployed website. Changing the package
repository's visibility is not needed for publishing this documentation.
