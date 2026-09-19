"""Guides hub: GPS tracking by industry and use."""
from facts import BASE, TRIAL_DAYS, UPDATE_INTERVALS, gbp

HUB = "industry"

GUIDES = [
# ------------------------------------------------------------------------------------------
dict(
    slug="gps-tracking-business-efficiency",
    hub=HUB,
    h1="How does GPS tracking improve business efficiency?",
    title="How GPS Tracking Improves Business Efficiency (and Cuts Costs)",
    desc="How GPS tracking improves business efficiency: fewer wasted miles, lower fuel and maintenance costs, faster customer answers and less admin.",
    answer="""GPS tracking saves time and money in four main ways: <strong>sending the nearest person</strong> to each
      job, <strong>cutting wasted miles</strong> (and with them fuel and wear), <strong>answering customers
      instantly</strong> instead of ringing round, and <strong>replacing admin</strong> such as mileage logs and
      &ldquo;where are you?&rdquo; calls. The gains are largest for teams that spend much of the day on the road.""",
    body="""
      <h2>1. Dispatch the nearest person</h2>
      <p>With everyone on one live map, a new job goes to whoever is closest and free &mdash; not whoever answers the
      phone first. Across a week, that cuts driving time noticeably for most mobile teams.</p>

      <h2>2. GPS tracking for vehicle maintenance and fuel costs</h2>
      <ul>
        <li><strong>Fewer miles, less fuel.</strong> Route history shows detours, doubled-back journeys and rounds that
          could be ordered better.</li>
        <li><strong>Less wear.</strong> Fewer miles means fewer services, tyres and brakes over a year.</li>
        <li><strong>Mileage records.</strong> Route history makes it much easier to keep business mileage records, for
          example for HMRC mileage allowance claims, than relying on memory.</li>
      </ul>
      <p>For engine-level data (idling, harsh braking, fuel burn) you need vehicle telematics hardware; a phone app
      tracks the person, not the engine.</p>

      <h2>3. How GPS data improves customer service and response times</h2>
      <p>&ldquo;Your engineer is about 15 minutes away&rdquo; is a better answer than &ldquo;I&rsquo;ll find out and call
      you back&rdquo;. With a live map, anyone in the office can answer in seconds, and arrival alerts can confirm when
      someone reaches a site. Disputes (&ldquo;nobody turned up&rdquo;) are settled by the route history.</p>

      <h2>4. Less admin and fewer interruptions</h2>
      <p>No check-in calls, no paper mileage sheets, fewer timesheet queries. Staff get interrupted less, managers spend
      less time chasing. See <a href="/guides/gps-time-tracking-field-service/">GPS time tracking</a>.</p>

      <h2>Real-world examples: how businesses reduce costs with GPS tracking</h2>
      <p>The following are <strong>illustrative worked examples</strong>, not customer case studies:</p>
      <ul>
        <li><strong>A four-van plumbing firm</strong> sends emergency call-outs to whoever is nearest rather than
          whoever is next on the list. Saving 20 minutes of driving per call-out across a few call-outs a day adds up to
          hours a week of billable time.</li>
        <li><strong>A courier round</strong> uses route history to spot that two drops are done on separate loops every
          day; reordering them removes a daily detour.</li>
        <li><strong>A cleaning company</strong> answers &ldquo;is anyone coming?&rdquo; calls from the live map instead of
          phoning cleaners mid-job.</li>
      </ul>

      <h2>Is it worth it?</h2>
      <p>For most small mobile teams, if tracking saves each person even a few minutes of driving or admin a day, it
      pays for itself. The simplest way to find out is a trial with a couple of real team members. TrackLink offers
      {TRIAL_DAYS} days free.</p>
""".replace("{TRIAL_DAYS}", str(TRIAL_DAYS)),
    faqs=[
        ("Can GPS tracking reduce fuel costs?",
         "Yes, mainly by cutting wasted miles through better dispatch and routing. Detailed fuel-burn data needs vehicle telematics hardware."),
        ("Does GPS tracking help with HMRC mileage records?",
         "Route history makes business mileage much easier to record accurately. Check HMRC's current rules for what records you need to keep."),
    ],
    related=["gps-time-tracking-field-service", "gps-tracking-logistics-delivery", "gps-tracking-cost-small-business"],
),
# ------------------------------------------------------------------------------------------
dict(
    slug="gps-time-tracking-field-service",
    hub=HUB,
    h1="GPS time tracking for field service businesses: is it worth it?",
    title="GPS Time Tracking for Field Service Businesses: Worth It?",
    desc="Is GPS time tracking worth it for field service businesses? How location data supports timesheets, job costing, invoicing and accounting software.",
    answer="""For most field service businesses, yes. GPS time tracking gives you <strong>objective arrival and
      departure times</strong> for every job, which makes timesheets, job costing and customer invoices faster and far
      less disputed. The return comes from less admin, fewer disputes and more accurate billing, not from watching
      people.""",
    body="""
      <h2>What GPS time tracking actually records</h2>
      <ul>
        <li><strong>When someone arrives</strong> at and <strong>leaves</strong> each site.</li>
        <li><strong>Travel time</strong> between jobs.</li>
        <li><strong>Start and finish</strong> of the working day.</li>
      </ul>
      <p>With geofenced sites (&ldquo;zones&rdquo;), arrivals and departures are recorded and can trigger alerts
      automatically.</p>

      <h2>Evaluating the ROI for workforce management</h2>
      <ul>
        <li><strong>Billing accuracy.</strong> Charge for real time on site, backed by a record.</li>
        <li><strong>Fewer disputes.</strong> &ldquo;We were on site from 8:52 to 11:40&rdquo; ends most arguments.</li>
        <li><strong>Payroll.</strong> Overtime and travel time become simple to check.</li>
        <li><strong>Less admin.</strong> No chasing paper timesheets on a Friday.</li>
      </ul>

      <h2>Integration with accounting and invoicing software</h2>
      <p>Some tracking services integrate directly with accounting packages; many offer a CSV export that you can
      import into a spreadsheet, payroll or invoicing tool. TrackLink exports route history as CSV (time, position,
      speed, device and the person it belongs to), which works with most accounting and spreadsheet tools without a
      direct integration.</p>

      <h2>Doing it fairly</h2>
      <p>Time tracking works best when staff see it as protecting them too &mdash; a record that shows they were on site
      is as useful to them as to you. Limit tracking to working hours and explain it up front; see
      <a href="/guides/employee-concerns-gps-tracking/">managing employee concerns</a>.</p>
""",
    faqs=[
        ("Can GPS tracking replace timesheets?",
         "It can do most of the work, but many businesses keep a simple timesheet for breaks and exceptions. GPS gives the objective arrival and departure times."),
        ("Can I export GPS data to my accounting software?",
         "With a CSV export you can bring the data into spreadsheets and most accounting or payroll tools. TrackLink exports route history as CSV."),
    ],
    related=["gps-tracking-business-efficiency", "gps-tracking-electricians-tradespeople", "gps-tracking-vs-employee-monitoring"],
),
# ------------------------------------------------------------------------------------------
dict(
    slug="gps-tracking-contractors-job-sites",
    hub=HUB,
    h1="GPS tracking for contractors: how to track job sites legally",
    title="GPS Tracking for Contractors: How to Track Job Sites Legally",
    desc="GPS tracking for contractors and field workers: tracking job sites and arrivals legally in the UK, subcontractors, and what to put in writing before you start.",
    answer="""Contractors can track <strong>their own employees at job sites</strong> lawfully by being open about
      it, limiting it to working time and having a clear reason, such as coordinating teams or confirming site
      attendance. Tracking <strong>self-employed subcontractors</strong> needs their agreement and should be limited to
      what the contract actually requires.""",
    body="""
      <h2>Implementing tracking for field workers and projects</h2>
      <ol>
        <li><strong>Define the purpose:</strong> scheduling, site attendance, lone-worker safety, client updates.</li>
        <li><strong>Set up your sites as zones</strong> so arrivals and departures are logged automatically.</li>
        <li><strong>Tell the team</strong> in a short written policy what is tracked, when and why.</li>
        <li><strong>Limit it to working hours</strong>, especially if people use their own phones or vehicles.</li>
      </ol>

      <h2>Employees vs subcontractors</h2>
      <ul>
        <li><strong>Employees:</strong> the usual rules apply &mdash; a lawful basis (normally legitimate interests),
          transparency and proportionality. See <a href="/guides/is-gps-tracking-legal-uk-business/">is GPS tracking
          legal for UK businesses</a>.</li>
        <li><strong>Self-employed subcontractors:</strong> you have much less basis to monitor them. If you need proof of
          attendance, agree it in the contract and keep it to site attendance during the job.</li>
      </ul>

      <h2>How to track job sites legally</h2>
      <ul>
        <li>Track people, not their private lives: tracking should stop at the end of the day.</li>
        <li>Keep records only as long as you need them for the job, payroll or disputes.</li>
        <li>Be ready to show staff their own data if they ask.</li>
      </ul>

      <h2>How TrackLink works for contractors</h2>
      <p>Create each site as a zone and TrackLink records arrivals and departures and can alert your Hub users. Your
      team switch tracking on at the start of the day from their Android phones and off at the end, and a notification
      shows while it runs.</p>
""",
    faqs=[
        ("Can I track subcontractors with GPS?",
         "Only with their agreement, and only as far as the contract needs — typically attendance at your sites during the job."),
        ("Can GPS tracking prove site attendance?",
         "It gives strong evidence of arrival and departure times, typically to within a few metres outdoors."),
    ],
    related=["gps-tracking-electricians-tradespeople", "gps-construction-equipment-theft", "is-gps-tracking-legal-uk-business"],
),
# ------------------------------------------------------------------------------------------
dict(
    slug="gps-tracking-electricians-tradespeople",
    hub=HUB,
    h1="GPS tracking solutions for electricians and tradespeople",
    title="GPS Tracking for Electricians and Tradespeople (UK)",
    desc="GPS tracking solutions for electricians, plumbers and tradespeople: fleet tracking for small trade firms, job timing, customer ETAs and keeping costs down.",
    answer="""For electricians, plumbers and other trades, the most useful GPS tracking is simple: <strong>a live map
      of your vans or engineers</strong>, <strong>route history</strong> to settle job times, and <strong>arrival
      alerts</strong> for key sites. Small trade firms rarely need full vehicle telematics; a phone app on each
      engineer&rsquo;s phone covers the day-to-day for far less.""",
    body=f"""
      <h2>What trade businesses actually use tracking for</h2>
      <ul>
        <li><strong>Emergency call-outs</strong> &mdash; send whoever is nearest.</li>
        <li><strong>Customer ETAs</strong> &mdash; tell customers when the engineer will arrive.</li>
        <li><strong>Job timing</strong> &mdash; how long each job really took, for quoting and invoicing.</li>
        <li><strong>Lone working</strong> &mdash; know where your people are if something goes wrong.</li>
      </ul>

      <h2>Industry-specific fleet management needs</h2>
      <ul>
        <li><strong>Mixed vehicles.</strong> Engineers often switch between vans or use their own. Tracking the person
          rather than the vehicle avoids re-fitting trackers.</li>
        <li><strong>Tools and materials.</strong> Tools stored in vans are a theft target; for kit you need separate
          asset trackers &mdash; see <a href="/guides/track-company-assets-gps/">tracking company assets</a>.</li>
        <li><strong>Small teams.</strong> A two- to ten-person firm needs something that works in minutes without an
          installer.</li>
      </ul>

      <h2>Keeping it fair for your engineers</h2>
      <p>Tradespeople often have strong views on being tracked. Being clear that tracking is for dispatch and customer
      updates, and that it stops at the end of the day, goes a long way. See
      <a href="/guides/employee-concerns-gps-tracking/">managing employee concerns</a>.</p>

      <h2>TrackLink for trade firms</h2>
      <p>TrackLink starts at {gbp(BASE)} a month for one office user and three engineers, runs on Android phones,
      updates {UPDATE_INTERVALS}, and includes route history, groups (for example &ldquo;Electrical&rdquo; and
      &ldquo;Plumbing&rdquo;) and zone arrival alerts.</p>
""",
    faqs=[
        ("Do electricians need vehicle trackers or a phone app?",
         "For dispatch, ETAs and job times, a phone app is usually enough. Fitted trackers make sense for pool vans or if you want engine data."),
        ("Can I track tools and equipment too?",
         "Not with a phone app — use small dedicated asset trackers for valuable tools and kit."),
    ],
    related=["gps-tracking-contractors-job-sites", "gps-time-tracking-field-service", "gps-tracking-business-efficiency"],
),
# ------------------------------------------------------------------------------------------
dict(
    slug="gps-tracking-logistics-delivery",
    hub=HUB,
    h1="GPS tracking for logistics and delivery companies",
    title="GPS Tracking for Logistics and Delivery Companies",
    desc="GPS tracking for logistics and delivery companies: route planning, proof of delivery timing, customer transparency and live ETAs for small delivery fleets.",
    answer="""For logistics and delivery companies, GPS tracking provides <strong>live visibility of every
      driver</strong>, <strong>route history for planning and proof</strong>, and <strong>better customer
      transparency</strong> &mdash; accurate ETAs and confirmation of when a drop was made. Small delivery fleets can get
      most of that from a phone app; larger operations often add route-optimisation and vehicle telematics.""",
    body="""
      <h2>Route planning and optimisation</h2>
      <p>Route history is the raw material for better planning: it shows how long each run really takes, where drivers
      lose time and which drops belong together. Dedicated route-optimisation software can plan the order of stops;
      tracking tells you what actually happened.</p>

      <h2>Customer transparency</h2>
      <ul>
        <li><strong>Live ETAs</strong> answered from the map, without calling the driver.</li>
        <li><strong>Delivery timing</strong> confirmed from route history, or automatically with zone arrival alerts
          for regular drop points.</li>
        <li><strong>Fewer &ldquo;where&rsquo;s my delivery?&rdquo; calls</strong> tying up the office.</li>
      </ul>

      <h2>Driver safety and accountability</h2>
      <p>Knowing where drivers are helps if a vehicle breaks down or a driver is working alone late. Route history also
      protects drivers: it shows they were where they said they were.</p>

      <h2>Choosing tracking for a small delivery fleet</h2>
      <ul>
        <li><strong>Owner-drivers or regular drivers:</strong> a phone app is quick to roll out and costs little.</li>
        <li><strong>Large, shared fleets:</strong> fitted telematics per vehicle.</li>
        <li><strong>High-value loads:</strong> consider separate trackers on trailers or cargo.</li>
      </ul>
      <p>See also <a href="/guides/gps-tracking-rideshare-delivery-drivers/">GPS tracking for delivery drivers</a> and
      <a href="/guides/how-often-gps-trackers-update/">how often trackers update</a>.</p>
""",
    faqs=[
        ("Is GPS tracking proof of delivery?",
         "It shows the driver was at the address at a given time, which is strong supporting evidence. Many businesses pair it with a photo or signature."),
        ("What update interval suits delivery tracking?",
         "Every 30 to 60 seconds is enough for ETAs and route history. Faster intervals use more battery."),
    ],
    related=["gps-tracking-rideshare-delivery-drivers", "gps-tracking-business-efficiency", "how-often-gps-trackers-update"],
),
# ------------------------------------------------------------------------------------------
dict(
    slug="gps-tracking-rideshare-delivery-drivers",
    hub=HUB,
    h1="GPS tracking for rideshare and delivery drivers",
    title="GPS Tracking for Rideshare and Delivery Drivers",
    desc="GPS tracking for rideshare and delivery drivers: route optimisation, safety, mileage records and battery tips — for self-employed drivers and small delivery firms.",
    answer="""Rideshare and gig delivery platforms already track drivers while they work. Where extra GPS tracking
      helps is <strong>your own records</strong>: business mileage, working patterns and <strong>safety</strong> &mdash;
      someone you trust knowing where you are on a late shift. For small delivery firms employing drivers, a team
      tracking app adds dispatch and route history.""",
    body="""
      <h2>For self-employed rideshare and delivery drivers</h2>
      <ul>
        <li><strong>Mileage records.</strong> Keeping a record of business mileage helps with tax. Route history is
          far more accurate than memory.</li>
        <li><strong>Knowing your best areas and hours.</strong> Your own route history shows where your time goes.</li>
        <li><strong>Safety.</strong> Sharing your location with a trusted person on late shifts.</li>
      </ul>

      <h2>Route optimisation and safety for delivery firms</h2>
      <p>If you run a small delivery business with employed drivers, tracking helps you dispatch the nearest driver,
      give customers ETAs and plan better rounds. See
      <a href="/guides/gps-tracking-logistics-delivery/">GPS tracking for logistics and delivery companies</a>.</p>

      <h2>Battery tips for drivers</h2>
      <ul>
        <li>Keep the phone on charge in a dashboard mount.</li>
        <li>Use a 30 to 60 second interval unless you need live following.</li>
        <li>Exclude your tracking app from battery optimisation so it keeps running.</li>
      </ul>
      <p>More in <a href="/guides/gps-tracker-battery-life/">battery life</a>.</p>

      <h2>Privacy for drivers</h2>
      <p>If an employer or platform tracks you, UK data protection law still applies: you are entitled to know what is
      collected and to request your data. See <a href="/guides/can-employer-track-your-phone/">can your employer track
      your phone</a>.</p>
""",
    faqs=[
        ("Do rideshare apps track drivers?",
         "Yes, while you are logged in and working. You can request the data a platform holds about you under UK data protection law."),
        ("Is GPS good enough for mileage records?",
         "GPS route history is typically far more accurate than a hand-written log. Check HMRC's current guidance on the records you need to keep."),
    ],
    related=["gps-tracking-logistics-delivery", "gps-tracker-battery-life", "can-employer-track-your-phone"],
),
# ------------------------------------------------------------------------------------------
dict(
    slug="gps-tracking-seasonal-businesses",
    hub=HUB,
    h1="GPS tracking for seasonal businesses",
    title="GPS Tracking for Seasonal Businesses: Scale Up and Down",
    desc="GPS tracking for seasonal businesses — landscapers, farms, events, gritting and holiday services — and how to choose tracking that scales with your busy season.",
    answer="""Seasonal businesses need tracking that can <strong>scale up for the busy season and back down
      afterwards</strong> without long contracts or hardware sitting in a drawer. Phone-based tracking with monthly
      seat changes is usually the best fit: add seasonal staff when you hire them, remove the seats when the season
      ends.""",
    body="""
      <h2>Which seasonal businesses use GPS tracking?</h2>
      <ul>
        <li><strong>Landscaping and grounds maintenance</strong> in spring and summer.</li>
        <li><strong>Farms</strong> at harvest, with extra drivers and contractors.</li>
        <li><strong>Winter gritting and snow clearing.</strong></li>
        <li><strong>Events and festivals</strong>, with crews spread across a site.</li>
        <li><strong>Holiday lets, cleaning and changeover teams.</strong></li>
      </ul>

      <h2>What to look for</h2>
      <ul>
        <li><strong>No long contracts</strong> &mdash; avoid paying for trackers all winter.</li>
        <li><strong>No hardware to fit</strong> &mdash; seasonal staff can use their own phones for work hours.</li>
        <li><strong>Quick onboarding</strong> &mdash; invite a batch of new starters in one go.</li>
        <li><strong>Groups</strong> &mdash; separate seasonal crews on the map.</li>
      </ul>

      <h2>Seasonal staff and privacy</h2>
      <p>Seasonal and temporary workers have the same data protection rights as permanent staff. Tell them about
      tracking when they start, limit it to working hours and remove their access when the season ends. See
      <a href="/guides/is-gps-tracking-legal-uk-business/">is GPS tracking legal</a>.</p>

      <h2>How TrackLink handles seasonal teams</h2>
      <p>You can add and remove seats month to month, invite many people at once by email, organise them into groups,
      and remove people (and their data) at the end of the season.</p>
""",
    faqs=[
        ("Can I pause GPS tracking in the off-season?",
         "With a monthly plan you can reduce seats when the season ends rather than paying for unused trackers."),
    ],
    related=["gps-tracking-cost-small-business", "employee-concerns-gps-tracking", "choosing-a-gps-tracker"],
),
# ------------------------------------------------------------------------------------------
dict(
    slug="gps-tracking-hikers-outdoors",
    hub=HUB,
    h1="GPS tracking for hikers and outdoor enthusiasts",
    title="GPS Tracking for Hikers and Outdoor Enthusiasts (UK)",
    desc="GPS tracking for hikers and walkers in the UK: phone GPS vs satellite messengers, sharing your location and staying safe where there is no signal.",
    answer="""For most UK hill walking, <strong>your phone&rsquo;s GPS plus offline maps</strong> works well, as long
      as you protect the battery and carry a backup. Where there is no mobile signal, a phone can still show where you
      are but can&rsquo;t share it; <strong>satellite messengers</strong> fill that gap. Always leave a route plan with
      someone, and don&rsquo;t rely on a phone alone in the mountains.""",
    body="""
      <h2>Phone GPS for walking and hiking</h2>
      <ul>
        <li><strong>Download maps offline</strong> before you go; GPS works without signal, but map tiles don&rsquo;t.</li>
        <li><strong>Protect the battery</strong>: airplane mode with location on, a power bank, keep the phone warm.</li>
        <li><strong>Carry a paper map and compass</strong> and know how to use them.</li>
      </ul>

      <h2>Safety and emergency communication</h2>
      <ul>
        <li><strong>Leave a route plan</strong> and expected return time with someone.</li>
        <li><strong>Share your location</strong> with a trusted person while you have signal.</li>
        <li><strong>In an emergency</strong>, call 999 and ask for the police, then mountain rescue.</li>
        <li><strong>No signal?</strong> A satellite messenger or personal locator beacon can send an alert or position
          without mobile coverage.</li>
      </ul>

      <h2>Dedicated GPS devices and satellite messengers</h2>
      <p>Handheld GPS units have long battery life and rugged builds. Satellite messengers send your position via
      satellite, so someone at home can follow you where phones can&rsquo;t reach; they usually need a subscription. See
      <a href="/guides/gps-tracking-without-signal/">GPS without signal</a> for how offline GPS works.</p>

      <h2>Where TrackLink fits (and doesn&rsquo;t)</h2>
      <p>TrackLink is built for businesses tracking working teams, not personal hiking. It can suit <strong>outdoor
      businesses</strong> &mdash; guides, outdoor activity instructors, estate and countryside staff &mdash; that want
      to see where their team is during working hours. It is not a safety or emergency device and depends on mobile
      signal to share positions live.</p>
""",
    faqs=[
        ("Does phone GPS work in the mountains without signal?",
         "GPS works without signal, so your phone can show where you are on offline maps. It can't share your location until it reconnects."),
        ("What is the best GPS tracker for hiking?",
         "For most walkers, a phone with offline maps and a power bank. For remote areas without coverage, add a satellite messenger."),
    ],
    related=["gps-tracking-without-signal", "gps-tracker-battery-life", "how-accurate-is-gps-tracking"],
),
]
