#!/usr/bin/env python3
"""Dependency-free release checks for the published static files."""
from pathlib import Path
from html.parser import HTMLParser
from struct import unpack

ROOT = Path(__file__).resolve().parents[1]
INDEX = ROOT / "docs" / "index.html"
source = INDEX.read_text(encoding="utf-8")

class Page(HTMLParser):
    def __init__(self):
        super().__init__()
        self.meta = []
        self.ids = set()
        self.hrefs = []
        self.title = False
        self.scripts = []
    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        if "id" in a:
            self.ids.add(a["id"])
        if tag == "meta":
            self.meta.append(a)
        if tag == "a":
            self.hrefs.append(a.get("href", ""))
        if tag == "script":
            self.scripts.append(a.get("src", ""))
        if tag == "title":
            self.title = True

page = Page()
page.feed(source)
assert page.title, "Missing page title"
assert 'lang="en"' in source, "Missing page language"
assert 'name="viewport"' in source, "Missing responsive viewport"
assert 'rel="canonical" href="https://alwakile.com/"' in source
assert 'Alwakile.com' in source and "الوكيل" in source
assert "Al-Wakile" not in source and "al-wakīl" not in source and "al-wakile" not in source.lower(), "Inconsistent branded spelling"
assert "Escrow.com" in source
assert "agent@sohadot.com" in source
for prop in ["og:title", "og:description", "og:image", "og:url", "og:image:width", "og:image:height"]:
    assert any(m.get("property") == prop and m.get("content") for m in page.meta), f"Missing {prop}"
for name in ["twitter:card", "twitter:image", "description"]:
    assert any(m.get("name") == name and m.get("content") for m in page.meta), f"Missing {name}"
for href in page.hrefs:
    if href.startswith("#"):
        assert href[1:] in page.ids, f"Broken anchor: {href}"
assert not any(s for s in page.scripts), "No external runtime scripts allowed"
for f in ["favicon.svg", "robots.txt", "sitemap.xml", "og-card.png"]:
    assert (ROOT / "docs" / f).is_file(), f"Missing deployed file: {f}"
with open(ROOT / "docs" / "og-card.png", "rb") as file:
    header = file.read(24)
assert header[:8] == b"\x89PNG\r\n\x1a\n", "OG card is not PNG"
assert unpack(">II", header[16:24]) == (1200, 630), "OG card must be 1200x630"
print("PASS: HTML identity, metadata, links, binary social image, static packaging")
