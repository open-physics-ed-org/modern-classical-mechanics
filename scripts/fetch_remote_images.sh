#!/bin/bash
# fetch_remote_images.sh
# Find and download remote images in .ipynb and .md files, replace links with local paths
# Also report on all local image references and whether the files exist

set -e

# Regex for remote image URLs
IMG_REGEX='https?://[^)"'\'' ]+\.(png|jpg|jpeg|gif|svg)'

# Regex for local image references in markdown: ![desc](path)
LOCAL_IMG_REGEX='!\\[[^\\]]*\\]\\(([^)]+\\.(png|jpg|jpeg|gif|svg))\\)'

# --- Remote image handling (as before) ---
for ext in ipynb md; do
  find notebooks chapters -type f -name "*.$ext" | while read -r file; do
    grep -Eo "$IMG_REGEX" "$file" | sort -u | while read -r url; do
      fname=$(basename "$url" | cut -d'?' -f1)
      IMG_DIR=""
      for dir in notebooks/images/notes/*/; do
        if [ -d "$dir" ] && [ -f "$dir/$fname" ]; then
          IMG_DIR="$dir"
          break
        fi
      done
      if [ -z "$IMG_DIR" ]; then
        IMG_DIR="notebooks/images/notes/week1"
        mkdir -p "$IMG_DIR"
      fi
      dest="$IMG_DIR/$fname"
      if [ ! -f "$dest" ]; then
        echo "[INFO] Downloading $url -> $dest"
        if curl -Ls "$url" -o "$dest"; then
          echo "[INFO] Downloaded: $dest"
        else
          echo "[ERROR] Failed to download: $url" >&2
        fi
      else
        echo "[INFO] Already exists: $dest"
      fi
      rel_dir=$(echo "$IMG_DIR" | sed 's|^notebooks/||')
      if grep -q "$url" "$file"; then
        sed -i '' "s|$url|$rel_dir/$fname|g" "$file"
        echo "[INFO] Replaced $url with $rel_dir/$fname in $file"
      fi
      echo "[REPORT] (remote) File: $file | URL: $url | Local: $rel_dir/$fname | Folder: $IMG_DIR"
    done
  done
done

# --- Local image reference reporting ---
for ext in ipynb md; do
  find notebooks chapters -type f -name "*.$ext" | while read -r file; do
    # Extract all local image references
    grep -Eo "$LOCAL_IMG_REGEX" "$file" | sed -E 's/.*\(([^)]+)\).*/\\1/' | sort -u | while read -r imgpath; do
      # Remove possible leading/trailing whitespace
      imgpath=$(echo "$imgpath" | xargs)
      # Only check if not a remote URL
      if [[ ! "$imgpath" =~ ^https?:// ]]; then
        # Try to resolve relative to the file's directory
        filedir=$(dirname "$file")
        fullpath="$filedir/$imgpath"
        if [ -f "$fullpath" ]; then
          echo "[REPORT] (local) File: $file | Image: $imgpath | Status: FOUND"
          # Normalize the image path (example: strip leading ../ or set to images/notes/weekX/filename)
          norm_imgpath=$(echo "$fullpath" | sed 's|.*/images/notes/|images/notes/|')
          if [ "$imgpath" != "$norm_imgpath" ]; then
            # Replace the old path with the normalized path in the file
            sed -i '' "s|$imgpath|$norm_imgpath|g" "$file"
            echo "[INFO] Replaced $imgpath with $norm_imgpath in $file"
          fi
        else
          echo "[REPORT] (local) File: $file | Image: $imgpath | Status: MISSING"
        fi
      fi
    done
  done
done