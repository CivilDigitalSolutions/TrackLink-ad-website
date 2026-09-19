"""Guides hub: accuracy, battery and how GPS works."""
from facts import UPDATE_INTERVALS

HUB = "tech"
GPS_ACCURACY = "https://www.gps.gov/gps-accuracy"

GUIDES = [
# ------------------------------------------------------------------------------------------
dict(
    slug="how-accurate-is-gps-tracking",
    hub=HUB,
    h1="How accurate are GPS trackers for business use?",
    title="How Accurate Are GPS Trackers? Business Accuracy Explained",
    desc="How accurate GPS trackers are for business use, what the most accurate GPS tracker on the market really means, and why accuracy drops near buildings and trees.",
    answer=f"""A GPS-enabled smartphone is typically accurate to <strong>about 5 metres</strong> (4.9&nbsp;m) under
      open sky, according to the US government&rsquo;s official <a href="{GPS_ACCURACY}" rel="noopener">GPS
      information site</a>. Accuracy gets worse near tall buildings, under bridges and among trees. For business
      tracking &mdash; which street, which site, which customer &mdash; that is more than enough.""",
    body="""
      <h2>What GPS accuracy actually means</h2>
      <p>A GPS position is an estimate with a margin of error, usually expressed as a radius: &ldquo;accurate to 5
      metres&rdquo; means the true position is very probably within a 5-metre circle. Good receivers report that
      estimate alongside each position, which lets software throw away the weak ones.</p>

      <h2>What makes GPS less accurate</h2>
      <ul>
        <li><strong>Tall buildings</strong> block and reflect signals (&ldquo;urban canyons&rdquo;).</li>
        <li><strong>Tree cover</strong> weakens signals.</li>
        <li><strong>Indoors, tunnels and underground car parks</strong> &mdash; GPS mostly doesn&rsquo;t work there at all.</li>
        <li><strong>A cold start</strong> &mdash; the first fix after the phone has been off can be rough.</li>
      </ul>
      <p>See <a href="/guides/what-blocks-gps-tracker/">what blocks a GPS tracker</a> for the full list.</p>

      <h2>What&rsquo;s the most accurate GPS tracker on the market?</h2>
      <p>For everyday tracking, the differences between decent devices matter less than the conditions they are used
      in. Surveying-grade dual-frequency receivers reach centimetre accuracy, but they cost far more and aren&rsquo;t
      what a business needs to see which job a van is at. Recent flagship phones are also very good: many use several
      satellite systems (GPS, Galileo, GLONASS, BeiDou) and some use dual frequencies.</p>
      <p>What makes the biggest practical difference is <strong>what the software does with the positions</strong>:
      discarding poor-accuracy fixes, smoothing jitter and not drawing a parked phone as a scribble.</p>

      <h2>How accurate is TrackLink?</h2>
      <p>TrackLink uses each phone&rsquo;s high-accuracy location mode, discards any position the phone reports as worse
      than 25 metres, and smooths the rest so routes follow the roads rather than zig-zagging. When a phone is parked,
      its history stops recording jitter and holds a single settled position.</p>

      <h2>Is GPS accurate enough for timesheets and disputes?</h2>
      <p>For &ldquo;was the engineer at the customer&rsquo;s address at 9am?&rdquo;, yes. For &ldquo;which side of the
      road were they on?&rdquo;, not reliably. Treat GPS as strong evidence of where someone was, to within a few metres
      in the open and a few tens of metres in a dense city centre.</p>
""",
    faqs=[
        ("How accurate is phone GPS?",
         "Typically about 5 metres in open sky, worse near tall buildings and trees, and unreliable indoors."),
        ("Why does my GPS location jump around?",
         "Reflections from buildings and weak signals produce occasional bad positions. Good tracking software filters these out."),
        ("Is GPS more accurate than cell tower location?",
         "Much more. Cell tower location can be off by hundreds of metres; GPS is usually within a few metres outdoors."),
    ],
    related=["how-often-gps-trackers-update", "what-blocks-gps-tracker", "best-real-time-gps-tracking-app"],
),
# ------------------------------------------------------------------------------------------
dict(
    slug="how-often-gps-trackers-update",
    hub=HUB,
    h1="How often do GPS trackers update location?",
    title="How Often Do GPS Trackers Update Location? Real-Time Explained",
    desc="How often GPS trackers update their location, what 'real-time' really means, and how to choose an update interval that balances detail, battery and data.",
    answer=f"""It varies from <strong>every second</strong> to <strong>every few hours</strong>, depending on the
      device and its settings. For business tracking, updates every <strong>30 to 60 seconds</strong> give a live map
      and good route history without draining batteries; every few seconds is needed only for genuinely live following.
      TrackLink updates {UPDATE_INTERVALS}.""",
    body="""
      <h2>What &ldquo;real-time&rdquo; really means</h2>
      <p>Most trackers are <em>near</em> real-time: the device takes a position, sends it, and the map updates. The
      delay you see is the update interval plus a few seconds of transmission. Battery trackers built to last months
      may only report a few times a day.</p>

      <h2>Choosing an update interval</h2>
      <table>
        <caption>What different update intervals are good for</caption>
        <thead><tr><th>Interval</th><th>Good for</th><th>Trade-off</th></tr></thead>
        <tbody>
          <tr><td>1&ndash;5 seconds</td><td>Following someone live, detailed routes</td><td>Much higher battery and data use</td></tr>
          <tr><td>30&ndash;60 seconds</td><td>Dispatch, customer ETAs, everyday route history</td><td>The usual business balance</td></tr>
          <tr><td>5 minutes</td><td>Roughly where people are through the day</td><td>Routes are less detailed</td></tr>
          <tr><td>Hours</td><td>Long-life asset trackers</td><td>Useless for live tracking</td></tr>
        </tbody>
      </table>

      <h2>Why faster isn&rsquo;t always better</h2>
      <p>Each update wakes the GPS and the radio, which costs battery. Updating every second can use many times the
      battery of updating every 30 seconds. See <a href="/guides/gps-tracker-battery-life/">battery life</a>.</p>

      <h2>How TrackLink handles updates</h2>
      <ul>
        <li>Choose every 30 seconds, 60 seconds or 5 minutes; 60 seconds is the default.</li>
        <li>A 5-second high-frequency mode and a 1-second Live Track mode are explicit opt-ins, with battery guidance shown first.</li>
        <li>The Hub map moves within about five seconds of an update arriving.</li>
        <li>A parked phone keeps checking in without cluttering its route history.</li>
      </ul>
""",
    faqs=[
        ("How often should a business GPS tracker update?",
         "Every 30 to 60 seconds suits most businesses. Faster is only worth it if you need to follow someone live."),
        ("Why does the tracker show someone in the wrong place for a minute?",
         "The map shows the last position received. With a 60-second interval, the person may have moved up to a minute's travel since."),
    ],
    related=["gps-tracker-battery-life", "how-accurate-is-gps-tracking", "best-real-time-gps-tracking-app"],
),
# ------------------------------------------------------------------------------------------
dict(
    slug="what-blocks-gps-tracker",
    hub=HUB,
    h1="What blocks a GPS tracker from working?",
    title="What Blocks a GPS Tracker From Working? Causes & Fixes",
    desc="What blocks a GPS tracker from working: buildings, tunnels, metal, weather, battery saving and jammers — and how to get a reliable signal.",
    answer="""GPS signals are weak and travel in straight lines from satellites, so anything <strong>solid overhead
      or around the receiver</strong> blocks them: roofs, tunnels, underground car parks, tall buildings and metal
      enclosures. On phones, <strong>battery-saving settings</strong> stop tracking far more often than the sky does.
      Deliberate blocking with a jammer is illegal in the UK.""",
    body="""
      <h2>Physical things that block GPS</h2>
      <ul>
        <li><strong>Roofs and buildings.</strong> GPS rarely works well indoors.</li>
        <li><strong>Tunnels and underground car parks.</strong> No sky, no fix.</li>
        <li><strong>Tall buildings.</strong> They block and reflect signals, which causes errors as well as gaps.</li>
        <li><strong>Metal.</strong> A tracker inside a metal box, container or van with a metal load has a much
          harder time.</li>
        <li><strong>Dense tree cover and heavy rain</strong> weaken signals, though usually not completely.</li>
      </ul>

      <h2>Things on the phone that stop tracking</h2>
      <ul>
        <li><strong>Battery optimisation</strong> closing the app in the background &mdash; the most common cause.</li>
        <li><strong>Location permission</strong> set to &ldquo;only while using the app&rdquo;.</li>
        <li><strong>Location turned off</strong> or airplane mode.</li>
        <li><strong>No mobile data</strong> &mdash; the phone may know where it is but can&rsquo;t send it
          (see <a href="/guides/gps-tracking-without-signal/">GPS without signal</a>).</li>
      </ul>

      <h2>GPS jammers are illegal</h2>
      <p>GPS jammers block signals deliberately. Using one in the UK is a criminal offence under section 68 of the
      Wireless Telegraphy Act 2006, punishable by up to two years in prison and an unlimited fine. Jammers are
      associated with vehicle theft, which is one reason some trackers report when their signal suddenly drops.</p>

      <h2>How to get a reliable GPS signal</h2>
      <ol>
        <li>Keep the phone or tracker with a view of the sky where possible (a dashboard mount, not a glovebox).</li>
        <li>Exclude the tracking app from battery optimisation.</li>
        <li>Grant location permission for tracking while working.</li>
        <li>Use an app that stores positions offline and sends them when signal returns.</li>
      </ol>
""",
    faqs=[
        ("Does GPS work indoors?",
         "Rarely well. Near windows it may work poorly; deep inside buildings it usually doesn't."),
        ("Can weather block GPS?",
         "Heavy rain and cloud weaken GPS slightly but rarely stop it. Obstacles like roofs and tunnels matter far more."),
        ("Is it illegal to block a GPS tracker?",
         "Using a jammer is illegal in the UK. Removing a tracker from your own vehicle is not."),
    ],
    related=["gps-tracking-without-signal", "how-accurate-is-gps-tracking", "detect-remove-gps-tracker"],
),
# ------------------------------------------------------------------------------------------
dict(
    slug="gps-tracking-without-signal",
    hub=HUB,
    h1="Does GPS tracking work without phone signal?",
    title="Does GPS Tracking Work Without Cell Service?",
    desc="Does GPS work without cell service or mobile data? What still works offline, what doesn't, and how good tracking apps handle dead spots in rural areas.",
    answer="""Yes and no. <strong>GPS itself works without mobile signal</strong>: the phone receives satellite
      signals directly and can still work out where it is. What it <strong>can&rsquo;t do without signal is send
      that position</strong> to anyone. A well-built tracking app stores positions while offline and uploads them once
      the phone reconnects, so the route is complete &mdash; just late.""",
    body="""
      <h2>GPS vs mobile data: two different things</h2>
      <p>GPS is receive-only: satellites broadcast, your phone listens. No SIM, no data, no mobile mast needed. Mobile
      data is what carries the position <em>from</em> the phone to a server and on to a map. Lose signal and you lose
      the second part, not the first.</p>

      <h2>Why the first fix can be slower without signal</h2>
      <p>Phones use the mobile network to speed up the first GPS fix (assisted GPS). Without it, the first position
      after the phone has been off or moved a long way can take longer. Once it has a fix, tracking works normally.</p>

      <h2>Does GPS tracking work without cell service in rural areas?</h2>
      <p>Rural dead spots are common across the UK, especially in hills and valleys. Positions are still recorded; they
      arrive in a burst when coverage returns. On a live map, the person appears to stop, then jumps along the route
      when they reconnect.</p>

      <h2>How TrackLink handles dead spots</h2>
      <p>TrackLink holds positions on the phone while it is offline and uploads them once it reconnects, so route
      history fills in &mdash; even after a long spell without signal. The live map shows how long ago each device was
      last heard from, so a gap is obvious rather than misleading.</p>

      <h2>If you need tracking with no signal at all</h2>
      <p>For remote areas with no coverage for long periods, satellite messengers can send positions via satellite
      rather than the mobile network. They are a different category of device, usually with their own subscription.
      See <a href="/guides/gps-tracking-hikers-outdoors/">GPS tracking for hikers</a>.</p>
""",
    faqs=[
        ("Does GPS use mobile data?",
         "Working out your position doesn't. Sending it to a map does, but only a tiny amount."),
        ("Will I lose tracking data in a dead spot?",
         "Not with an app that stores positions offline. They upload when the phone reconnects."),
    ],
    related=["what-blocks-gps-tracker", "gps-tracking-hikers-outdoors", "best-real-time-gps-tracking-app"],
),
# ------------------------------------------------------------------------------------------
dict(
    slug="gps-tracker-battery-life",
    hub=HUB,
    h1="How long do GPS tracker batteries last?",
    title="How Long Do GPS Tracker Batteries Last? Best for Long Shifts",
    desc="How long GPS tracker batteries last, how tracking apps affect phone battery, and choosing a GPS tracker with the best battery life for long shifts.",
    answer="""A dedicated battery tracker can last from <strong>a few days to several months</strong>, depending
      almost entirely on <strong>how often it reports</strong>. For phone tracking apps, a sensible interval (every 30
      to 60 seconds) on a modern phone will usually get through a working shift; updating every second will drain a
      battery far faster.""",
    body="""
      <h2>What drains a GPS tracker&rsquo;s battery</h2>
      <ul>
        <li><strong>Update frequency</strong> &mdash; by far the biggest factor. Each update wakes the GPS and the radio.</li>
        <li><strong>Signal strength</strong> &mdash; weak mobile signal makes the radio work harder.</li>
        <li><strong>Temperature</strong> &mdash; cold weather shortens battery life.</li>
        <li><strong>Movement</strong> &mdash; many trackers report more often when moving.</li>
      </ul>

      <h2>How long do GPS tracker batteries last?</h2>
      <table>
        <caption>Rough battery life by device type</caption>
        <thead><tr><th>Device</th><th>Typical battery life</th></tr></thead>
        <tbody>
          <tr><td>Asset tracker reporting a few times a day</td><td>Months</td></tr>
          <tr><td>Portable tracker reporting every few minutes</td><td>Days to a couple of weeks</td></tr>
          <tr><td>Phone app, updates every 30&ndash;60 seconds</td><td>Usually a full working shift on a healthy battery</td></tr>
          <tr><td>Phone app, updates every second</td><td>Hours, unless the phone is on charge</td></tr>
        </tbody>
      </table>

      <h2>GPS tracker with best battery life for long shifts</h2>
      <p>For people on long shifts, the most practical answer is often <strong>the phone they already carry, plus a
      charger in the vehicle</strong>. A phone on a dashboard mount with a charging cable can track all day at any
      interval. Away from a vehicle, choose a moderate interval (60 seconds or 5 minutes) and replace ageing phone
      batteries.</p>

      <h2>How TrackLink manages battery use</h2>
      <ul>
        <li>60-second updates by default, with 30-second and 5-minute options.</li>
        <li>The 5-second and 1-second modes are opt-ins with battery guidance shown first.</li>
        <li>When a phone is parked, TrackLink stops filling its history and just keeps a light check-in going.</li>
        <li>Tracking only runs when switched on, so it isn&rsquo;t using battery outside working time.</li>
      </ul>
""",
    faqs=[
        ("Does GPS tracking drain phone battery?",
         "Some, depending mostly on the update interval. Every 30 to 60 seconds is a reasonable balance; every second uses much more."),
        ("How can I make a tracker's battery last longer?",
         "Reduce the update frequency, keep it warm and in good signal, and keep phones on charge in vehicles."),
    ],
    related=["how-often-gps-trackers-update", "best-real-time-gps-tracking-app", "gps-tracking-rideshare-delivery-drivers"],
),
]
