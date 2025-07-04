#!/bin/bash
# fetch_remote_images.sh
# Find and download remote images in .ipynb and .md files, replace links with local paths

set -e

# Directory to store downloaded images
IMG_DIR="notebooks/images/notes/week1"
mkdir -p "$IMG_DIR"


 # Regex for remote image URLs
IMG_REGEX='https?://[^)"'\'' ]+\.(png|jpg|jpeg|gif|svg)'

# Loop through files and process (portable, no arrays)
for ext in ipynb md; do
  find notebooks chapters -type f -name "*.$ext" | while read -r file; do
    # Extract remote image URLs
    grep -Eo "$IMG_REGEX" "$file" | sort -u | while read -r url; do
      fname=$(basename "$url" | cut -d'?' -f1)
      dest="$IMG_DIR/$fname"
      # Download if not present
      if [ ! -f "$dest" ]; then
        echo "Downloading $url -> $dest"
        if curl -Ls "$url" -o "$dest"; then
          echo "Downloaded: $dest"
        else
          echo "Failed to download: $url" >&2
        fi
      else
        echo "Already exists: $dest"
      fi
      # Replace remote URL with local path in file
      if grep -q "$url" "$file"; then
        sed -i '' "s|$url|images/notes/week1/$fname|g" "$file"
        echo "Replaced $url with images/notes/week1/$fname in $file"
      fi
    done
  done
done

echo "Remote image fetching and replacement complete."
