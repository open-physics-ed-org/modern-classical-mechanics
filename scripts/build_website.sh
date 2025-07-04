#!/bin/bash
# build_website.sh
# Ensure .nojekyll is always present in docs for GitHub Pages
touch docs/.nojekyll

# Build a static website from notebooks using Jupyter Book

set -e

# Fetch remote images before building website
"$(dirname "$0")/fetch_remote_images.sh"

# Ensure jupyter-book is installed
if ! command -v jupyter-book &> /dev/null; then
    echo "jupyter-book not found. Please install it with 'pip install jupyter-book'"
    exit 1
fi

# Build the website
jupyter-book build .


# Remove any old docs/ content (except .git and .nojekyll if present)
find docs/ -mindepth 1 ! -regex 'docs/\(.git\|.nojekyll\).*' -delete

# Copy the entire built site to docs/, preserving all files (including .nojekyll)
cp -a _build/html/. docs/


# Copy figures to both output locations for image rendering
if [ -d "../chapters/figures" ]; then
  cp -r ../chapters/figures docs/figures
fi

# Copy images to docs/images/notes/week1 for correct notebook/chapter rendering
IMAGES_SRC="../notebooks/images/notes"
IMAGES_DST="docs/images/notes"
if [ -d "$IMAGES_SRC" ]; then
  mkdir -p "$IMAGES_DST"
  cp "$IMAGES_SRC"/* "$IMAGES_DST/"
fi

# Ensure the homepage is correct for GitHub Pages
if [ -f docs/intro.html ]; then
  cp docs/intro.html docs/index.html
fi

echo "Website built in docs/ (ready for GitHub Pages)"
