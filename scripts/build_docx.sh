#!/bin/bash
set -e

NOTEBOOK_DIR="$(dirname "$0")/../notebooks"
CHAPTERS_DIR="$(dirname "$0")/../chapters"
BOOK_DIR="$(dirname "$0")/../book"

mkdir -p "$CHAPTERS_DIR" "$BOOK_DIR"

# Copy all images from notebooks to chapters so Pandoc can find them
if [ -d "$NOTEBOOK_DIR/images" ]; then
    mkdir -p "$CHAPTERS_DIR/images"
    cp -r "$NOTEBOOK_DIR/images/"* "$CHAPTERS_DIR/images/"
fi

# Convert each notebook to Markdown and DOCX
for nb in "$NOTEBOOK_DIR"/*.ipynb; do
    base=$(basename "$nb" .ipynb)
    # Convert to Markdown in CHAPTERS_DIR
    jupyter nbconvert --to markdown "$nb" --output "$base.md" --output-dir "$CHAPTERS_DIR"
    # Convert Markdown to DOCX with Pandoc, using resource path for images
    pandoc "$CHAPTERS_DIR/$base.md" -o "$CHAPTERS_DIR/$base.docx" --resource-path="$CHAPTERS_DIR:$NOTEBOOK_DIR"
done

echo "Markdown and DOCX chapters built in $CHAPTERS_DIR"
echo "All tasks completed successfully."