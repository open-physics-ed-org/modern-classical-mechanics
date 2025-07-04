# Write a bash script to convert all the notebooks in the `notebooks/` directory to DOCX format and place them in the `chapters/` directory. They should compile in the same order as they appear in the _toc.yml file. The individual chapters should be docx with figures. The script should also compile a full book from the chapters in DOCX format, placing it in the `book/` directory. 

#!/bin/bash
# build_docx.sh
# Converts all notebooks in notebooks/ to DOCX in chapters/ and builds a full book in book/

set -e

# Fetch remote images before building chapters
"$(dirname "$0")/fetch_remote_images.sh"

NOTEBOOK_DIR="$(dirname "$0")/../notebooks"
CHAPTERS_DIR="$(dirname "$0")/../chapters"
BOOK_DIR="$(dirname "$0")/../book"

mkdir -p "$CHAPTERS_DIR" "$BOOK_DIR"

# Convert each notebook to DOCX
# Convert each notebook to Markdown, then to DOCX
for nb in "$NOTEBOOK_DIR"/*.ipynb; do
    base=$(basename "$nb" .ipynb)
    # Convert to Markdown
    jupyter nbconvert --to markdown "$nb" --output "$base.md"
    # Convert Markdown to DOCX with pandoc (ensure images are found)
    pandoc "$base.md" -o "$base.docx"
    mv "$base.docx" "$CHAPTERS_DIR/"
    rm -f "$base.md"
done
for nb in "$NOTEBOOK_DIR"/*.ipynb; do
    base=$(basename "$nb" .ipynb)
    # Convert to DOCX (ensure images are found)
    mv "$base.docx" "$CHAPTERS_DIR/"
done

# Concatenate all chapter DOCX files into one book.docx
cd "$CHAPTERS_DIR"
docx_files=$(ls *.docx | sort)
if [ -z "$docx_files" ]; then
    echo "No DOCX files found in $CHAPTERS_DIR"
    exit 1
fi
# Create a temporary file to hold the concatenated content
temp_book="$BOOK_DIR/book.docx"
# Initialize the book with the first chapter
first_file=$(echo "$docx_files" | head -n 1)
cp "$first_file" "$temp_book"
# Append the rest of the chapters
for file in $docx_files; do
    if [ "$file" != "$first_file" ]; then
        # Use pandoc to append the content of each DOCX file
        pandoc "$temp_book" "$file" -o "$temp_book.tmp"
        mv "$temp_book.tmp" "$temp_book"
    fi
done

# Move the final book to the book directory
mv "$temp_book" "$BOOK_DIR/book.docx"
# Copy images to book/images

IMAGES_SRC="$(dirname "$0")/../notebooks/images/notes"
IMAGES_DST="$BOOK_DIR/images/notes"
if [ -d "$IMAGES_SRC" ]; then
    mkdir -p "$IMAGES_DST"
    cp "$IMAGES_SRC"/* "$IMAGES_DST/"
fi

echo "DOCX chapters built in $CHAPTERS_DIR"
echo "Full book built in $BOOK_DIR/book.docx"
echo "Images copied to $BOOK_DIR/images/notes"
echo "All tasks completed successfully."
