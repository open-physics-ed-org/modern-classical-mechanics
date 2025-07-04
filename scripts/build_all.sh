#!/bin/bash
# build_all.sh
# Run all build steps for the project: chapters, book, and website

set -e

SCRIPT_DIR="$(dirname "$0")"


# Fetch remote images before any build step
"$SCRIPT_DIR/fetch_remote_images.sh"

# Build chapters (notebooks to md/pdf/docx, copy figures)
"$SCRIPT_DIR/build_chapters.sh"

# Build book (concatenate chapters, create book.pdf and book.docx)
"$SCRIPT_DIR/build_book.sh"

# Build website (Jupyter Book, copy figures to output)
"$SCRIPT_DIR/build_website.sh"

echo "All build steps completed."
