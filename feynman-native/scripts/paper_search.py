#!/usr/bin/env python3
"""Tiny arXiv API search helper for Feynman Native."""

from __future__ import annotations

import argparse
import html
import textwrap
import urllib.parse
import urllib.request
import xml.etree.ElementTree as ET

ATOM = "http://www.w3.org/2005/Atom"
NS = {"atom": ATOM}


def fetch(query: str, max_results: int) -> str:
    params = urllib.parse.urlencode(
        {
            "search_query": f"all:{query}",
            "start": 0,
            "max_results": max_results,
            "sortBy": "relevance",
            "sortOrder": "descending",
        }
    )
    url = f"https://export.arxiv.org/api/query?{params}"
    with urllib.request.urlopen(url, timeout=20) as resp:
        return resp.read().decode("utf-8", errors="replace")


def parse(feed_xml: str) -> list[dict[str, str]]:
    root = ET.fromstring(feed_xml)
    out: list[dict[str, str]] = []
    for entry in root.findall("atom:entry", NS):
        title = (entry.findtext("atom:title", default="", namespaces=NS) or "").strip().replace("\n", " ")
        summary = (entry.findtext("atom:summary", default="", namespaces=NS) or "").strip().replace("\n", " ")
        published = entry.findtext("atom:published", default="", namespaces=NS)
        links = entry.findall("atom:link", NS)
        pdf = ""
        html_url = ""
        for link in links:
            href = link.attrib.get("href", "")
            title_attr = link.attrib.get("title", "")
            if title_attr == "pdf":
                pdf = href
            if href.startswith("http") and not html_url:
                html_url = href
        authors = [a.findtext("atom:name", default="", namespaces=NS) for a in entry.findall("atom:author", NS)]
        out.append(
            {
                "title": html.unescape(title),
                "summary": html.unescape(summary),
                "published": published,
                "authors": ", ".join(a for a in authors if a),
                "html": html_url,
                "pdf": pdf,
            }
        )
    return out


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("query")
    parser.add_argument("--max-results", type=int, default=5)
    args = parser.parse_args()

    xml_text = fetch(args.query, args.max_results)
    entries = parse(xml_text)

    print(f"# arXiv search: {args.query}\n")
    for i, entry in enumerate(entries, start=1):
        print(f"## {i}. {entry['title']}")
        print(f"- **Published:** {entry['published']}")
        print(f"- **Authors:** {entry['authors']}")
        print(f"- **Paper:** {entry['html']}")
        if entry['pdf']:
            print(f"- **PDF:** {entry['pdf']}")
        print(f"- **Summary:** {textwrap.shorten(entry['summary'], width=400, placeholder=' …')}")
        print()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
