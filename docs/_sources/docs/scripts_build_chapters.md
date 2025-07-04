# build_chapters.sh

This script converts all Jupyter notebooks in `notebooks/` to Markdown, PDF, and DOCX in the `chapters/` directory.

## What it does
- Fetches and relinks remote images for reproducibility (calls `fetch_remote_images.sh`).
- Converts each `.ipynb` in `notebooks/` to:
  - Markdown (`.md`) using `jupyter nbconvert`.
  - PDF (`.pdf`) using `jupyter nbconvert` piped to `pandoc` (with resource path for images).
  - DOCX (`.docx`) using `jupyter nbconvert` piped to `pandoc` (with resource path for images).
- Copies images from `notebooks/images/notes/week1/` to `chapters/figures/`, `chapters/images/notes/week1/`, and `docs/figures/` for correct rendering in all outputs.

## Usage
```bash
bash scripts/build_chapters.sh
```
