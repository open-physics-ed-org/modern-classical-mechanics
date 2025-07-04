#!/bin/bash
# fetch_remote_images.sh
# Find and download remote images in .ipynb and .md files, replace links with local paths
# Also report on all local image references and whether the files exist

set -e


# Regex for remote image URLs (excluding YouTube thumbnails)
IMG_REGEX='https?://[^)"'\'' ]+\.(png|jpg|jpeg|gif|svg)'
# Regex for YouTube thumbnail URLs
YOUTUBE_REGEX='https://img\.youtube\.com/vi/[^/]+/hqdefault\.jpg'

# --- Remote image handling (skip YouTube thumbnails here) ---
for ext in ipynb md; do
  echo "[DEBUG] Looking for *.$ext files in notebooks and chapters..."
  find notebooks chapters -type f -name "*.$ext" | while read -r file; do
    echo "[DEBUG] Processing file: $file"
    grep -Eo "$IMG_REGEX" "$file" | sort -u | while read -r url; do
      echo "[DEBUG] Found image URL: $url in $file"
      # Skip YouTube thumbnails in this loop
      if [[ "$url" =~ ^https://img\.youtube\.com/vi/.*/hqdefault\.jpg$ ]]; then
        echo "[DEBUG] Skipping YouTube thumbnail: $url"
        continue
      fi
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

# --- YouTube thumbnail image handling (dedicated section) ---
YOUTUBE_IMG_DIR="notebooks/images/youtube-img"
mkdir -p "$YOUTUBE_IMG_DIR"

for ext in ipynb md; do
  echo "[DEBUG] Looking for YouTube thumbnails in *.$ext files..."
  find notebooks chapters -type f -name "*.$ext" | while read -r file; do
    echo "[DEBUG] Processing file for YouTube: $file"
    grep -Eo "$YOUTUBE_REGEX" "$file" | sort -u | while read -r yturl; do
      echo "[DEBUG] Found YouTube thumbnail: $yturl in $file"
      # Extract the video ID
      video_id=$(echo "$yturl" | sed -E 's|https://img\.youtube\.com/vi/([^/]+)/hqdefault\.jpg|\1|')
      fname="${video_id}.jpg"
      dest="$YOUTUBE_IMG_DIR/$fname"
      if [ ! -f "$dest" ]; then
        echo "[INFO] Downloading YouTube thumbnail $yturl -> $dest"
        if curl -Ls "$yturl" -o "$dest"; then
          echo "[INFO] Downloaded: $dest"
        else
          echo "[ERROR] Failed to download: $yturl" >&2
        fi
      else
        echo "[INFO] Already exists: $dest"
      fi
      rel_path="images/youtube-img/$fname"
      if grep -q "$yturl" "$file"; then
        sed -i '' "s|$yturl|$rel_path|g" "$file"
        echo "[INFO] Replaced $yturl with $rel_path in $file"
      fi
      echo "[REPORT] (youtube) File: $file | URL: $yturl | Local: $rel_path | Folder: $YOUTUBE_IMG_DIR"
    done
  done
done
