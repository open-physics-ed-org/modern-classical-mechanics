
# Build System Documentation

## Overview

This repository uses a modern, streamlined build system to generate all course outputs (HTML web site, PDFs, DOCX, Markdown, LaTeX, and images) from Jupyter notebooks and Markdown sources. The build process is designed to be robust, non-redundant, and easy to invoke.

## Key Build Scripts

- **build.py**: The main entry point for all builds. Handles PDF, DOCX, Markdown, LaTeX, and image collection. For HTML/web builds, it delegates to `build-web.py`.
- **build-web.py**: Contains all logic for building the HTML web site, including notebook conversion, menu generation, asset copying, and post-processing.


## Typical Usage

Run from the repository root:

```
python build.py --all            # Build everything: LaTeX, PDF, Markdown, DOCX, and HTML web site (docs/)
python build.py --html           # Build the full HTML web site (outputs to docs/)
python build.py --pdf            # Build PDFs for all notebooks
python build.py --md             # Build Markdown for all notebooks
python build.py --docx           # Build DOCX for all notebooks
python build.py --latex          # Build LaTeX for all notebooks
python build.py --img            # Collect all referenced images into _build/images/
```

You can also build specific notebooks with `--files`:

```
python build.py --html --files 01_notes.ipynb 02_notes.ipynb
```


## How the Build Works

- **All Formats (`--all`)**: `python build.py --all` builds all non-web formats first (LaTeX, PDF, Markdown, DOCX), then automatically builds the HTML/web output. This is the recommended way to build everything in one step.

- **HTML/Web Build**: `python build.py --html` simply calls `build-web.py --html`, which:
  - Converts all notebooks and Markdown pages to HTML using nbconvert and custom templates.
  - Builds navigation menus from `_menu.yml`.
  - Copies and organizes all images, CSS, and assets into sectioned folders.
  - Cleans up Jupyter/nbconvert markup for a polished web appearance.
  - Outputs all HTML and assets to `_build/html/` and then copies them to `docs/` for publishing (e.g., GitHub Pages).

- **PDF, DOCX, Markdown, LaTeX**: Handled directly by `build.py` using nbconvert and pandoc. Images are collected and flattened for each output type.

- **Image Collection**: `--img` scans all notebooks and Markdown for referenced images (including YouTube thumbnails) and copies them to `_build/images/`.

## File/Folder Organization

- `build.py`                — Main build script (all formats except HTML web)
- `build-web.py`            — All HTML/web build logic
- `notebooks/` or `content/notebooks/` — All Jupyter notebooks (source)
- `docs/`                   — Final HTML web site output (for GitHub Pages)
- `_build/`                 — All intermediate and final build outputs
    - `html/`               — HTML outputs (before copying to docs/)
    - `pdf/`                — PDF outputs
    - `docx/`               — DOCX outputs
    - `md/`                 — Markdown outputs
    - `latex/`              — LaTeX outputs
    - `images/`             — All collected images (flattened)
- `images/`                 — Project-wide images (source)
- `static/css/`             — CSS for the web site
- `_menu.yml`               — Navigation/menu structure
- `_notebooks.yaml`         — List of notebooks to build
- `_toc.yml`                — Jupyter Book table of contents (auto-generated)
- `README.md`               — Project overview
- `build.md`                — (This file) Build system documentation

## Best Practices

- **Single Source of Truth**: All web build logic is in `build-web.py`. Do not duplicate HTML/web logic in `build.py`.
- **Always Use `build.py`**: For consistency, always invoke builds via `build.py`.
- **Keep `_notebooks.yaml` Up to Date**: This file controls which notebooks are included in builds.
- **Do Not Edit `docs/` Directly**: All files in `docs/` are generated. Edit sources in `notebooks/`, `content/`, or `images/`.

## Publishing

The `docs/` folder is ready for static hosting (e.g., GitHub Pages). After running `python build.py --html`, simply push the repository to update the live site. 

**Make sure `.nojekyll` is present in `docs/` to prevent Jekyll processing; this is plain HTML and CSS, not Jekyll content.**

---
*Last updated: July 2025*
