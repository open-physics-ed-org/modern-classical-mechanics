
#!/bin/bash
# build_pdf.sh
#
# Flexible script to convert Jupyter notebooks to PDF using nbconvert, and/or build a Jupyter Book website.
#
# USAGE:
#   ./build_pdf.sh [--pdf] [--html]  # Build PDFs, HTML website, or both (default: both)
#   ./build_pdf.sh --pdf             # Only build PDFs
#   ./build_pdf.sh --html            # Only build Jupyter Book website
#
# FLAGS:
#   --pdf   Build PDFs only
#   --html  Build Jupyter Book website only
#   (If neither flag is given, both are built)
#
# OUTPUT:
#   - PDFs are written to the chapters directory, named after the notebook (e.g., notebook.ipynb -> notebook.pdf).
#   - If Jupyter Book config files (_config.yml, _toc.yml) are present in the repo root, a Jupyter Book website is built in the book directory.
#
# DEPENDENCIES:
#   - jupyter nbconvert
#   - jupyter-book (optional, for Jupyter Book build)
#
# EXAMPLES:
#   ./build_pdf.sh           # Build both PDFs and website
#   ./build_pdf.sh --pdf     # Build only PDFs
#   ./build_pdf.sh --html    # Build only website


set -e
# Parse flags
BUILD_PDF=false
BUILD_HTML=false
if [ $# -eq 0 ]; then
  BUILD_PDF=true
  BUILD_HTML=true
else
  for arg in "$@"; do
    case $arg in
      --pdf)
        BUILD_PDF=true
        ;;
      --html)
        BUILD_HTML=true
        ;;
      *)
        echo "[ERROR] Unknown argument: $arg"
        echo "Usage: $0 [--pdf] [--html]"
        exit 1
        ;;
    esac
  done
  # If only one flag is set, don't build the other
  if $BUILD_PDF && ! $BUILD_HTML; then
    BUILD_HTML=false
  elif $BUILD_HTML && ! $BUILD_PDF; then
    BUILD_PDF=false
  fi
fi
# Fetch remote images before building book
echo "[INFO] Fetching remote images and updating references..."
"$(dirname "$0")/fetch_remote_images.sh"
echo "[INFO] Remote image fetch and update complete."

NOTEBOOK_DIR="$(dirname "$0")/../notebooks"
CHAPTERS_DIR="$(dirname "$0")/../chapters"
BOOK_DIR="$(dirname "$0")/../book"


echo "[INFO] Creating book output directory: $BOOK_DIR"
mkdir -p "$BOOK_DIR"

echo "Individual chapter PDFs built in $CHAPTERS_DIR"






# Build PDFs if requested
if $BUILD_PDF; then
  NOTEBOOKS_YAML="$(dirname "$0")/../notebooks.yaml"
  echo "[INFO] Building individual chapter PDFs from notebooks listed in $NOTEBOOKS_YAML..."
  NOTEBOOKS=()
  if [ -f "$NOTEBOOKS_YAML" ]; then
    # Extract notebook paths from YAML (ignoring comments and blank lines)
    while IFS= read -r line; do
      line="${line#- }"
      [[ "$line" =~ ^notebooks:|^#|^$ ]] && continue
      NOTEBOOKS+=("$NOTEBOOK_DIR/$line")
    done < "$NOTEBOOKS_YAML"
  else
    echo "[ERROR] $NOTEBOOKS_YAML not found. Exiting."
    exit 1
  fi

  for nb in "${NOTEBOOKS[@]}"; do
    [ -f "$nb" ] || continue
    base=$(basename "$nb" .ipynb)
    echo "[INFO] Converting $nb to $CHAPTERS_DIR/$base.pdf using nbconvert (best math support)"
    jupyter nbconvert --to pdf "$nb" --output "$base.pdf" --output-dir "$CHAPTERS_DIR"
  done
  echo "[INFO] Individual chapter PDFs built in $CHAPTERS_DIR using nbconvert."
fi





# Build Jupyter Book website if requested
if $BUILD_HTML; then
  REPO_ROOT="$(dirname "$0")/.."
  echo "[INFO] Updating _toc.yml from notebooks.yaml..."
  "$REPO_ROOT/scripts/update_toc.sh"

  echo "[INFO] Checking for Jupyter Book config files in $REPO_ROOT..."
  if [ -f "$REPO_ROOT/_config.yml" ] && [ -f "$REPO_ROOT/_toc.yml" ]; then
      echo "[INFO] Found _config.yml and _toc.yml in repo root. Building Jupyter Book..."
      jupyter-book build "$REPO_ROOT" --path-output "$BOOK_DIR"
      echo "[INFO] Jupyter Book build complete. Output in $BOOK_DIR/_build."
  else
      echo "[WARN] _config.yml and/or _toc.yml not found in $REPO_ROOT. Jupyter Book build skipped."
  fi
fi


echo "[INFO] Book build process finished. Output directory: $BOOK_DIR"
