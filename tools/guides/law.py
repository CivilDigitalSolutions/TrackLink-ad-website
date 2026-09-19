"""Guides hub: UK law and privacy.

Written for UK law (UK GDPR, the Data Protection Act 2018, the ICO's guidance on monitoring
workers, the Protection from Harassment Act 1997). Every guide in this hub gets a "not legal
advice" note from the builder. The ICO guidance was under review following the Data (Use and
Access) Act 2025 at the time of writing, so the guides point readers at the ICO for the current text.
"""
HUB = "law"

ICO_MONITORING = "https://ico.org.uk/for-organisations/uk-gdpr-guidance-and-resources/employment/monitoring-workers/"
ICO_RIGHTS = "https://ico.org.uk/for-the-public/"
CPS_STALKING = "https://www.cps.gov.uk/legal-guidance/stalking-and-harassment"

GUIDES = [
# ------------------------------------------------------------------------------------------
dict(
    slug="is-gps-tracking-legal-uk-business",
    hub=HUB,
    h1="Is GPS tracking legal for UK businesses and company vehicles?",
    title="Is GPS Tracking Legal for Fleet Businesses? (UK Guide)",
    desc="Is it legal to put a GPS tracker on a company vehicle in the UK? What UK GDPR and the ICO expect from fleet businesses, plus a compliance checklist.",
    answer=f"""Yes &mdash; in the UK it is generally <strong>legal for a business to use GPS tracking on company vehicles
      and staff</strong>, provided you have a genuine business reason, you <strong>tell people</strong> what you track
      and why, you track no more than you need, and you handle the data under UK GDPR. What usually gets businesses
      into trouble isn&rsquo;t tracking itself; it&rsquo;s tracking <em>secretly</em>, or tracking people in their own
      time.""",
    body=f"""
      <h2>Is it legal to put a GPS tracker on a company vehicle?</h2>
      <p>A company can generally track its own vehicles. But a vehicle is almost always driven by a person, and a
      vehicle&rsquo;s location tells you where that person is &mdash; so the location data is usually
      <strong>personal data</strong>, and UK data protection law applies. That means you need:</p>
      <ul>
        <li><strong>A lawful basis.</strong> For most businesses this is <em>legitimate interests</em> &mdash; for example
          safety, security, scheduling or responding to customers. The ICO points out that <em>consent</em> is often
          the wrong basis at work, because staff may feel they have no real choice.</li>
        <li><strong>Transparency.</strong> The ICO says employers <em>must</em> tell workers about monitoring in a way
          that is easy to understand: what is monitored, why, and how.</li>
        <li><strong>Proportionality.</strong> Pick the least intrusive way to achieve your purpose, and don&rsquo;t
          collect more than you need or keep it longer than you need.</li>
      </ul>

      <h2>Is GPS tracking legal for fleet businesses?</h2>
      <p>Yes, and it is common &mdash; couriers, trades, logistics and field-service firms use it every day. The same
      rules apply at fleet scale, plus a few practical points that matter more with a fleet:</p>
      <ul>
        <li><strong>Private use.</strong> If staff may use a vehicle privately (evenings, weekends), tracking those
          journeys is much harder to justify. Allow tracking to be switched off outside working time, or don&rsquo;t
          look at private trips.</li>
        <li><strong>Who can see it.</strong> Limit access to the people who need it, such as dispatchers and managers.</li>
        <li><strong>How long you keep it.</strong> Set a retention period and stick to it. (TrackLink deletes route
          history automatically after 30 days as standard.)</li>
      </ul>

      <h2>Covert tracking: the line not to cross</h2>
      <p>The ICO&rsquo;s position is that covert monitoring is unlikely to be justified in normal circumstances. The
      narrow exception is a specific investigation into suspected criminal activity or gross misconduct &mdash;
      authorised at a senior level, time-limited and assessed first. Secretly tracking staff &ldquo;to see what they get
      up to&rdquo; doesn&rsquo;t meet that bar.</p>

      <h2>GPS tracking compliance checklist (UK)</h2>
      <ol>
        <li>Write down <strong>why</strong> you are tracking and why a less intrusive option wouldn&rsquo;t do.</li>
        <li>Carry out a <strong>data protection impact assessment</strong> (DPIA). The ICO says you should do one for
          monitoring even when it is not strictly required.</li>
        <li>Write a short <strong>tracking policy</strong> and give it to staff before you start.</li>
        <li>Update your <strong>privacy notice</strong> for employees.</li>
        <li>Decide what happens <strong>outside working hours</strong> and on private journeys.</li>
        <li>Limit <strong>access</strong> to those who need it.</li>
        <li>Set a <strong>retention period</strong> and make sure data is actually deleted.</li>
        <li>Be ready for <strong>subject access requests</strong> &mdash; staff can ask for the tracking data you hold on them.</li>
      </ol>
      <p>This checklist replaces the US-style &ldquo;compliance checklist by state&rdquo;: in the UK the same data
      protection law applies across England, Scotland, Wales and Northern Ireland.</p>

      <h2>How TrackLink is designed to help</h2>
      <ul>
        <li>Only the person holding the phone can switch their tracking on or off &mdash; there is no remote switch.</li>
        <li>A visible notification shows whenever tracking is running, so it is never covert.</li>
        <li>Route history is deleted automatically after 30 days.</li>
        <li>Data is stored in London and walled off per organisation.</li>
      </ul>
      <p>You remain responsible for using it lawfully &mdash; the tool can make transparency easy, but the policy
      and the decisions are yours. The ICO&rsquo;s <a href="{ICO_MONITORING}" rel="noopener">guidance on monitoring
      workers</a> is the place to check current expectations.</p>
""",
    faqs=[
        ("Do I need my employees' consent to track company vehicles?",
         "Usually not — and consent is often the wrong lawful basis at work, because staff may not feel free to refuse. Most employers rely on legitimate interests, which still requires you to tell staff about the tracking and keep it proportionate."),
        ("Can I track a company vehicle outside working hours?",
         "Tracking private use is much harder to justify. Many employers let staff switch tracking off, or simply don't record, outside working hours."),
        ("Do I need to tell staff where the tracker is?",
         "You need to tell staff that tracking happens, what it records and why. Covert tracking is only justifiable in narrow circumstances, such as investigating suspected crime."),
    ],
    related=["can-employer-track-your-phone", "employee-concerns-gps-tracking", "gps-tracking-contractors-job-sites"],
),
# ------------------------------------------------------------------------------------------
dict(
    slug="can-employer-track-your-phone",
    hub=HUB,
    h1="Can your employer track your phone? Your rights in the UK",
    title="Can Your Employer Track Your Phone Without Permission? (UK)",
    desc="Can your employer track your phone without permission? How to tell if your employer is tracking your location, and whether you can refuse at work (UK).",
    answer="""Your employer <strong>cannot lawfully track your personal phone in secret</strong>. Tracking a
      work phone or a work app is generally allowed, but UK data protection law says they must <strong>tell you what
      they track and why</strong>, keep it proportionate, and not use it to monitor your private life. If you think
      you are being tracked without being told, you can ask your employer for the data they hold on you.""",
    body=f"""
      <h2>Can your employer track your personal phone without permission?</h2>
      <p>Not secretly, and not without a good reason. Installing tracking on your own phone without your knowledge
      would be covert monitoring, which the ICO says is very unlikely to be justified at work &mdash; and accessing your
      phone or accounts without authorisation can also be a criminal offence under the Computer Misuse Act 1990.</p>
      <p>What is common, and generally lawful, is an employer asking you to <strong>install a work app</strong> on a
      phone (yours or theirs) that shares your location <strong>while you work</strong>. In that case you should have been
      told what it collects, when, and why.</p>

      <h2>Work phone vs personal phone</h2>
      <ul>
        <li><strong>Company phone:</strong> your employer has more scope to manage the device, but monitoring still has
          to be transparent and proportionate.</li>
        <li><strong>Your own phone for work:</strong> any tracking should be limited to work time and work purposes.
          An app that tracks you around the clock on your personal phone is hard to justify.</li>
      </ul>

      <h2>How to know if your employer is tracking your location</h2>
      <ol>
        <li><strong>Check your contract, handbook and privacy notice.</strong> Monitoring should be described there.</li>
        <li><strong>Look at the apps on the phone.</strong> Work apps, device-management profiles or anything you
          were asked to install.</li>
        <li><strong>Check location permissions.</strong> On Android: Settings &rarr; Location &rarr; App location permissions
          shows which apps can use your location and when.</li>
        <li><strong>Look for a persistent notification.</strong> On Android, apps that track continuously in the
          background generally show one.</li>
        <li><strong>Ask.</strong> You can make a <em>subject access request</em> for the personal data your employer holds
          about you, including location data.</li>
      </ol>

      <h2>Can you refuse GPS tracking at work?</h2>
      <p>It depends. If tracking is lawful, proportionate and part of your job (for example a delivery driver on shift),
      refusing outright may become a conduct issue. But you have real rights:</p>
      <ul>
        <li><strong>The right to be told</strong> what is tracked and why.</li>
        <li><strong>The right to object</strong> where your employer relies on legitimate interests; they must then show
          compelling reasons that override your interests.</li>
        <li><strong>The right of access</strong> to the data they hold on you.</li>
        <li><strong>A reasonable expectation of privacy</strong> in your own time &mdash; tracking outside working hours
          is much harder for an employer to justify.</li>
      </ul>
      <p>If you can&rsquo;t resolve it with your employer, Acas and the ICO both offer guidance, and you can complain to the ICO.</p>

      <h2>What fair workplace tracking looks like</h2>
      <p>A fair set-up is visible and under your control: you know when it is on, you can see that it is running, and
      it isn&rsquo;t tracking you in your own time. That is how TrackLink works &mdash; only the person holding the phone
      can switch tracking on or off, and a notification shows whenever it is running. (Employers are still responsible
      for using it lawfully.)</p>
""",
    faqs=[
        ("Is it legal for my employer to track me without telling me?",
         "Generally no. UK data protection law requires transparency; covert monitoring is only justifiable in narrow cases such as investigating suspected crime."),
        ("Can my employer track me after work?",
         "Tracking outside working hours is very hard to justify. If a work app or vehicle tracks you in your own time, ask your employer why."),
        ("How do I get the location data my employer holds on me?",
         "Make a subject access request in writing. Employers normally have one month to respond."),
    ],
    related=["is-gps-tracking-legal-uk-business", "can-someone-track-your-location", "employee-concerns-gps-tracking"],
),
# ------------------------------------------------------------------------------------------
dict(
    slug="gps-tracking-personal-vehicles-law",
    hub=HUB,
    h1="GPS tracking on personal vehicles: the legal issues (UK)",
    title="Legal Issues With GPS Tracking on Personal Vehicles (UK)",
    desc="The legal issues with GPS tracking on personal vehicles in the UK, and whether you can track a vehicle with GPS without the owner knowing. Plain-English guide.",
    answer=f"""Putting a GPS tracker on <strong>someone else&rsquo;s vehicle without their knowledge</strong> can be
      a criminal offence in the UK &mdash; covert tracking is a recognised form of stalking and harassment. Tracking
      your <strong>own</strong> vehicle is fine. For businesses, tracking an employee&rsquo;s <strong>personal</strong>
      car is only defensible for work journeys, with the employee fully informed.""",
    body=f"""
      <h2>Can you track a vehicle with GPS without the owner knowing?</h2>
      <p>You can track your own vehicle however you like. Tracking a vehicle <strong>someone else</strong> owns or
      uses, without their knowledge, is where the law comes in:</p>
      <ul>
        <li><strong>Stalking and harassment.</strong> The Protection from Harassment Act 1997 lists behaviours
          associated with stalking, including &ldquo;watching or spying on a person&rdquo; and monitoring their
          electronic communications. The Crown Prosecution Service&rsquo;s
          <a href="{CPS_STALKING}" rel="noopener">guidance</a> treats covert surveillance as a stalking behaviour, and
          secretly tracking a partner&rsquo;s or ex-partner&rsquo;s car has led to prosecutions.</li>
        <li><strong>Data protection.</strong> A business tracking a person without a lawful basis and without telling
          them is likely to breach UK GDPR.</li>
      </ul>
      <p>If you are worried <em>you</em> are being tracked, see
      <a href="/guides/detect-remove-gps-tracker/">how to detect and remove a GPS tracker</a>.</p>

      <h2>Legal issues with GPS tracking on personal vehicles used for work</h2>
      <p>Many small businesses rely on staff using their own cars or vans. You can&rsquo;t fit a tracker to a
      car you don&rsquo;t own without permission, and even with permission, tracking someone&rsquo;s private journeys
      in their own vehicle is very hard to justify. The workable approach is to track the <strong>person during working
      time</strong>, not the vehicle all the time:</p>
      <ul>
        <li>Use a phone app the employee switches on at the start of a shift and off at the end.</li>
        <li>Put it in writing: what is tracked, when, why and who sees it.</li>
        <li>Keep only what you need, for as long as you need it.</li>
      </ul>

      <h2>Family and shared vehicles</h2>
      <p>Tracking a vehicle you own that a family member drives is a grey area that depends on circumstances. Being
      open about it is both the ethical and the legally safer approach; secret tracking of an adult family member or
      partner can cross into harassment.</p>

      <h2>Where TrackLink fits</h2>
      <p>TrackLink tracks a <em>phone</em>, not a vehicle, and only while its holder has switched tracking on &mdash;
      which makes it a natural fit for staff using their own vehicles for work, and unsuited to covert tracking by
      design.</p>
""",
    faqs=[
        ("Is it illegal to put a tracker on someone's car in the UK?",
         "Doing it covertly to monitor a person can amount to stalking or harassment, which are criminal offences. Tracking your own vehicle is lawful."),
        ("Can my employer track my personal car?",
         "Only with your knowledge, and realistically only for work journeys. Continuous tracking of your private use would be very hard for an employer to justify."),
    ],
    related=["is-gps-tracking-legal-uk-business", "detect-remove-gps-tracker", "can-someone-track-your-location"],
),
# ------------------------------------------------------------------------------------------
dict(
    slug="can-someone-track-your-location",
    hub=HUB,
    h1="Can someone track your location without you knowing?",
    title="Can Someone Track Your Location Without Your Knowledge?",
    desc="Can someone track your location without your knowledge, or track your phone without an app? How covert tracking happens, the UK law, and how to check your phone.",
    answer="""It is possible, but it usually requires <strong>access to your phone or your accounts</strong>, or a
      hidden tracker on something you carry or drive. Most real cases involve someone who already knew a password or
      had the phone in their hands. In the UK, covertly tracking someone can be a criminal offence. The fix is
      usually straightforward: check your location sharing, your apps and your account security.""",
    body=f"""
      <h2>How covert location tracking actually happens</h2>
      <ul>
        <li><strong>Shared accounts.</strong> Someone who knows your Google or Apple account password can see your
          phone&rsquo;s location through the device-finding features built into those accounts.</li>
        <li><strong>Location sharing left on.</strong> Maps and family apps let you share your location &mdash; sometimes
          indefinitely &mdash; and it is easy to forget it is on.</li>
        <li><strong>Stalkerware.</strong> Apps secretly installed by someone with access to your unlocked phone.</li>
        <li><strong>Hidden hardware.</strong> A small tracker or item-finder tag in a bag or car.</li>
      </ul>

      <h2>Can you track someone&rsquo;s phone without an app?</h2>
      <p>Only through the phone&rsquo;s own account features &mdash; for example Google&rsquo;s or Apple&rsquo;s
      find-my-device services &mdash; which need that person&rsquo;s account login. Using someone else&rsquo;s account
      without permission to locate them is unauthorised access, which can be an offence under the Computer Misuse Act
      1990, and doing it to monitor someone can amount to stalking. There is no legitimate &ldquo;track any number&rdquo;
      service; sites claiming to locate a phone from its number alone should be treated as scams.</p>

      <h2>How to check whether your phone is sharing your location</h2>
      <ol>
        <li>Review location sharing in your maps and messaging apps and stop anything you don&rsquo;t recognise.</li>
        <li>On Android: Settings &rarr; Location &rarr; App location permissions &mdash; check which apps can see your
          location and whether it is &ldquo;all the time&rdquo;.</li>
        <li>Look for unfamiliar apps and device-admin or device-management profiles.</li>
        <li>Change your Google/Apple password and turn on two-step verification, then sign out other devices.</li>
        <li>For physical trackers, see <a href="/guides/detect-remove-gps-tracker/">how to detect a GPS tracker</a>.</li>
      </ol>

      <h2>If you think you are being tracked</h2>
      <p>If you are worried for your safety, contact the police (999 in an emergency). Removing stalkerware or a
      tracker can alert the person who placed it, so if you are in a risky situation, speak to a specialist support
      service first. The CPS treats covert surveillance as a stalking behaviour.</p>

      <h2>The legitimate side: transparent tracking</h2>
      <p>Location tracking has plenty of legitimate uses &mdash; families who agree to share, and businesses
      coordinating their teams. The difference is <strong>knowledge and control</strong>. TrackLink is built on that
      principle: tracking only runs when the person holding the phone switches it on, and a notification shows while
      it does.</p>
""",
    faqs=[
        ("Can someone track my phone with just my number?",
         "Not through any legitimate service. Location lookups by number alone are a common scam. Real phone location needs access to the phone or its accounts."),
        ("Will I know if someone is tracking my phone?",
         "Not always, which is why it is worth checking location sharing, app permissions and account security regularly."),
    ],
    related=["detect-remove-gps-tracker", "what-data-gps-trackers-collect", "can-employer-track-your-phone"],
),
# ------------------------------------------------------------------------------------------
dict(
    slug="detect-remove-gps-tracker",
    hub=HUB,
    h1="How to detect and remove a GPS tracker from your vehicle",
    title="How to Detect a GPS Tracker on Your Vehicle (and Remove It)",
    desc="How to detect a GPS tracker on your vehicle, where hidden trackers are usually placed, and how to remove a GPS tracker safely and legally in the UK.",
    answer="""Most hidden vehicle trackers are <strong>magnetic or battery units under the car, in wheel arches or
      bumpers</strong>, or small plug-in devices in the <strong>OBD port</strong> under the dashboard. Check those places
      with a torch, look for unexplained wiring, and use your phone to scan for unknown item-finder tags. If you find
      one on a vehicle you own, you can remove it &mdash; but if you think someone is stalking you, contact the police
      before you do.""",
    body="""
      <h2>How to detect a GPS tracker on your vehicle</h2>
      <p>Do a slow, systematic check in daylight or with a good torch:</p>
      <ol>
        <li><strong>Underneath:</strong> along the sills, behind the bumpers and on the chassis rails &mdash; anywhere
          flat and metal where a magnetic box could stick.</li>
        <li><strong>Wheel arches:</strong> feel behind the plastic liners.</li>
        <li><strong>OBD port:</strong> usually under the dashboard on the driver&rsquo;s side. Anything plugged in that
          you didn&rsquo;t fit is worth questioning.</li>
        <li><strong>Inside:</strong> under seats, in seat pockets, the boot and spare-wheel well, and the glovebox.</li>
        <li><strong>Behind the dashboard or near the battery:</strong> hardwired trackers take power from the
          vehicle; look for wiring that doesn&rsquo;t match the rest.</li>
        <li><strong>Item-finder tags:</strong> both Android and iPhone can alert you to, or scan for, unknown Bluetooth
          trackers travelling with you. Check your phone&rsquo;s safety settings for this feature.</li>
      </ol>
      <p>If you still suspect a tracker, a garage or a specialist sweep service can check properly.</p>

      <h2>Is it a legitimate tracker?</h2>
      <p>Not every tracker is sinister. Finance companies, lease firms, insurers (telematics &ldquo;black boxes&rdquo;)
      and employers may fit trackers legitimately, and should have told you. Check your finance, lease, insurance and
      employment paperwork before assuming the worst.</p>

      <h2>How to remove a GPS tracker safely and legally</h2>
      <ul>
        <li><strong>Your own vehicle, unexplained tracker:</strong> you can remove it. Photograph it where you found it
          first &mdash; it may be evidence.</li>
        <li><strong>If you suspect stalking:</strong> speak to the police before removing it. Removal can alert the
          person watching you, and the device is evidence.</li>
        <li><strong>A company, lease or finance vehicle:</strong> removing a tracker you agreed to may breach your
          agreement &mdash; raise it with the company instead.</li>
        <li><strong>Hardwired units:</strong> have a professional remove them; cutting wires can damage the
          vehicle&rsquo;s electrics.</li>
      </ul>

      <h2>A note on GPS jammers</h2>
      <p>Using a GPS or phone jammer to block a tracker is <strong>illegal in the UK</strong> under section 68 of the
      Wireless Telegraphy Act 2006, with penalties of up to two years in prison and an unlimited fine. Jammers also
      interfere with other people&rsquo;s signals. Remove the tracker instead. See
      <a href="/guides/what-blocks-gps-tracker/">what blocks a GPS tracker</a> for more.</p>
""",
    faqs=[
        ("Where are GPS trackers usually hidden on a car?",
         "Under the car on flat metal surfaces, behind bumpers, inside wheel arches, in the OBD port under the dashboard, or inside under seats and in the boot."),
        ("Is it legal to remove a GPS tracker from my car?",
         "From a vehicle you own, yes. From a company, lease or finance vehicle, check your agreement first — and if you suspect stalking, contact the police before removing it."),
        ("Can my phone detect a GPS tracker?",
         "Phones can detect many Bluetooth item-finder tags travelling with you. Dedicated GPS trackers with their own SIM don't use Bluetooth, so a physical check is still needed."),
    ],
    related=["can-someone-track-your-location", "gps-tracking-personal-vehicles-law", "what-blocks-gps-tracker"],
),
# ------------------------------------------------------------------------------------------
dict(
    slug="what-data-gps-trackers-collect",
    hub=HUB,
    h1="What information can GPS trackers collect?",
    title="What Information Can GPS Trackers Collect? Data & Privacy",
    desc="What information GPS trackers collect — location, speed, stops, battery and more — what that data reveals, and what privacy-first GPS tracking looks like.",
    answer="""A GPS tracker collects its <strong>position</strong> and the <strong>time</strong>, and from those
      a service can work out <strong>speed, direction, routes, stops and how long you stayed</strong>. Some trackers
      add battery level and device details; vehicle telematics can add engine data. Over time, location history can
      reveal a great deal about a person &mdash; which is exactly why it should be collected openly and kept only as
      long as needed.""",
    body="""
      <h2>What GPS trackers collect directly</h2>
      <ul>
        <li><strong>Latitude and longitude</strong> &mdash; the position itself.</li>
        <li><strong>Time</strong> of each position.</li>
        <li><strong>Accuracy</strong> &mdash; how confident the receiver is (for example &ldquo;within 5 metres&rdquo;).</li>
        <li><strong>Speed and heading</strong>, measured by the receiver or calculated between positions.</li>
      </ul>

      <h2>What can be worked out from it</h2>
      <ul>
        <li><strong>Routes</strong> driven or walked, and <strong>distances</strong>.</li>
        <li><strong>Stops</strong> and how long they lasted.</li>
        <li><strong>Arrivals and departures</strong> at defined places (geofences).</li>
        <li><strong>Patterns</strong> &mdash; where someone usually starts and finishes, regular visits.</li>
      </ul>
      <p>That last point is why location data is sensitive. Even without names attached, a pattern of where someone
      sleeps and works can identify them. Under UK GDPR, location data about an identifiable person is personal data.</p>

      <h2>What trackers <em>don&rsquo;t</em> collect</h2>
      <p>A GPS tracker doesn&rsquo;t record conversations, messages or photos. A <em>phone</em> tracking app only gets
      what the phone&rsquo;s permissions allow; a legitimate business tracking app asks for location permission and
      shows that it is running.</p>

      <h2>Privacy-first GPS tracking solutions</h2>
      <p>If you are choosing a tracking service, look for these privacy-first traits:</p>
      <ul>
        <li><strong>Visible, not covert</strong> &mdash; the tracked person can see when tracking is on.</li>
        <li><strong>Under the tracked person&rsquo;s control</strong> &mdash; tracking stops outside working time.</li>
        <li><strong>Automatic deletion</strong> after a set period.</li>
        <li><strong>Limited access</strong> &mdash; only the people who need it can see it.</li>
        <li><strong>No advertising or data resale.</strong></li>
      </ul>

      <h2>What TrackLink collects</h2>
      <p>For each position: latitude, longitude, accuracy, speed, heading, the phone&rsquo;s battery level and the time.
      Route history is deleted automatically after 30 days as standard. There is no advertising or analytics SDK in the
      app, tracking runs only when the phone&rsquo;s holder switches it on, and each organisation&rsquo;s data is isolated
      from every other&rsquo;s. See the <a href="/privacy/">privacy policy</a> for the full detail.</p>
""",
    faqs=[
        ("Is GPS location data personal data?",
         "Yes, when it relates to an identifiable person — and a work phone or a driver's vehicle almost always does. UK GDPR then applies."),
        ("How long should a business keep GPS tracking data?",
         "Only as long as needed for the purpose. Many businesses keep route history for 30 to 90 days; TrackLink deletes it after 30 days as standard."),
    ],
    related=["is-gps-tracking-legal-uk-business", "gps-tracking-vs-employee-monitoring", "can-someone-track-your-location"],
),
# ------------------------------------------------------------------------------------------
dict(
    slug="gps-tracking-vs-employee-monitoring",
    hub=HUB,
    h1="GPS tracking vs other employee monitoring methods",
    title="GPS Tracking vs Other Employee Monitoring Methods",
    desc="GPS tracking compared with timesheets, check-in calls, dashcams, telematics and screen monitoring — what each is good for, how intrusive it is, and when to use it.",
    answer="""GPS tracking answers <strong>where</strong> and <strong>when</strong> &mdash; nothing more. That makes it
      a good fit for mobile teams and less intrusive than methods that capture what people say, type or look at.
      For field workers it often <em>replaces</em> more intrusive or time-wasting checks, such as repeated
      &ldquo;where are you?&rdquo; calls.""",
    body="""
      <h2>The common ways businesses monitor mobile teams</h2>
      <table>
        <caption>Comparing workforce management options</caption>
        <thead><tr><th>Method</th><th>What it tells you</th><th>Intrusiveness</th></tr></thead>
        <tbody>
          <tr><td>Paper or app timesheets</td><td>Hours worked, as reported by the worker</td><td>Low, but relies on accuracy and memory</td></tr>
          <tr><td>Check-in calls or texts</td><td>Where someone says they are</td><td>Low data, high interruption</td></tr>
          <tr><td>GPS tracking (phone)</td><td>Location, routes, arrival times</td><td>Moderate; limited to where and when</td></tr>
          <tr><td>Vehicle telematics</td><td>Location plus engine data, harsh braking, idling</td><td>Moderate to high</td></tr>
          <tr><td>Dashcams</td><td>Video of the road, sometimes the cab</td><td>High if cab-facing or recording audio</td></tr>
          <tr><td>Screen or keystroke monitoring</td><td>What someone does on a computer</td><td>High; the ICO expects a DPIA for keystroke monitoring</td></tr>
        </tbody>
      </table>

      <h2>When GPS tracking is the right tool</h2>
      <ul>
        <li>Coordinating a team that moves around &mdash; who is nearest to the next job?</li>
        <li>Answering customers &mdash; &ldquo;your engineer is ten minutes away&rdquo;.</li>
        <li>Safety for lone workers &mdash; knowing where someone was last seen.</li>
        <li>Settling disputes &mdash; did the van actually arrive at 9:05?</li>
      </ul>

      <h2>Choosing the least intrusive method</h2>
      <p>UK data protection law asks you to choose the <strong>least intrusive</strong> way to meet your purpose. If
      you only need to know hours worked, timesheets may be enough. If you need live location for dispatch or safety,
      GPS tracking is proportionate &mdash; audio or cab-facing video probably isn&rsquo;t.</p>

      <h2>Combining methods sensibly</h2>
      <p>Many small businesses find that GPS tracking with route history reduces the need for other checks: the
      route answers most &ldquo;what happened?&rdquo; questions. See
      <a href="/guides/gps-time-tracking-field-service/">GPS time tracking for field service</a> for using it alongside
      timesheets.</p>
""",
    faqs=[
        ("Is GPS tracking more intrusive than timesheets?",
         "It collects more data than a timesheet, but it is objective and needs no admin from the worker. What matters is being open about it and limiting it to working time."),
        ("Do I need a DPIA for GPS tracking?",
         "The ICO says employers should carry out a DPIA for monitoring even when it is not strictly required, and must for high-risk processing."),
    ],
    related=["employee-concerns-gps-tracking", "is-gps-tracking-legal-uk-business", "gps-time-tracking-field-service"],
),
# ------------------------------------------------------------------------------------------
dict(
    slug="employee-concerns-gps-tracking",
    hub=HUB,
    h1="Managing employee concerns about workplace GPS tracking",
    title="Managing Employee Concerns About Workplace GPS Tracking",
    desc="How to introduce GPS tracking at work without losing trust: what staff worry about, what to put in a tracking policy, and how to answer the difficult questions.",
    answer="""Staff usually worry about three things: <strong>being watched all the time</strong>, <strong>being
      tracked in their own time</strong>, and <strong>data being used against them</strong>. Address each one directly
      before you switch anything on &mdash; explain why you are tracking, show exactly what managers can see, limit it
      to working hours, and put it in writing.""",
    body="""
      <h2>What employees are really worried about</h2>
      <ul>
        <li><strong>&ldquo;You don&rsquo;t trust us.&rdquo;</strong> Tracking can feel like an accusation.</li>
        <li><strong>&ldquo;You&rsquo;ll see where I go after work.&rdquo;</strong> The biggest and most legitimate worry.</li>
        <li><strong>&ldquo;It&rsquo;ll be used to nitpick.&rdquo;</strong> Every long stop becomes a question.</li>
        <li><strong>&ldquo;It&rsquo;ll drain my phone.&rdquo;</strong> A practical concern, especially on personal phones.</li>
      </ul>

      <h2>How to introduce GPS tracking fairly</h2>
      <ol>
        <li><strong>Lead with the reason.</strong> Dispatch, customer updates, lone-worker safety &mdash; say which.</li>
        <li><strong>Show the screen.</strong> Let staff see exactly what a manager sees on the map.</li>
        <li><strong>Limit it to working time.</strong> Make clear that tracking stops at the end of a shift.</li>
        <li><strong>Say what it won&rsquo;t be used for.</strong> For example, not for monitoring breaks minute by minute.</li>
        <li><strong>Write a short policy</strong> covering purpose, what is collected, who sees it and how long it&rsquo;s kept.</li>
        <li><strong>Invite questions</strong> and review the policy after a few months.</li>
      </ol>

      <h2>Answers to the questions staff will ask</h2>
      <ul>
        <li><strong>Can you track me when I&rsquo;m not working?</strong> Your answer should be no &mdash; and your set-up
          should make that true.</li>
        <li><strong>Who can see my location?</strong> Name the roles.</li>
        <li><strong>How long do you keep it?</strong> Give a period, such as 30 days.</li>
        <li><strong>Can I see my own data?</strong> Yes &mdash; staff have a legal right of access.</li>
        <li><strong>What about my battery?</strong> Explain the update interval and its impact; see
          <a href="/guides/gps-tracker-battery-life/">battery life</a>.</li>
      </ul>

      <h2>Design choices that build trust</h2>
      <p>The easiest concerns to resolve are the ones the system itself answers. In TrackLink, only the person holding
      the phone can switch tracking on or off, a notification shows whenever it runs, and history is deleted after 30
      days. That turns &ldquo;trust us&rdquo; into something staff can see for themselves.</p>
""",
    faqs=[
        ("Should I get employees to sign a tracking policy?",
         "Giving staff a written policy and keeping a record that they received it is good practice. A signature isn't the same as consent, which is usually not the right lawful basis at work."),
        ("What if an employee refuses tracking?",
         "Listen to the reason first — often it is about private time or battery, both solvable. If tracking is lawful and necessary for the role, it may become a conduct matter, but that should be a last resort."),
    ],
    related=["is-gps-tracking-legal-uk-business", "can-employer-track-your-phone", "gps-tracking-vs-employee-monitoring"],
),
]
