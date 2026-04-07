# Preview and Export

Use this adapter for rendering and exporting research artifacts.

## Goal
Preview Markdown, code, or PDF artifacts before delivery — or export to PDF for sharing.

## Native OpenClaw approach

### Markdown preview
OpenClaw artifacts are Markdown by default. Preview options:
- open in any Markdown viewer or editor
- render in a browser via a lightweight server
- use VS Code / Obsidian / any Markdown-capable app

### PDF export via pandoc
If `pandoc` is available:
```bash
pandoc outputs/<slug>.md -o outputs/<slug>.pdf --pdf-engine=xelatex
```

If `pandoc` is not available:
```bash
# check
command -v pandoc || echo "pandoc not installed — install with: sudo apt install pandoc texlive-xetex"
```

### HTML export
```bash
pandoc outputs/<slug>.md -o outputs/<slug>.html --standalone --metadata title="<title>"
```

### Browser preview (quick)
```bash
# macOS
open outputs/<slug>.md

# Linux with xdg
xdg-open outputs/<slug>.md

# or serve locally
python3 -m http.server 8080 --directory outputs/
```

## When to use
- user asks to preview or export a research artifact
- user wants a PDF version of a report
- user wants to share a rendered version

## Rules
- always check if pandoc/xelatex are available before attempting PDF export
- inform the user if export tools are missing
- keep the canonical artifact as Markdown — PDF/HTML are secondary exports
