# Build System Documentation

This document describes in detail the build system for the Modern Classical Mechanics project, focusing on the two main scripts: `build.py` and `build-web.py`.

---

## `build.py` — The Main Build Script

### Purpose
`build.py` is the primary build automation script for generating all course outputs from Jupyter notebooks. It supports building LaTeX, PDF, Markdown, and DOCX files, and generates the `_toc.yml` for Jupyter Book. It is designed to be robust, reproducible, and non-destructive to source notebooks.

### Usage
```sh
python build.py [--pdf] [--md] [--docx] [--latex] [--html] [--files ...]
```
- If no flags are given, all formats except HTML are built.
- `--files` allows building a subset of notebooks.

### Key Features
- **Reads notebook list** from `_notebooks.yaml` (or `--files` argument)
- **Never modifies source notebooks**
- **Copies all local images** referenced in Markdown to `_build/md/images` and updates links
- **Builds LaTeX** using `jupyter nbconvert --to latex`
- **Builds PDF** using `jupyter nbconvert --to pdf`
- **Builds Markdown** using `jupyter nbconvert --to markdown`
- **Builds DOCX** from Markdown using Pandoc
- **Generates `_toc.yml`** for Jupyter Book
- **Cleans up** `_build/` directory, keeping only output folders
- **Logs** all output to `log/build.log`

### Detailed Workflow
1. **Argument Parsing**
   - Determines which formats to build based on CLI flags.
2. **Notebook List**
   - Reads from `_notebooks.yaml` or `--files`.
3. **LaTeX Build**
   - Converts each notebook to LaTeX (`.tex`) in `_build/latex`.
4. **PDF Build**
   - Converts each notebook to PDF in `_build/pdf`.
5. **Markdown Build**
   - Converts each notebook to Markdown in `_build/md`.
   - Copies all local images referenced in Markdown to `_build/md/images`.
   - Updates all image links in Markdown to point to the copied images.
6. **DOCX Build**
   - Converts each Markdown file to DOCX using Pandoc, with resource path set to `_build/md` and `_build/md/images`.
7. **TOC Generation**
   - Always generates `_toc.yml` from `_notebooks.yaml`.
8. **Cleanup**
   - Removes all folders in `_build` except `latex`, `html`, `md`, `docx`, `pdf`.
9. **Logging**
   - All output and errors are logged to `log/build.log`.

### Notes
- **HTML build is currently disabled.**
- **Remote images are not fetched or rewritten.**
- **Notebooks are never altered.**

---

## `build-web.py` — Web Build Script

### Purpose
`build-web.py` is a specialized script for building the web version of the course site. It is typically used to generate the HTML site for deployment.

### Usage
```sh
python build-web.py
```

### Key Features
- **Builds the HTML site** using Jupyter Book or a custom workflow
- **Updates navigation** and menu files as needed
- **May call `build.py`** as a subprocess to ensure all outputs are up to date
- **Copies static assets** (CSS, JS, images) to the appropriate locations in the web build
- **Handles web-specific configuration** (e.g., custom navigation, menus)

### Typical Workflow
1. **Update Navigation/Menu**
   - Regenerates or updates navigation files (e.g., `_menu.yml`, `menu.json`).
2. **Build HTML**
   - Runs Jupyter Book build or custom HTML build process.
3. **Copy Static Assets**
   - Ensures all CSS, JS, and image files are present in the web output directory.
4. **Post-processing**
   - May perform additional steps such as fixing links, updating metadata, or cleaning up temporary files.

### Notes
- `build-web.py` is intended for web deployment and may be customized for the course's specific needs.
- It is often run after `build.py` to ensure all source outputs are current.

---

## Output Directory Structure
- `_build/latex/` — LaTeX files (`.tex`)
- `_build/pdf/` — PDF files (`.pdf`)
- `_build/md/` — Markdown files (`.md`)
- `_build/md/images/` — Images referenced in Markdown
- `_build/docx/` — DOCX files (`.docx`)
- `_build/html/` — HTML site (if enabled)

---

## Best Practices
- Always run `build.py` before `build-web.py` to ensure all outputs are up to date.
- Never edit files in `_build/` directly; always edit source notebooks or configuration files.
- Check `log/build.log` for build errors or warnings.
- Use version control to track changes to build scripts and configuration files.

---

## Troubleshooting
- **Missing images in Markdown/DOCX:** Ensure figures are present in notebook outputs before building.
- **Build errors:** Check `log/build.log` for details.
- **PDF/LaTeX errors:** Review `.tex` files and LaTeX logs in `_build/latex`.

---

For further details, see comments in the scripts or contact the course maintainers.
