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

---

## � More Documentation

- See [build.md](build.md) for build system details, troubleshooting, and advanced usage.
- See [jupyter-markup-tips.md](jupyter-markup-tips.md) for writing and formatting tips in Jupyter Notebooks.
- See [releases/RELEASE-v0.9.md](releases/RELEASE-v0.9.md) for the latest release notes and summary of changes.

---


## 🚀 Features

- Unified build system: one command builds all outputs (LaTeX, PDF, Markdown, DOCX, HTML web site)
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
   - PDFs: `_build/pdf/`
   - DOCX: `_build/docx/`
   - LaTeX: `_build/latex/`
   - Markdown: `_build/md/`
   - Theme CSS: `static/css/theme-light.css`, `static/css/theme-dark.css` (auto-generated)

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
