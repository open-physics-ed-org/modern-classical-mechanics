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
    # Convert to PDF
    jupyter nbconvert --to pdf "$nb" --output "$base.pdf" --output-dir="$CHAPTERS_DIR"
    # Convert to DOCX (via pandoc)
    jupyter nbconvert --to markdown "$nb" --stdout | pandoc -f markdown -o "$CHAPTERS_DIR/$base.docx"
done

# Copy figures to chapters/figures if not already present
FIGURES_SRC="$(dirname "$0")/../notebooks/images/notes/week1"
FIGURES_DST="$CHAPTERS_DIR/figures"
if [ -d "$FIGURES_SRC" ]; then
  mkdir -p "$FIGURES_DST"
  cp "$FIGURES_SRC"/* "$FIGURES_DST/"
fi

echo "Chapters built in $CHAPTERS_DIR"
