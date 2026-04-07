#!/usr/bin/env python3
"""Extract URLs from markdown/text files and verify that they resolve."""

from __future__ import annotations

import argparse
import re
from pathlib import Path
from urllib.error import HTTPError, URLError
from urllib.request import Request, urlopen

URL_RE = re.compile(r'https?://[^\s)>\]"\']+')


def extract_urls(text: str) -> list[str]:
    seen: list[str] = []
    for url in URL_RE.findall(text):
        if url not in seen:
            seen.append(url)
    return seen


def check_url(url: str, timeout: float) -> tuple[str, str]:
    req = Request(url, headers={"User-Agent": "feynman-native/0.1"})
    try:
        with urlopen(req, timeout=timeout) as resp:
            return "live", str(getattr(resp, "status", 200))
    except HTTPError as e:
        return "dead", f"HTTP {e.code}"
    except URLError as e:
        return "dead", str(e.reason)
    except Exception as e:  # noqa: BLE001
        return "dead", str(e)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("paths", nargs="+", help="Markdown/text files to inspect")
    parser.add_argument("--timeout", type=float, default=10.0)
    args = parser.parse_args()

    urls: list[str] = []
    for raw in args.paths:
        text = Path(raw).read_text(encoding="utf-8")
        for url in extract_urls(text):
            if url not in urls:
                urls.append(url)

    print("| URL | Status | Detail |")
    print("|---|---|---|")
    exit_code = 0
    for url in urls:
        status, detail = check_url(url, args.timeout)
        if status != "live":
            exit_code = 1
        print(f"| {url} | {status} | {detail} |")
    return exit_code


if __name__ == "__main__":
    raise SystemExit(main())
