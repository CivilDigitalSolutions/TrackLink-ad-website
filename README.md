# TrackLink Marketing Site — tracklink.civildigital.co.uk

Production static marketing site for **TrackLink**, a live GPS fleet-tracking
platform for small businesses (couriers, farms, trades, delivery and other
field-service teams), operated by Civil Digital. Published with GitHub Pages.
The repository root **is** the website root (no build step). Plain HTML + one
shared stylesheet, mirroring the structure of the BoatLog and Dispatch
marketing sites.

This repo (`CivilDigitalSolutions/TrackLink-ad-website`) is deliberately
separate from `CivilDigitalSolutions/TrackLink`, which is the **app** repo
description on GitHub (the actual Android/Firebase app lives locally at
`C:\Users\Tom\AndroidStudioProjects\GPS Tracker`, Firebase project
`tracklink-a9030`). Nothing in this repo touches that one.

## Structure

```
/
├── index.html                # Home page (hero, features, how it works, pricing, FAQ, CTA)
├── privacy/index.html        # Privacy Policy (placeholder — see callout on the page)
├── terms/index.html          # Terms & Conditions (placeholder — see callout on the page)
├── 404.html                  # Not-found page
├── CNAME                     # Pins tracklink.civildigital.co.uk
├── robots.txt / sitemap.xml
├── .nojekyll                 # So Pages doesn't run Jekyll processing over the site
├── images/
│   ├── favicon.png            # 48×48, generated from the real app icon
│   ├── apple-touch-icon.png   # 180×180, generated from the real app icon
│   └── og-default.png         # 1200×630 Open Graph banner, composed from the real logo assets
└── assets/
    ├── css/styles.css         # Shared stylesheet — TrackLink's real brand tokens
    ├── js/main.js             # Mobile nav toggle + footer year, progressive enhancement only
    └── brand/
        ├── tracklink-icon.png       # Master app icon (512×512, as supplied — "TL Favicon.png")
        ├── tracklink-icon-192.png   # 192×192 copy used in the OG banner composition
        ├── tracklink-wordmark.svg   # Master wordmark logo (vector, as supplied)
        └── tracklink-wordmark.png   # Raster copy of the wordmark, used to compose the OG banner
```

## Publish (GitHub Pages, deploy from root)

1. **Settings → Pages → Build and deployment → Deploy from a branch → `main` / `/ (root)`**.
2. **Settings → Pages → Custom domain:** `tracklink.civildigital.co.uk` — already pinned by the `CNAME` file.
3. **DNS** at your registrar: `tracklink` as `CNAME` → `civildigitalsolutions.github.io` (or your GitHub Pages target — confirm the exact org/user Pages hostname in the repo's Pages settings once enabled).
4. Enable **Enforce HTTPS** once the certificate provisions.

## App URL (single swap point) — needs owner attention

Every "Start free trial" button points at `https://app.tracklink.civildigital.co.uk`.
That domain is **not wired up yet**. As of this build:

- The **Hub web dashboard** is confirmed live in production at
  `https://tracklink-a9030.web.app` (Firebase Hosting), per the app repo's
  `CLAUDE.md` build log ("PRODUCTION WEB LIVE"). It is a **sign-in** surface
  (existing Hub accounts + new-org creation via the auth screen) — read+write
  for Hub users.
- The **Android app** (`com.tracklink.app`) is feature-complete and has a
  signed release build tested on physical devices, but per
  `PLAY_BILLING_DEPLOYMENT.md`'s own checklist, the **Play Console app/listing
  has not been created yet** — there is no public Play Store page to link to.
  Do not link to a Play Store URL until the owner confirms one exists.
- `app.tracklink.civildigital.co.uk` as a custom domain for the web Hub is
  **not yet configured** (no DNS record, no Firebase Hosting custom-domain
  link) — this mirrors the exact same open item the Dispatch marketing site
  flagged for `app.dispatch.civildigital.co.uk`.

**Owner action needed:** either (a) point `app.tracklink.civildigital.co.uk`
at the Firebase-hosted web Hub via a custom domain, or (b) tell me to swap
every "Start free trial" link to `https://tracklink-a9030.web.app` directly
until the custom domain exists. To change it, find-and-replace the exact
string `https://app.tracklink.civildigital.co.uk` across all HTML files — it
appears in the nav, hero, pricing card, CTA section and footer of every page.

Because public sign-up status was genuinely ambiguous at build time (backend
and billing are live in production, but the Play listing isn't public and the
marketing funnel isn't wired up), the site deliberately avoids "now live"
banner language and routes primary interest through the free-trial link *and*
a `mailto:info@civildigital.co.uk` fallback everywhere, so a visitor can
always reach a real human either way.

## Logo & brand assets

`assets/brand/tracklink-icon.png` and `assets/brand/tracklink-wordmark.svg`
are the owner-supplied, already-approved TrackLink brand assets, copied in
as-is from `C:\Users\Tom\AndroidStudioProjects\GPS Tracker\Images\` ("TL
Favicon.png" and "TrackLink Text Logo.svg" — the same files referenced by the
app's own `TRACKLINK_DESIGN_BUILD.md` §10 rebrand). `tracklink-icon-192.png`,
`images/favicon.png`, `images/apple-touch-icon.png` and `images/og-default.png`
were all generated from those master files via .NET `System.Drawing` (no
ImageMagick/PIL available in the build environment) — same technique used for
the Dispatch site's derived assets.

**To rebrand:** replace `tracklink-icon.png` and `tracklink-wordmark.svg`,
then regenerate the derived PNGs from them.

## Colour palette — sourced from the app repo, not invented

Every token in `assets/css/styles.css` is taken from the TrackLink app's own
"light rebrand" spec entry in `CLAUDE.md` (2026-07-14, spec §10) and matches
what's already live in the app and web Hub:

| Token | Hex | Used for |
|---|---|---|
| Ink / navy | `#14224E` | Headings, dark hero/footer gradient |
| Footer navy | `#0F1B3D` | Site-wide footer background |
| Brand blue | `#2F6BE4` | Primary royal blue, links, icons |
| Sky blue | `#70ABEC` | Secondary blue, banner background |
| Accent orange | `#F5821F` | CTA buttons |
| Background | `#F3F7FC` | Light section tint |

Typography leads with "Avenir Next" (per the same spec note — the Android
app itself stays on Roboto; this is a web-only choice) falling back to the
system font stack.

## Pricing — sourced from the app repo, not invented

Every figure on the pricing section is taken verbatim from
`PLAY_BILLING_DEPLOYMENT.md` §2 ("Subscription & base-plan pricing (spec
§8)") and cross-checked against `TRACKLINK_DESIGN_BUILD.md` §1/§2 and the
app's `CLAUDE.md` "Key product decisions" section — all three agree:

| Item | Monthly | Annual (~10×) |
|---|---|---|
| Base plan (1 Hub seat + 3 Track seats) | **£18** | £180 |
| +5 Track seats | **£25** | £250 |
| +10 Track seats | **£50** | £500 |
| +15 Track seats | **£75** | £750 |
| +2 Hub seats | **£12** | £120 |
| +4 Hub seats | **£24** | £240 |
| History retention add-on (30 → 365 days) | **£15 flat, org-wide** | ~£150 |

The 14-day free trial is granted server-side at org creation (no card
required), per the same source. The site does not show Stripe's ~10%-cheaper
web pricing (`web/src/pricing.ts`) since the app's own Android client
deliberately doesn't advertise it either (anti-steering, per `CLAUDE.md`) —
keeping the public site consistent with the product's own pricing-display
policy.

**Nothing on this page is a placeholder.** No feature or price was invented.

## Feature copy — sourced from the app repo

Feature descriptions are drawn from `TRACKLINK_DESIGN_BUILD.md` (system
overview, data model, groups, multi-Hub model, security rules) and the app's
`README.md` (implemented feature list: live tracking, live map, 24h/7d/30d
history, groups, org isolation). The "queues and flushes on reconnect" FAQ
answer and the "<5s upload-to-marker" / cadence stats in the hero card are
both real, sourced figures (spec §3 realtime-strategy and offline-behaviour
notes), not invented marketing numbers.

## Design notes

Design tokens and page structure are adapted directly from the Dispatch
marketing site (`assets/css/styles.css`), which itself carries the BoatLog
site's conventions forward — token-driven CSS, system font stack, accessible
FAQ via native `<details>`, mobile nav toggle as the only JS. Recoloured to
TrackLink's own brand (see palette table above) rather than reusing
Dispatch's navy/teal scheme.

## Quality floor

Responsive to mobile (no horizontal overflow at 375px), keyboard-focus
visible, `prefers-reduced-motion` respected, semantic headings, FAQ
accordions use native `<details>`. Only JS is the mobile nav toggle and
footer year — the whole site works with JavaScript disabled.
