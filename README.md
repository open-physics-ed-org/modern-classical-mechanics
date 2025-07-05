<div align="center">

# 📚 Modern Classical Mechanics

**An open, free, and ever-evolving set of notes and resources for learning and teaching classical mechanics.**

<br>
<strong>Author:</strong> Danny Caballero  
<strong>Contact:</strong> caball14@msu.edu  
<strong>Michigan State University</strong>

![Build](https://img.shields.io/badge/build-passing-brightgreen) ![License: CC BY-NC 4.0](https://img.shields.io/badge/license-CC--BY--NC%204.0-blue)

</div>

---

## 🌐 About & Webpage

**Modern Classical Mechanics** is an open-source, interactive, and accessible static website and resource set for PHY 321: Classical Mechanics 1 at Michigan State University, authored by Marcos D. Caballero.

This project is not just a collection of Jupyter notebooks—it builds a fully static, accessible set of web pages from notebooks, with robust support for dark/light mode, accessible admonitions, and MathJax/LaTeX rendering. The site is designed for clarity, accessibility, and future extensibility.

**Built with custom Python scripts (not Jupyter Book)** to convert Jupyter notebooks into a static, accessible website and multiple downloadable formats.


---

## 🚧 Work in Progress: Major Site Modernization (2025)

This project is currently undergoing a major overhaul to modernize the navigation, accessibility, and download experience:

- **Modern, accessible navigation:**
  - Single horizontal menu with dropdowns for children, centered below the site title.
  - Responsive hamburger menu for mobile.
  - Fully accessible and keyboard-friendly.
  - Built at build time from `_menu.yml` (no client-side JS for menu data).
- **Robust light/dark mode:**
  - All backgrounds and borders are forced to white (light) or black (dark) for seamless appearance.
  - No white lines or borders in dark mode.
- **Minimal, reproducible spacing:**
  - All vertical gaps between nav and content are minimized and consistent.
- **Legacy code removed:**
  - All old side-nav/side-menu code is gone.
- **Planned:**
  - Per-page download menus for PDF, DOCX, Markdown, LaTeX, and Jupyter Notebook formats (see [issue #11](https://github.com/dannycab/modern-classical-mechanics/issues/11)).
  - Merge `build.py` and `build-web.py` into a single unified build script (see [issue #12](https://github.com/dannycab/modern-classical-mechanics/issues/12)).

**This is a work in progress!**

Some features and download links may be missing or incomplete as we continue to improve the site. Please [open an issue](https://github.com/dannycab/modern-classical-mechanics/issues) if you spot a bug or want to help.

---

- **Webpage:** [View the Book Online](https://dannycaballero.info/modern-classical-mechanics/)
- **GitHub Repo:** [github.com/dannycab/modern-classical-mechanics](https://github.com/dannycab/modern-classical-mechanics)
- **License:** CC BY-NC 4.0 (free for non-commercial use)
- **Contact:** caball14@msu.edu

All content is built from Jupyter notebooks and published automatically to the web. Contributions, issues, and pull requests are welcome!

---

## 🗂️ Project Structure (2025)

```
modern-classical-mechanics/
├── build.py              # Build script for PDF, DOCX, LaTeX, Markdown
├── build-web.py          # Build script for HTML website (docs/)
├── notebooks/            # Source Jupyter notebooks and images
│   ├── 01_notes.ipynb
│   ├── 02_notes.ipynb
│   ├── ...
│   └── images/
│       └── ...
├── static/
│   └── css/
│       └── book.css      # Custom CSS for the site
├── _build/
│   ├── html/             # HTML output (intermediate, not for deployment)
│   │   ├── images/
│   │   ├── css/
│   │   └── *.html
│   ├── pdf/              # PDF output
│   ├── docx/             # DOCX output
│   ├── latex/            # LaTeX output
│   └── md/               # Markdown output
│       └── images/
├── docs/                 # Final HTML website for GitHub Pages
│   ├── images/
│   ├── css/
│   └── *.html
└── .nojekyll             # Ensures GitHub Pages does not use Jekyll
```

---



## 🚀 Features (Current & Planned)

- **Static, accessible HTML site** built from Jupyter notebooks, with robust dark/light mode and accessible color theming.
- **Admonition support:** Converts all common admonition syntaxes (MyST, Markdown, code-fence, curly-brace, etc.) to accessible, visually distinct HTML blocks with LaTeX/MathJax support.
- **Image and YouTube handling:** Copies and renames all images, auto-fetches YouTube thumbnails, and ensures all references are correct in the static site.
- **Multiple output formats:**
  - HTML (website, in `docs/`)
  - PDF (`_build/pdf/`)
  - DOCX (`_build/docx/`)
  - LaTeX (`_build/latex/`)
  - Markdown (`_build/md/`)
  - Jupyter Notebook (.ipynb) (planned for direct download)
- **Automatic copying** of all outputs and assets to the `docs/` directory for GitHub Pages hosting.
- **Accessible design:** All HTML output is designed for screen readers and keyboard navigation.
- **Dark mode toggle** in the HTML output.

**In Progress:**
- Per-page download menus for all formats (PDF, DOCX, Markdown, LaTeX, ipynb)
- Unified build script for all outputs
- Further accessibility and navigation improvements

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
   python build.py --md --pdf --docx --latex
   python build-web.py
   ```
5. **View outputs:**
   - Website: `docs/index.html`
   - PDFs: `_build/pdf/`
   - DOCX: `_build/docx/`
   - LaTeX: `_build/latex/`
   - Markdown: `_build/md/`

---

## 🛠️ Admonition Syntax Supported

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

*Made with 🧑‍🔬, ☕, and a love for teaching physics.*

</div>
