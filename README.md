<!--
RELEASE v0.7 "Robust Routhian" (July 2025)
See [RELEASE-v0.7.md](RELEASE-v0.7.md) for details.

- Robust image handling in Markdown build: all images referenced in notebooks are reliably copied to _build/md/images and all image links in Markdown are rewritten to point to the copied images.
- No source notebook changes required; all fixes are post-processing only.
- Closes issues #11 and #12 (per-page download menus and unified build script improvements).
-->

<div align="center">

# 📚 Modern Classical Mechanics

**An open, free, and ever-evolving set of notes and resources for learning and teaching classical mechanics.**

<br>
<strong>Author:</strong> Danny Caballero<br>
<strong>Contact:</strong> caball14@msu.edu<br>
<strong>Michigan State University</strong>

![Build](https://img.shields.io/badge/build-passing-brightgreen) ![License: CC BY-NC 4.0](https://img.shields.io/badge/license-CC--BY--NC%204.0-blue)

</div>

---

## 🌐 About & Webpage

**Modern Classical Mechanics** is an open-source, interactive, and accessible static website and resource set for Classical Mechanics 1 at Michigan State University. It is principally authored by Danny Caballero, but with contributions from many others in the physics education community.

This project is not just a collection of Jupyter notebooks—it builds a fully static, accessible set of web pages from notebooks, with robust support for dark/light mode, accessible admonitions, and MathJax/LaTeX rendering. The site is designed for clarity, accessibility, and future extensibility.

**Built with custom Python scripts (not Jupyter Book)** to convert Jupyter notebooks into a static, accessible website and multiple downloadable formats. *If you have suggestions for improvements or want to contribute, please [open an issue or pull request](https://github.com/dannycab/modern-classical-mechanics/issues).*


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


**Planned / Open Issues:**

- [Integrate activities into the book (#7)](https://github.com/dannycab/modern-classical-mechanics/issues/7) <br>
  <sub>Labels: bug, enhancement, build, activities</sub>
- [Write an instructional guide for teachers (#8)](https://github.com/dannycab/modern-classical-mechanics/issues/8) <br>
  <sub>Labels: documentation, enhancement, teaching-guide</sub>
- [Mobile menu usability and dark mode issues (#15)](https://github.com/dannycab/modern-classical-mechanics/issues/15) <br>
  <sub>Labels: accessibility, bug, enhancement, mobile, dark-mode</sub>

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
│   ├── 01_start.ipynb
│   ├── 02_notes.ipynb
│   ├── 02_start.ipynb
│   ├── ... (all chapters and homeworks)
│   ├── hw1.ipynb
│   ├── hw2.ipynb
│   ├── ...
│   └── images/
│       ├── notes/
│       └── youtube-img/
├── static/
│   └── css/
│       └── main.css      # CSS for the site
├── _build/
│   ├── html/             # HTML output (intermediate, not for deployment)
│   │   ├── *.html
│   │   ├── css/
│   │   ├── images/
│   │   └── ...
│   ├── pdf/              # PDF output
│   │   └── *.pdf
│   ├── docx/             # DOCX output
│   │   └── *.docx
│   ├── latex/            # LaTeX output
│   │   ├── *.tex
│   │   └── *_files/
│   └── md/               # Markdown output
│       ├── *.md
│       ├── images/
│       └── *_files/
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
│       ├── ... (all chapters and homeworks)
│       └── hw8/
│           ├── hw8.ipynb
│           ├── hw8.md
│           ├── hw8.tex
│           ├── hw8.docx
│           └── hw8.pdf
└── .nojekyll             # Ensures GitHub Pages does not use Jekyll
```

---



## 📖 Build System Documentation

See [build.md](build.md) for detailed, step-by-step documentation of the build system, including how `build.py` and `build-web.py` work, troubleshooting, and best practices.

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

## 🎨 Modern CSS Styling & Accessibility (2025)

- The site uses a fully custom, modern CSS (`static/css/main.css`) designed for clarity, readability, and accessibility.
- All navigation and main content links use consistent coloring and hover effects for a unified experience.
- Button colors are carefully chosen for both light and dark modes, ensuring strong contrast and visual appeal.
- Dark mode download buttons use teal by default and purple (matching the dark mode title) on hover, with correct text color for readability.
- All color choices are WCAG AA compliant for contrast and accessibility.
- The CSS is documented, maintainable, and removes legacy/duplicate rules.
- Emphasis on keyboard navigation, screen reader support, and accessible admonition blocks.

> _This summary was written by Ollama and edited by a human for clarity and accuracy._

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

## 📂 Build Outputs

- All notebooks listed in `_notebooks.yaml` are converted to LaTeX, PDF, Markdown, DOCX, and Jupyter Notebook formats.
- Downloadable sources are available for each notebook on the course site.
- **PDF generation is currently being improved.** Some PDFs may be missing or incomplete if LaTeX errors occur (e.g., missing images). All other formats are complete.

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
