#!/usr/bin/env python3
"""Initialize standard Feynman Native artifact folders and a starter plan file."""

from __future__ import annotations

import argparse
from datetime import datetime, timezone
from pathlib import Path
import subprocess
import sys

SCRIPT_DIR = Path(__file__).resolve().parent
MAKE_SLUG = SCRIPT_DIR / "make_slug.py"

PLAN_TEMPLATE = """# Research Plan: {topic}

- **Slug:** `{slug}`
- **Created:** {created}

## Questions
1. 
2. 
3. 

## Strategy
- 

## Acceptance Criteria
- [ ] Core questions answered with direct sources
- [ ] Major contradictions addressed
- [ ] Final artifact has citations/provenance

## Task Ledger
| ID | Owner | Task | Status | Output |
|---|---|---|---|---|
| T1 | lead | Create plan | done | outputs/.plans/{slug}.md |

## Verification Log
| Item | Method | Status | Evidence |
|---|---|---|---|
| Core factual claims | source verification | pending | |

## Decision Log
- Initial plan created.
"""


def derive_slug(topic: str) -> str:
    result = subprocess.run([sys.executable, str(MAKE_SLUG), topic], capture_output=True, text=True, check=True)
    return result.stdout.strip()


def ensure_dirs(root: Path) -> None:
    for rel in [
        "outputs/.plans",
        "outputs/.drafts",
        "outputs",
        "papers",
        "notes",
        "experiments",
    ]:
        (root / rel).mkdir(parents=True, exist_ok=True)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("topic")
    parser.add_argument("--root", default=".")
    parser.add_argument("--slug", default=None)
    args = parser.parse_args()

    root = Path(args.root).resolve()
    ensure_dirs(root)
    slug = args.slug or derive_slug(args.topic)
    plan_path = root / "outputs/.plans" / f"{slug}.md"

    if not plan_path.exists():
        plan_path.write_text(
            PLAN_TEMPLATE.format(
                topic=args.topic,
                slug=slug,
                created=datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M UTC"),
            )
        )

    print(plan_path)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
