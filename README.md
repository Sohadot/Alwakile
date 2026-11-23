# Alwakile.com

**Alwakile.com** is an acquisition landing page for the domain name, rooted in the Arabic **الوكيل** (the authorized representative). The brand is always written **Alwakile** as one word, without a hyphen.

## Deployment — GitHub Pages

The main production URL is **https://alwakile.com/**. GitHub Pages has been switched between **main / (root)** and **main / docs** during setup. When the selected directory did not contain `index.html`, Jekyll published the repository's README as the homepage.

To make both choices safe, the same landing page and assets are committed into **the repository root** and **docs/**. The root is the preferred publishing source; both are verified together in CI. GitHub Pages itself only publishes the *one* folder selected under Settings → Pages. Do not mistake a successful GitHub Action for a successful Pages publication.

Each publish folder contains:
- `index.html`: actual styled landing page, not this README.
- `og-card.png`: 1200 × 630 PNG used by LinkedIn, Facebook and X.
- `favicon.svg`, `robots.txt`, `sitemap.xml`: identity and discovery assets.
- `CNAME`: `alwakile.com`.
- `.nojekyll`: bypass the Jekyll README-as-index converter.

When publishing the repository root, the nested `/docs/` is not meant as a separate site. Both pages carry the canonical URL `https://alwakile.com/`; robots.txt discourages indexing the duplicate `/docs/` path.

**Recommended GitHub Pages source: Deploy from a branch → main → /(root).** The alternative `/docs` is supported by the mirrored assets as a fallback, not an instruction to toggle settings repeatedly.

## Copy and acquisition

Headline: **AI can act. Who gave it the authority?**

The site offers the **domain**, not a deployed AI product, certification or legal service. Contact: **agent@sohadot.com**. Escrow.com or another mutually agreed independent escrow provider may be used, subject to the provider's eligibility and terms.

## Release process

The generator writes identical images to both publication folders. The verifier checks metadata, canonical URL, links, the image signature and dimensions, plus strict equivalence of public files across both folders.

```sh
python -m pip install Pillow==11.3.0
python scripts/render_og.py
python scripts/verify_site.py
```

After merging, check the **pages build and deployment** workflow specifically, then confirm the domain's actual HTML `<title>` contains “The Authorized Agent,” not the README's GitHub-generated title. Also verify the live URL `https://alwakile.com/og-card.png` returns image/png. DNS/TLS and social card caches must be verified independently.
