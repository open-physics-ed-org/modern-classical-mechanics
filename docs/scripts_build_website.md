# build_website.sh

This script builds the static website for Modern Classical Mechanics using Jupyter Book and prepares it for GitHub Pages deployment.

## What it does
- Fetches and relinks remote images for reproducibility (calls `fetch_remote_images.sh`).
- Builds the Jupyter Book website from source.
- Cleans and copies the build output to the `docs/` directory.
- Ensures all static assets and figures are present.
- Copies `intro.html` to `index.html` for correct homepage.
- Creates `.nojekyll` so GitHub Pages serves all static files (including CSS/JS).

## Usage
```bash
bash scripts/build_website.sh
```
