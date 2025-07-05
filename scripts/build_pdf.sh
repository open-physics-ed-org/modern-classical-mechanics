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

# Set directory variables early
CURRENT_DIR="$(cd "$(dirname "$0")" && pwd)"
BOOK_DIR="${CURRENT_DIR}/../_build/latex"
NOTEBOOK_DIR="${CURRENT_DIR}/../notebooks"
CHAPTERS_DIR="${CURRENT_DIR}/../_build/latex"

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

# Always sync _toc.yml from notebooks.yaml before any build
REPO_ROOT="$(dirname "$0")/.."
echo "[INFO] Syncing _toc.yml from notebooks.yaml..."
"$REPO_ROOT/scripts/update_toc.sh"

# Fetch remote images before building book
echo "[INFO] Fetching remote images and updating references..."
"$CURRENT_DIR/fetch_remote_images.sh"
echo "[INFO] Remote image fetch and update complete."

echo "[INFO] Creating book output directory: $BOOK_DIR"
mkdir -p "$BOOK_DIR"


echo "Individual chapter PDFs will be built in $CHAPTERS_DIR"






# Build PDFs if requested
if $BUILD_PDF; then
  NOTEBOOKS_YAML="$(dirname "$0")/../notebooks.yaml"
  echo "[INFO] Building individual chapter PDFs from notebooks listed in $NOTEBOOKS_YAML..."
  NOTEBOOKS=()
  if [ -f "$NOTEBOOKS_YAML" ]; then
    # Extract notebook paths from YAML (ignoring comments and blank lines)
    while IFS= read -r line; do
      line="$(echo "$line" | sed 's/^ *- *//')"
      [[ "$line" =~ ^notebooks:|^#|^$ ]] && continue
      NOTEBOOKS+=("$NOTEBOOK_DIR/$line")
    done < "$NOTEBOOKS_YAML"
  else
    echo "[ERROR] $NOTEBOOKS_YAML not found. Exiting."
    exit 1
  fi


  mkdir -p "$CHAPTERS_DIR"
  for nb in "${NOTEBOOKS[@]}"; do
    if [ -f "$nb" ]; then
      base=$(basename "$nb" .ipynb)
      pdf_file="$CHAPTERS_DIR/$base.pdf"
      # Only build if notebook is newer than PDF or PDF does not exist
      if [ ! -f "$pdf_file" ] || [ "$nb" -nt "$pdf_file" ]; then
        echo "[INFO] Converting $nb to $pdf_file using nbconvert (best math support)"
        jupyter nbconvert --to pdf "$nb" --output "$base.pdf" --output-dir "$CHAPTERS_DIR"
      else
        echo "[SKIP] $pdf_file is up to date. Skipping."
      fi
    else
      echo "[WARN] File not found: $nb"
    fi
  done


  echo "[INFO] Individual chapter PDFs built in $CHAPTERS_DIR using nbconvert."

  # Build full book PDF using Jupyter Book if config files exist
  if [ -f "$REPO_ROOT/_config.yml" ] && [ -f "$REPO_ROOT/_toc.yml" ]; then
    echo "[INFO] Building full book PDF using Jupyter Book (pdflatex builder)..."
    jupyter-book build "$REPO_ROOT" --path-output "$BOOK_DIR" --builder pdflatex || {
      echo "[WARN] Jupyter Book PDF build failed. Check LaTeX errors above.";
    }
    # Leave the generated PDF in _build/latex as per Jupyter Book convention
    PDF_PATH="$BOOK_DIR/_build/latex/book.pdf"
    if [ -f "$PDF_PATH" ]; then
      echo "[INFO] Full book PDF available at $PDF_PATH"
    else
      echo "[WARN] Full book PDF was not generated."
    fi
  else
    echo "[WARN] _config.yml and/or _toc.yml not found in $REPO_ROOT. Skipping full book PDF build."
  fi
fi






# Build Jupyter Book website if requested
if $BUILD_HTML; then
  REPO_ROOT="$(dirname "$0")/.."
  echo "[INFO] Updating _toc.yml from notebooks.yaml..."
  "$REPO_ROOT/scripts/update_toc.sh"

  echo "[INFO] Checking for Jupyter Book config files in $REPO_ROOT..."
  if [ -f "$REPO_ROOT/_config.yml" ] && [ -f "$REPO_ROOT/_toc.yml" ]; then
      echo "[INFO] Found _config.yml and _toc.yml in repo root. Building Jupyter Book..."
      # Always build the book into the book directory
      jupyter-book build "$REPO_ROOT" --path-output "${CURRENT_DIR}"
      # Move the built HTML files to ${CURRENT_DIR} if not already there
      if [ -d "${CURRENT_DIR}/_build/html" ]; then
        echo "[INFO] Moving built HTML files to ${CURRENT_DIR}..."
        cp -a "${CURRENT_DIR}/_build/html/." "${CURRENT_DIR}/"
      fi
      echo "[INFO] Jupyter Book build complete. Output in ${CURRENT_DIR}."
  else
      echo "[WARN] _config.yml and/or _toc.yml not found in $REPO_ROOT. Jupyter Book build skipped."
  fi
fi


echo "[INFO] Book build process finished. Output directory: ${CURRENT_DIR}"

echo "$BOOK_DIR"
echo "$CHAPTERS_DIR"