# 📚 Modern Classical Mechanics

**An open, free, and ever-evolving set of notes and resources for learning and teaching classical mechanics.**

<div align="center">
<strong>Developer:</strong> Danny Caballero<br>
<strong>Contact:</strong> caball14@msu.edu<br>
<strong>Michigan State University</strong><br>
</div>

![Build](https://img.shields.io/badge/build-passing-brightgreen) 
![License: CC BY-NC 4.0](https://img.shields.io/badge/license-CC--BY--NC%204.0-blue)
---

## 🌐 About & Webpage

**Modern Classical Mechanics** is an open-source, interactive, and accessible static website and resource set for Classical Mechanics 1 at Michigan State University. It is principally authored by Danny Caballero, but with contributions from many others in the physics education community.

This project is not just a collection of Jupyter notebooks—it builds a fully static, accessible set of web pages from notebooks, with robust support for dark/light mode, accessible admonitions, and MathJax/LaTeX rendering. The site is designed for clarity, accessibility, and future extensibility.

**Built with custom Python scripts and Jupyter Book** to convert Jupyter notebooks into a static, accessible website and multiple downloadable formats. *If you have suggestions for improvements or want to contribute, please [open an issue or pull request](https://github.com/dannycab/modern-classical-mechanics/issues).*

---

## 🏗️ Project Organization & Build Outputs

### Key Directories

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

## 🚀 Features

- Unified build system: one command builds all outputs (LaTeX, PDF, Markdown, DOCX, HTML web site, Jupyter Book site)
- Static, accessible HTML site with robust YAML-driven dark/light mode and accessible, WCAG AAA-compliant color theming
- Admonition support for notes, tips, warnings, etc.
- Image and YouTube handling
- Multiple output formats: HTML, PDF, DOCX, LaTeX, Markdown, Jupyter Notebook
- Automatic copying of all outputs and assets to the `docs/` directory for GitHub Pages hosting
- Accessible design: all HTML output is designed for screen readers and keyboard navigation
- Dark/light mode toggle in the HTML output, with instant switching and full content coverage

---

## 🏗️ How to Build Locally

1. **Clone the repo:**
   ```sh
   git clone https://github.com/dannycab/modern-classical-mechanics.git
   cd modern-classical-mechanics
   ```
2. **Set up Python environment:**
   ```sh
   python3 -m venv .venv
   source .venv/bin/activate
   pip install -r requirements.txt
   ```
3. **Install Jupyter and Pandoc:**
   - Jupyter: `pip install jupyter nbconvert`
   - Pandoc: [Install from pandoc.org](https://pandoc.org/installing.html)
4. **Build all outputs:**
   ```sh
   python build.py --all
   ```
   Or build just the web output:
   ```sh
   python build.py --html
   ```
5. **View outputs:**
   - Website: `docs/index.html`
   - PDFs, DOCX, Markdown, TeX: see `docs/sources/<notebook_stem>/`
   - Jupyter Book HTML: `docs/jupyter/` and `docs/sources/jupyterbook_html/`
   - Theme CSS: `static/css/theme-light.css`, `static/css/theme-dark.css` (auto-generated)

---

## ⚙️ Build System Details

See [build.md](build.md) for a full description of the build system, output directory structure, and advanced usage.

### Build Everything
- `python build.py --all` — Runs all build steps in order:
    1. DOCX (and Markdown)
    2. PDF (and TeX)
    3. Jupyter Book HTML (unified site)
    4. Custom HTML web output (via build-web.py)

### Build Individual Formats
- `python build.py --docx` — Only build DOCX (and Markdown) for all notebooks.
- `python build.py --pdf` — Only build PDF (and TeX) for all notebooks.
- `python build.py --jupyter` — Only build the unified Jupyter Book HTML site.
- `python build.py --html` — Only build the custom HTML web output (calls `build-web.py`).
- `python build.py --md` — Only build Markdown for all notebooks.
- `python build.py --tex` — Only build TeX for all notebooks.
- `python build.py --img` — Collect all referenced images into `_build/images/`.
- Use `--files <notebook1> <notebook2> ...` to build only specific notebooks.

---

## 📂 Build Outputs

- All notebooks listed in `_notebooks.yaml` are converted to LaTeX, PDF, Markdown, DOCX, and Jupyter Notebook formats.
- Downloadable sources are available for each notebook on the course site in `docs/sources/<notebook_stem>/`.
- The full Jupyter Book HTML site is available in `docs/jupyter/` and `docs/sources/jupyterbook_html/`.
- All referenced images are collected into `_build/images/`.
- **PDF generation is robust, but may fail if LaTeX errors occur (e.g., missing images).**

---

## 🎨 Theming & Accessibility

YAML-driven, accessible theming for both light and dark modes. All official themes are WCAG AAA-compliant. See `static/themes/` for available themes and [build.md](build.md) for details on how to select or create your own.

**Quick usage:**
Edit `_config.yml`:
```yaml
theme:
  light: clarity_light   # or any available theme name
  dark: clarity_dark
  default: clarity_dark
```
Only two CSS files are used: `theme-light.css` and `theme-dark.css` (auto-generated).

For a full list of themes and advanced options, see [build.md](build.md).

---

## 🛠️ Jupyter Markup & Admonition Syntax

See [jupyter-markup-tips.md](jupyter-markup-tips.md) for a full guide.


## 🖼️ Images & YouTube Handling

- All images referenced in notebooks are copied and renamed for uniqueness.
- YouTube thumbnails are auto-downloaded if referenced by video ID or thumbnail URL.

---

## 🤖 Automated Builds (CI/CD)

- GitHub Actions automatically build the book and website on every push.
- All assets (notebooks, images, outputs) are kept in sync.
- Want to help improve the workflow? [Open an issue](https://github.com/dannycab/modern-classical-mechanics/issues) or [send a pull request](https://github.com/dannycab/modern-classical-mechanics/pulls)!

---

## 📝 License

This book and all its content are licensed under [Creative Commons Attribution-NonCommercial 4.0 International (CC BY-NC 4.0)](https://creativecommons.org/licenses/by-nc/4.0/).

- **You are free to:** Share, adapt, and remix for non-commercial purposes, with attribution.
- **You may not:** Use for commercial purposes without permission.

See [LICENSE](LICENSE) for details.

---

## 💡 Contributing

**Everyone is welcome!**

- Found a typo? Have a suggestion? [Open an issue](https://github.com/dannycab/modern-classical-mechanics/issues)!
- Want to add a new example, fix a bug, or improve the build? [Send a pull request](https://github.com/dannycab/modern-classical-mechanics/pulls)!
- New to open source? Check out our [contributing guide](CONTRIBUTING.md) (coming soon) or just ask a question in the issues.

Let's make physics education better, together! 🚀

---

<div align="center">

*This README and the v0.9.2 release notes were created with the help of Ollama.*

</div>
