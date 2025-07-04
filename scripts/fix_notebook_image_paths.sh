#!/bin/bash
# fix_notebook_image_paths.sh
# Find all image calls in notebooks looking for ../../images and replace with ../images

set -e

NOTEBOOK_DIR="notebooks"

find "$NOTEBOOK_DIR" -name '*.ipynb' | while read -r nb; do
    echo "Processing $nb ..."
    # Use sed to replace ../../images with ../images in-place
    sed -i '' 's#../../images#../images#g' "$nb"
done

echo "All notebook image paths updated."
