#!/bin/bash
# ============================================================
# compile_pdf.sh — Compile Meeting Minutes LaTeX → PDF
# Usage:  cd docs/meeting-minutes && bash compile_pdf.sh
# ============================================================
set -e

TEX_FILE="Meeting_01_20260908.tex"
OUT_DIR="."

echo "╔══════════════════════════════════════════════════════╗"
echo "║  Compiling: ${TEX_FILE}                              ║"
echo "╚══════════════════════════════════════════════════════╝"

# Pass 1: Generate .aux, .out
pdflatex -interaction=nonstopmode -output-directory="${OUT_DIR}" "${TEX_FILE}"

# Pass 2: Resolve cross-references & hyperlinks
pdflatex -interaction=nonstopmode -output-directory="${OUT_DIR}" "${TEX_FILE}"

echo ""
echo "✅ PDF generated successfully:"
ls -lh "${OUT_DIR}/Meeting_01_20260908.pdf"

# Clean auxiliary files (optional)
echo ""
read -p "🧹 Remove auxiliary files (.aux, .log, .out)? [y/N] " -n 1 -r
echo
if [[ $REPLY =~ ^[Yy]$ ]]; then
    rm -f "${OUT_DIR}"/*.aux "${OUT_DIR}"/*.log "${OUT_DIR}"/*.out
    echo "   Cleaned up."
fi
