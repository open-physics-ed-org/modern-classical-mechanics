---

## 🛠️ Build Scripts Overview

All build and utility scripts are in the `scripts/` directory. Here’s what each one does:

- **build_chapters.sh**: Converts all Jupyter notebooks in `notebooks/` to Markdown, PDF, and DOCX in `chapters/`. Also fetches remote images and copies figures.
- **build_book.sh**: Builds the full book (website and other formats) from the chapters and configuration files.
- **build_website.sh**: Builds the HTML website version of the book using Jupyter Book.
- **build_all.sh**: Runs all build steps in sequence (chapters, book, website, etc.).
- **fetch_remote_images.sh**: Finds, downloads, and relinks any remote images referenced in notebooks or markdown files, ensuring all images are local for reproducibility.

Run any script with `bash scripts/<scriptname>.sh` from the project root.

---

<div align="center">

# 📚 Modern Classical Mechanics

**An open, free, and ever-evolving set of notes and resources for learning and teaching classical mechanics.**

![Build](https://img.shields.io/badge/build-passing-brightgreen) ![License: CC BY-NC 4.0](https://img.shields.io/badge/license-CC--BY--NC%204.0-blue)

</div>

---

## 🚀 What is this?

Welcome to the home of **Modern Classical Mechanics**! This is a living, collaborative, and open-source book built from Jupyter notebooks, designed for students, educators, and the curious. All content is free to use, adapt, and remix for non-commercial purposes.

- **Multiple formats:** Website, PDF, DOCX, Markdown
- **Reproducible:** All code, figures, and outputs are version-controlled and built automatically
- **Open:** Contributions, issues, and pull requests are *highly* encouraged!
- **Fun:** Physics is awesome, and so is open science 🌟

---

## 📦 Project Structure

```
modern-classical-mechanics/
├── notebooks/        # Source Jupyter notebooks (edit here!)
├── chapters/         # Auto-generated Markdown, PDF, DOCX, figures
├── book/             # Website build (Jupyter Book)
├── docs/             # GitHub Pages output (optional)
├── scripts/          # Build and utility scripts
├── .github/workflows # GitHub Actions CI/CD
├── Dockerfile, docker-compose.yml
├── _config.yml, _toc.yml, book_metadata.yml
└── README.md         # You are here!
```

---

## 🛠️ How to Build Locally

1. **Clone the repo:**
   ```bash
   git clone https://github.com/dannycab/modern-classical-mechanics.git
   cd modern-classical-mechanics
   ```
2. **Set up Python environment:**
   ```bash
   python3 -m venv .venv
   source .venv/bin/activate
   pip install -r requirements.txt
   ```
3. **Build everything:**
   ```bash
   ./scripts/build_all.sh
   ```
   Or build just the chapters:
   ```bash
   ./scripts/build_chapters.sh
   ```
4. **View outputs:**
   - Website: `book/_build/html/index.html`
   - PDFs/DOCX: `chapters/`

---

## 🤖 Automated Builds (CI/CD)

- GitHub Actions automatically build the book and website on every push.
- All assets (notebooks, images, outputs) are kept in sync.
- Want to help improve the workflow? [Open an issue](https://github.com/dannycab/modern-classical-mechanics/issues) or [send a pull request](https://github.com/dannycab/modern-classical-mechanics/pulls)!

---

## 🖼️ Images & Figures

- All images are stored locally for reproducibility and PDF/LaTeX compatibility.
- Remote images are automatically downloaded and relinked by our scripts.
- Want to add a cool diagram? Just drop it in `notebooks/images/` and reference it in your notebook!

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

## 🙏 Acknowledgments

- Inspired by the open science and Jupyter communities
- Built with [Jupyter Book](https://jupyterbook.org/), [nbconvert](https://nbconvert.readthedocs.io/), and lots of ❤️

---

<div align="center">

*Made with 🧑‍🔬, ☕, and a love for teaching physics.*

</div>
