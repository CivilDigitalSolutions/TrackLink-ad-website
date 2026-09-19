"""Guides hub: assets, equipment and theft.

TrackLink tracks PEOPLE (phones), not objects. These guides say so plainly and help the reader
choose the right kind of tracker — honesty that keeps the rest of the site credible.
"""
HUB = "assets"

GUIDES = [
# ------------------------------------------------------------------------------------------
dict(
    slug="track-company-assets-gps",
    hub=HUB,
    h1="Can you track company assets with GPS?",
    title="Can You Track Company Assets With GPS? Trailers, Rental Gear",
    desc="Can you track company assets with GPS? The best GPS tracker for trailers, rental equipment and gear, and when to use a hardware tracker instead of a phone app.",
    answer="""Yes. Company assets &mdash; <strong>trailers, rental equipment, generators, tools, containers</strong>
      &mdash; are tracked with <strong>dedicated hardware trackers</strong>, not phone apps, because the asset has no one
      carrying a phone. Choose a battery tracker for things without power and a wired tracker for anything with its own
      battery or engine.""",
    body="""
      <h2>Phone app or hardware tracker? Which you need</h2>
      <table>
        <caption>Tracking people vs tracking things</caption>
        <thead><tr><th>You want to know&hellip;</th><th>Use</th></tr></thead>
        <tbody>
          <tr><td>Where your team is</td><td>A phone tracking app (like TrackLink)</td></tr>
          <tr><td>Where a trailer, machine or piece of kit is</td><td>A hardware GPS tracker on the asset</td></tr>
          <tr><td>Where a pool vehicle is, whoever drives it</td><td>A fitted vehicle tracker</td></tr>
        </tbody>
      </table>
      <p>Many businesses use both: an app for people, hardware for high-value kit.</p>

      <h2>Best GPS tracker for trailers and rental equipment</h2>
      <ul>
        <li><strong>Battery life.</strong> A trailer sits unpowered for weeks; look for months of battery at a low
          reporting rate.</li>
        <li><strong>Movement alerts.</strong> An alert when something moves unexpectedly matters more than frequent updates.</li>
        <li><strong>Weatherproofing</strong> for anything stored outside.</li>
        <li><strong>Concealment.</strong> A tracker thieves can see and remove in seconds protects little.</li>
      </ul>

      <h2>Best GPS tracker for rental equipment and gear</h2>
      <p>Rental businesses &mdash; plant, event gear, sound and lighting kit &mdash; want to know that equipment went where
      it was supposed to and came back. Small battery trackers work well in flight cases and equipment boxes; for
      expensive powered kit, a wired tracker avoids charging. Bluetooth tags suit items that stay near your staff, not
      things that travel alone.</p>

      <h2>Asset protection and inventory management</h2>
      <p>Tracking helps with more than theft: knowing where every piece of kit is cuts time spent searching and helps
      you spot equipment sitting idle. See also
      <a href="/guides/gps-construction-equipment-theft/">GPS trackers for construction equipment and theft recovery</a>.</p>

      <h2>Where TrackLink fits</h2>
      <p>TrackLink tracks the <em>people</em> moving your assets around, through their phones. It doesn&rsquo;t track
      unattended equipment. If your main need is asset tracking, a dedicated asset tracker is the right tool; if you
      need both, TrackLink covers the team side.</p>
""",
    faqs=[
        ("Can I track a trailer with GPS?",
         "Yes, with a battery-powered hardware tracker hidden on the trailer. A phone app can't track an unattended trailer."),
        ("Do asset trackers need a subscription?",
         "Most live asset trackers do, because they send positions over a mobile or low-power network."),
    ],
    related=["gps-construction-equipment-theft", "choosing-a-gps-tracker", "gps-tracker-without-monthly-subscription"],
),
# ------------------------------------------------------------------------------------------
dict(
    slug="gps-construction-equipment-theft",
    hub=HUB,
    h1="GPS trackers for construction equipment, plant theft and recovery",
    title="Best GPS Tracker for Construction Equipment & Theft Recovery",
    desc="The best GPS tracker for construction equipment and materials, and for theft recovery and prevention — what works against plant and vehicle theft on UK job sites.",
    answer="""For construction equipment and plant, the most effective theft protection is a <strong>hidden, wired
      GPS tracker</strong> with <strong>out-of-hours movement alerts</strong>, backed up by visible marking and good
      site security. Trackers help most with <strong>recovery</strong>; prevention comes from making kit harder to
      take and harder to sell.""",
    body="""
      <h2>Best GPS tracker for construction equipment and materials</h2>
      <ul>
        <li><strong>Wired to the machine</strong> so it never needs charging, with a backup battery if power is cut.</li>
        <li><strong>Hidden</strong> where it can&rsquo;t be found quickly.</li>
        <li><strong>Movement and geofence alerts</strong> &mdash; an alert when a digger leaves site at 2am is worth more
          than a map you check the next morning.</li>
        <li><strong>Engine hours</strong> reporting, useful for maintenance and hire billing.</li>
      </ul>
      <p>Materials are harder: they&rsquo;re often not worth a tracker each. Secure storage and site CCTV do more there.</p>

      <h2>Best GPS tracker for theft recovery and prevention</h2>
      <p><strong>Recovery</strong> depends on knowing quickly and knowing where: fast alerts, reliable reporting and a
      tracker thieves don&rsquo;t find. <strong>Prevention</strong> depends on deterrence:</p>
      <ul>
        <li>Visible marking and registration of plant with recognised schemes.</li>
        <li>Immobilisers and physical locks.</li>
        <li>Secure compounds and lighting.</li>
        <li>Stickers stating that equipment is tracked.</li>
      </ul>

      <h2>Protecting vehicles and assets</h2>
      <p>Thieves sometimes use jammers to block trackers, which is illegal in the UK. Better trackers report when they
      lose signal suddenly, which can itself be an alert. See <a href="/guides/what-blocks-gps-tracker/">what blocks a
      GPS tracker</a>.</p>

      <h2>Jobsite asset management, not just theft</h2>
      <p>Tracking plant across several sites cuts time lost looking for machines and shows which ones are underused.
      For tracking the <em>people</em> working across your sites, see
      <a href="/guides/gps-tracking-contractors-job-sites/">GPS tracking for contractors</a> &mdash; that part is what
      TrackLink does.</p>
""",
    faqs=[
        ("Do GPS trackers stop plant theft?",
         "They mainly help recovery. Prevention comes from immobilisers, secure storage, marking and visible deterrents — a tracker adds a fast alert and a location."),
        ("Where should a tracker go on construction equipment?",
         "Hidden and wired into the machine's power, with a backup battery. Exact placement is best left to an installer."),
    ],
    related=["track-company-assets-gps", "gps-tracking-contractors-job-sites", "what-blocks-gps-tracker"],
),
]
