#!/usr/bin/env python3
"""Build a provenance sidecar for a Feynman Native artifact."""

from __future__ import annotations

import argparse
from datetime import datetime, timezone
from pathlib import Path
import re

URL_RE = re.compile(r'https?://[^\s)>\]"\']+')


def count_urls(paths: list[Path]) -> tuple[int, list[str]]:
    seen: list[str] = []
    for path in paths:
        text = path.read_text(encoding="utf-8")
        for url in URL_RE.findall(text):
            if url not in seen:
                seen.append(url)
    return len(seen), seen


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("topic")
    parser.add_argument("slug")
    parser.add_argument("--plan", required=True)
    parser.add_argument("--final", required=True)
    parser.add_argument("--research", nargs="*", default=[])
    parser.add_argument("--review", default=None)
    parser.add_argument("--status", default="PASS")
    parser.add_argument("--output", required=True)
    args = parser.parse_args()

    research_paths = [Path(p) for p in args.research]
    final_path = Path(args.final)
    plan_path = Path(args.plan)
    review_path = Path(args.review) if args.review else None

    consulted_count, _consulted_urls = count_urls(research_paths) if research_paths else (0, [])
    accepted_count, accepted_urls = count_urls([final_path])

    lines = [
        f"# Provenance: {args.topic}",
        "",
        f"- **Date:** {datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M UTC')}",
        f"- **Slug:** `{args.slug}`",
        f"- **Plan:** {plan_path}",
        f"- **Final artifact:** {final_path}",
        f"- **Sources consulted:** {consulted_count}",
        f"- **Sources accepted in final artifact:** {accepted_count}",
        f"- **Verification:** {args.status}",
        "",
        "## Research files",
    ]

    if research_paths:
        for path in research_paths:
            lines.append(f"- {path}")
    else:
        lines.append("- None recorded")

    lines.extend(["", "## Review file"])
    lines.append(f"- {review_path}" if review_path else "- None recorded")

    lines.extend(["", "## Accepted source URLs"])
    if accepted_urls:
        for url in accepted_urls:
            lines.append(f"- {url}")
    else:
        lines.append("- None extracted")

    Path(args.output).write_text("\n".join(lines) + "\n", encoding="utf-8")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
