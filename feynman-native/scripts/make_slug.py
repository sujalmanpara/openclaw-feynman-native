#!/usr/bin/env python3
"""Create short Feynman-style slugs from arbitrary research topics."""

from __future__ import annotations

import re
import sys
import unicodedata

STOPWORDS = {
    "a",
    "an",
    "and",
    "for",
    "from",
    "how",
    "in",
    "into",
    "of",
    "on",
    "or",
    "the",
    "to",
    "vs",
    "what",
    "when",
    "where",
    "why",
    "with",
}


def slugify(text: str, max_words: int = 5) -> str:
    text = unicodedata.normalize("NFKD", text).encode("ascii", "ignore").decode("ascii")
    text = text.lower()
    words = re.findall(r"[a-z0-9]+", text)
    filtered = [w for w in words if w not in STOPWORDS]
    picked = filtered[:max_words] or words[:max_words] or ["research"]
    return "-".join(picked)


def main() -> int:
    raw = " ".join(sys.argv[1:]).strip()
    if not raw:
        print("usage: make_slug.py <topic>", file=sys.stderr)
        return 1
    print(slugify(raw))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
