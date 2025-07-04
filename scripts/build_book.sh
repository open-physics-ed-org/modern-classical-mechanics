#!/bin/bash
# build_book.sh
# Concatenate all chapter markdown files and convert to PDF and DOCX for the full book


set -e

# Fetch remote images before building book
"$(dirname "$0")/fetch_remote_images.sh"

CHAPTERS_DIR="$(dirname "$0")/../chapters"
BOOK_DIR="$(dirname "$0")/../book"

mkdir -p "$BOOK_DIR"

# Concatenate all markdown chapters into one book.md
cat $(ls "$CHAPTERS_DIR"/*.md | sort) > "$BOOK_DIR/book.md"


# Convert to PDF (ensure images are found)
pandoc --resource-path="$BOOK_DIR" "$BOOK_DIR/book.md" -o "$BOOK_DIR/book.pdf"
# Convert to DOCX (ensure images are found)
pandoc --resource-path="$BOOK_DIR" "$BOOK_DIR/book.md" -o "$BOOK_DIR/book.docx"


# Copy images to book/images/notes/week1 for correct relative paths in PDF/DOCX
IMAGES_SRC="$(dirname "$0")/../notebooks/images/notes/week1"
IMAGES_DST="$BOOK_DIR/images/notes/week1"
if [ -d "$IMAGES_SRC" ]; then
  mkdir -p "$IMAGES_DST"
  cp "$IMAGES_SRC"/* "$IMAGES_DST/"
fi

echo "Book built in $BOOK_DIR"
