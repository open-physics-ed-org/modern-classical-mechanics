#!/bin/bash
# build_pdf.sh
# Concatenate all chapter markdown files and convert to PDF and DOCX for the full book


set -e


# Fetch remote images before building book
echo "[INFO] Fetching remote images and updating references..."
"$(dirname "$0")/fetch_remote_images.sh"
echo "[INFO] Remote image fetch and update complete."

NOTEBOOK_DIR="$(dirname "$0")/../notebooks"
CHAPTERS_DIR="$(dirname "$0")/../chapters"
BOOK_DIR="$(dirname "$0")/../book"


echo "[INFO] Creating book output directory: $BOOK_DIR"
mkdir -p "$BOOK_DIR"

echo "Individual chapter PDFs built in $CHAPTERS_DIR"


echo "[INFO] Building individual chapter PDFs from notebooks in $NOTEBOOK_DIR..."
for nb in "$NOTEBOOK_DIR"/*.ipynb; do
    base=$(basename "$nb" .ipynb)
    echo "[INFO] Converting $nb to $CHAPTERS_DIR/$base.pdf using nbconvert (best math support)"
    jupyter nbconvert --to pdf "$nb" --output "$base.pdf" --output-dir "$CHAPTERS_DIR"
done
echo "[INFO] Individual chapter PDFs built in $CHAPTERS_DIR using nbconvert."



echo "[INFO] Checking for Jupyter Book config files in $NOTEBOOK_DIR..."
if [ -f "$NOTEBOOK_DIR/_config.yml" ] && [ -f "$NOTEBOOK_DIR/_toc.yml" ]; then
    echo "[INFO] Found _config.yml and _toc.yml. Building Jupyter Book..."
    jupyter-book build "$NOTEBOOK_DIR" --path-output "$BOOK_DIR"
    echo "[INFO] Jupyter Book build complete. Output in $BOOK_DIR/_build."
else
    echo "[WARN] _config.yml and/or _toc.yml not found in $NOTEBOOK_DIR. Jupyter Book build skipped."
fi


echo "[INFO] Book build process finished. Output directory: $BOOK_DIR"
