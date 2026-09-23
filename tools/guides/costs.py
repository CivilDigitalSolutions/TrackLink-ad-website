"""Guides hub: costs and choosing a tracker."""
from facts import (BASE, BASE_ANNUAL, EX20_TOTAL, EX20_TRACK, HISTORY_DAYS, HUB_PACK, HUB_SEAT,
                   PLAY_BASE, TRACK_PACK, TRACK_SEAT, TRIAL_DAYS, UPDATE_INTERVALS, gbp)

HUB = "costs"

GUIDES = [
# ------------------------------------------------------------------------------------------
dict(
    slug="gps-tracking-cost-small-business",
    hub=HUB,
    h1="How much does GPS tracking cost for a small business?",
    title="How Much Does GPS Tracking Cost for Small Businesses? (UK)",
    desc="What GPS tracking really costs a UK small business: hardware vs phone apps, monthly fees, installation, contracts and the hidden costs to check first.",
    answer=f"""For a UK small business, GPS tracking usually costs somewhere between <strong>a few pounds and
      around £20 per vehicle or person, per month</strong>. Hardware trackers add the price of the unit and often
      installation; phone-based apps skip both. The cheapest option that works well is usually a phone app if your
      team already carries smartphones &mdash; TrackLink, for example, is {gbp(BASE)} a month for one manager and
      three tracked people.""",
    body=f"""
      <h2>What you are actually paying for</h2>
      <p>Every GPS tracking service charges for the same three things, just packaged differently:</p>
      <ul>
        <li><strong>The device that knows where it is.</strong> Either a dedicated tracker (a box wired into a van,
          or a battery unit stuck to a trailer) or the smartphone someone already carries.</li>
        <li><strong>Getting the location to you.</strong> The device has to send its position over a mobile network.
          Hardware trackers carry their own SIM and data plan; a phone app uses the phone&rsquo;s existing data.</li>
        <li><strong>The software you look at.</strong> The live map, route history, reports and alerts &mdash; usually
          the part the monthly fee is really for.</li>
      </ul>
      <p>So when you compare prices, compare the <em>total</em> for your team over a year, not the headline monthly
      figure.</p>

      <h2>Typical GPS tracking costs in the UK</h2>
      <table>
        <caption>Rough ranges &mdash; always check a supplier&rsquo;s current terms</caption>
        <thead><tr><th>Type</th><th>Upfront</th><th>Ongoing</th></tr></thead>
        <tbody>
          <tr><td>Hardwired vehicle tracker (telematics)</td><td>Unit plus professional installation, sometimes bundled into a contract</td><td>Commonly around £8&ndash;£20 per vehicle per month, often on a 24&ndash;36 month contract</td></tr>
          <tr><td>Battery or plug-in tracker</td><td>The unit, typically tens of pounds</td><td>A data subscription for most models, plus your time charging or replacing batteries</td></tr>
          <tr><td>Phone-based tracking app</td><td>Nothing if the team has smartphones</td><td>A per-person or per-plan subscription; no installation, no hardware to replace</td></tr>
        </tbody>
      </table>
      <p>These are broad market ranges, not quotes &mdash; suppliers price very differently, and many hide the true
      total behind a contract. Which brings us to the costs that don&rsquo;t appear on the price page.</p>

      <h2>Hidden costs of GPS tracking services to avoid</h2>
      <ul>
        <li><strong>Long contracts.</strong> A low monthly price tied to a three-year term can cost more than a higher
          price you can cancel. Ask what happens if your fleet shrinks.</li>
        <li><strong>Installation and removal.</strong> Hardwired trackers need fitting &mdash; and fitting again when you
          change vehicles, which small businesses do often.</li>
        <li><strong>Hardware replacement.</strong> Lost, broken or out-of-date units are often your cost.</li>
        <li><strong>Charging per feature.</strong> Some services sell the map, history, alerts and reports as separate
          tiers. Check that the features you need are in the price you were quoted.</li>
        <li><strong>History limits.</strong> How far back can you look? Some cheap plans keep only a few days.</li>
        <li><strong>Per-user fees for managers.</strong> A plan might be cheap per vehicle but charge again for every
          office login.</li>
      </ul>

      <h2>The cheapest GPS tracker that actually works well</h2>
      <p>&ldquo;Cheapest&rdquo; and &ldquo;works well&rdquo; pull in different directions. The cheap trackers that
      disappoint people usually fail on one of three things: the <a href="/guides/how-accurate-is-gps-tracking/">accuracy</a>
      of the position, <a href="/guides/how-often-gps-trackers-update/">how often it updates</a>, or a
      <a href="/guides/gps-tracker-battery-life/">battery that dies</a> halfway through the day.</p>
      <p>If your team already carries Android phones, a phone app is almost always the cheapest option that still
      works well: modern phones have excellent GPS receivers, the data cost is already paid, and there&rsquo;s nothing
      to install. Where a phone app is <em>not</em> the answer is tracking things rather than people &mdash; see
      <a href="/guides/track-company-assets-gps/">tracking company assets</a>.</p>

      <h2>What TrackLink costs</h2>
      <p>TrackLink is priced per person, not per feature. Every plan includes the live map, route history, groups,
      zone alerts and CSV export.</p>
      <ul>
        <li><strong>Base plan: {gbp(BASE)} a month</strong> (or {gbp(BASE_ANNUAL)} a year) &mdash; 1 Hub seat for a
          manager and 3 Track seats for the people being tracked.</li>
        <li><strong>More people:</strong> Track seats come in packs of five for {gbp(TRACK_PACK)} a month
          ({gbp(TRACK_PACK / 5)} a seat). Once you have three packs, single extra seats are {gbp(TRACK_SEAT)} each.</li>
        <li><strong>More managers:</strong> Hub seats come in packs of two for {gbp(HUB_PACK)} a month, then
          {gbp(HUB_SEAT)} each.</li>
        <li><strong>{TRIAL_DAYS}-day free trial</strong>, no card needed to start, and {HISTORY_DAYS} days of route history included.</li>
      </ul>
      <p>Worked example: a team of {EX20_TRACK} people tracked with three managers comes to <strong>{gbp(EX20_TOTAL)} a
      month</strong> on the web. Prices above are for signing up on the web; subscribing inside the Android app through
      Google Play costs more ({gbp(PLAY_BASE)} for the base plan, including VAT), because Google takes a larger share of
      in-app payments. See <a href="/pricing/">full pricing</a>.</p>

      <h2>How to budget for GPS tracking</h2>
      <ol>
        <li>Count the people or vehicles you actually need to see, and how many people need to see them.</li>
        <li>Decide whether you are tracking <em>people</em> (a phone app fits) or <em>assets</em> (you need hardware).</li>
        <li>Work out the total over 12 months, including installation, hardware and any contract minimum.</li>
        <li>Use a free trial with two or three real team members before committing the whole business.</li>
      </ol>
""",
    faqs=[
        ("Is GPS tracking worth it for a small business?",
         "For most teams that drive for work, yes — the savings from fewer wasted journeys, quicker answers to customers and less time spent chasing people usually outweigh a few pounds a month per person. See <a href=\"/guides/gps-tracking-business-efficiency/\">how GPS tracking improves efficiency</a>."),
        ("Do I have to sign a long contract?",
         "Not always. Many hardwired systems use 24 to 36 month contracts, while app-based services such as TrackLink are monthly or annual and can be cancelled."),
        ("Does a GPS tracking app use a lot of mobile data?",
         f"No — a location update is tiny. At the standard intervals ({UPDATE_INTERVALS}) the data use is small compared with normal phone use."),
    ],
    related=["gps-tracker-without-monthly-subscription", "choosing-a-gps-tracker", "best-real-time-gps-tracking-app"],
),
# ------------------------------------------------------------------------------------------
dict(
    slug="gps-tracker-without-monthly-subscription",
    hub=HUB,
    h1="GPS tracker without a monthly subscription: do they exist?",
    title="GPS Tracker Without Monthly Subscription: Do They Exist?",
    desc="GPS tracker without a monthly subscription: what no-fee trackers can and can't do, the catch with 'no fee' devices, and when a subscription is worth it.",
    answer="""Yes, but they come with a catch. A GPS tracker with <strong>no monthly subscription</strong> either
      <strong>doesn&rsquo;t send its location anywhere live</strong> (it records a log you download later), or it relies
      on someone else&rsquo;s network to report roughly where it is. If you want to see where someone or something is
      <em>right now</em>, something has to pay for the mobile data &mdash; and that is what the subscription is.""",
    body="""
      <h2>Why most GPS trackers charge a monthly fee</h2>
      <p>Knowing your position is free: GPS satellites broadcast signals any receiver can use at no cost. The expense
      is <strong>telling someone else</strong> where you are. A live tracker needs a mobile connection (a SIM and a
      data plan), servers to receive the positions, and software to show them to you. The monthly fee pays for those
      three things.</p>

      <h2>The kinds of &ldquo;no subscription&rdquo; GPS tracker</h2>
      <ul>
        <li><strong>GPS data loggers.</strong> They record where they&rsquo;ve been and you download the track later.
          Genuinely subscription-free, but you only find out where something went after it comes back.</li>
        <li><strong>Bluetooth item finders.</strong> Small tags that report their position through nearby phones.
          No fee, but they are designed for finding keys and bags, not tracking a vehicle or a team: accuracy and
          update timing depend entirely on who happens to walk past.</li>
        <li><strong>Trackers with the fee bundled in.</strong> Some sell the device with &ldquo;lifetime&rdquo;
          data included. Read the small print on what &ldquo;lifetime&rdquo; means and how often it updates.</li>
        <li><strong>Pay-as-you-go SIM trackers.</strong> You supply your own SIM and top it up. Still a running cost,
          just paid to a network instead of the tracker company.</li>
      </ul>

      <h2>When a subscription-free tracker is enough</h2>
      <p>If you only need to know where something <em>was</em> &mdash; a walking route, a one-off journey, a check that
      a machine stayed on site &mdash; a logger can do the job. If you need to know where people or vehicles
      <em>are</em>, or be alerted when they arrive somewhere, you need live data, which costs money somewhere.</p>

      <h2>The lowest-cost way to get live tracking</h2>
      <p>For tracking people, the lowest-cost live option is usually an app on the phone they already carry: the
      phone&rsquo;s own data plan does the sending, so you don&rsquo;t pay for a second SIM per person. TrackLink works
      this way &mdash; see <a href="/guides/gps-tracking-cost-small-business/">what GPS tracking costs</a> for a
      full comparison, including the hidden costs of hardware.</p>
""",
    faqs=[
        ("Do GPS trackers need a SIM card?",
         "A tracker that shows its location live needs a way to send it — usually a SIM and mobile data. Data loggers don't, because they store the route to download later."),
        ("Can I use my phone as a GPS tracker with no monthly fee?",
         "Your phone's built-in location sharing can show family or friends where you are. For a business that needs a team map, route history and alerts, a business tracking app is the practical option — usually a small monthly fee per person."),
    ],
    related=["gps-tracking-cost-small-business", "gps-tracking-without-signal", "choosing-a-gps-tracker"],
),
# ------------------------------------------------------------------------------------------
dict(
    slug="choosing-a-gps-tracker",
    hub=HUB,
    h1="How to choose a GPS tracker: the features that matter",
    title="How to Choose a GPS Tracker: Features That Matter",
    desc="How to choose between GPS trackers with different features, the best GPS tracker for fleet vehicles, cloud vs local systems and DIY vs professional setup.",
    answer="""Start with <strong>what you are tracking</strong> (people or things), then <strong>how live</strong> it
      needs to be, then <strong>who needs to see it</strong>. For a small fleet of vans driven by the same people every
      day, a phone app on each driver&rsquo;s phone is usually enough; for machinery, trailers or vehicles that change
      drivers constantly, a fitted hardware tracker is the better choice.""",
    body=f"""
      <h2>1. People or things?</h2>
      <p>This one question rules out half the market. A phone app tracks <strong>a person</strong> &mdash; it goes
      wherever they go, whichever vehicle they drive. A hardware tracker tracks <strong>an object</strong> &mdash; a
      van, a trailer, a digger. If what you care about is &ldquo;where is my team&rdquo;, choose people-tracking. If it
      is &ldquo;where is my equipment&rdquo;, see <a href="/guides/track-company-assets-gps/">tracking company assets</a>.</p>

      <h2>2. How to choose between GPS trackers with different features</h2>
      <table>
        <caption>Features worth comparing</caption>
        <thead><tr><th>Feature</th><th>What to ask</th></tr></thead>
        <tbody>
          <tr><td>Update frequency</td><td>How often does the position refresh? Can you choose? (<a href="/guides/how-often-gps-trackers-update/">why it matters</a>)</td></tr>
          <tr><td>Route history</td><td>How many days back can you look, and can you pick exact dates and times?</td></tr>
          <tr><td>Alerts</td><td>Can it tell you when someone arrives at or leaves a site (geofencing)?</td></tr>
          <tr><td>Managers</td><td>How many people can see the map, and does each cost extra?</td></tr>
          <tr><td>Export</td><td>Can you get the data out, for example as a CSV for timesheets or invoicing?</td></tr>
          <tr><td>Privacy controls</td><td>Can the tracked person see when tracking is on? (<a href="/guides/is-gps-tracking-legal-uk-business/">this matters legally</a>)</td></tr>
          <tr><td>Battery impact</td><td>What does it do to a phone&rsquo;s battery over a shift? (<a href="/guides/gps-tracker-battery-life/">battery guide</a>)</td></tr>
        </tbody>
      </table>

      <h2>Best GPS tracker for fleet vehicles: what should you choose?</h2>
      <p>There is no single best GPS tracker for fleet vehicles &mdash; there is a best fit for your fleet:</p>
      <ul>
        <li><strong>Same driver, same van, every day:</strong> a phone app on the driver&rsquo;s phone gives you live
          location and route history with no installation. Cheapest and quickest to start.</li>
        <li><strong>Pool vehicles shared between many drivers:</strong> a fitted tracker per vehicle, because the
          vehicle is the constant.</li>
        <li><strong>You need engine data</strong> (fuel use, harsh braking, engine hours): hardwired telematics that
          reads the vehicle itself. A phone app can&rsquo;t see inside the engine.</li>
      </ul>

      <h2>Cloud-based vs local GPS tracking systems</h2>
      <p>Almost every modern tracking service is <strong>cloud-based</strong>: devices send positions to the
      supplier&rsquo;s servers and you view them in a browser or app from anywhere. <strong>Local</strong> systems keep
      data on your own computer or server &mdash; more control, but you run the server, the backups and the security
      yourself. For a small business, cloud is almost always the practical choice; the questions to ask are where the
      data is stored and who can see it. TrackLink, for example, stores its data in London and keeps every
      organisation&rsquo;s data isolated at the database level.</p>

      <h2>DIY vs professional GPS tracking implementation</h2>
      <p>Hardwired trackers usually need a professional installer. Battery trackers and phone apps are DIY: you can be
      running the same day. The real &ldquo;implementation&rdquo; work in a small business isn&rsquo;t technical at all
      &mdash; it is <a href="/guides/employee-concerns-gps-tracking/">telling your team what you are doing and why</a>,
      which is also what UK data protection law expects.</p>

      <h2>A short checklist before you buy</h2>
      <ol>
        <li>Trial it with real people on real days, not a demo.</li>
        <li>Check the total yearly cost, not the headline price (<a href="/guides/gps-tracking-cost-small-business/">cost guide</a>).</li>
        <li>Check how far back history goes and whether you can export it.</li>
        <li>Write a short tracking policy before you roll it out.</li>
      </ol>
""",
    faqs=[
        ("What is the most important feature in a GPS tracker?",
         "For live tracking, how reliably it updates — a cheap tracker that goes quiet for twenty minutes is worse than no tracker. Then route history, then alerts."),
        ("Can one system track both people and vehicles?",
         "Some can, but it is usually cleaner to track people with a phone app and equipment with dedicated hardware trackers, each doing what it is good at."),
        ("Is TrackLink a hardware tracker?",
         f"No. TrackLink is an Android app plus a web dashboard: it tracks the person carrying the phone, updating {UPDATE_INTERVALS}."),
    ],
    related=["best-real-time-gps-tracking-app", "gps-tracking-cost-small-business", "track-company-assets-gps"],
),
# ------------------------------------------------------------------------------------------
dict(
    slug="best-real-time-gps-tracking-app",
    hub=HUB,
    h1="Real-time GPS tracking apps: which is most reliable?",
    title="Real-Time GPS Tracking Apps: Which Is Most Reliable?",
    desc="What makes a real-time GPS tracking app reliable, how to test one, and how to find the most reliable GPS tracking service for small teams.",
    answer="""The most reliable real-time GPS tracking app is the one that <strong>keeps reporting when the phone is
      locked, in a pocket, on a bad signal</strong> &mdash; not the one with the prettiest map. Look for an app that
      runs as a visible foreground service, holds positions while offline and sends them when signal returns, filters
      out bad GPS fixes, and tells you clearly when a device has gone quiet.""",
    body=f"""
      <h2>What &ldquo;reliable&rdquo; really means for a tracking app</h2>
      <ul>
        <li><strong>It keeps running.</strong> Phones aggressively close background apps to save battery. A tracking
          app that isn&rsquo;t built for this simply stops, and you only notice when the dot hasn&rsquo;t moved all
          afternoon. On Android the reliable approach is a foreground service with a visible notification.</li>
        <li><strong>It survives bad signal.</strong> Positions taken with no signal should be stored and sent later,
          not lost. See <a href="/guides/gps-tracking-without-signal/">GPS without phone signal</a>.</li>
        <li><strong>It rejects bad positions.</strong> Phones occasionally report a wildly wrong location. A good app
          filters those out instead of drawing a line across town.</li>
        <li><strong>It is honest about staleness.</strong> The map should show when a device was last heard from, so
          you can tell &ldquo;parked&rdquo; from &ldquo;phone off&rdquo;.</li>
      </ul>

      <h2>How to test a real-time GPS tracking app before you commit</h2>
      <ol>
        <li>Install it on two or three real phones &mdash; including the oldest phone in your team.</li>
        <li>Lock the phones, put them in pockets and go about a normal working day.</li>
        <li>Check the route history in the evening: are there gaps? Straight lines where there were turns?</li>
        <li>Drive through a known dead spot and check the route fills in once signal is back.</li>
      </ol>

      <h2>Most reliable GPS tracking service for small teams</h2>
      <p>For a small team, reliability also means <em>simple</em>. Fewer moving parts &mdash; no hardware to fit, no
      installer, nothing to charge &mdash; means fewer things to fail. A phone-based service that everyone can set up
      in minutes is usually more dependable in practice than a sophisticated system nobody maintains.</p>

      <h2>How TrackLink approaches reliability</h2>
      <ul>
        <li>Tracking runs as an Android foreground service with a visible notification, so it keeps going with the
          screen off.</li>
        <li>Positions are filtered for accuracy and smoothed, and a parked phone stops filling your history with
          jitter.</li>
        <li>Positions taken offline are held on the phone and uploaded when the connection returns.</li>
        <li>You choose how live it is: {UPDATE_INTERVALS}.</li>
        <li>The Hub map shows online, idle and offline at a glance.</li>
      </ul>
      <p>The honest limitation: TrackLink is Android-only on the tracking side. The dashboard works in any browser.</p>
""",
    faqs=[
        ("Why does my tracking app stop working when the phone is locked?",
         "Most likely the phone's battery optimisation is closing it. Reliable tracking apps use a foreground service, and some phone makers also need the app excluding from battery saving."),
        ("Are free tracking apps reliable enough for a business?",
         "Family location-sharing apps are built for occasional check-ins, not a working day of route history and team visibility. They can work for a very small team, but you lose the business features."),
    ],
    related=["how-often-gps-trackers-update", "how-accurate-is-gps-tracking", "choosing-a-gps-tracker"],
),
]
