#!/bin/bash
# build_website.sh
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


# Copy the built site to docs/
cp -r _build/html/* docs/

# Copy figures to both output locations for image rendering
if [ -d "../chapters/figures" ]; then
  cp -r ../chapters/figures _build/html/figures
  cp -r ../chapters/figures docs/figures
fi

echo "Website built in docs/"
