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

# Convert to PDF
pandoc "$BOOK_DIR/book.md" -o "$BOOK_DIR/book.pdf"
# Convert to DOCX
pandoc "$BOOK_DIR/book.md" -o "$BOOK_DIR/book.docx"

echo "Book built in $BOOK_DIR"
