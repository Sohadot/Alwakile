#!/usr/bin/env python3
"""Check both GitHub Pages publication modes and prevent serving README.md as home."""
from pathlib import Path
from html.parser import HTMLParser
from struct import unpack

ROOT = Path(__file__).resolve().parents[1]

class Page(HTMLParser):
    def __init__(self):
        super().__init__()
        self.meta = []
        self.ids = set()
        self.hrefs = []
        self.title = False
        self.scripts = []
    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if "id" in attrs:
            self.ids.add(attrs["id"])
        if tag == "meta":
            self.meta.append(attrs)
        if tag == "a":
            self.hrefs.append(attrs.get("href", ""))
        if tag == "script":
            self.scripts.append(attrs.get("src", ""))
        if tag == "title":
            self.title = True

for folder in (ROOT, ROOT/"docs"):
    index = folder/"index.html"
    assert index.is_file(), f"Missing landing homepage: {index}; README must never be used as index"
    content = index.read_text(encoding="utf-8")
    page = Page()
    page.feed(content)
    assert content.lower().startswith("<!doctype html>") and page.title
    assert 'lang="en"' in content and 'name="viewport"' in content
    assert 'rel="canonical" href="https://alwakile.com/"' in content
    assert 'Alwakile.com' in content and "الوكيل" in content
    assert 'Who gave it the authority?' in content
    assert not any(s in content for s in ("Al-Wakile", "al-wakīl", "al-wakile"))
    assert "Escrow.com" in content and "agent@sohadot.com" in content
    for prop in ("og:title", "og:description", "og:image", "og:url", "og:image:width", "og:image:height"):
        assert any(m.get("property") == prop and m.get("content") for m in page.meta), f"Missing {prop}: {index}"
    for name in ("twitter:card", "twitter:image", "description"):
        assert any(m.get("name") == name and m.get("content") for m in page.meta), f"Missing {name}: {index}"
    assert 'https://alwakile.com/og-card.png' in content
    assert all(href[1:] in page.ids for href in page.hrefs if href.startswith("#")), f"Broken anchor in {index}"
    assert not any(page.scripts), f"Unexpected script in {index}"
    assert (folder/"CNAME").read_text(encoding="utf-8").strip()=="alwakile.com"
    assert (folder/".nojekyll").is_file(), f"Missing .nojekyll marker: {folder}"
    for name in ("favicon.svg", "robots.txt", "sitemap.xml", "og-card.png"):
        assert (folder/name).is_file(), f"Missing {name} in {folder}"
    with (folder/"og-card.png").open("rb") as image:
        h=image.read(24)
    assert h[:8] == b"\x89PNG\r\n\x1a\n" and unpack(">II",h[16:24]) == (1200,630)
for name in ("index.html","og-card.png","favicon.svg","robots.txt","sitemap.xml","CNAME"):
    assert (ROOT/name).read_bytes()==(ROOT/"docs"/name).read_bytes(), f"Root/docs drift: {name}"
print("PASS: both root and docs can publish the same Alwakile landing, CNAME and OG preview")
