
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

**Built with custom Python scripts (not Jupyter Book)** to convert Jupyter notebooks into a static, accessible website and multiple downloadable formats. *If you have suggestions for improvements or want to contribute, please [open an issue or pull request](https://github.com/dannycab/modern-classical-mechanics/issues).*

---

## 🗂️ Project Structure (2025)

```
modern-classical-mechanics/
├── build.py              # Main build script (PDF, DOCX, LaTeX, Markdown, HTML)
├── build-web.py          # All web/HTML build logic
├── content/
│   ├── notebooks/        # All Jupyter notebooks (source)
│   ├── about.md
│   ├── activities.md
│   ├── announcement.md
│   ├── cards.md
│   ├── index.md
│   ├── resources.md
│   └── images/
├── static/
│   ├── css/
│   │   ├── main.css      # Main CSS for the site
│   │   └── card-link.css
│   ├── html_template.html
│   └── js/
├── _build/
│   ├── html/             # HTML output (intermediate, not for deployment)
│   ├── pdf/              # PDF output
│   ├── docx/             # DOCX output
│   ├── latex/            # LaTeX output
│   ├── md/               # Markdown output
│   └── images/           # All collected images (flattened)
├── docs/                 # Final HTML website for GitHub Pages
│   ├── *.html
│   ├── css/
│   │   └── main.css
│   ├── images/
│   │   ├── chapters/
│   │   └── activities/
│   └── sources/
│       ├── 01_notes/
│       │   ├── 01_notes.ipynb
│       │   ├── 01_notes.md
│       │   ├── 01_notes.tex
│       │   ├── 01_notes.docx
│       │   └── 01_notes.pdf
│       └── ... (all chapters and homeworks)
├── .nojekyll             # Ensures GitHub Pages does not use Jekyll
├── _menu.yml             # Navigation/menu structure
├── _notebooks.yaml       # List of notebooks to build
├── _toc.yml              # Jupyter Book table of contents (auto-generated)
├── requirements.txt      # Python dependencies
├── LICENSE
├── README.md
├── build.md              # Build system documentation
└── releases/             # Release notes
```

---


## 📖 Build System & Markup Documentation

- See [build.md](build.md) for detailed, step-by-step documentation of the build system, including how `build.py` and `build-web.py` work, troubleshooting, and best practices.
- See [jupyter-markup-tips.md](jupyter-markup-tips.md) for tips and best practices on writing Markdown, LaTeX, images, links, and admonitions in Jupyter Notebooks.

---

## 🚀 Features (Current & Planned)

- **Unified build system:** One command (`python build.py --all`) builds all outputs (LaTeX, PDF, Markdown, DOCX, HTML web site).
- **Static, accessible HTML site** built from Jupyter notebooks, with robust dark/light mode and accessible color theming.
- **Admonition support:** Converts all common admonition syntaxes (MyST, Markdown, code-fence, curly-brace, etc.) to accessible, visually distinct HTML blocks with LaTeX/MathJax support.
- **Image and YouTube handling:** Copies and renames all images, auto-fetches YouTube thumbnails, and ensures all references are correct in the static site.
- **Multiple output formats:**
  - HTML (website, in `docs/`)
  - PDF (`_build/pdf/`)
  - DOCX (`_build/docx/`)
  - LaTeX (`_build/latex/`)
  - Markdown (`_build/md/`)
  - Jupyter Notebook (.ipynb) (for download)
- **Automatic copying** of all outputs and assets to the `docs/` directory for GitHub Pages hosting.
- **Accessible design:** All HTML output is designed for screen readers and keyboard navigation.
- **Dark mode toggle** in the HTML output.

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
   - PDFs: `_build/pdf/`
   - DOCX: `_build/docx/`
   - LaTeX: `_build/latex/`
   - Markdown: `_build/md/`

---

## 📂 Build Outputs

- All notebooks listed in `_notebooks.yaml` are converted to LaTeX, PDF, Markdown, DOCX, and Jupyter Notebook formats.
- Downloadable sources are available for each notebook on the course site.
- **PDF generation is currently being improved.** Some PDFs may be missing or incomplete if LaTeX errors occur (e.g., missing images). All other formats are complete.

---


## 🛠️ Jupyter Markup & Admonition Syntax

See [jupyter-markup-tips.md](jupyter-markup-tips.md) for a full guide.

- `::: tip [Title]` ... `:::`
- `!!! warning [Title]` (with indented content)
- `{admonition} note [Title]` ... `{/admonition}`
- `{tip}` ... `{/tip}` (single-line)
- Code-fence style:
  ```
  ```{tip} Optional Title
  Content here
  ```
  ```

---

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

*This README and the v0.9 release notes were created with the help of Ollama.*

</div>
