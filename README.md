<div align="center">

# 📚 Modern Classical Mechanics

**An open, free, and ever-evolving set of notes and resources for learning and teaching classical mechanics.**

<br>
<strong>Author:</strong> Marcos D. Caballero  
<strong>Contact:</strong> caball14@msu.edu  
<strong>Michigan State University</strong>

![Build](https://img.shields.io/badge/build-passing-brightgreen) ![License: CC BY-NC 4.0](https://img.shields.io/badge/license-CC--BY--NC%204.0-blue)

</div>

---

## 🌐 About & Webpage

**Modern Classical Mechanics** is an open-source, interactive, and reproducible book for PHY 321: Classical Mechanics 1 at Michigan State University, authored by Marcos D. Caballero.

- **Webpage:** [View the Book Online](https://dannycaballero.info/modern-classical-mechanics/)
- **GitHub Repo:** [github.com/dannycab/modern-classical-mechanics](https://github.com/dannycab/modern-classical-mechanics)
- **License:** CC BY-NC 4.0 (free for non-commercial use)
- **Contact:** caball14@msu.edu

All content is built from Jupyter notebooks and published automatically to the web. Contributions, issues, and pull requests are welcome!

---

## 🚀 What is this?

Welcome to the home of **Modern Classical Mechanics**! This is a living, collaborative, and open-source book built from Jupyter notebooks, designed for students, educators, and the curious. All content is free to use, adapt, and remix for non-commercial purposes.

- **Multiple formats:** Website, PDF, DOCX, Markdown
- **Reproducible:** All code, figures, and outputs are version-controlled and built automatically
- **Automated workflow:** Robust scripts ensure all images are local, YouTube thumbnails are correct, and LaTeX/math is PDF-compatible before export
- **Open:** Contributions, issues, and pull requests are *highly* encouraged!
- **Fun:** Physics is awesome, and so is open science 🌟

---

## 🗂️ Project Structure

```
modern-classical-mechanics/
├── notebooks/        # Source Jupyter notebooks (edit here!)
├── _build/           # Auto-generated Markdown, PDF, DOCX, and figures (do not edit by hand)
│   ├── latex/        # LaTeX files
│   ├── pdf/          # PDF files
│   ├── md/           # Markdown files
│   │   └── images/   # All images referenced in Markdown/DOCX
│   └── docx/         # DOCX files
├── docs/             # Website output for GitHub Pages (auto-generated, do not edit)
├── scripts/          # Build and utility scripts (edit here)
├── .github/workflows # GitHub Actions CI/CD workflows
├── Dockerfile, docker-compose.yml  # Containerized build environment
├── _config.yml, _toc.yml, book_metadata.yml  # Build config
└── README.md         # You are here!
```

---

## 🏗️ Build & Utility Scripts

All build and utility scripts are in the `scripts/` directory. Run any script with `bash scripts/<scriptname>.sh` from the project root.

- **build.py**: Main Python build script for converting notebooks to Markdown, PDF, DOCX, and handling all image logic.
- **build-web.py**: Builds the HTML website version of the book for GitHub Pages.
- **fetch_remote_images.sh**: Finds, downloads, and relinks any remote images referenced in notebooks or markdown files, ensuring all images are local for reproducibility.

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
3. **Install Jupyter and Pandoc:**
   - Jupyter: `pip install jupyter nbconvert`
   - Pandoc: [Install from pandoc.org](https://pandoc.org/installing.html)
4. **Build everything:**
   ```bash
   python build.py
   ```
   Or build just the chapters:
   ```bash
   python build.py --md --pdf --docx
   ```
5. **Build the website:**
   ```bash
   python build-web.py
   ```
6. **View outputs:**
   - Website: `docs/index.html`
   - PDFs/DOCX: `_build/pdf/`, `_build/docx/`
   - Markdown: `_build/md/`

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

## 📄 Chapters and Figures Index

See [docs/chapters_index.md](docs/chapters_index.md) for direct links to all chapters in every available format (notebook, markdown, PDF, DOCX) and to all figures used in the book.

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
