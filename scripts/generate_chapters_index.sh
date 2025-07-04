#!/bin/bash
# generate_chapters_index.sh
# Generate chapter_index.md at the project root with links to all chapter documents and lists of images/figures

INDEX_FILE="docs/chapter_index.md"
CHAPTERS_DIR="chapters"
IMAGES_DIR="$CHAPTERS_DIR/images/notes"
FIGURES_DIR="docs/figures"

echo "# Chapters Index" > "$INDEX_FILE"
echo "" >> "$INDEX_FILE"

# Add links to all .md, .pdf, .docx files in chapters/
for ext in md pdf docx; do
  for f in "$CHAPTERS_DIR"/*.$ext; do
    [ -e "$f" ] || continue
    fname=$(basename "$f")
    echo "- [$fname]($CHAPTERS_DIR/$fname)" >> "$INDEX_FILE"
  done
done

echo -e "\n## Images by Week\n" >> "$INDEX_FILE"
if [ -d "$IMAGES_DIR" ]; then
  for week in "$IMAGES_DIR"/week*/; do
    [ -d "$week" ] || continue
    weekname=$(basename "$week")
    echo "### $weekname" >> "$INDEX_FILE"
    for img in "$week"*; do
      [ -f "$img" ] || continue
      imgname=$(basename "$img")
      relpath="$CHAPTERS_DIR/images/notes/$weekname/$imgname"
      echo "- $relpath" >> "$INDEX_FILE"
    done
    echo "" >> "$INDEX_FILE"
  done
fi

echo -e "\n## Figures\n" >> "$INDEX_FILE"
if [ -d "$FIGURES_DIR" ]; then
  for fig in "$FIGURES_DIR"/*; do
    [ -f "$fig" ] || continue
    figname=$(basename "$fig")
    echo "- $FIGURES_DIR/$figname" >> "$INDEX_FILE"
  done
fi

echo "chapter_index.md generated at $INDEX_FILE"