# Alwakile.com

A static-first editorial acquisition landing page for the **Alwakile.com** domain. Its meaning derives from the Arabic **الوكيل** (the authorized representative). The commercial name is spelled **Alwakile**, one word, with no hyphen.

## Positioning

**AI can act. Who gave it the authority?**

The site explores the role of identity, scope, delegation, revocation and accountability as AI agents act on behalf of people and organizations. The illustrated markets are potential uses of the name — not operating Alwakile products, standards, certifications, or legal services.

## Publish

Deploy the repository root as a static site at **https://alwakile.com/**, for example through Cloudflare Pages (no frontend build step required). Serve `index.html`, `favicon.svg`, `og-card.png`, `robots.txt`, and `sitemap.xml` from the web root.

The source design is intentionally implemented as accessible HTML/CSS without the exported React mockup runtime. The external fonts are optional and have local fallbacks.

## Social preview

Use `og-card.png`, a real **1200 × 630 PNG**, for Open Graph and X previews. It is generated from the reproducible source `scripts/render_og.py`. On CI, `.github/workflows/site-quality.yml` renders the card, validates the site, and commits the card if changed. For local generation:

```sh
python -m pip install 'Pillow==11.3.0'
python scripts/render_og.py
python scripts/verify_site.py
```

After DNS/TLS is active, validate the canonical URL and refresh social-platform caches using LinkedIn Post Inspector and Facebook Sharing Debugger.

## Acquisition

Private inquiries: **agent@sohadot.com**. A secure escrow service such as **Escrow.com** may be used by mutual agreement, subject to provider eligibility and terms. This does not assert a current listing or escrow arrangement. The offered asset is the **domain name**, not a deployed AI authority platform.

## Governance

No unverified product functionality, certification claims, invented partners, false scarcity, analytics trackers or bulk programmatic SEO. The public root holds only site delivery files; development and documentation files remain in the repository, not an automatically exposed production directory when deploying.
