# TrackLink Marketing Site — tracklink.civildigital.co.uk

Production static marketing site for **TrackLink**, a live GPS tracking
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
├── index.html                # Home — hero + a summary of each section, linking out
├── features/index.html       # Features in detail (3 product screenshots)
├── how-it-works/index.html   # The Track/Hub model, walked through in 3 steps
├── pricing/index.html        # Full pricing: base plan, seat packs, add-ons
├── faq/index.html            # All 10 questions (carries the FAQPage schema)
├── privacy/index.html        # Privacy Policy
├── terms/index.html          # Terms & Conditions
├── 404.html                  # Not-found page
├── CNAME                     # Pins tracklink.civildigital.co.uk
├── robots.txt / sitemap.xml
├── site.webmanifest          # PWA/install metadata (name, icons, theme colour)
├── .nojekyll                 # So Pages doesn't run Jekyll processing over the site
├── tools/build-pages.py      # Optional page generator — see "Editing pages" below
├── images/
│   ├── favicon.png            # 48×48, generated from the real app icon
│   ├── apple-touch-icon.png   # 180×180, generated from the real app icon
│   ├── og-default.png         # 1200×630 Open Graph banner, composed from the real logo assets
│   └── product/               # Product UI imagery — see "Product imagery" below
│       ├── hub-live-map.{png,webp}
│       ├── hub-route-history.{png,webp}
│       └── track-app.{png,webp}
└── assets/
    ├── css/styles.css         # Shared stylesheet — TrackLink's real brand tokens
    ├── js/main.js             # Mobile nav toggle + footer year, progressive enhancement only
    └── brand/
        ├── tracklink-icon.png       # Master app icon (512×512, as supplied — "TL Favicon.png")
        ├── tracklink-icon-192.png   # 192×192 copy used in the OG banner composition
        ├── tracklink-wordmark.svg   # Master wordmark logo (vector, as supplied)
        └── tracklink-wordmark.png   # Raster copy of the wordmark, used to compose the OG banner
```

## Editing pages

The site is served as plain static HTML — there is no build step in the deploy
path, and you can edit any `.html` file directly and push.

There *is* an optional generator, `tools/build-pages.py`, which emits the five
marketing pages from one shared template so the header, footer and `<head>`
boilerplate cannot drift across eight files. Its output is what is committed.

```
python3 tools/build-pages.py
```

**It overwrites `index.html`, `features/`, `how-it-works/`, `pricing/` and
`faq/`.** If you hand-edit one of those, either port the change back into the
script or stop running it. `privacy/`, `terms/` and `404.html` are maintained
by hand — the script only patches their nav and footer links, rerunnably.

If you change the navigation, the footer or anything else in the page chrome,
doing it in the script and re-running is far less error-prone than editing
eight files.

## Product imagery — constructed renders, NOT screen captures

**Read this before treating the images in `images/product/` as photographs of
the running product.** They are HTML/SVG renders, built to match the app's own
design tokens and documented behaviour, then screenshotted headlessly. They
were produced this way because the build environment could not reach the live
Hub (`app.tracklink.civildigital.co.uk` and `tracklink-a9030.web.app` are both
outside its network policy, and the Hub is a sign-in surface in any case).

What that means in practice:

- **The layout is inferred, not observed.** Sidebar order, control placement
  and labelling are a reasonable reconstruction from `TRACKLINK_DESIGN_BUILD.md`
  and the feature list — they are not guaranteed to match what a Hub user
  actually sees. Check them against the real app before relying on them.
- **The data is invented and deliberately generic.** "Bedford Couriers",
  "Jamie M.", the speeds, battery levels and dwell times are made up. No real
  customer, employee or location appears in any of them.
- **The map is drawn, not tiled.** It is a generated SVG suggesting a UK market
  town, so there is no Google/Mapbox/OpenStreetMap tile licensing question and
  no third-party network request from the marketing site. Street names are
  Bedford's; the geometry is not.

**Replace them with real captures when you can** — a genuine screenshot of the
Hub will always be more convincing than a reconstruction, and removes the risk
of the site showing a UI that no longer matches the product. Drop the new files
in at the same paths and dimensions and nothing else needs to change; the
`<picture>` elements already prefer WebP with a PNG fallback.

Colours in the renders come from the same `--tl-*` tokens as the site, so they
stay consistent with the brand if the palette ever moves.

## SEO baseline

The site has had a technical SEO pass. What is in place, so it doesn't get
undone by accident:

- **One indexable page per URL**, each with a self-referencing `<link rel="canonical">`.
- **Titles** lead with the search term, brand last (`Live GPS Tracking for
  Small Business Teams | TrackLink`). **Meta descriptions** are kept under
  ~155 characters so Google doesn't truncate them.
- **Robots directives**: indexable pages carry
  `index, follow, max-image-preview:large, max-snippet:-1, max-video-preview:-1`
  (the `max-image-preview:large` is what allows a large thumbnail in results).
  `404.html` is `noindex, follow`.
- **Structured data** is a single consolidated `@graph` per page rather than
  several loose blocks, so nodes cross-reference by `@id`:
  `Organization` → `WebSite` → `WebPage` (+ `FAQPage` on the home page) →
  `SoftwareApplication` with monthly and annual `Offer`s. Every value is
  truthful and matches visible page copy — do not add `aggregateRating` or
  `review` unless real reviews exist; fabricated ones are a manual-action risk.
- **`sitemap.xml`** lists the seven indexable URLs with `lastmod` only —
  Google ignores `changefreq`/`priority`, so they were removed. **Update
  `lastmod` when you change a page.**
- **Images** carry `width`/`height` (no layout shift) and the hero mark uses
  the 192px asset rather than the 512px master.

- **One page per topic.** The home page was a single URL with anchor links,
  which meant features, pricing and the FAQ all competed for the same URL.
  Each now has its own page, its own title and its own canonical; the home
  page keeps a short summary of each and links out.
- **`position: sticky` needs care.** `html, body { overflow-x: hidden }` used
  to make `<body>` a scroll container, which silently stopped the header
  sticking. It is now `body { overflow-x: clip }` — do not change it back.

Still outstanding: an analytics tag (Search Console is registered, but there is
no GA4 or equivalent in the repo) and per-audience landing pages
(courier / farm / trades / field service).

## Publish (GitHub Pages, deploy from root)

1. **Settings → Pages → Build and deployment → Deploy from a branch → `main` / `/ (root)`**.
2. **Settings → Pages → Custom domain:** `tracklink.civildigital.co.uk` — already pinned by the `CNAME` file.
3. **DNS** at your registrar: `tracklink` as `CNAME` → `civildigitalsolutions.github.io` (or your GitHub Pages target — confirm the exact org/user Pages hostname in the repo's Pages settings once enabled).
4. Enable **Enforce HTTPS** once the certificate provisions.

## App URL (single swap point)

Every "Start free trial" button points at `https://app.tracklink.civildigital.co.uk`,
which the owner has confirmed is **live and serving the web Hub**.

To repoint it, find-and-replace the exact string
`https://app.tracklink.civildigital.co.uk` across all HTML files — it appears
in the nav, hero, pricing card, CTA section and footer of every page.

Do **not** link to a Play Store URL until the owner confirms the Play Console
listing exists; as of the last check it had not been created.

Every page also carries a `mailto:info@civildigital.co.uk` fallback alongside
the trial link, so a visitor can always reach a real human either way.

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

## Colour palette — verbatim from two live sources, not invented

Every `--tl-*` token in `assets/css/styles.css` is copied character-for-
character from two authoritative sources that agree exactly:

1. **Android app** — `app/src/main/java/com/tracklink/app/ui/theme/Color.kt`
   (the `TLBlue`/`TLSky`/`TLOrange`/`TLNavy`/... `Color(0xFFxxxxxx)` constants)
   and `Theme.kt` (`TrackLinkLightColors` — confirms `primary=TLBlue`,
   `secondary=TLSky`, `tertiary=TLOrange`).
2. **Live production web Hub** — fetched directly from
   `https://tracklink-a9030.web.app/assets/index-BBJIMeYW.css` at build time;
   its `:root{--tl-blue:#2f6be4; ...}` block is **byte-identical** to
   `web/src/theme.css` in the app repo, confirming there is no drift between
   source and what's actually deployed.

| Token | Hex | Source constant | Used for |
|---|---|---|---|
| `--tl-blue` | `#2F6BE4` | `TLBlue` / `--tl-blue` | Primary — links, icons, plan-card gradient start |
| `--tl-blue-container` | `#D9E7FB` | `TLBlueContainer` | Banner bg, feature-icon tiles, callouts |
| `--tl-sky` | `#70ABEC` | `TLSky` | Secondary — plan-card gradient end |
| `--tl-orange` | `#F5821F` | `TLOrange` | The one CTA colour (buttons) |
| `--tl-navy` | `#14224E` | `TLNavy` | Ink / heading text |
| `--tl-footer` | `#0F1B3D` | `--tl-footer` (web theme.css) | Site-footer bg — the app's one dark accent |
| `--tl-background` | `#F3F7FC` | `TLBackground` | Page/section background |
| `--tl-outline` | `#D6E0EC` | `TLOutline` | Borders |
| `--tl-text-secondary` | `#5B6B8C` | `TLTextSecondary` | Muted/body-secondary text |
| `--tl-online` / `--tl-amber` / `--tl-offline` | `#2E9E5B` / `#D9922F` / `#8C96A6` | status colours | (reserved; not currently used on the marketing site) |
| `--tl-error` | `#B3261E` | Material default error | Error text (unused on this site currently) |

**Corrected from the previous build:** `--line`/border, `--muted` and
`--error` had been approximated to nearby-but-wrong hex values
(`#E4E8F0`, `#5B6577`, `#b91c1c`) instead of the product's actual
`#D6E0EC`, `#5B6B8C`, `#B3261E` — now fixed to exact source values.
`--brand-dark`/`--accent-dark` (hover-state shades) and `--focus` remain the
only non-product tokens, clearly commented as such in the CSS — the app's
Material theme doesn't define hover/focus colours for a static site to reuse.

## Design language — matches the real product, not reused from Dispatch/BoatLog

The first build borrowed Dispatch's dark-navy-hero template wholesale. That
was wrong on its own terms: `Theme.kt` says outright **"there is intentionally
no dark scheme; the brand is the light blue/white look with orange CTAs"**,
and `web/src/theme.css` explicitly calls the footer band **"the light theme's
single dark accent, coordinated with the marketing site"** — i.e. the footer
is deliberately the *only* dark surface anywhere in the real product. So this
build:

- **Hero**: light (`--tl-background` + a soft `--tl-blue-container` radial
  wash), white elevated card — not a navy gradient.
- **Page headers** (privacy/terms breadcrumb band): light, matching the
  app/web's actual `.topbar` (`background: var(--tl-card)`, white) rather than
  a dark strip.
- **Pricing highlight card**: brand-blue → sky gradient (the app's actual
  primary/secondary pair), not navy.
- **Footer**: navy `#0F1B3D` — the ONE dark section on the whole site,
  exactly matching the real product's "single dark accent" design intent.
- **Buttons**: 16px rounded rectangles (`--radius-btn`, matching the real
  app/web `.btn { border-radius: 16px }`), not fully-pill shapes — Dispatch
  and BoatLog both use pill buttons, so this alone reads differently at a
  glance.
- **OG banner** (`images/og-default.png`): regenerated light-first (white
  card on a pale blue wash) to match, replacing the earlier dark-navy banner
  that looked identical in spirit to Dispatch's.

TrackLink's navy (`#14224E`) and Dispatch's navy (`#0B1F3A`) are genuinely
different hex values from different real products — kept as each product's
own truth — but the *structural* fix above is what actually makes the two
sites stop reading as the same template in different colours.

Typography leads with "Avenir Next" (per `Theme.kt`'s font-family comment and
`web/src/theme.css`'s `font-family` declaration verbatim — the Android app
itself stays on Roboto; Avenir Next is a web-only choice already made by the
real web Hub) falling back to the system font stack.

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
