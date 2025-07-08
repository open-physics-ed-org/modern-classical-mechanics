# RELEASE v0.9.2 "Unified Urubu" (July 2025)

**Unified Build, Output Consistency, and Documentation Overhaul**

This release brings further polish and reliability to the Modern Classical Mechanics build system, with a focus on output consistency, documentation, and a robust all-in-one workflow.

## 🚀 Highlights

- **Consistent All-in-One Build:**
  - The `--all` flag in `build.py` now runs all major build steps in strict order: DOCX (and Markdown) → PDF → Jupyter Book HTML → Custom HTML web output.
  - All output formats are copied to `docs/sources/<notebook_stem>/` for each notebook, ensuring every format is always available for download.
  - Markdown is always built before DOCX, guaranteeing up-to-date DOCX output.
- **Jupyter Book HTML Improvements:**
  - Jupyter Book HTML is built into a temp directory, then copied to both `docs/jupyter/` and `docs/sources/jupyterbook_html/` for easy access and deployment.
- **Documentation Overhaul:**
  - `README.md` and `build.md` have been fully rewritten to reflect the new build workflow, directory structure, and usage patterns.
  - All build commands, output locations, and troubleshooting tips are now up to date and easy to follow.
- **Output Directory Clarity:**
  - All outputs are organized in `_build/` (intermediate) and `docs/` (final, published), with clear subfolders for each format.
  - Downloadable sources for each notebook are always available in `docs/sources/<notebook_stem>/`.
- **Robust Image Handling:**
  - All referenced images are collected into `_build/images/` and linked consistently in all output formats.
- **No Automatic Cleanup:**
  - The build system no longer deletes any files or folders automatically; manual cleanup is recommended if needed.

## 🛠️ How to Upgrade

1. Pull the latest changes.
2. Review the updated `README.md` and `build.md` for new features and instructions.
3. Use `python build.py --all` to build everything, or `python build.py --html` for just the web output.
4. All outputs are in `_build/` and `docs/`.

---

See the `releases/` folder for full historical release notes.
