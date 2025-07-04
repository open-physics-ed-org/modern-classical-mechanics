# build_chapters.sh

This script converts all Jupyter notebooks in `notebooks/` to Markdown, PDF, and DOCX in the `chapters/` directory.

## What it does
- Fetches and relinks remote images for reproducibility
- Converts each notebook to Markdown, PDF, and DOCX
- Copies figures to `chapters/figures/` if needed

## Usage
```bash
bash scripts/build_chapters.sh
```

## Steps in detail
1. **Fetch remote images:**
   - Calls `fetch_remote_images.sh` to download and relink any remote images in notebooks or markdown files.
2. **Convert notebooks:**
   - For each `.ipynb` in `notebooks/`, runs:
     - `jupyter nbconvert --to markdown` (to Markdown)
     - `jupyter nbconvert --to pdf` (to PDF)
     - `jupyter nbconvert --to markdown | pandoc` (to DOCX)
3. **Copy figures:**
   - Copies images from `notebooks/images/notes/week1/` to `chapters/figures/` if present.

## See also
- [build_website.sh](scripts_build_website.md)
- [fetch_remote_images.sh](scripts_fetch_remote_images.md)
