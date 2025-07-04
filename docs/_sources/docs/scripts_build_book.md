# build_book.sh

This script concatenates all chapter markdown files and converts them into a single PDF and DOCX for the full book.

## What it does
- Fetches and relinks remote images (calls `fetch_remote_images.sh`).
- Concatenates all `.md` files in `chapters/` into `book/book.md`.
- Converts `book/book.md` to `book/book.pdf` and `book/book.docx` using `pandoc` (with resource path for images).
- Copies images from `notebooks/images/notes/week1/` to `book/images/notes/week1/` for correct rendering in PDF/DOCX.

## Usage
```bash
bash scripts/build_book.sh
```
