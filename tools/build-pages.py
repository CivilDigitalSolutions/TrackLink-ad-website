#!/usr/bin/env python3
"""Emit the TrackLink marketing pages from one shared chrome template.

    python3 tools/build-pages.py

The published site is still plain static HTML with no build step: this script
is run by hand and its OUTPUT is what gets committed and served. It exists so
the header, footer and <head> boilerplate cannot drift across eight pages.

!! IT OVERWRITES index.html, features/, how-it-works/, pricing/, faq/, guides/ and sitemap.xml !!

The guides (2026-09-19) are content in tools/guides/*.py — one module per topic hub, with every
price and product claim taken from tools/guides/facts.py — rendered by this script into
/guides/ and /guides/<slug>/.

So if you hand-edit any of those five files, either port the change back into
this script or stop using the script. It only patches (rather than rewrites)
privacy/, terms/ and 404.html, whose bodies are maintained by hand; those
patches are rerunnable and touch the nav and footer links only.
"""
import json, os, pathlib, re

ROOT = pathlib.Path(__file__).resolve().parent.parent
BASE = "https://tracklink.civildigital.co.uk"
APP = "https://app.tracklink.civildigital.co.uk"
# Where "Start free trial" goes (2026-09-19). It used to be APP, which is the Hub SIGN-IN page: a
# new visitor could not create an organisation there. /signup creates the account + org + trial.
SIGNUP = APP + "/signup"
OG = BASE + "/images/og-default.png"

NAV = [
    ("/features/", "Features"),
    ("/how-it-works/", "How it works"),
    ("/pricing/", "Pricing"),
    ("/faq/", "FAQ"),
    ("/guides/", "Guides"),
]

BANNER = ('<strong>Free trial</strong> &nbsp;&bull;&nbsp; 14 days free '
          '&mdash; no card required to start.')

ROBOTS = ('<meta name="robots" content="index, follow, max-image-preview:large, '
          'max-snippet:-1, max-video-preview:-1">')


# --------------------------------------------------------------------------
# shared chrome
# --------------------------------------------------------------------------

def head(title, desc, path, extra_schema, og_title=None, og_desc=None):
    url = BASE + path
    og_title = og_title or title
    og_desc = og_desc or desc
    return f"""<!DOCTYPE html>
<html lang="en-GB">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{title}</title>
  <meta name="description" content="{desc}">
  <link rel="canonical" href="{url}">
  {ROBOTS}
  <meta name="theme-color" content="#14224E">

  <!-- Open Graph -->
  <meta property="og:type" content="website">
  <meta property="og:site_name" content="TrackLink">
  <meta property="og:locale" content="en_GB">
  <meta property="og:title" content="{og_title}">
  <meta property="og:description" content="{og_desc}">
  <meta property="og:url" content="{url}">
  <meta property="og:image" content="{OG}">
  <meta property="og:image:type" content="image/png">
  <meta property="og:image:width" content="1200">
  <meta property="og:image:height" content="630">
  <meta property="og:image:alt" content="TrackLink — live GPS tracking for teams">
  <meta name="twitter:card" content="summary_large_image">
  <meta name="twitter:title" content="{og_title}">
  <meta name="twitter:description" content="{og_desc}">
  <meta name="twitter:image" content="{OG}">
  <meta name="twitter:image:alt" content="TrackLink — live GPS tracking for teams">

  <link rel="icon" href="/images/favicon.png" type="image/png" sizes="48x48">
  <link rel="apple-touch-icon" href="/images/apple-touch-icon.png" sizes="180x180">
  <link rel="manifest" href="/site.webmanifest">
  <link rel="stylesheet" href="/assets/css/styles.css">
  <script type="application/ld+json">
{json.dumps(extra_schema, ensure_ascii=False, indent=2)}
  </script>
</head>
<body>
  <a class="skip-link" href="#main">Skip to main content</a>

  <div class="banner">
    {BANNER}
  </div>
"""


def header(path):
    links = []
    for href, label in NAV:
        cur = ' aria-current="page"' if href == path else ""
        links.append(f'        <li><a href="{href}"{cur}>{label}</a></li>')
    links = "\n".join(links)
    return f"""
  <header class="site-header">
    <nav class="container nav" aria-label="Primary">
      <a class="brand" href="/" aria-label="TrackLink home">
        <img class="brand__wordmark" src="/assets/brand/tracklink-wordmark.svg" alt="TrackLink" width="128" height="26">
      </a>
      <button class="nav__toggle" aria-expanded="false" aria-controls="primary-nav">
        <svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" aria-hidden="true"><line x1="3" y1="6" x2="21" y2="6"/><line x1="3" y1="12" x2="21" y2="12"/><line x1="3" y1="18" x2="21" y2="18"/></svg>
        <span class="visually-hidden">Menu</span>
      </button>
      <ul class="nav__links" id="primary-nav">
{links}
        <li class="nav__cta"><a class="btn btn--primary" href="{SIGNUP}">Start free trial</a></li>
      </ul>
    </nav>
  </header>

  <main id="main">
"""


FOOTER = f"""
  </main>

  <footer class="site-footer">
    <div class="container">
      <div class="footer-grid">
        <div class="footer-brand">
          <a class="brand" href="/" aria-label="TrackLink home">
            <img class="brand__wordmark" src="/assets/brand/tracklink-wordmark.svg" alt="TrackLink" width="128" height="26">
          </a>
          <p>Live GPS tracking, a real-time team map and route history for small businesses. TrackLink is operated by Civil Digital.</p>
        </div>
        <nav aria-label="Product">
          <h2>Product</h2>
          <ul class="footer-links">
            <li><a href="/features/">Features</a></li>
            <li><a href="/how-it-works/">How it works</a></li>
            <li><a href="/pricing/">Pricing</a></li>
            <li><a href="/faq/">FAQ</a></li>
            <li><a href="/guides/">Guides</a></li>
            <li><a href="{SIGNUP}">Start free trial</a></li>
          </ul>
        </nav>
        <div>
          <h2>Contact Info</h2>
          <ul class="footer-links">
            <li><a href="mailto:info@civildigital.co.uk">info@civildigital.co.uk</a></li>
            <li><a href="https://wa.me/447568296136">WhatsApp: +44 7568 296136</a></li>
            <li>Bedford, United Kingdom</li>
            <li><a href="/privacy/">Privacy Policy</a></li>
            <li><a href="/terms/">Terms</a></li>
            <li><a href="/delete-account/">Delete your account</a></li>
          </ul>
        </div>
      </div>
      <div class="footer-bottom">
        <p>&copy; <span id="year">2026</span> TrackLink &mdash; operated by Civil Digital. All rights reserved.</p>
        <p>Track with certainty. Link with trust.</p>
      </div>
    </div>
  </footer>

  <script src="/assets/js/main.js" defer></script>
</body>
</html>
"""


def cta(heading, para):
    return f"""
    <section class="section" id="trial" aria-labelledby="trial-h">
      <div class="container">
        <div class="cta">
          <h2 id="trial-h">{heading}</h2>
          <p>{para}</p>
          <div class="cta__actions">
            <a class="btn btn--primary btn--lg" href="{SIGNUP}">Start free trial</a>
            <a class="btn btn--ghost btn--lg" href="mailto:info@civildigital.co.uk">Talk to us first</a>
          </div>
        </div>
      </div>
    </section>
"""


def page_head(crumb, h1, sub):
    return f"""
    <div class="page-head">
      <div class="container">
        <nav class="breadcrumb" aria-label="Breadcrumb">
          <ol>
            <li><a href="/">Home</a></li>
            <li>{crumb}</li>
          </ol>
        </nav>
        <h1>{h1}</h1>
        <p>{sub}</p>
      </div>
    </div>
"""


IMAGES = {
    "map": ("hub-live-map", 2240, 1400, "TrackLink Hub &mdash; live team map",
            "The TrackLink Hub live map: five tracked devices on one map with a device list showing speed, group, battery and last-seen time."),
    "route": ("hub-route-history", 2240, 1400, "TrackLink Hub &mdash; route history",
              "The TrackLink Hub route history view: a full day's route with numbered stops, dwell times, distance, moving time and speed."),
    "phone": ("track-app", 680, 1330, "The TrackLink Track app",
              "The TrackLink Track app on a phone, showing tracking switched on, the update-interval selector and the ongoing notification."),
}


ZOOM_CUE = (
    '<span class="shot__cue" aria-hidden="true">'
    '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">'
    '<circle cx="11" cy="11" r="7"/><path d="M20 20l-3.6-3.6M11 8.4v5.2M8.4 11h5.2" stroke-linecap="round"/>'
    '</svg></span>')


def shot(key, bar_label, caption=None, eager=False, phone=False):
    """A framed screenshot that opens full size in a lightbox when clicked.

    The wrapper is a real <a> to the full-resolution file, so with JavaScript
    off a click still opens the image — main.js only intercepts it."""
    base, w, h, title, alt = IMAGES[key]
    cls = "shot shot--phone" if phone else "shot"
    bar = "" if phone else (
        '<div class="shot__bar" aria-hidden="true"><span></span><span></span><span></span>'
        f'<em>{bar_label}</em></div>')
    loading = ('loading="eager" fetchpriority="high"' if eager
               else 'loading="lazy"')
    cap = f'\n            <figcaption>{caption}</figcaption>' if caption else ""
    return f"""<figure class="{cls}">
            <div class="shot__frame">{bar}
              <a class="shot__zoom" href="/images/product/{base}.png"
                 data-webp="/images/product/{base}.webp" data-title="{title}"
                 aria-label="View a larger version: {title}">
                <picture>
                  <source srcset="/images/product/{base}.webp" type="image/webp">
                  <img src="/images/product/{base}.png" alt="{alt}" width="{w}" height="{h}" {loading} decoding="async">
                </picture>
                {ZOOM_CUE}
              </a>
            </div>{cap}
          </figure>"""


# --------------------------------------------------------------------------
# schema nodes
# --------------------------------------------------------------------------

ORG = {
    "@type": "Organization",
    "@id": BASE + "/#organization",
    "name": "Civil Digital",
    "alternateName": "Civil Digital Solutions",
    "url": "https://civildigital.co.uk/",
    "logo": {
        "@type": "ImageObject", "@id": BASE + "/#logo",
        "url": BASE + "/assets/brand/tracklink-icon.png",
        "width": 512, "height": 512,
        "caption": "TrackLink, a product of Civil Digital",
    },
    "image": {"@id": BASE + "/#logo"},
    "email": "info@civildigital.co.uk",
    "telephone": "+44 7568 296136",
    "address": {"@type": "PostalAddress", "addressLocality": "Bedford", "addressCountry": "GB"},
    "contactPoint": [{
        "@type": "ContactPoint", "contactType": "customer support",
        "email": "info@civildigital.co.uk", "telephone": "+44 7568 296136",
        "areaServed": "GB", "availableLanguage": ["en-GB"],
    }],
    "sameAs": ["https://civildigital.co.uk/"],
}

SITE = {
    "@type": "WebSite",
    "@id": BASE + "/#website",
    "name": "TrackLink",
    "url": BASE + "/",
    "description": "Live GPS tracking, a real-time team map and route history for small businesses.",
    "inLanguage": "en-GB",
    "publisher": {"@id": BASE + "/#organization"},
}

APP_NODE = {
    "@type": "SoftwareApplication",
    "@id": BASE + "/#app",
    "name": "TrackLink",
    "url": BASE + "/",
    "applicationCategory": "BusinessApplication",
    "applicationSubCategory": "GPS tracking",
    "operatingSystem": "Android, Web",
    "inLanguage": "en-GB",
    "image": OG,
    "screenshot": [
        BASE + "/images/product/hub-live-map.png",
        BASE + "/images/product/hub-route-history.png",
        BASE + "/images/product/track-app.png",
    ],
    "description": "TrackLink is a lightweight GPS tracking platform for small businesses — couriers, farms, trades, delivery and field services. Track users share live GPS location; Hub users see every device on a live map, review route history and manage their team.",
    "featureList": [
        "Live GPS tracking with background location upload",
        "Real-time team map for every device in the organisation",
        "Route history for the last 24 hours, 7 days or 30 days",
        "Custom groups and map filtering",
        "Multiple Hub (admin) users per organisation",
        "Per-organisation data isolation enforced in database security rules",
    ],
    "offers": [
        {
            "@type": "Offer", "name": "Base plan — monthly",
            "price": "16.00", "priceCurrency": "GBP",
            "url": BASE + "/pricing/",
            "availability": "https://schema.org/InStock",
            "description": "Base plan: 1 Hub seat + 3 Track seats, billed monthly, includes a 14-day free trial.",
            "priceSpecification": {
                "@type": "UnitPriceSpecification", "price": "16.00",
                "priceCurrency": "GBP", "billingIncrement": 1, "unitCode": "MON",
            },
            "seller": {"@id": BASE + "/#organization"},
        },
        {
            "@type": "Offer", "name": "Base plan — annual",
            "price": "160.00", "priceCurrency": "GBP",
            "url": BASE + "/pricing/",
            "availability": "https://schema.org/InStock",
            "description": "Base plan billed annually: 1 Hub seat + 3 Track seats, two months free versus monthly billing.",
            "priceSpecification": {
                "@type": "UnitPriceSpecification", "price": "160.00",
                "priceCurrency": "GBP", "billingIncrement": 1, "unitCode": "ANN",
            },
            "seller": {"@id": BASE + "/#organization"},
        },
    ],
    "publisher": {"@id": BASE + "/#organization"},
    "provider": {"@id": BASE + "/#organization"},
}


def webpage(path, name, desc, crumb=None, types="WebPage", about=None):
    url = BASE + path
    node = {
        "@type": types,
        "@id": url + "#webpage",
        "url": url,
        "name": name,
        "description": desc,
        "isPartOf": {"@id": BASE + "/#website"},
        "about": {"@id": about or (BASE + "/#app")},
        "inLanguage": "en-GB",
        "primaryImageOfPage": {"@type": "ImageObject", "url": OG, "width": 1200, "height": 630},
    }
    if crumb:
        node["breadcrumb"] = {"@id": url + "#breadcrumb"}
    return node


def breadcrumb(path, crumb):
    url = BASE + path
    return {
        "@type": "BreadcrumbList",
        "@id": url + "#breadcrumb",
        "itemListElement": [
            {"@type": "ListItem", "position": 1, "name": "Home", "item": BASE + "/"},
            {"@type": "ListItem", "position": 2, "name": crumb, "item": url},
        ],
    }


def graph(nodes):
    return {"@context": "https://schema.org", "@graph": nodes}


# --------------------------------------------------------------------------
# shared content fragments
# --------------------------------------------------------------------------

FEATURE_CARDS = {
    "tracking": ("""<svg viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
                <path d="M12 21s-7-6.2-7-11a7 7 0 0 1 14 0c0 4.8-7 11-7 11z" stroke="#14224E" stroke-width="1.8"/>
                <circle cx="12" cy="10" r="2.6" stroke="#2F6BE4" stroke-width="1.8"/>
              </svg>""", "Live GPS tracking",
     "Track users toggle tracking on and forget it &mdash; a persistent notification confirms it&rsquo;s running while location uploads in the background at a chosen interval."),
    "map": ("""<svg viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
                <rect x="3.5" y="5" width="17" height="14" rx="2.5" stroke="#14224E" stroke-width="1.8"/>
                <circle cx="9" cy="12" r="2.2" stroke="#2F6BE4" stroke-width="1.8"/>
                <path d="M14 10.5h4M14 13.5h4" stroke="#2F6BE4" stroke-width="1.8" stroke-linecap="round"/>
              </svg>""", "Live team map",
     "Hub users see every device on one map, refreshing automatically, with under 5-second latency from upload to marker move &mdash; no manual refresh needed."),
    "history": ("""<svg viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
                <circle cx="6" cy="19" r="2.4" stroke="#14224E" stroke-width="1.8"/>
                <circle cx="18" cy="5" r="2.4" stroke="#14224E" stroke-width="1.8"/>
                <path d="M8 19h7a4 4 0 0 0 0-8H9a4 4 0 0 1 0-8h1" stroke="#2F6BE4" stroke-width="1.8" stroke-linecap="round"/>
              </svg>""", "Route history",
     "Review the last 24 hours, 7 days or 30 days for any device &mdash; a full route with stats, kept for 30 days."),
    "groups": ("""<svg viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
                <circle cx="8.5" cy="8" r="3" stroke="#14224E" stroke-width="1.8"/>
                <circle cx="17" cy="9.5" r="2.4" stroke="#14224E" stroke-width="1.8"/>
                <path d="M3.5 19c.5-3 2.7-4.5 5-4.5s4.5 1.5 5 4.5" stroke="#2F6BE4" stroke-width="1.8" stroke-linecap="round"/>
                <path d="M14.5 19c.4-2.2 1.9-3.4 3.5-3.4" stroke="#2F6BE4" stroke-width="1.8" stroke-linecap="round"/>
              </svg>""", "Custom groups",
     "Organise Track users into your own groups &mdash; &ldquo;Morning shift&rdquo;, &ldquo;North round&rdquo;, whatever fits &mdash; then filter the map and device list by group in one tap."),
    "hubs": ("""<svg viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
                <rect x="4" y="3" width="16" height="18" rx="2" stroke="#14224E" stroke-width="1.8"/>
                <path d="M7.5 8h9M7.5 12h9M7.5 16h5.5" stroke="#14224E" stroke-width="1.8" stroke-linecap="round"/>
                <path d="M16 15.5l1.6 1.6L21 13.5" stroke="#2F6BE4" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"/>
              </svg>""", "Multi-Hub organisations",
     "Add as many Hub (admin) users as you need &mdash; every Hub sees every device, so dispatchers and managers all work from the same live picture."),
    "isolation": ("""<svg viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
                <path d="M12 3l7 3v6c0 4.5-3 7.5-7 9-4-1.5-7-4.5-7-9V6l7-3z" stroke="#14224E" stroke-width="1.8" stroke-linejoin="round"/>
                <path d="M9 12l2 2 4-4" stroke="#2F6BE4" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"/>
              </svg>""", "Isolated by design",
     "Every organisation&rsquo;s data is walled off in the database&rsquo;s own security rules &mdash; not just filtered on screen &mdash; so one business can never see another&rsquo;s."),
}


def cards(keys):
    out = []
    for k in keys:
        icon, title, body = FEATURE_CARDS[k]
        out.append(f"""
          <article class="card">
            <span class="card__icon" aria-hidden="true">
              {icon}
            </span>
            <h3>{title}</h3>
            <p>{body}</p>
          </article>""")
    return "\n".join(out)


PLAN_CARD = f"""
        <div class="plan-card">
          <div>
            <h3>Base plan</h3>
            <div class="plan-card__amount">&pound;16<small>/month</small></div>
            <p class="plan-card__note">or &pound;160/year (2 months free)</p>
            <ul class="plan-card__features">
              <li>1 Hub seat</li>
              <li>3 Track seats</li>
              <li>Live map &amp; route history</li>
              <li>Custom groups</li>
              <li>30-day history included</li>
              <li>All features included</li>
            </ul>
          </div>
          <div class="plan-card__cta">
            <a class="btn btn--primary btn--lg" href="{SIGNUP}">Start free trial</a>
            <span class="plan-card__trial">14 days free, no card required</span>
          </div>
        </div>
"""

ADDONS = """
        <div class="addons-grid">
          <div class="addon-card">
            <h4>Track seat packs</h4>
            <p class="addon-rate">&pound;4.40 per seat / month</p>
            <table>
              <caption class="visually-hidden">Track seat pack pricing</caption>
              <tr><td>+5 Track seats</td><td>&pound;22/mo</td></tr>
              <tr><td>+10 Track seats</td><td>&pound;44/mo</td></tr>
              <tr><td>+15 Track seats</td><td>&pound;66/mo</td></tr>
              <tr><td>Each seat beyond +15</td><td>&pound;5/mo</td></tr>
            </table>
          </div>
          <div class="addon-card">
            <h4>Hub seat packs</h4>
            <p class="addon-rate">&pound;5.50 per seat / month</p>
            <table>
              <caption class="visually-hidden">Hub seat pack pricing</caption>
              <tr><td>+2 Hub seats</td><td>&pound;11/mo</td></tr>
              <tr><td>+4 Hub seats</td><td>&pound;22/mo</td></tr>
              <tr><td>Each seat beyond +4</td><td>&pound;6/mo</td></tr>
            </table>
          </div>
          <div class="addon-card">
            <h4>Route history</h4>
            <p class="addon-rate">Included</p>
            <table>
              <caption class="visually-hidden">Route history retention</caption>
              <tr><td>30 days of history</td><td>Included</td></tr>
              <tr><td>Need longer?</td><td><a href="mailto:info@civildigital.co.uk">Ask us</a></td></tr>
            </table>
          </div>
        </div>
"""

FAQS = [
    ("Is TrackLink available yet?",
     f"Yes. <a href=\"{SIGNUP}\">Create your organisation</a> on the web and start a 14-day free trial &mdash; no card needed &mdash; then invite your team. The people being tracked use the TrackLink Android app; managers use the web dashboard or the app.",
     "Yes. Create your organisation on the web and start a 14-day free trial — no card needed — then invite your team. The people being tracked use the TrackLink Android app; managers use the web dashboard or the app."),
    ("Do I need a tracker box or any hardware?",
     "No. TrackLink runs on the phone your team member already carries &mdash; there is no box to fit, no installer to book and nothing to move when someone changes vehicle.",
     "No. TrackLink runs on the phone your team member already carries — there is no box to fit, no installer to book and nothing to move when someone changes vehicle."),
    ("What does TrackLink cost?",
     "TrackLink starts at &pound;16/month for 1 Hub seat plus 3 Track seats, with a 14-day free trial. Extra Track and Hub seats come in packs &mdash; see <a href=\"/pricing/\">full pricing</a>.",
     "TrackLink starts at £16/month for 1 Hub seat plus 3 Track seats, with a 14-day free trial. Extra Track and Hub seats come in packs."),
    ("How often does TrackLink update a device&rsquo;s location?",
     "The standard cadences are 30 seconds, 60 seconds or 5 minutes. A 5-second high-frequency mode and a 1-second Live Track mode are also available as explicit opt-ins for near-live tracking, with in-app battery and data guidance so you know the trade-off before you turn them on.",
     "The standard cadences are 30 seconds, 60 seconds or 5 minutes. A 5-second high-frequency mode and a 1-second Live Track mode are also available as explicit opt-ins for near-live tracking, with in-app battery and data guidance."),
    ("Is our team&rsquo;s location data isolated from other companies?",
     "Yes. Every organisation&rsquo;s data is isolated by a unique organisation ID and enforced in the database&rsquo;s own security rules, not just by the app &mdash; one business can never read or write another business&rsquo;s data.",
     "Yes. Every organisation's data is isolated by a unique organisation ID and enforced in the database's own security rules, not just by the app — one business can never read or write another business's data."),
    ("What happens if a device loses signal?",
     "Fixes queue on the device and flush automatically once it reconnects &mdash; even after an extended period offline, nothing is lost, it just arrives a little later.",
     "Fixes queue on the device and flush automatically once it reconnects — even after an extended period offline, nothing is lost, it just arrives a little later."),
    ("Can a Track user turn tracking off?",
     "Yes. Only the person holding a device can switch its tracking on or off &mdash; TrackLink gives no one a remote switch over someone else&rsquo;s phone. Employers are responsible for using tracking lawfully, which in the UK generally means telling staff what is monitored and why.",
     "Yes. Only the person holding a device can switch its tracking on or off — TrackLink gives no one a remote switch over someone else's phone. Employers are responsible for using tracking lawfully, which in the UK generally means telling staff what is monitored and why."),
    ("Who controls billing &mdash; every Hub user?",
     "No. The account owner is the single person who controls the subscription: the payment method, plan changes, buying and removing seats, and cancellation. Other Hub users can use everything day to day &mdash; the live map, route history, groups and members &mdash; but cannot change what your organisation is paying. The owner is not an extra seat; they are one of your Hub users.",
     "No. The account owner is the single person who controls the subscription: the payment method, plan changes, buying and removing seats, and cancellation. Other Hub users can use everything day to day — the live map, route history, groups and members — but cannot change what your organisation is paying. The owner is not an extra seat; they are one of your Hub users."),
    ("Can more than one person manage the team?",
     "Yes &mdash; an organisation can have any number of Hub users, and every Hub sees every Track device. You can also organise Track users into custom groups (e.g. &ldquo;Morning shift&rdquo;) and filter the map by group.",
     "Yes — an organisation can have any number of Hub users, and every Hub sees every Track device. You can also organise Track users into custom groups and filter the map by group."),
    ("How long is location history kept?",
     "Live location is overwritten on every update. Stored route history is kept for 30 days; older points are deleted automatically once they expire.",
     "Live location is overwritten on every update. Stored route history is kept for 30 days; older points are deleted automatically once they expire."),
    ("How do I pay, and can I cancel?",
     "Paid plans are billed in advance via Google Play Billing on Android or Stripe on the web, depending on how your organisation subscribes. You can cancel at any time from within TrackLink; access runs to the end of the current billing period.",
     "Paid plans are billed in advance via Google Play Billing on Android or Stripe on the web, depending on how your organisation subscribes. You can cancel at any time from within TrackLink; access runs to the end of the current billing period."),
]


def faq_html(items):
    out = []
    for q, a, _ in items:
        out.append(f"""          <details>
            <summary>{q}</summary>
            <p>{a}</p>
          </details>""")
    return "\n".join(out)


def faq_schema(items):
    return [{
        "@type": "Question",
        "name": re.sub(r"&rsquo;", "’", q),
        "acceptedAnswer": {"@type": "Answer", "text": plain},
    } for q, _, plain in items]


# --------------------------------------------------------------------------
# pages
# --------------------------------------------------------------------------

def write(path, html):
    p = ROOT / path
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(html, encoding="utf-8")
    print("wrote", path, f"({len(html):,} bytes)")


# ---------- home ----------
home_faqs = FAQS[:4]
home = (
    head(
        "Live GPS Tracking for Small Business Teams | TrackLink",
        "Live GPS tracking, a real-time team map and route history for UK couriers, farms, trades and field teams. From &pound;16/month with a 14-day free trial.".replace("&pound;", "£"),
        "/",
        graph([ORG, SITE,
               webpage("/", "Live GPS Tracking for Small Business Teams | TrackLink",
                       "Live GPS tracking, a real-time team map and route history for UK couriers, farms, trades and field teams. From £16/month with a 14-day free trial."),
               APP_NODE]),
        og_title="TrackLink — live GPS tracking for teams",
        og_desc="Live location tracking, a real-time team map, route history and simple seat-based pricing — built for couriers, farms, trades and field-service teams.",
    )
    + header("/")
    + f"""
    <!-- Hero -->
    <section class="hero">
      <div class="container">
        <div class="hero__copy">
          <span class="eyebrow">GPS tracking for teams</span>
          <h1>Live GPS tracking for teams, <span class="accent">without the guesswork</span>.</h1>
          <p class="hero__lead">TrackLink links every person on your team to a live map your whole business can trust &mdash; built for couriers, farms, trades and delivery teams who need simple, honest location tracking.</p>
          <div class="hero__actions">
            <a class="btn btn--primary btn--lg" href="{SIGNUP}">Start free trial</a>
            <a class="btn btn--secondary btn--lg" href="/features/">See what&rsquo;s included</a>
          </div>
          <p class="hero__tagline">Track with certainty. Link with trust.</p>
        </div>
        <div class="hero__art">
          {shot("map", "Hub &middot; Live map", eager=True)}
        </div>
      </div>
    </section>

    <!-- Features -->
    <section class="section" id="features" aria-labelledby="features-h">
      <div class="container">
        <div class="section-head">
          <p class="eyebrow">What TrackLink does</p>
          <h2 id="features-h">Everything a team needs to stay in sync</h2>
          <p>Two simple roles &mdash; Track and Hub &mdash; cover the whole job: Track users report their position, and the business sees exactly where everyone is.</p>
        </div>
        <div class="features">
{cards(["tracking", "map", "history", "groups", "hubs", "isolation"])}
        </div>
        <p class="section-foot"><a class="more" href="/features/">See every feature in detail</a></p>
      </div>
    </section>

    <!-- How it works -->
    <section class="section section--tint" id="how" aria-labelledby="how-h">
      <div class="container">
        <div class="section-head">
          <p class="eyebrow">How it works</p>
          <h2 id="how-h">Two roles, one live picture</h2>
        </div>
        <div class="steps">
          <div class="step">
            <span class="step__num" aria-hidden="true">1</span>
            <h3>Track toggles on</h3>
            <p>A team member opens the app and toggles tracking on. Location uploads automatically in the background &mdash; no fiddling required.</p>
          </div>
          <div class="step">
            <span class="step__num" aria-hidden="true">2</span>
            <h3>Hub watches the map</h3>
            <p>The business owner or dispatcher opens the live map and sees every active device update in near real time, filterable by group.</p>
          </div>
          <div class="step">
            <span class="step__num" aria-hidden="true">3</span>
            <h3>Review the history</h3>
            <p>Pull up any device&rsquo;s route for the last 24 hours, 7 days or 30 days &mdash; journeys, stops and timing, all logged automatically.</p>
          </div>
        </div>
        <p class="section-foot"><a class="more" href="/how-it-works/">Walk through how it works</a></p>
      </div>
    </section>

    <!-- Pricing -->
    <section class="section" id="pricing" aria-labelledby="pricing-h">
      <div class="container">
        <div class="section-head">
          <p class="eyebrow">Pricing</p>
          <h2 id="pricing-h">One base plan. Add exactly the seats you need.</h2>
          <p>Every plan includes every feature &mdash; live tracking, the team map, route history and groups. You only pay for how many people you&rsquo;re tracking and managing.</p>
        </div>
{PLAN_CARD}
        <p class="section-foot"><a class="more" href="/pricing/">See seat packs and add-ons</a></p>
      </div>
    </section>

    <!-- FAQ -->
    <section class="section section--tint" id="faq" aria-labelledby="faq-h">
      <div class="container">
        <div class="section-head">
          <p class="eyebrow">Questions</p>
          <h2 id="faq-h">Frequently asked questions</h2>
        </div>
        <div class="faq">
{faq_html(home_faqs)}
        </div>
        <p class="section-foot"><a class="more" href="/faq/">Read all {len(FAQS)} questions</a></p>
      </div>
    </section>
"""
    + cta("Ready to see your team on one map?",
          "Start your 14-day free trial &mdash; 1 Hub seat and 3 Track seats included, no card required.")
    + FOOTER
)
write("index.html", home)


# ---------- features ----------
features = (
    head(
        "GPS Tracking Features: Live Map &amp; Route History | TrackLink",
        "Every TrackLink feature in detail: background GPS tracking, a real-time team map with under 5-second latency, route history, groups and data isolation.",
        "/features/",
        graph([ORG, SITE,
               webpage("/features/", "TrackLink features", "Every TrackLink feature in detail: live GPS tracking, the real-time team map, route history, custom groups, multi-Hub organisations and data isolation.", crumb=True),
               breadcrumb("/features/", "Features"), APP_NODE]),
    )
    + header("/features/")
    + page_head("Features", "Everything TrackLink does",
                "Two roles cover the whole job. Your team reports its position from the phones they already carry; the business sees every one of them on a single live map.")
    + f"""
    <section class="section">
      <div class="container">

        <div class="feature-row">
          <div class="feature-row__copy">
            <span class="eyebrow">On the team member&rsquo;s phone</span>
            <h3>Live GPS tracking that stays out of the way</h3>
            <p>A Track user opens the app, toggles tracking on and gets on with the job. Location uploads in the background at the interval you choose, and an ongoing notification makes it obvious that tracking is running &mdash; no silent monitoring.</p>
            <p>No tracker box, no installer, nothing to fit to a vehicle. If someone changes vehicle, their phone goes with them.</p>
            <ul class="spec-list">
              <li>Update every 30 seconds, 60 seconds or 5 minutes</li>
              <li>5-second and 1-second modes as explicit opt-ins</li>
              <li>Battery and data guidance shown before you switch</li>
              <li>Only the person holding the phone can switch it off</li>
            </ul>
          </div>
          {shot("phone", "", phone=True)}
        </div>

        <div class="feature-row feature-row--flip">
          <div class="feature-row__copy">
            <span class="eyebrow">In the office</span>
            <h3>A live team map the whole business can trust</h3>
            <p>Hub users see every active device on one map, refreshing on its own. From upload to the marker moving is under five seconds, so what you are looking at is what is happening.</p>
            <p>Each device carries its speed, its group, its battery level and how long ago it was last heard from &mdash; so you can tell the difference between &ldquo;parked&rdquo; and &ldquo;phone died&rdquo; at a glance.</p>
            <ul class="spec-list">
              <li>Under 5-second latency from upload to marker move</li>
              <li>Filter the map and device list by group in one tap</li>
              <li>Online, idle and offline status at a glance</li>
              <li>No manual refresh, ever</li>
            </ul>
          </div>
          {shot("map", "Hub &middot; Live map")}
        </div>

        <div class="feature-row">
          <div class="feature-row__copy">
            <span class="eyebrow">After the fact</span>
            <h3>Route history that answers the awkward questions</h3>
            <p>Pull up any device&rsquo;s day and get the whole route back &mdash; where they went, where they stopped and for how long. Useful for a delivery dispute, a timesheet query, or working out why Tuesday&rsquo;s round takes an hour longer than Wednesday&rsquo;s.</p>
            <p>History is kept for 30 days. Older points are deleted automatically once they expire.</p>
            <ul class="spec-list">
              <li>Last 24 hours, 7 days or 30 days for any device</li>
              <li>Distance, moving time, stop count and speeds</li>
              <li>Stops flagged with how long the device sat there</li>
              <li>30 days of route history included</li>
            </ul>
          </div>
          {shot("route", "Hub &middot; Route history")}
        </div>

      </div>
    </section>

    <section class="section section--tint">
      <div class="container">
        <div class="section-head">
          <p class="eyebrow">And the rest</p>
          <h2>Built for a real team, not a demo</h2>
        </div>
        <div class="features">
{cards(["groups", "hubs", "isolation"])}
        </div>
      </div>
    </section>
"""
    + cta("See it with your own team on the map",
          "Start your 14-day free trial &mdash; 1 Hub seat and 3 Track seats included, no card required.")
    + FOOTER
)
write("features/index.html", features)


# ---------- how it works ----------
how = (
    head(
        "How TrackLink Works: Track and Hub Explained | TrackLink",
        "How TrackLink works in three steps: a team member toggles tracking on, the business watches the live team map, and any day&rsquo;s route can be reviewed afterwards.".replace("&rsquo;", "’"),
        "/how-it-works/",
        graph([ORG, SITE,
               webpage("/how-it-works/", "How TrackLink works", "How TrackLink works in three steps: Track users toggle tracking on, Hub users watch the live map, and route history is reviewable afterwards.", crumb=True),
               breadcrumb("/how-it-works/", "How it works"), APP_NODE]),
    )
    + header("/how-it-works/")
    + page_head("How it works", "How TrackLink works",
                "There are only two roles to understand, and one of them takes about ten seconds to explain to the person carrying the phone.")
    + f"""
    <section class="section">
      <div class="container">
        <div class="section-head">
          <p class="eyebrow">The two roles</p>
          <h2>Track reports. Hub watches.</h2>
          <p>Every person in your organisation is one or the other. That is the whole model.</p>
        </div>
        <div class="steps">
          <div class="step">
            <span class="step__num" aria-hidden="true">T</span>
            <h3>Track &mdash; the person on the move</h3>
            <p>Anyone on your team who is out and about. They install the app, join your organisation and toggle tracking on when they start work. One Track seat is one tracked device.</p>
          </div>
          <div class="step">
            <span class="step__num" aria-hidden="true">H</span>
            <h3>Hub &mdash; the person who needs to know</h3>
            <p>An owner, dispatcher or manager. They see every device on the live map, review route history and manage groups and members. One Hub seat is one such person &mdash; and one of them, the account owner, also controls the billing.</p>
          </div>
        </div>
      </div>
    </section>

    <section class="section section--tint">
      <div class="container">

        <div class="feature-row">
          <div class="feature-row__copy">
            <span class="eyebrow">Step 1</span>
            <h3>The team member toggles tracking on</h3>
            <p>One switch, at the start of the shift. Location then uploads in the background at whatever interval the organisation has set &mdash; typically every 30 seconds &mdash; and an ongoing notification sits in the tray so it is never a secret that tracking is running.</p>
            <p>If they pass through a signal blackspot, fixes queue on the phone and flush automatically the moment it reconnects. Nothing is lost; it just arrives a little later.</p>
          </div>
          {shot("phone", "", phone=True)}
        </div>

        <div class="feature-row feature-row--flip">
          <div class="feature-row__copy">
            <span class="eyebrow">Step 2</span>
            <h3>The business watches the map</h3>
            <p>A Hub user opens the live map and sees everyone at once &mdash; who is moving, who is parked, who has gone quiet. Markers move on their own within five seconds of an upload, so nobody is refreshing a page to find out where someone is.</p>
            <p>Got more than one kind of team? Put them in groups and filter the map down to just the one you care about.</p>
          </div>
          {shot("map", "Hub &middot; Live map")}
        </div>

        <div class="feature-row">
          <div class="feature-row__copy">
            <span class="eyebrow">Step 3</span>
            <h3>Anyone&rsquo;s day can be reviewed afterwards</h3>
            <p>Pick a device, pick 24 hours, 7 days or 30 days, and the route comes back with its stops, dwell times, distance and speeds. That is usually enough to settle a &ldquo;we never got that delivery&rdquo; conversation in about a minute.</p>
            <p>History is retained for 30 days.</p>
          </div>
          {shot("route", "Hub &middot; Route history")}
        </div>

      </div>
    </section>

    <section class="section">
      <div class="container">
        <div class="section-head">
          <p class="eyebrow">Before you ask</p>
          <h2>The three things everyone checks</h2>
        </div>
        <div class="faq">
{faq_html([FAQS[1], FAQS[5], FAQS[6]])}
        </div>
        <p class="section-foot"><a class="more" href="/faq/">Read all {len(FAQS)} questions</a></p>
      </div>
    </section>
"""
    + cta("Set your team up this week",
          "Start your 14-day free trial &mdash; 1 Hub seat and 3 Track seats included, no card required.")
    + FOOTER
)
write("how-it-works/index.html", how)


# ---------- pricing ----------
pricing = (
    head(
        "Pricing: GPS Tracking from &pound;16 a Month | TrackLink".replace("&pound;", "£"),
        "TrackLink pricing: £16/month for 1 Hub seat and 3 Track seats, with a 14-day free trial. Track and Hub seat packs, plus an optional 365-day history add-on.",
        "/pricing/",
        graph([ORG, SITE,
               webpage("/pricing/", "TrackLink pricing", "TrackLink pricing: £16/month for 1 Hub seat and 3 Track seats with a 14-day free trial, plus Track and Hub seat packs.", crumb=True),
               breadcrumb("/pricing/", "Pricing"), APP_NODE]),
    )
    + header("/pricing/")
    + page_head("Pricing", "Simple, seat-based pricing",
                "Every plan includes every feature. You only pay for how many people you are tracking and how many are managing them.")
    + f"""
    <section class="section">
      <div class="container">
{PLAN_CARD}
{ADDONS}
        <p class="pricing-note">Seat packs are billed monthly or annually (annual &asymp; 10&times; the monthly rate, roughly 2 months free). Need a bigger team or a custom plan? <a href="mailto:info@civildigital.co.uk">Get in touch</a>.</p>
        <p class="pricing-note"><strong>These are the prices you pay.</strong> Subscribing inside the Android app instead costs more &mdash; &pound;21.49 base plan, &pound;29.99 Track pack, &pound;14.49 Hub pack &mdash; because Google takes a larger share of in-app payments and sets its own Play prices.</p>
      </div>
    </section>

    <section class="section section--tint">
      <div class="container">
        <div class="section-head">
          <p class="eyebrow">The one thing to get right</p>
          <h2>Track, Hub, and the account owner</h2>
          <p>Two kinds of seat, and one role that sits on top of them. Nearly every pricing question comes down to these, so here they are plainly.</p>
        </div>
        <div class="steps">
          <div class="step">
            <span class="step__num" aria-hidden="true">T</span>
            <h3>A Track seat is one tracked device</h3>
            <p>One phone reporting its location. A Track user switches their own tracking on and off and reports their position &mdash; they are not watching anyone else&rsquo;s.</p>
            <p>If someone changes vehicle, the seat goes with them: you are paying per person, not per vehicle.</p>
          </div>
          <div class="step">
            <span class="step__num" aria-hidden="true">H</span>
            <h3>A Hub seat is one person who can see the team</h3>
            <p>They see every device on the live map, review route history, and manage groups and members. Every Hub user sees every Track device &mdash; there is no partial view.</p>
            <p>Add as many as you need. Hub users run the day to day, but they cannot change what your organisation is paying.</p>
          </div>
          <div class="step">
            <span class="step__num" aria-hidden="true">&pound;</span>
            <h3>The account owner holds the billing</h3>
            <p>One person &mdash; and only one &mdash; controls the subscription: the payment method, plan changes, buying and removing seats, and cancellation.</p>
            <p><strong>The owner is not an extra seat.</strong> They are one of your Hub users, with the finances attached. So a team of one owner plus two managers needs three Hub seats, not four.</p>
          </div>
        </div>
        <p class="section-foot"><a class="more" href="/how-it-works/">See how Track and Hub work together</a></p>
      </div>
    </section>

    <section class="section">
      <div class="container">
        <div class="section-head">
          <p class="eyebrow">Billing questions</p>
          <h2>Trial, payment and cancellation</h2>
        </div>
        <div class="faq">
{faq_html([FAQS[2], FAQS[9], FAQS[8]])}
        </div>
      </div>
    </section>
"""
    + cta("Try it free for 14 days",
          "1 Hub seat and 3 Track seats included, no card required to start.")
    + FOOTER
)
write("pricing/index.html", pricing)


# ---------- faq ----------
faq_page = (
    head(
        "TrackLink FAQ: GPS Tracking Questions Answered | TrackLink",
        "Answers on TrackLink pricing, update intervals, hardware, offline behaviour, data retention, data isolation, billing control and cancellation.",
        "/faq/",
        graph([ORG, SITE,
               dict(webpage("/faq/", "TrackLink frequently asked questions",
                            "Answers on TrackLink pricing, update intervals, hardware, offline behaviour, data retention, data isolation, billing control and cancellation.",
                            crumb=True, types=["WebPage", "FAQPage"]),
                    **{"mainEntity": faq_schema(FAQS)}),
               breadcrumb("/faq/", "FAQ"), APP_NODE]),
    )
    + header("/faq/")
    + page_head("FAQ", "Frequently asked questions",
                "Everything people ask before they set a team up. If yours is not here, email us and we will answer it directly.")
    + f"""
    <section class="section">
      <div class="container">
        <div class="faq">
{faq_html(FAQS)}
        </div>
        <p class="section-foot">Still stuck? <a href="mailto:info@civildigital.co.uk">Email info@civildigital.co.uk</a> or <a href="https://wa.me/447568296136">message us on WhatsApp</a>.</p>
      </div>
    </section>
"""
    + cta("Ready to see your team on one map?",
          "Start your 14-day free trial &mdash; 1 Hub seat and 3 Track seats included, no card required.")
    + FOOTER
)
write("faq/index.html", faq_page)



# --------------------------------------------------------------------------
# guides (2026-09-19) — SEO articles built from tools/guides/*.py
# --------------------------------------------------------------------------
import sys
sys.path.insert(0, str(ROOT / "tools" / "guides"))
import costs as _g_costs, law as _g_law, tech as _g_tech, industry as _g_industry, assets as _g_assets  # noqa: E402

GUIDES_UPDATED = "2026-09-19"
GUIDES_UPDATED_TEXT = "19 September 2026"

HUBS = [
    ("costs", "Costs and choosing a tracker",
     "What GPS tracking costs, what to look for and how to pick the right kind of tracker."),
    ("law", "UK law and privacy",
     "Tracking staff, vehicles and phones lawfully under UK data protection law &mdash; and your rights if you are the one being tracked."),
    ("tech", "Accuracy, battery and how GPS works",
     "How accurate GPS is, how often trackers update, what blocks the signal and how long batteries last."),
    ("industry", "GPS tracking by industry",
     "How trades, contractors, delivery firms and other mobile teams use GPS tracking day to day."),
    ("assets", "Assets, equipment and theft",
     "Tracking trailers, plant and equipment &mdash; and when you need a hardware tracker rather than an app."),
]
HUB_NAMES = {k: name for k, name, _ in HUBS}

GUIDES = _g_costs.GUIDES + _g_law.GUIDES + _g_tech.GUIDES + _g_industry.GUIDES + _g_assets.GUIDES
BY_SLUG = {g["slug"]: g for g in GUIDES}

# Nothing ships with a broken internal link or a duplicate: refuse to build instead.
assert len(BY_SLUG) == len(GUIDES), "duplicate guide slug"
for g in GUIDES:
    assert g["hub"] in HUB_NAMES, g["slug"] + ": unknown hub"
    for r in g["related"]:
        assert r in BY_SLUG and r != g["slug"], f'{g["slug"]}: related guide "{r}" does not exist'
    for text in [g["answer"], g["body"]] + [a for _, a in g["faqs"]]:
        for linked in re.findall(r'href="/guides/([^"/]+)/"', text):
            assert linked in BY_SLUG, f'{g["slug"]}: links to missing guide "{linked}"'
    if len(g["desc"]) > 165:
        print(f'  note: {g["slug"]} description is {len(g["desc"])} chars')


def _plain(html):
    """HTML fragment -> plain text for schema and meta (entities decoded, tags dropped)."""
    import html as _h
    return re.sub(r"\s+", " ", _h.unescape(re.sub(r"<[^>]+>", "", html))).strip()


def _slugify(text):
    return re.sub(r"[^a-z0-9]+", "-", _plain(text).lower()).strip("-")[:60]


def _with_ids(body):
    """Give every <h2> an id and return (body, [(id, heading)]) for the contents list."""
    toc = []

    def add(m):
        heading = m.group(1)
        hid = _slugify(heading)
        toc.append((hid, heading))
        return f'<h2 id="{hid}">{heading}</h2>'
    return re.sub(r"<h2>(.*?)</h2>", add, body), toc


def _minutes(g):
    words = len(_plain(g["answer"] + g["body"] + " ".join(q + a for q, a in g["faqs"])).split())
    return max(3, round(words / 200))


def guide_crumbs(path, title=None):
    url = BASE + path
    items = [
        {"@type": "ListItem", "position": 1, "name": "Home", "item": BASE + "/"},
        {"@type": "ListItem", "position": 2, "name": "Guides", "item": BASE + "/guides/"},
    ]
    if title:
        items.append({"@type": "ListItem", "position": 3, "name": title, "item": url})
    else:
        items = items[:2]
    return {"@type": "BreadcrumbList", "@id": url + "#breadcrumb", "itemListElement": items}


def guide_card(g):
    return f"""
          <a class="guide-card" href="/guides/{g["slug"]}/">
            <span class="guide-card__hub">{HUB_NAMES[g["hub"]]}</span>
            <h3>{g["h1"][0].upper() + g["h1"][1:]}</h3>
            <p>{g["desc"]}</p>
          </a>"""


LEGAL_NOTE = """<p class="guide-note"><strong>Not legal advice.</strong> This guide explains UK law in general terms,
      as at the date shown. The ICO&rsquo;s guidance on monitoring workers was under review following the Data (Use and
      Access) Act 2025 when this was written &mdash; check the <a href="https://ico.org.uk/" rel="noopener">ICO</a> for
      the current position, and take advice for your own circumstances.</p>"""


def render_guide(g):
    path = f'/guides/{g["slug"]}/'
    url = BASE + path
    body, toc = _with_ids(g["body"])
    h1 = g["h1"][0].upper() + g["h1"][1:]
    faqs_html = "\n".join(
        f"""          <details>
            <summary>{q}</summary>
            <p>{a}</p>
          </details>""" for q, a in g["faqs"])
    toc_html = "\n".join(f'              <li><a href="#{hid}">{h}</a></li>' for hid, h in toc)
    related = "".join(guide_card(BY_SLUG[r]) for r in g["related"])
    article = {
        "@type": "Article",
        "@id": url + "#article",
        "headline": _plain(h1),
        "description": _plain(g["desc"]),
        "datePublished": GUIDES_UPDATED,
        "dateModified": GUIDES_UPDATED,
        "inLanguage": "en-GB",
        "author": {"@id": BASE + "/#organization"},
        "publisher": {"@id": BASE + "/#organization"},
        "image": OG,
        "mainEntityOfPage": {"@id": url + "#webpage"},
        "articleSection": _plain(HUB_NAMES[g["hub"]]),
        "isPartOf": {"@id": BASE + "/guides/#webpage"},
    }
    page = dict(webpage(path, _plain(g["title"]), _plain(g["desc"]), crumb=True, about=BASE + "/#organization"))
    faq_node = {
        "@type": "FAQPage",
        "@id": url + "#faq",
        "mainEntity": [{
            "@type": "Question", "name": _plain(q),
            "acceptedAnswer": {"@type": "Answer", "text": _plain(a)},
        } for q, a in g["faqs"]],
    }
    html = (
        head(g["title"] + " | TrackLink", _plain(g["desc"]), path,
             graph([ORG, SITE, page, article, faq_node, guide_crumbs(path, _plain(h1))]))
        + header("/guides/")
        + f"""
    <div class="page-head">
      <div class="container">
        <nav class="breadcrumb" aria-label="Breadcrumb">
          <ol>
            <li><a href="/">Home</a></li>
            <li><a href="/guides/">Guides</a></li>
            <li>{HUB_NAMES[g["hub"]]}</li>
          </ol>
        </nav>
        <h1>{h1}</h1>
        <p class="guide-meta">Updated <time datetime="{GUIDES_UPDATED}">{GUIDES_UPDATED_TEXT}</time> &middot; {_minutes(g)} min read &middot; By Civil Digital</p>
      </div>
    </div>

    <section class="section guide-section">
      <div class="container">
        <article class="prose guide">
          <div class="guide-answer">
            <p class="guide-answer__label">The short answer</p>
            <p>{g["answer"]}</p>
          </div>
          {LEGAL_NOTE if g["hub"] == "law" else ""}
          <nav class="guide-toc" aria-label="In this guide">
            <p class="guide-toc__label">In this guide</p>
            <ol>
{toc_html}
              <li><a href="#guide-faq">Common questions</a></li>
            </ol>
          </nav>
{body}
          <h2 id="guide-faq">Common questions</h2>
          <div class="faq guide-faq">
{faqs_html}
          </div>
        </article>
      </div>
    </section>

    <section class="section section--tint">
      <div class="container">
        <div class="section-head">
          <p class="eyebrow">Keep reading</p>
          <h2>Related guides</h2>
        </div>
        <div class="guide-grid">{related}
        </div>
        <p class="section-foot"><a class="more" href="/guides/">All GPS tracking guides</a></p>
      </div>
    </section>
"""
        + cta("Track your team the transparent way",
              "TrackLink puts your team on one live map from the phones they already carry. 14-day free trial, no card required.")
        + FOOTER
    )
    write(f'guides/{g["slug"]}/index.html', html)


for _g in GUIDES:
    render_guide(_g)

# ---------- guides index ----------
_hub_sections = []
for key, name, intro in HUBS:
    items = [g for g in GUIDES if g["hub"] == key]
    _hub_sections.append(f"""
        <section class="guide-hub" id="{key}" aria-labelledby="hub-{key}">
          <h2 id="hub-{key}">{name}</h2>
          <p>{intro}</p>
          <div class="guide-grid">{"".join(guide_card(g) for g in items)}
          </div>
        </section>""")
_guides_desc = "Plain-English guides to GPS tracking for UK businesses: costs, choosing a tracker, UK law and privacy, accuracy, battery life and tracking by industry."
guides_index = (
    head("GPS Tracking Guides for UK Businesses | TrackLink", _guides_desc, "/guides/",
         graph([ORG, SITE,
                dict(webpage("/guides/", "GPS tracking guides", _guides_desc, crumb=True,
                             types=["WebPage", "CollectionPage"], about=BASE + "/#organization"),
                     **{"hasPart": [{"@id": f'{BASE}/guides/{g["slug"]}/#article'} for g in GUIDES]}),
                guide_crumbs("/guides/")]))
    + header("/guides/")
    + f"""
    <div class="page-head">
      <div class="container">
        <nav class="breadcrumb" aria-label="Breadcrumb">
          <ol>
            <li><a href="/">Home</a></li>
            <li>Guides</li>
          </ol>
        </nav>
        <h1>GPS tracking guides</h1>
        <p>Straight answers to the questions businesses and their teams ask about GPS tracking &mdash; what it costs, what the law says in the UK, how accurate it is and how to use it well.</p>
        <nav class="guide-hubnav" aria-label="Guide topics">
          {" ".join(f'<a href="#{k}">{n}</a>' for k, n, _ in HUBS)}
        </nav>
      </div>
    </div>

    <section class="section">
      <div class="container">{"".join(_hub_sections)}
      </div>
    </section>
"""
    + cta("Ready to see your team on one map?",
          "Start your 14-day free trial &mdash; 1 Hub seat and 3 Track seats included, no card required.")
    + FOOTER
)
write("guides/index.html", guides_index)

# ---------- sitemap (generated from here on, so new guides can't be forgotten) ----------
_sitemap_pages = [
    ("/", GUIDES_UPDATED), ("/features/", GUIDES_UPDATED), ("/how-it-works/", GUIDES_UPDATED),
    ("/pricing/", GUIDES_UPDATED), ("/faq/", GUIDES_UPDATED), ("/guides/", GUIDES_UPDATED),
] + [(f'/guides/{g["slug"]}/', GUIDES_UPDATED) for g in GUIDES] + [
    ("/privacy/", "2026-09-05"), ("/terms/", "2026-09-05"), ("/delete-account/", "2026-09-17"),
]
write("sitemap.xml",
      '<?xml version="1.0" encoding="UTF-8"?>\n'
      '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
      + "".join(f"  <url>\n    <loc>{BASE}{p}</loc>\n    <lastmod>{d}</lastmod>\n  </url>\n"
                for p, d in _sitemap_pages)
      + "</urlset>\n")

# --------------------------------------------------------------------------
# patch the nav + footer on the hand-maintained pages (privacy, terms, 404)
# --------------------------------------------------------------------------
NAV_ITEMS = "\n".join(
    f'        <li><a href="{h}">{l}</a></li>' for h, l in NAV)

# The <ul> line appears in BOTH the pattern and the replacement, which is what
# makes this rerunnable — an earlier version dropped it and broke the markup.
NAV_PATTERN = (
    r'      <ul class="nav__links" id="primary-nav">\n'
    r'(?:        <li><a href="[^"]*"[^>]*>[^<]*</a></li>\n)*'
    r'        <li class="nav__cta">')
NAV_BLOCK = ('      <ul class="nav__links" id="primary-nav">\n'
             + NAV_ITEMS + '\n        <li class="nav__cta">')

FOOTER_PATTERN = (
    r'            <li><a href="[^"]*#features">Features</a></li>\n'
    r'            <li><a href="[^"]*#how">How it works</a></li>\n'
    r'            <li><a href="[^"]*#pricing">Pricing</a></li>\n')
FOOTER_BLOCK = ('            <li><a href="/features/">Features</a></li>\n'
                '            <li><a href="/how-it-works/">How it works</a></li>\n'
                '            <li><a href="/pricing/">Pricing</a></li>\n'
                '            <li><a href="/faq/">FAQ</a></li>\n')

# Every footer carries the account-deletion link Google Play requires (it asks for a URL
# reachable without the app on the Data Safety form); rerunnable like the nav patch.
DELETE_LINK = '            <li><a href="/delete-account/">Delete your account</a></li>\n'
TERMS_LINK = '            <li><a href="/terms/">Terms</a></li>\n'
FAQ_LINK = '            <li><a href="/faq/">FAQ</a></li>\n'
GUIDES_LINK = '            <li><a href="/guides/">Guides</a></li>\n'

for f in ["privacy/index.html", "terms/index.html", "delete-account/index.html", "404.html"]:
    p = ROOT / f
    s = p.read_text(encoding="utf-8")

    s, n = re.subn(NAV_PATTERN, NAV_BLOCK, s, count=1)
    assert n == 1, f + ": nav block did not match"

    s = re.sub(FOOTER_PATTERN, FOOTER_BLOCK, s, count=1)
    s = s.replace('<a href="/#pricing">current pricing</a>',
                  '<a href="/pricing/">current pricing</a>')
    if TERMS_LINK in s and DELETE_LINK not in s:
        s = s.replace(TERMS_LINK, TERMS_LINK + DELETE_LINK, 1)
    if GUIDES_LINK not in s and FAQ_LINK in s:
        s = s.replace(FAQ_LINK, FAQ_LINK + GUIDES_LINK, 1)
    s = s.replace(f'href="{APP}">Start free trial', f'href="{SIGNUP}">Start free trial')

    assert '<ul class="nav__links" id="primary-nav">' in s, f + ": lost the <ul>"
    assert s.count('</ul>') == s.count('<ul'), f + ": unbalanced <ul>"
    p.write_text(s, encoding="utf-8")
    print("patched", f)
