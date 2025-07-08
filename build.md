# Build System

## Overview
This document describes the updated build system for the Modern Classical Mechanics project, including the new behavior of `build.py` and `build-web.py`. The build system is designed to generate all course materials (PDF, DOCX, Markdown, TeX, WCAG-compliant HTML, and Jupyter Book site) in a consistent, reproducible, and organized way.

The build system is meant to be more general-purpose, allowing for easy addition of new notebooks and formats. It supports both a unified build process and selective builds for individual formats or notebooks.


---

## Project Structure (Key Directories)

- **_build/**: All build outputs (not organized for direct publishing)
    - `docx/`   — DOCX files (one per notebook, if `build.py` used with `build --docx`)
    - `html/`   — Jupyter Book HTML site (a full unified build from the generated .autogen/_toc.yml, if `build.py` used with `build --jupyter`)
    - `images/` — All images referenced in notebooks/markdown (stored flat and with consistent paths, automatic,  `build.py --img`)
    - `md/`     — Markdown files (one per notebook, `build.py --md`)
    - `pdf/`    — PDF files (one per notebook, `build.py --pdf`)
    - `tex/`    — TeX files (one per notebook, `build.py --tex`)
    - `wcag-html/` — (`build.py --html`) WCAG-compliant HTML output
- **content/**: Source markdown, notebooks (**put materials here**)
- **docs/**: All published outputs for the website
    - WCAG-compliant HTML files for each page (dark and light mode).
    - `css/` - Styles for HTML
    - `images/` - Local flat image library for HTML
    - `sources/` — Contains a subfolder for each notebook stem, with all output formats for that notebook:
        - `<notebook_stem>/<notebook_stem>.md`
        - `<notebook_stem>/<notebook_stem>.docx`
        - `<notebook_stem>/<notebook_stem>.pdf`
        - `<notebook_stem>/<notebook_stem>.tex`
        - ...
    - `sources/jupyter/` — The full Jupyter Book HTML site
- **images/**: Source images for markdown and notebooks; used in automated builds (**put images here**)
- **log/**: Logs for build, can be reviewed
- **releases/:** Release information
- **scripts/:** Helper scripts for `build.py` and `build-web.py`
  - `debuggers` - Debugging scripts; not needed for production
- **static/**: HTML templates, CSS, JS, and themes
- **build.py**: Main build script for website and document converstion
- **build-web.py**: Web build script (subroutine for build.py, but can be called alone)

---

## Build Workflow

### 1. Building Everything: `python build.py --all`
This is the recommended way to build all outputs. It will:

1. **Build DOCX** (and Markdown): `python build.py --docx`
    - Converts each notebook to Markdown and DOCX.
    - Copies both `.md` and `.docx` to `docs/sources/<notebook_stem>/`.
    - **Build MD**: Converts each notebook to Markdown. Run by default. `build.py --md`
    - Copies `.md` to `docs/sources/<notebook_stem>/`.
2. **Build PDF**: `python build.py --pdf`
    - Converts each notebook to TeX and PDF.
    - Copies both `.tex` and `.pdf` to `docs/sources/<notebook_stem>/`.
    - **Build TeX**: Converts each notebook to TeX. Run by default. `build.py --tex`
    - Copies `.tex` to `docs/sources/<notebook_stem>/`.
3. **Build Jupyter Book HTML**: `python build.py --jupyter`
    - Builds the full Jupyter Book HTML site into `_build/html`.
    - Copies the site to `docs/jupyter/` and to `docs/sources/jupyterbook_html/`.
4. **Build WCAG-compliant HTML Web Output**: `python build.py --html`
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
images/      # All images referenced in `content/`
md/          # All .md files (one per notebook)
pdf/         # All .pdf files (one per notebook)
tex/         # All .tex files (one per notebook)
wcag-html/   # WCAG-compliant HTML (published web output)
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
- Jupyter Book HTML is built into a temp directory, then copied to `docs/jupyter/`.
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
