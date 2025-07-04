#!/bin/bash
# build_chapters.sh
# Converts all notebooks in notebooks/ to Markdown, PDF, and DOCX in chapters/


set -e

# Fetch remote images before building chapters
"$(dirname "$0")/fetch_remote_images.sh"

NOTEBOOK_DIR="$(dirname "$0")/../notebooks"
CHAPTERS_DIR="$(dirname "$0")/../chapters"

mkdir -p "$CHAPTERS_DIR"


for nb in "$NOTEBOOK_DIR"/*.ipynb; do
    base=$(basename "$nb" .ipynb)
    # Convert to Markdown
    jupyter nbconvert --to markdown "$nb" --output "$base.md" --output-dir="$CHAPTERS_DIR"
    # Convert to PDF (ensure images are found, use absolute path)
    jupyter nbconvert --to markdown "$nb" --stdout | pandoc --resource-path="$(realpath "$CHAPTERS_DIR")" -f markdown -o "$CHAPTERS_DIR/$base.pdf"
    # Convert to DOCX (ensure images are found, use absolute path)
    jupyter nbconvert --to markdown "$nb" --stdout | pandoc --resource-path="$(realpath "$CHAPTERS_DIR")" -f markdown -o "$CHAPTERS_DIR/$base.docx"
done


# Copy images to all required locations for chapters, website, and PDF/DOCX builds
IMAGES_SRC="$(dirname "$0")/../notebooks/images/notes/week1"
FIGURES_DST="$CHAPTERS_DIR/figures"
DOCS_FIGURES_DST="$(dirname "$0")/../docs/figures"
IMAGES_DST="$CHAPTERS_DIR/images/notes/week1"
if [ -d "$IMAGES_SRC" ]; then
  mkdir -p "$FIGURES_DST" "$DOCS_FIGURES_DST" "$IMAGES_DST"
  cp "$IMAGES_SRC"/* "$FIGURES_DST/"
  cp "$IMAGES_SRC"/* "$DOCS_FIGURES_DST/"
  cp "$IMAGES_SRC"/* "$IMAGES_DST/"
fi

echo "Chapters built in $CHAPTERS_DIR"
