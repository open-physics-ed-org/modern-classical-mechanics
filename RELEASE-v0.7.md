# Release v0.7 "Robust Routhian" (July 2025)

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
