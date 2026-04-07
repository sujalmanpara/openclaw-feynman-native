#!/usr/bin/env python3
"""Merge and deduplicate URLs from research artifacts into a numbered source list."""

from __future__ import annotations

import argparse
import re
from pathlib import Path

URL_RE = re.compile(r'https?://[^\s)>\]"\']+')


def extract_urls(text: str) -> list[str]:
    seen: list[str] = []
    for url in URL_RE.findall(text):
        if url not in seen:
            seen.append(url)
    return seen


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("paths", nargs="+", help="Research files to merge")
    parser.add_argument("--output", help="Optional output markdown path")
    args = parser.parse_args()

    merged: list[tuple[str, str]] = []
    seen: set[str] = set()
    for raw in args.paths:
        path = Path(raw)
        text = path.read_text(encoding="utf-8")
        for url in extract_urls(text):
            if url in seen:
                continue
            seen.add(url)
            merged.append((path.name, url))

    lines = ["# Unified Sources", "", "| # | First seen in | URL |", "|---|---|---|"]
    for i, (source_file, url) in enumerate(merged, start=1):
        lines.append(f"| {i} | {source_file} | {url} |")

    output = "\n".join(lines) + "\n"
    if args.output:
        Path(args.output).write_text(output, encoding="utf-8")
    else:
        print(output, end="")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
