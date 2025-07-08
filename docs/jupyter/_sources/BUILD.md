# Modern Classical Mechanics Build System

## Overview
This document describes the updated build system for the Modern Classical Mechanics project, including the new behavior of `build.py` and `build-web.py`. The build system is designed to generate all course materials (PDF, DOCX, Markdown, TeX, HTML, and Jupyter Book site) in a consistent, reproducible, and organized way.

---

## Project Structure (Key Directories)

- **_build/**: All intermediate and final build outputs (not for direct publishing)
    - `docx/`   — DOCX files (one per notebook)
    - `html/`   — Jupyter Book HTML site (temporary, unified build)
    - `images/` — All images referenced in notebooks/markdown
    - `latex/`  — (if used) LaTeX build artifacts
    - `md/`     — Markdown files (one per notebook)
    - `pdf/`    — PDF files (one per notebook)
    - `tex/`    — TeX files (one per notebook)
    - `wcag-html/` — (if used) Accessibility HTML
- **docs/**: All published outputs for the website
    - HTML files for each chapter, homework, etc.
    - `css/`, `images/`, `sources/` (see below)
    - `sources/` — Contains a subfolder for each notebook stem, with all output formats for that notebook:
        - `<notebook_stem>/<notebook_stem>.md`
        - `<notebook_stem>/<notebook_stem>.docx`
        - `<notebook_stem>/<notebook_stem>.pdf`
        - `<notebook_stem>/<notebook_stem>.tex`
        - ...
    - `sources/jupyterbook_html/` — The full Jupyter Book HTML site
- **content/**: Source markdown, notebooks, and images
- **static/**: HTML templates, CSS, JS, and themes
- **build.py**: Main build script
- **build-web.py**: Custom web build script

---

## Build Workflow

### 1. Building Everything: `python build.py --all`
This is the recommended way to build all outputs. It will:

1. **Build DOCX** (and Markdown):
    - Converts each notebook to Markdown and DOCX.
    - Copies both `.md` and `.docx` to `docs/sources/<notebook_stem>/`.
2. **Build PDF**:
    - Converts each notebook to TeX and PDF.
    - Copies both `.tex` and `.pdf` to `docs/sources/<notebook_stem>/`.
3. **Build Jupyter Book HTML**:
    - Builds the full Jupyter Book HTML site into `_build/html`.
    - Copies the site to `docs/jupyter/` and to `docs/sources/jupyterbook_html/`.
4. **Build Custom HTML Web Output**:
    - Runs `build-web.py` to generate the custom website in `docs/`.

All steps are run in the correct order to ensure dependencies are satisfied (e.g., Markdown is always built before DOCX).

### 2. Building Individual Formats
- `python build.py --docx` — Only build DOCX (and Markdown) for all notebooks.
- `python build.py --pdf` — Only build PDF (and TeX) for all notebooks.
- `python build.py --jupyter` — Only build the unified Jupyter Book HTML site.
- `python build.py --html` — Only build the custom HTML web output (calls `build-web.py`).
- `python build.py --md` — Only build Markdown for all notebooks.
- `python build.py --tex` — Only build TeX for all notebooks.
- `python build.py --img` — Collect all referenced images into `_build/images/`.

### 3. Selective Builds
- Use `--files <notebook1> <notebook2> ...` to build only specific notebooks.

---

## Output Directory Details

### _build/
```
docx/        # All .docx files (one per notebook)
html/        # Jupyter Book HTML site (temporary, unified build)
images/      # All images referenced in notebooks/markdown
latex/       # (if used) LaTeX build artifacts
md/          # All .md files (one per notebook)
pdf/         # All .pdf files (one per notebook)
tex/         # All .tex files (one per notebook)
wcag-html/   # (if used) Accessibility HTML
```

### docs/
```
01_notes.html   01_start.html   ...   index.html   ...
css/           images/         sources/
  sources/
    <notebook_stem>/
      <notebook_stem>.md
      <notebook_stem>.docx
      <notebook_stem>.pdf
      <notebook_stem>.tex
    jupyterbook_html/
      (full Jupyter Book HTML site)
```

### Project Root
```
_config.yml   _menu.yml   _notebooks.yaml   _toc.yml
basic_yaml2json.py   build-web.py   build.py   ...
content/   docs/   static/   _build/   ...
```

---

## Notable Features & Updates

- **--all** now runs: DOCX (and Markdown) → PDF → Jupyter Book HTML → Custom HTML web output, in that order.
- All output formats are copied to `docs/sources/<notebook_stem>/` for each notebook.
- Markdown is always built before DOCX (DOCX is generated from Markdown).
- Jupyter Book HTML is built into a temp directory, then copied to both `docs/jupyter/` and `docs/sources/jupyterbook_html/`.
- `build-web.py` is always called last in the `--all` workflow.
- All referenced images are collected into `_build/images/`.
- No automatic cleanup of `_build/` or `docs/` directories—manual cleanup is recommended if needed.

---

## Example Usage

- Build everything:
  ```sh
  python build.py --all
  ```
- Build only PDFs:
  ```sh
  python build.py --pdf
  ```
- Build only DOCX for a specific notebook:
  ```sh
  python build.py --docx --files content/notebooks/01_notes.ipynb
  ```

---

## Troubleshooting
- If you see missing images in outputs, try running with `--img` or ensure all image paths are correct.
- If you add new notebooks, update `_notebooks.yaml` and re-run the build.
- For custom web output, edit `build-web.py` and re-run with `--html` or `--all`.

---

## See Also
- `README.md` for project overview
- `requirements.txt` for dependencies
- `build-web.py` for custom web build logic
- Jupyter Book documentation: https://jupyterbook.org/
