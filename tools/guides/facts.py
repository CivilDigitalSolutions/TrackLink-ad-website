"""Single source of TrackLink facts quoted in the guides.

Every price, limit and product claim a guide makes comes from here, so a price change is one
edit — not a hunt through 27 articles for a stale figure. Keep in step with the product:
prices = web (Stripe) prices, the ones a visitor to this site pays when they sign up here
(app repo: web/src/pricing.ts). Subscribing inside the Android app via Google Play costs more.
"""

APP = "https://app.tracklink.civildigital.co.uk"
SIGNUP = APP + "/signup"

# Web (direct) prices, GBP per month. Annual = 10x monthly (two months free).
BASE = 16            # 1 Hub + 3 Track seats
BASE_ANNUAL = 160
TRACK_PACK = 22      # +5 Track seats  (£4.40 a seat)
HUB_PACK = 11        # +2 Hub seats    (£5.50 a seat)
TRACK_SEAT = 5       # single Track seats, only once all 3 Track packs are on the plan
HUB_SEAT = 6         # single Hub seats, only once both Hub packs are on the plan
PLAY_BASE = 18       # the same base plan bought inside the Android app via Google Play

TRIAL_DAYS = 14
HISTORY_DAYS = 30

# Worked example used in the cost guide: 20 people tracked, 3 managers.
#   base (3 Track, 1 Hub) + 3 Track packs (+15 = 18) + 2 single Track seats (= 20)
#   + 1 Hub pack (+2 = 3 Hub seats)
EX20_TRACK = 20
EX20_TOTAL = BASE + 3 * TRACK_PACK + 2 * TRACK_SEAT + HUB_PACK    # 16 + 66 + 10 + 11 = 103


def gbp(n):
    return f"£{n:,}" if isinstance(n, int) else f"£{n:,.2f}"


# Phrases used across guides
UPDATE_INTERVALS = "every 30 seconds, 60 seconds or 5 minutes, with 5-second and 1-second modes as explicit opt-ins"
PLATFORMS = "an Android app for the people being tracked and a web dashboard (plus the same app) for the people managing them"
