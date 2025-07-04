#!/bin/bash
# build_book.sh
# Concatenate all chapter markdown files and convert to PDF and DOCX for the full book


set -e

# # Fetch remote images before building book
# "$(dirname "$0")/fetch_remote_images.sh"

CHAPTERS_DIR="$(dirname "$0")/../chapters"
BOOK_DIR="$(dirname "$0")/../book"

mkdir -p "$BOOK_DIR"

# Concatenate all markdown chapters into one book.md
# Build individual chapter PDFs
for md in "$CHAPTERS_DIR"/*.md; do
    base=$(basename "$md" .md)
    pandoc --resource-path="$CHAPTERS_DIR:$BOOK_DIR" "$md" -o "$CHAPTERS_DIR/$base.pdf"
done
# cat $(ls "$CHAPTERS_DIR"/*.md | sort) > "$BOOK_DIR/book.md"


# # Convert concatenated book to PDF
# pandoc --resource-path="$CHAPTERS_DIR:$BOOK_DIR" "$BOOK_DIR/book.md" -o "$BOOK_DIR/book.pdf"
# pandoc --resource-path="$BOOK_DIR" "$BOOK_DIR/book.md" -o "$BOOK_DIR/book.pdf"
# pandoc --resource-path="$BOOK_DIR" "$BOOK_DIR/book.md" -o "$BOOK_DIR/book.docx"


# # Copy all images to book/images/notes for correct relative paths in PDF
# IMAGES_SRC="$(dirname "$0")/../notebooks/images/notes"
# IMAGES_DST="$BOOK_DIR/images/notes"
# if [ -d "$IMAGES_SRC" ]; then
#   mkdir -p "$IMAGES_DST"
#   cp -r "$IMAGES_SRC"/* "$IMAGES_DST"/
# fi
# IMAGES_SRC="$(dirname "$0")/../notebooks/images/notes/week1"
# IMAGES_DST="$BOOK_DIR/images/notes/week1"
# if [ -d "$IMAGES_SRC" ]; then
#   mkdir -p "$IMAGES_DST"
#   cp "$IMAGES_SRC"/* "$IMAGES_DST/"
# fi

echo "Book built in $BOOK_DIR"
