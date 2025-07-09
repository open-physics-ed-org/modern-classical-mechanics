# RELEASE v0.9 (July 2025)

**Major Build System Overhaul & Unified Output**

This release brings a complete modernization of the build system, file organization, and web output for Modern Classical Mechanics. All update text was created with the help of Ollama.

## 🚀 Highlights

- **Unified Build System:**
  - New `--all` flag in `build.py` builds all formats (LaTeX, PDF, Markdown, DOCX) and then the HTML web output in one step.
  - `build.py --html` now delegates all web build logic to `build-web.py`, ensuring a single source of truth for web output.
  - All custom `--web`/`--html` logic removed from `build.py`.

- **Modern File/Folder Structure:**
  - All source notebooks are in `content/notebooks/`.
  - All outputs are organized in `_build/` (with subfolders for `html/`, `pdf/`, `docx/`, `latex/`, `md/`, and `images/`).
  - The final static website is in `docs/`, ready for GitHub Pages.
  - All downloadable sources (PDF, DOCX, MD, TEX, IPYNB) are available per notebook in `docs/sources/`.

- **Robust Web Output:**
  - All HTML, CSS, images, and assets are generated and copied to `docs/`.
  - Navigation menus, download links, and per-page assets are built from YAML and Markdown sources.
  - All admonitions, images, and YouTube thumbnails are handled robustly.

- **Documentation Overhaul:**
  - `build.md` fully rewritten to document the new build process, file organization, and best practices.
  - `README.md` updated to reflect the new workflow, file structure, and features.

- **Accessibility & Modernization:**
  - Modern, accessible navigation and color theming.
  - Robust dark/light mode and accessible download menus.
  - All outputs are WCAG-compliant and keyboard/screen-reader friendly.

## 🛠️ How to Upgrade

1. Pull the latest changes.
2. Review the new `build.md` and `README.md` for updated instructions.
3. Use `python build.py --all` to build everything, or `python build.py --html` for just the web output.
4. All outputs are now in `_build/` and `docs/`.

## ⚠️ Notes
- Some legacy files and scripts have been removed or replaced.
- If you have custom scripts, update them to use the new build workflow.
- All update text for this release was created with the help of Ollama.

---

*Thank you for using and contributing to Modern Classical Mechanics!*
