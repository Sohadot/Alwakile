# Alwakile.com

Production-ready editorial landing page for the domain **Alwakile.com**; the concept is derived from the Arabic **الوكيل** (authorized agent). The brand is spelled **Alwakile**, always one word without a hyphen.

## Authoritative GitHub Pages publishing contract

The GitHub Pages deployment workflow actually builds from **`/docs`** (confirmed by the Pages build log on 2026-11-23). Earlier documentation assumed `/(root)`, causing the live domain to show the README before a configuration change, then the Pages Jekyll build to fail because `docs/` did not exist.

This release now publishes from **`main` → `/docs`**, with the following deployed files:
- `docs/index.html` — authoritative editorial acquisition landing page.
- `docs/og-card.png` — real 1200×630 social sharing image.
- `docs/favicon.svg`, `docs/robots.txt`, `docs/sitemap.xml` — supporting public assets.
- `docs/CNAME` — alwakile.com.
- `docs/.nojekyll` — static deployment without unintended theme transformations.

The repository root is **not** the web output; `README.md`, `scripts/`, and `.github/` are development files excluded from the published folder. No JavaScript build or framework dependencies are required.

**Canonical website:** https://alwakile.com/

## Brand and market positioning

**AI can act. Who gave it the authority?** The page explores the conceptual relationship between Arabic agency and the governance of AI agents: identity, delegated limits, revocation, and accountability. Markets are strategic applications for the name, not representations of a working technical standard, legal service, or operational SaaS.

Private acquisition inquiries: **agent@sohadot.com**. Escrow.com or another reputable independent escrow service may be used when mutually agreed and subject to provider terms.

## Social preview and release checks

The page references `https://alwakile.com/og-card.png` in Open Graph and X tags. This URL is correct **only if** GitHub Pages publishes `/docs` to the domain root, as configured.

The reproducible image renderer and static release checks are run from the repository root:

```sh
python -m pip install Pillow==11.3.0
python scripts/render_og.py
python scripts/verify_site.py
```

CI uses the same `docs/og-card.png` as the deployed site. GitHub Pages also deploys automatically upon changes to the selected branch. Verify the Pages build-and-deployment workflow after merging; application checks alone do **not** prove that Pages succeeded.

## Governance

Do not change the Pages publishing source to `/(root)` without moving or regenerating the site artifact to match. Do not duplicate live pages across root and docs. No invented customers, products, industry standards, transaction histories, tracking pixels, or artificial scarcity are represented.
