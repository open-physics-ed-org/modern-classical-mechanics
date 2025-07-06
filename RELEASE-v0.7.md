
# Release v0.7 "Robust Routhian" (July 2025)

## 🚀 Major Improvements

- **Robust image handling in Markdown build:**
  - All images referenced in notebooks are now reliably copied to `_build/md/images`.
  - All image links in Markdown are rewritten to point to the copied images, ensuring figures always display correctly in Markdown and DOCX outputs.
  - This resolves issues with missing or broken figures in exported formats.
- **No source notebook changes required:**
  - All fixes are post-processing only; your original `.ipynb` files remain untouched.
- **TOC and logging improvements:**
  - Improved TOC generation and build logging for easier debugging and transparency.
- **Documentation overhaul:**
  - Created a detailed `build.md` documenting the build system and process.
  - Updated `README.md` to reflect new features, closed issues, and current open issues.
- **Issue tracking and release process:**
  - Closed issues #11 and #12 (per-page download menus and unified build script) via commit and GitHub CLI.
  - Created and labeled a new issue for mobile menu usability and dark mode (#15), ensuring all relevant labels exist in the repo.
  - Updated the "Planned / Open Issues" section in the README to reflect the current state of open issues (#7, #8, #15).

## 🐛 Bug Fixes & Accessibility

- **Mobile menu and dark mode accessibility:**
  - Created issue #15 to track and address mobile navigation and dark mode contrast/usability problems.
  - All required labels (accessibility, bug, enhancement, mobile, dark-mode) are now present in the repository.

## 📝 How to use

- Run the build as usual:
  ```sh
  python build.py --md --pdf --docx --latex
  ```
- All images will be handled automatically for Markdown and DOCX outputs.
- See the [README.md](README.md) for full project details and build instructions.

---

**Release date:** July 2025

---

## Highlights

- **Robust image handling in Markdown build:**
  - All images referenced in notebooks are now reliably copied to `_build/md/images`.
  - All image links in Markdown are rewritten to point to the copied images, ensuring figures always display correctly in Markdown and DOCX outputs.
  - This resolves issues with missing or broken figures in exported formats.
- **No source notebook changes required:**
  - All fixes are post-processing only; your original `.ipynb` files remain untouched.
- **Closes issues #11 and #12:**
  - Per-page download menus and unified build script improvements are now complete.

## How to use

- Run the build as usual:
  ```sh
  python build.py --md --pdf --docx --latex
  ```
- All images will be handled automatically for Markdown and DOCX outputs.

---

See the [README.md](README.md) for full project details and build instructions.
