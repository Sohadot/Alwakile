# Alwakile.com

The canonical strategic-acquisition landing page for **Alwakile.com**, rooted in the Arabic **الوكيل** (the authorized agent). The domain brand is one word, **Alwakile**, without a hyphen.

## Public website

**Live address:** https://alwakile.com/

**Hosting:** GitHub Pages from `main` / `(root)`, with `CNAME` specifying `alwakile.com`.

The public landing page is **`/index.html` at the repository root**, not this README and not `public/index.html`. This location matches the actual GitHub Pages source settings.

The page is static HTML/CSS with no application build step. Its only optional remote dependencies are fonts (with local fallback); there are no user-tracking scripts or forms.

## Brand and acquisition

**AI can act. Who gave it the authority?**

The page describes the name's potential relevance to agent identity, delegation, least-privilege authority, revocation and accountability; these are positioning opportunities, not claims of a live platform, industry standard or legal offering.

Private acquisition inquiries: **agent@sohadot.com**.

An independent escrow arrangement such as **Escrow.com** may be used with mutual agreement, subject to provider eligibility and terms. No fixed price, active escrow transaction or platform is represented.

## Social sharing

The actual PNG image at `/og-card.png` (1200×630) must remain in the repository root because the HTML references **https://alwakile.com/og-card.png** in Open Graph and X cards. The SVG favicon and sitemap/robots files also reside at the repository root.

The image renderer is versioned in `scripts/render_og.py`, and the deployment checks are in `scripts/verify_site.py`:

```sh
python -m pip install Pillow==11.3.0
python scripts/render_og.py
python scripts/verify_site.py
```

The GitHub Actions workflow generates and checks the image; on the configured push branch it can commit updates to `og-card.png` when needed. The source page and scripts should not be represented as operational products.

## Release verification

Check https://alwakile.com/ directly for the styled landing page, check https://alwakile.com/og-card.png for a **real image**, and confirm the canonical URL and social metadata. LinkedIn/Facebook/X previews need a live URL and may be cached externally.

## Deployment contract

GitHub Pages source: **Deploy from a branch** → `main` → `/(root)`. Do not change the publishing folder to `public`, which is not a supported branch-subdirectory selection in GitHub Pages. If hosting moves to Cloudflare Pages in the future, revisit the deployment contract explicitly.
