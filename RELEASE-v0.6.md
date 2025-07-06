# Release v0.6 "Hamiltonian Heron" (July 2025)

## Highlights

- **Admonition overhaul:** All admonition blocks (notes, tips, warnings, custom, etc.) in HTML output now:
  - Have the correct emoji prepended to the title, for both standard and custom classes.
  - Remove all `:class:` markup and any leftover MyST/Markdown-it syntax.
  - Robustly handle multi-paragraph and edge-case blocks.
  - Debug output and post-build checks ensure no unconverted blocks remain.
- **Cleaner HTML:** No more stray `:class:` lines or raw MyST blocks in output. All admonitions are visually and semantically correct.
- **No source notebook changes:** All fixes are post-processing only; your notebooks remain untouched.
- **Other improvements:**
  - Improved build script debug output and error reporting.
  - Minor HTML and menu tweaks for accessibility and navigation.

## How to update

- Pull the latest `main` branch.
- Run the build script as usual: `python3 build-web.py`
- All HTML output will have improved admonition rendering and no leftover markup.

---

Thanks to everyone who reported issues and tested edge cases!
