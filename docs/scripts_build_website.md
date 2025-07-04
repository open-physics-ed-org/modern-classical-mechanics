# build_website.sh

This script builds the static website for Modern Classical Mechanics using Jupyter Book and prepares it for GitHub Pages deployment.

## What it does
- Fetches and relinks remote images for reproducibility
- Builds the Jupyter Book website from source
- Cleans and copies the build output to the `docs/` directory
- Ensures all static assets and figures are present
- Copies `intro.html` to `index.html` for correct homepage
- Creates `.nojekyll` so GitHub Pages serves all static files (including CSS/JS)

## Usage
```bash
bash scripts/build_website.sh
```

## Steps in detail
1. **Fetch remote images:**
   - Calls `fetch_remote_images.sh` to download and relink any remote images in notebooks or markdown files.
2. **Build the book:**
   - Runs `jupyter-book build .` to generate the HTML site in `_build/html/`.
3. **Clean docs/:**
   - Removes old files in `docs/` (except `.git` and `.nojekyll`).
4. **Copy build output:**
   - Copies everything from `_build/html/` to `docs/`.
5. **Copy figures:**
   - Ensures figures from `chapters/figures/` are available in `docs/figures/`.
6. **Homepage fix:**
   - Copies `intro.html` to `index.html` so the homepage works on GitHub Pages.
7. **.nojekyll:**
   - Ensures `.nojekyll` is present in `docs/` for static asset support.

## See also
- [build_chapters.sh](scripts_build_chapters.md)
- [fetch_remote_images.sh](scripts_fetch_remote_images.md)
