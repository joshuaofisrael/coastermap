# ---------- evergreen question pages and manufacturer pages (batch 9, 10 Nov 2026) ----------
UOR_GUIDE = ("Universal Orlando Resort, Guide for Rider Safety and Accessibility (official PDF)", "https://www.universalorlando.com/contentdata/uor/en/us/files/Documents/universal-orlando-riders-guide.pdf")
UOR_HEIGHTS = ("Universal Orlando, official Ride Height Requirements page", "https://www.universalorlando.com/web/en/gb/plan-your-visit/hours-information/ride-height-requirements")
PLANDISNEY = ("planDisney (Walt Disney World's official planning panel): how heights are checked", "https://plandisney.disney.go.com/question/avoid-confusion-height-requirements-place-mk-epcot-child-241775/")
PLANDISNEY2 = ("planDisney (Walt Disney World's official planning panel): no central measuring station", "https://plandisney.disney.go.com/question/disney-centralized-height-measuring-station-608253/")
CDC_TRAVEL = ("CDC Travelers' Health: Motion Sickness", "https://wwwnc.cdc.gov/travel/page/motion-sickness")
CDC_YB = ("CDC Yellow Book: Motion Sickness", "https://www.cdc.gov/yellow-book/hcp/travel-air-sea/motion-sickness.html")
RCDB_REC = ("RCDB Record Holders", "https://rcdb.com/rhr.htm")
RCDB_SRC = ("Roller Coaster DataBase (RCDB)", "https://rcdb.com/")

def by_name(name, park=None):
    for c in ALL:
        if (c["rcdb_name"] == name or c["name"] == name) and (park is None or c["park"] == park): return c
    return None
def ul(items): return "<ul>" + "".join(f"<li>{x}</li>" for x in items) + "</ul>"
def clist(cs, extra=lambda c: ""): return ul([clink(c) + extra(c) for c in cs])
def withhr(c): return f": {hs(c['hr'])} minimum" if c["hr"] else ""
def clk(name, park=None, label=None):
    c = by_name(name, park); t = E(label or (c["name"] if c else name))
    return f'<a href="{coaster_path(c)}">{t}</a>' if c else t

def qpage(slug, title, desc, h1, answer, body, faqs, blurb, sources=(), related=(), group="Questions", items=None):
    path = f"/guides/{slug}/"
    if len(title) > 70: raise SystemExit("title too long: " + title)
    rel = "".join(f'<li><a href="{u}">{E(t)}</a></li>' for u, t in related)
    src = "".join(f"<li>{src_link(s)}</li>" for s in sources)
    html_ = (f'<article class="guide"><h1>{E(h1)}</h1>{byline()}<div class="answer" role="note"><p><strong>Quick answer:</strong> {answer}</p></div>{body}{faq_html(faqs)}'
             + (f'<section aria-labelledby="rel-h"><h2 id="rel-h">Related guides</h2><ul class="cols">{rel}</ul></section>' if rel else "")
             + f'<section class="sources"><h2>Sources and how this page is built</h2><p>Coaster statistics come from the <a href="https://rcdb.com/" rel="nofollow noopener" target="_blank">Roller Coaster DataBase</a> and height rules from each park\'s official pages, as listed on each coaster page, last verified {CHECKED}. Explanations of how rides work are general engineering background written by the {BRAND} editorial team, not advice from any park or manufacturer. Always follow the signs at each ride and the instructions of ride staff.</p>'
             + (f"<ul>{src}</ul>" if src else "") + '<p>See <a href="/methodology/">sources and methods</a>.</p></section></article>')
    ld = [article_ld(path, title, desc)] + ([faq_ld(faqs)] if faqs else []) + ([itemlist_ld(h1, items)] if items else [])
    write(path, page(path, title, desc, html_, ld, [("/", "Home"), ("/guides/", "Guides"), (path, h1)]))
    GUIDES.append((path, h1, blurb, group))

def _hr_coasters(): return [c for c in ALL if c["hr"]]

def fear_page():
    gentle = sorted([c for c in _hr_coasters() if c["inversions"] == 0 and c["scale"] in ("Kiddie", "Family")], key=lambda c: iscore(c))[:12]
    step2 = sorted([c for c in _hr_coasters() if c["inversions"] == 0 and c["scale"] == "Thrill" and c["height"] and c["height"] < 120], key=lambda c: iscore(c))[:8]
    body = f'''<h2>Why roller coasters feel scary</h2><p>Fear on a coaster usually comes from three things: the anticipation in the queue and on the lift hill, the feeling of falling on the drops, and a sense of not being in control. Your body reacts to a drop the same way it would to a real fall, with a rush of adrenaline, a racing heart and the familiar "stomach drop", even though you are held in a seat designed to keep you in place through every part of the ride.</p>
<p>Knowing what is coming takes away a lot of that fear. Watch the ride run a few times from the queue, read the ride's page so you know whether it has inversions, launches or a big drop, and pick your seat on purpose.</p>
<h2>Ten tips that actually help</h2><ol>
<li><strong>Start small.</strong> Ride a family coaster with no inversions first, then step up one level at a time. A ladder of rides builds confidence far better than jumping straight onto the biggest coaster in the park.</li>
<li><strong>Sit in the middle.</strong> The middle of the train feels the gentlest on most coasters. The front gives you the full view of every drop, and the back is pulled over the top of hills fastest.</li>
<li><strong>Breathe out, or shout, on the drops.</strong> Holding your breath tightens your stomach and makes the drop feel worse. A long exhale or a good scream relaxes your core.</li>
<li><strong>Keep your head back and your body relaxed.</strong> Rest your head against the headrest where there is one, sit up straight and hold the lap bar or grab handles.</li>
<li><strong>Look ahead, not down.</strong> Fixing your eyes on the track ahead or the horizon helps your brain predict the motion.</li>
<li><strong>Ride in daylight.</strong> Dark rides and night rides feel faster because you cannot see what is coming.</li>
<li><strong>Choose a short queue.</strong> A long wait gives anxiety time to build.</li>
<li><strong>Ride with someone calm.</strong> A friend who has ridden before can tell you what to expect, element by element.</li>
<li><strong>Ride it twice.</strong> The second ride is almost always less scary, because you know what is coming.</li>
<li><strong>You can step out.</strong> If you change your mind in the queue, tell a team member. Many coasters have an exit before the boarding platform.</li></ol>
<h2>Gentle coasters to start with</h2><p>These are among the least intense coasters on {BRAND} that have a verified height rule, ranked by RCDB's intensity class, height, speed and inversions:</p>{clist(gentle, withhr)}
<h2>A good second step</h2><p>Once a family coaster feels fine, try a thrill-class coaster under 120 feet with no inversions:</p>{clist(step2, withhr)}
<h2>Fear of drops, loops or launches</h2><p>If drops are the problem, a launch coaster can be easier than a big lift hill, because there is no slow climb and the launch is over in seconds. If loops are the worry, it may help to know that on most inversions you are pressed into your seat rather than hanging, so it rarely feels like being upside down. Our <a href="/guides/why-your-stomach-drops-on-a-roller-coaster/">stomach drop explainer</a> and <a href="/guides/how-do-roller-coaster-restraints-work/">restraints explainer</a> go into the details.</p>'''
    faqs = [("How do I stop being scared of roller coasters?", "Start with a gentle family coaster, sit in the middle of the train, breathe out on the drops, and step up one level at a time. Riding the same coaster twice also helps because the second ride is less of a surprise."),
            ("Which seat is least scary on a roller coaster?", "The middle of the train. The front shows you every drop and the back is pulled over hills fastest, so the middle usually feels the gentlest."),
            ("Is it normal to be scared of roller coasters?", "Yes. A drop triggers the same adrenaline response as a real fall. Many keen riders were nervous at first and built up gradually."),
            ("Can I leave the queue if I change my mind?", "Yes. Tell a team member. Many coasters have an exit before the boarding platform.")]
    qpage("how-to-not-be-scared-of-roller-coasters", f"How to Not Be Scared of Roller Coasters: 10 Tips | {BRAND}", "Ten practical tips for nervous and first-time roller coaster riders, why coasters feel scary, and gentle coasters to start with.",
          "How to not be scared of roller coasters", "start with a gentle family coaster with no inversions, sit in the middle of the train, breathe out on the drops and keep your head back. Step up one level at a time; the second ride on any coaster is easier than the first.",
          body, faqs, "Ten tips for nervous and first-time riders.", related=[("/guides/best-first-roller-coasters/", "Best first roller coasters"), ("/guides/best-seat-on-a-roller-coaster/", "Best seat on a roller coaster"), ("/guides/what-is-a-family-roller-coaster/", "What is a family roller coaster?"), ("/quiz/", "Which coaster should you ride? quiz")], items=gentle)

def stomach_page():
    drops = sorted([c for c in ALL if c["drop"]], key=lambda c: -c["drop"])[:10]
    body = f'''<h2>What you are feeling</h2><p>When a coaster crests a hill and starts down the other side, the train begins to fall faster than your body expects. For a moment the seat is no longer pushing up on you as hard as gravity pulls you down. Your organs are not held rigidly in place, so they shift slightly, and the nerves that sense that movement send a signal your brain reads as the "stomach drop" or "butterflies". At the same moment, the balance organs in your inner ear detect the change in vertical acceleration, and your body releases adrenaline, which adds the tingling, heart-racing feeling.</p>
<h2>G-forces in plain English</h2><p>Engineers describe the forces on a rider in g. Sitting still, you feel 1 g: the normal pull of gravity. At the bottom of a valley or through a tight loop you are pressed into the seat with more than 1 g, so you feel heavier. Over the top of a hill or at the start of a drop you can feel less than 1 g, so you feel lighter. At 0 g you feel weightless, and below 0 g (negative g) you are lifted out of the seat against your lap bar or harness. Coaster fans call those floating moments <a href="/guides/what-is-airtime-on-a-roller-coaster/">airtime</a>.</p>
<h2>Why some drops feel stronger than others</h2><ul><li><strong>Shape of the hill.</strong> A sharply pointed hill changes direction quickly and produces a sudden, strong float. A rounded hill gives a gentler floating feeling.</li>
<li><strong>Seat position.</strong> In the back of the train you are pulled over the crest at speed, so the drop starts more suddenly. See <a href="/guides/best-seat-on-a-roller-coaster/">best seat on a roller coaster</a>.</li>
<li><strong>Restraint.</strong> A lap bar leaves your upper body free, so floating feels stronger than with an over-the-shoulder harness.</li>
<li><strong>Anticipation.</strong> Tensing up makes the sensation sharper. Breathing out on the drop helps many riders.</li></ul>
<h2>The biggest drops on {BRAND}</h2><p>RCDB drop figures for the coasters we cover:</p>{clist(drops, lambda c: f": {ftm(c['drop'])} drop")}
<h2>How to make the feeling milder</h2><p>Sit in the middle or front of the train, keep your back against the seat, look ahead rather than down and breathe out as the train goes over the top. Coasters with rounded hills and no steep drops, such as many family coasters and mine trains, produce only a gentle version of the sensation.</p>'''
    faqs = [("Why does your stomach drop on a roller coaster?", "On a drop the seat briefly stops pushing up on you as hard as gravity pulls down, so your organs shift slightly and your inner ear senses the change in vertical acceleration. Your brain reads that as the stomach drop, and adrenaline adds the tingling."),
            ("Why do roller coasters make you feel weightless?", "Over the top of a hill or at the start of a drop, the train falls away beneath you, so the forces on you drop towards zero g and you feel weightless."),
            ("Which seat has the strongest stomach drop?", "Usually the back of the train, because it is pulled over the crest at speed."),
            ("How can I make the stomach drop feeling less intense?", "Sit in the middle or front, keep your back against the seat, look ahead and breathe out on the drop.")]
    qpage("why-your-stomach-drops-on-a-roller-coaster", f"Why Your Stomach Drops on a Roller Coaster | {BRAND}", "Why roller coaster drops make your stomach drop and make you feel weightless, g-forces explained in plain English, and how to make the feeling milder.",
          "Why your stomach drops on a roller coaster", "on a drop the seat briefly stops supporting your full weight, so you feel lighter than normal (below 1 g). Your organs shift slightly and your inner ear senses the change, and your brain reads it as the stomach drop. Adrenaline does the rest.",
          body, faqs, "Weightlessness and g-forces explained.", related=[("/guides/what-is-airtime-on-a-roller-coaster/", "What is airtime?"), ("/guides/best-seat-on-a-roller-coaster/", "Best seat on a roller coaster"), ("/guides/what-is-a-hypercoaster/", "What is a hypercoaster?"), ("/guides/how-to-not-be-scared-of-roller-coasters/", "How to not be scared of roller coasters")], items=drops)

def airtime_page():
    hyp = sorted([c for c in ALL if (c["model"] and "Hyper" in c["model"]) or (c["make"] == "Rocky Mountain Coasters")], key=lambda c: -(c["height"] or 0))[:14]
    body = f'''<h2>Airtime, defined</h2><p>Airtime is the moment on a roller coaster when you lift up out of your seat, held in only by your restraint. It happens when the track drops away faster than you would fall freely, so the forces on you dip below zero g and you are briefly pulled upwards relative to the seat. Fans split it into two kinds.</p>
<ul><li><strong>Floater airtime:</strong> a gentle, sustained float close to zero g, usually over a large rounded hill. You hover just above the seat for a second or two.</li>
<li><strong>Ejector airtime:</strong> a sharper, stronger negative g, usually over a pointed hill or a sudden drop, that pushes you firmly up into the lap bar.</li></ul>
<h2>Where you find airtime</h2><p>Airtime comes from the shape of the track rather than height alone. Hypercoasters are built around a series of tall "camelback" hills for floater airtime, and hybrid and modern wooden coasters use steep, quick hills and wave turns for ejector airtime. An airtime hill is any hill designed for that moment, and a "stall" is an inversion held slowly at the top so riders hang in the restraint.</p>
<h2>Is airtime safe?</h2><p>Airtime is a designed part of the ride. Restraints are built to hold riders through negative g, and parks set height and body-size requirements so the restraint fits. Follow the instructions of ride staff, keep your restraint as it was checked, and do not ride if a park's warning sign covers a condition you have.</p>
<h2>Seat choice</h2><p>The back rows usually get the strongest airtime on the first drop, because the train pulls the back car over the crest at its highest speed. On later hills the front can be stronger, depending on the layout. Rides with lap bars rather than shoulder harnesses make airtime feel more dramatic.</p>
<h2>Airtime coasters on {BRAND}</h2><p>Hypercoasters and Rocky Mountain Construction coasters are among the best-known airtime rides. Here are the ones we cover, tallest first:</p>{clist(hyp, withhr)}'''
    faqs = [("What is airtime on a roller coaster?", "Airtime is the moment you lift out of your seat because the forces drop below zero g, usually over a hill or at the top of a drop. Your restraint holds you in."),
            ("What is ejector airtime?", "A strong, sudden form of airtime that pushes you firmly up into your restraint, usually over a pointed hill."),
            ("What is floater airtime?", "A gentle, sustained floating feeling close to zero g, usually over a large rounded hill."),
            ("Where do you get the most airtime on a roller coaster?", "Usually in the back rows on the first drop, and on rides with lap bars rather than shoulder harnesses.")]
    qpage("what-is-airtime-on-a-roller-coaster", f"What Is Airtime on a Roller Coaster? Explained | {BRAND}", "What airtime is, floater vs ejector airtime, why it happens, where to sit for the most airtime and the best airtime coasters we cover.",
          "What is airtime on a roller coaster?", "airtime is the floating moment when you lift out of your seat, held in by your restraint. It happens when the track falls away faster than you would, so the forces on you drop below zero g. Floater airtime is gentle; ejector airtime is sharp and strong.",
          body, faqs, "Floater vs ejector airtime explained.", related=[("/guides/why-your-stomach-drops-on-a-roller-coaster/", "Why your stomach drops"), ("/guides/what-is-a-hypercoaster/", "What is a hypercoaster?"), ("/guides/what-is-a-hybrid-roller-coaster/", "What is a hybrid coaster?"), ("/guides/rocky-mountain-construction-roller-coasters/", "Rocky Mountain Construction coasters")], items=hyp)

def work_page():
    lifts = len([c for c in ALL if not launched(c)]); ln = len([c for c in ALL if launched(c)])
    tall = sorted([c for c in ALL if c["height"] and not launched(c)], key=lambda c: -c["height"])[:6]
    body = f'''<h2>Energy in, energy out</h2><p>A traditional roller coaster has no engine on the train. A lift hill or a launch gives the train energy at the start of the ride, and the rest of the circuit spends it. At the top of the lift the train has the most potential energy; as it drops, that becomes kinetic energy, or speed. Every following hill trades some speed back for height, and friction from the wheels and air resistance slowly drain the total. That is why the first drop is almost always the biggest and the hills get smaller as the ride goes on.</p>
<h2>Lift hills</h2><p>Most coasters use a chain lift: a moving chain under the track that a "chain dog" on the bottom of the train catches, pulling the train up the slope. The clacking sound is the anti-rollback device, a ratchet that stops the train rolling backwards if it ever stops on the lift. Some rides use a cable lift, which is faster and quieter, or a tyre-driven lift on smaller rides. Of the {len(ALL)} coasters on {BRAND}, {ln} have a launch model on RCDB and {lifts} do not.</p>
<h2>Launches</h2><p>A launch replaces the lift with a burst of acceleration. See <a href="/guides/how-do-roller-coaster-launches-work/">how roller coaster launches work</a>.</p>
<h2>Staying on the track and going upside down</h2><p>Coaster wheels clamp the rail from three sides, so the train cannot lift off even when riders are upside down or floating. See <a href="/guides/how-do-roller-coasters-stay-on-the-track/">how roller coasters stay on the track</a>.</p>
<h2>Blocks and brakes</h2><p>The track is divided into blocks, and only one train is allowed in each block at a time. Brakes at the end of each block stop a train if the block ahead is not clear, so trains cannot catch each other. See <a href="/guides/how-do-roller-coaster-brakes-work/">how roller coaster brakes work</a> and <a href="/guides/what-happens-if-a-roller-coaster-gets-stuck/">what happens if a roller coaster gets stuck</a>.</p>
<h2>Who designs and builds them</h2><p>A handful of specialist companies build most of the world's coasters. Our <a href="/guides/roller-coaster-manufacturers/">roller coaster manufacturers</a> guide covers each one with every example we document.</p>
<h2>Tallest lift-hill coasters we cover</h2>{clist(tall, lambda c: f": {ftm(c['height'])}")}'''
    faqs = [("How do roller coasters work?", "A lift hill or launch gives the train energy at the start, and gravity does the rest. The train turns height into speed on each drop and speed back into height on each hill, slowly losing energy to friction, so later hills are smaller."),
            ("Do roller coasters have engines?", "Not on the train in a traditional coaster. Motors drive the lift chain, cable or launch system, and the train coasts for the rest of the ride."),
            ("What is the clicking sound on a lift hill?", "The anti-rollback device: a ratchet that stops the train rolling backwards if it ever stops on the lift."),
            ("Why is the first hill the biggest?", "The train loses energy to friction and air resistance as it goes, so it cannot climb back to the height it started from.")]
    qpage("how-do-roller-coasters-work", f"How Do Roller Coasters Work? Lift Hills, Energy & More | {BRAND}", "How roller coasters work: lift hills, energy, launches, wheels, blocks and brakes, explained in plain English with examples from the coasters we cover.",
          "How do roller coasters work?", "a lift hill or launch gives the train its energy at the start, and gravity does the rest. On each drop the train turns height into speed, and on each hill speed back into height, losing a little to friction each time, which is why the first drop is the biggest.",
          body, faqs, "Lift hills, energy, blocks and brakes.", related=[("/guides/how-do-roller-coaster-launches-work/", "How launches work"), ("/guides/how-do-roller-coasters-stay-on-the-track/", "How coasters stay on the track"), ("/guides/how-do-roller-coaster-brakes-work/", "How brakes work"), ("/guides/roller-coaster-glossary/", "Roller coaster glossary")])

def track_page():
    wood = len([c for c in ALL if c["material"] == "Wood"]); steel = len([c for c in ALL if c["material"] == "Steel"])
    inv = sorted([c for c in ALL if c["inversions"]], key=lambda c: -c["inversions"])[:8]
    body = f'''<h2>Three sets of wheels</h2><p>Each car on a modern roller coaster has three kinds of wheels, gripping the rail from different sides:</p><ul>
<li><strong>Road wheels</strong> (or running wheels) sit on top of the rail and carry the weight of the train.</li>
<li><strong>Upstop wheels</strong> sit underneath the rail. They stop the train lifting off the track over hills, and they carry the load when the train is upside down.</li>
<li><strong>Side friction wheels</strong> (or guide wheels) run along the side of the rail and keep the train from moving sideways in the turns.</li></ul>
<p>Because the wheels wrap around the rail, the train is held onto the track in every direction. It cannot fall off at the top of a loop or lift off on an airtime hill.</p>
<h2>Loops and inversions</h2><p>At the top of a vertical loop riders feel pressed into their seats rather than falling out, because the train is moving fast enough that the track has to push it around the curve. Modern loops are tall and teardrop-shaped (a clothoid loop) rather than circular, which keeps the forces comfortable. The upstop wheels and the restraint are there as well, so the train and riders stay put regardless.</p>
<h2>Wooden coasters</h2><p>Wooden coasters use the same three-wheel idea. The track is made of layers of laminated wood with a steel strip on top for the wheels, and the upstop wheels run under the wooden track. {BRAND} covers {wood} wooden coasters and {steel} steel coasters.</p>
<h2>Coasters with the most inversions we cover</h2>{clist(inv, lambda c: f": {c['inversions']} inversions")}'''
    faqs = [("How do roller coasters stay on the track?", "Each car has road wheels on top of the rail, upstop wheels underneath and side friction wheels at the side, so the wheels wrap around the rail and hold the train onto the track."),
            ("How do roller coasters stay on the track when upside down?", "Speed presses the train against the track through the loop, and the upstop wheels under the rail hold it in place in any case."),
            ("Can a roller coaster fall off the track?", "Modern coasters are designed so the wheels clamp the rail from above, below and the side, so the train cannot lift off or slide off in normal operation.")]
    qpage("how-do-roller-coasters-stay-on-the-track", f"How Do Roller Coasters Stay on the Track? | {BRAND}", "How roller coaster wheels lock the train onto the track, why you do not fall out in a loop, and how wooden coasters do it, in plain English.",
          "How do roller coasters stay on the track?", "every car has three sets of wheels: road wheels on top of the rail, upstop wheels underneath it and side friction wheels beside it. Together they wrap around the rail, so the train cannot lift off over a hill or fall off upside down.",
          body, faqs, "Road, upstop and side friction wheels.", related=[("/guides/how-do-roller-coasters-work/", "How roller coasters work"), ("/guides/roller-coasters-with-the-most-inversions/", "Most inversions"), ("/guides/how-do-roller-coaster-restraints-work/", "How restraints work"), ("/guides/what-is-a-wooden-roller-coaster/", "What is a wooden coaster?")])

def launch_page():
    ls = sorted([c for c in ALL if launched(c) and c["speed"]], key=lambda c: -c["speed"])[:12]
    n = len([c for c in ALL if launched(c)])
    body = f'''<h2>The main launch systems</h2><ul>
<li><strong>Linear synchronous motors (LSM):</strong> rows of electromagnets along the track switch on and off in sequence, pulling magnets fixed under the train forward. LSM launches are smooth, precise and can be repeated several times in one ride.</li>
<li><strong>Linear induction motors (LIM):</strong> a similar idea, where electromagnets induce a current in a metal fin under the train, pushing it along. LIMs were common on early launch coasters.</li>
<li><strong>Hydraulic launches:</strong> hydraulic motors wind a cable onto a drum very quickly. The cable pulls a catch car that hooks the train, accelerates it and lets go. This system has powered many of the fastest coasters in the world.</li>
<li><strong>Pneumatic (compressed air) launches:</strong> compressed air drives the train or a catch car, giving very sudden acceleration.</li>
<li><strong>Tyre launches:</strong> rows of spinning tyres grip a fin under the train, the same way tyres drive trains up many lift hills. Common on family launch coasters.</li>
<li><strong>Flywheel and weight-drop catapults:</strong> older designs that store energy in a spinning flywheel or a falling weight and release it into a cable.</li></ul>
<h2>What a launch feels like</h2><p>Instead of the slow build-up of a lift hill, you are pushed back into your seat as the train accelerates, often reaching highway speeds in a few seconds. Some coasters launch more than once, launch backwards, or launch up a tall "top hat" tower. Many nervous riders find a launch easier than a big lift hill because there is no time to dwell; others find the acceleration the most intense part of any ride.</p>
<h2>Why launches sometimes roll back</h2><p>On a launch up a tall tower, the train needs just enough speed to clear the top. In some conditions, or with a lightly loaded train, it can fall short and roll back down to the launch track, where brakes stop it. Rides that can roll back are designed for it.</p>
<h2>Fastest launched coasters on {BRAND}</h2><p>We cover {n} coasters with a launch model on RCDB. The fastest:</p>{clist(ls, lambda c: f": {mphk(c['speed'])}")}'''
    faqs = [("How do roller coaster launches work?", "Most use linear synchronous or induction motors (electromagnets along the track), hydraulic motors pulling a cable, compressed air or spinning tyres to push the train from low speed to high speed in seconds."),
            ("What is an LSM launch?", "A launch using linear synchronous motors: electromagnets along the track switch on in sequence and pull magnets under the train forward."),
            ("What is a rollback on a launch coaster?", "When a train launched up a tall tower does not quite reach the top and rolls back to the launch track, where brakes stop it. Rides that can roll back are designed for it."),
            ("Are launch coasters scarier than lift hill coasters?", "It depends on the rider. There is no slow climb to build anticipation, but the acceleration is strong.")]
    qpage("how-do-roller-coaster-launches-work", f"How Do Roller Coaster Launches Work? LSM to Hydraulic | {BRAND}", "How roller coaster launches work: LSM, LIM, hydraulic, pneumatic and tyre launches explained, why rollbacks happen, and the fastest launch coasters we cover.",
          "How do roller coaster launches work?", "a launch replaces the lift hill with a burst of acceleration. Most use electromagnets along the track (LSM or LIM), a hydraulic motor pulling a cable, compressed air or spinning tyres to push the train up to speed in a few seconds.",
          body, faqs, "LSM, LIM, hydraulic and tyre launches.", related=[("/guides/what-is-a-launch-coaster/", "What is a launch coaster?"), ("/guides/fastest-roller-coasters/", "Fastest roller coasters"), ("/guides/how-do-roller-coasters-work/", "How roller coasters work"), ("/guides/world-record-roller-coasters/", "World record roller coasters")], items=ls)

def brakes_page():
    sh = [c for c in ALL if "Shuttle" in c["tags"]][:8]
    body = f'''<h2>Two kinds of brakes</h2><ul>
<li><strong>Friction brakes</strong> are pairs of pads, a bit like a giant bicycle brake, that squeeze a metal fin under the train. They can hold a train completely still, so they are used where the train has to stop, such as the station and block brakes, and they are usually designed to close if power or air pressure is lost.</li>
<li><strong>Magnetic brakes</strong> use rows of strong permanent magnets. As a metal fin on the train passes between them, it creates eddy currents that resist the motion and slow the train smoothly, with no contact and little wear. Because they rely only on the motion of the train, they work without power. They slow a train but cannot hold it at a standstill, so they are combined with friction brakes or tyres for the final stop.</li></ul>
<h2>Trim brakes, block brakes and the brake run</h2><p><strong>Trim brakes</strong> sit partway through a course and take a little speed off, so a ride runs within its design speed. <strong>Block brakes</strong> divide the track into sections; a train is only allowed into the next block when it is clear, so two trains can never meet. The <strong>final brake run</strong> brings the train down to walking pace before the station, where tyres usually move it into place.</p>
<h2>Are the brakes on the train?</h2><p>On nearly all coasters, the brakes are on the track and the train carries only the fins they grip. That way the ride's control system, not each train, decides when to slow or stop.</p>
<h2>Shuttle coasters and brakes</h2><p>Shuttle coasters, which run their course forwards and then backwards, rely on brakes and tyres at both ends. Examples we cover:</p>{clist(sh, withhr)}'''
    faqs = [("How do roller coaster brakes work?", "Most coasters use friction brakes, where pads squeeze a fin under the train, and magnetic brakes, where magnets slow a metal fin through eddy currents without touching it. The brakes are on the track, not the train."),
            ("How do magnetic brakes work on a roller coaster?", "A metal fin on the train passes between strong permanent magnets. The motion creates eddy currents that resist the fin and slow the train smoothly, with no contact and no power needed."),
            ("Do roller coasters have brakes?", "Yes, on the track: block brakes, trim brakes and a final brake run, managed by the ride's control system.")]
    qpage("how-do-roller-coaster-brakes-work", f"How Do Roller Coaster Brakes Work? Magnetic & Friction | {BRAND}", "How roller coaster brakes work: friction and magnetic brakes, trim and block brakes, and why the brakes are on the track rather than the train.",
          "How do roller coaster brakes work?", "the brakes are on the track, not the train. Friction brakes squeeze a fin under the train and can hold it still; magnetic brakes slow the fin with eddy currents, with no contact and no power. Block brakes keep every train in its own section of track.",
          body, faqs, "Friction, magnetic, trim and block brakes.", related=[("/guides/how-do-roller-coasters-work/", "How roller coasters work"), ("/guides/what-happens-if-a-roller-coaster-gets-stuck/", "What if a coaster gets stuck?"), ("/guides/what-is-a-shuttle-roller-coaster/", "What is a shuttle coaster?"), ("/guides/roller-coaster-glossary/", "Roller coaster glossary")])

def restraint_page():
    inv = [c for c in ALL if "Inverted" in c["tags"]][:6]
    body = f'''<h2>Types of restraint</h2><ul>
<li><strong>Lap bar:</strong> a padded bar that lowers across your thighs or hips. Common on family coasters, wooden coasters and hypercoasters, where it leaves your upper body free for airtime.</li>
<li><strong>T-bar or individual lap bar:</strong> a lap bar shaped to fit between the legs, or one bar per seat, so each rider is held separately.</li>
<li><strong>Over-the-shoulder restraint (OTSR):</strong> a padded harness that comes down over your shoulders and locks at your waist. Common on looping and inverted coasters.</li>
<li><strong>Vest restraint:</strong> a softer harness with flexible straps, used on many newer coasters for comfort.</li>
<li><strong>Seat belts:</strong> many rides add a seat belt as a secondary check, which ride staff confirm before dispatch.</li></ul>
<h2>How they lock</h2><p>Most restraints use a ratchet or hydraulic cylinder that lets the bar move towards you but not away. Once it is locked, it stays locked until the station system releases it at the end of the ride. Ride staff check restraints before the train leaves.</p>
<h2>Fit, body size and height</h2><p>Restraints are one reason parks set height requirements: a rider has to be tall enough for the bar or harness to hold them correctly. Body shape matters too. Universal Orlando's official rider guide says: "Guests who do not fit properly within any safety restraint will not be permitted to ride," and encourages larger guests to try the test seats at the entrance of certain rides. If you are unsure, try the test seat before you queue. See <a href="/guides/can-you-be-too-tall-for-a-roller-coaster/">can you be too tall for a roller coaster?</a></p>
<h2>Tips</h2><ul><li>Sit all the way back before the restraint comes down, so it locks in the right place.</li><li>Empty your pockets; loose items can stop a bar closing fully and can fall out.</li><li>Follow the ride's instructions about bags, phones and glasses.</li></ul>
<h2>Examples</h2><p>Inverted coasters, where your legs hang free, commonly use shoulder harnesses. Examples we cover:</p>{clist(inv, withhr)}'''
    faqs = [("How do roller coaster restraints lock?", "Most use a ratchet or hydraulic cylinder that lets the bar move towards you but not away, locked until the station releases it. Ride staff check restraints before dispatch."),
            ("What is an OTSR on a roller coaster?", "An over-the-shoulder restraint: a padded harness that comes down over your shoulders and locks at your waist."),
            ("What if the restraint does not fit me?", "Parks will not let a rider ride if the restraint does not fit properly. Try the test seat at the ride entrance where one is provided.")]
    qpage("how-do-roller-coaster-restraints-work", f"How Do Roller Coaster Restraints Work? Lap Bars & OTSRs | {BRAND}", "Lap bars, shoulder harnesses, vests and seat belts explained: how roller coaster restraints lock, why fit matters and what to do if you are unsure.",
          "How do roller coaster restraints work?", "a lap bar, shoulder harness or vest lowers onto you and locks with a ratchet or hydraulic cylinder, so it can move towards you but not away. Ride staff check restraints before the train leaves, and they stay locked until the station releases them.",
          body, faqs, "Lap bars, OTSRs, vests and fit.", sources=[UOR_GUIDE], related=[("/guides/can-you-be-too-tall-for-a-roller-coaster/", "Can you be too tall?"), ("/guides/roller-coaster-height-requirements-explained/", "Height requirements explained"), ("/guides/what-is-airtime-on-a-roller-coaster/", "What is airtime?"), ("/guides/how-do-roller-coasters-stay-on-the-track/", "How coasters stay on the track")])

def seat_page():
    dive = [c for c in ALL if c["model"] and "Dive" in c["model"]][:5]
    wing = [c for c in ALL if "Wing" in c["tags"]][:5]
    body = f'''<h2>Front, middle or back?</h2><div class="tablewrap"><table class="list"><thead><tr><th scope="col">Seat</th><th scope="col">What it feels like</th><th scope="col">Best for</th></tr></thead><tbody>
<tr><th scope="row">Front row</th><td>Full view of every drop and the track ahead; a slower, hanging start to the first drop as the train is pushed over the crest; the most wind.</td><td>Views, dive coasters, riders who like to see what is coming</td></tr>
<tr><th scope="row">Middle</th><td>The smoothest and mildest ride; drops and airtime feel the softest.</td><td>Nervous riders and anyone prone to motion sickness</td></tr>
<tr><th scope="row">Back row</th><td>The train's weight pulls the back car over the crest at speed, so drops start sooner and airtime is strongest; on older rides it can be the roughest.</td><td>Airtime fans, hypercoasters, wooden coasters</td></tr></tbody></table></div>
<h2>The physics in one paragraph</h2><p>A train behaves as one connected body. As it goes over a hill, the front cars start down while most of the train is still climbing, so they drop slowly, held back by the cars behind. By the time the back car crests, the rest of the train is already falling and pulls it over the top at speed. That is why the back gets the sharpest drop and strongest airtime, and the front gets a slower, more drawn-out drop with the best view.</p>
<h2>Outside or inside seats</h2><p>On wide trains, the outside seats feel more exposed. On wing coasters the outer seats hang out over nothing, and on inverted coasters the outside seats give the clearest view. On spinning coasters, seat choice matters less than how the weight is balanced in the car.</p>
<h2>By coaster type</h2><ul><li><strong>Dive coasters:</strong> the front row is held over the vertical drop with the clearest look down. Examples: {", ".join(clink(c, False) for c in dive) or "none"}.</li>
<li><strong>Wing coasters:</strong> the outermost seats feel the most open. Examples: {", ".join(clink(c, False) for c in wing) or "none"}.</li>
<li><strong>Hypercoasters and hybrids:</strong> the back rows for airtime. See <a href="/guides/what-is-airtime-on-a-roller-coaster/">airtime explained</a>.</li>
<li><strong>Wooden coasters:</strong> the back is wildest; the middle is smoothest.</li>
<li><strong>Launch coasters:</strong> the seat matters less, as everyone launches together, but the front gives the most dramatic view of top hat towers.</li></ul>
<h2>Each coaster page has seat advice</h2><p>Every coaster page on {BRAND} includes general seat guidance for that ride's style. Find a ride on the <a href="/coasters/">all coasters</a> page.</p>'''
    faqs = [("What is the best seat on a roller coaster?", "The back row for the strongest drops and airtime, the front row for the view, and the middle for the smoothest, gentlest ride."),
            ("Which seat on a roller coaster is the least scary?", "The middle of the train, where drops and airtime feel softest."),
            ("Is the front or back of a roller coaster faster?", "The whole train travels at the same speed, but the back car is pulled over the top of hills at higher speed, so drops feel faster and more sudden there."),
            ("Where should I sit if I get motion sick?", "The middle of the train, facing forward and looking ahead.")]
    qpage("best-seat-on-a-roller-coaster", f"Best Seat on a Roller Coaster: Front vs Back Explained | {BRAND}", "Front, middle or back: the best seat on a roller coaster for views, airtime or a smoother ride, the physics behind it and advice by coaster type.",
          "Best seat on a roller coaster", "sit in the back row for the strongest drops and airtime, the front row for the best view, and the middle for the smoothest, least scary ride. The back is pulled over each hill at speed, which is why it feels wildest.",
          body, faqs, "Front vs middle vs back, with the physics.", related=[("/guides/what-is-airtime-on-a-roller-coaster/", "What is airtime?"), ("/guides/how-to-not-be-scared-of-roller-coasters/", "How to not be scared"), ("/guides/what-is-a-dive-coaster/", "What is a dive coaster?"), ("/guides/what-is-a-wing-coaster/", "What is a wing coaster?")])

def heights_explained_page():
    from collections import Counter
    hr = _hr_coasters()
    inch = Counter(c["hr"]["min"] for c in hr if not metric(c["hr"])).most_common(5)
    cmc = Counter(c["hr"]["min"] for c in hr if metric(c["hr"])).most_common(5)
    acc = len([c for c in hr if c["hr"].get("acc_min")])
    body = f'''<h2>How parks measure</h2><p>Parks measure riders at the ride, not at the gate. Walt Disney World's official planDisney panel says children "can be measured at the entrance to each of the attractions", that Cast Members at rides with height restrictions have measuring sticks there, and that height restrictions are strictly enforced "even if your child is only off by a teensy-weensie amount". Another planDisney answer says there is no central measuring location: there is typically a measurement spot at the queue entrance "and possibly again right before entering the attraction itself", so a child who only just passes may be checked twice.</p>
<p>Universal Orlando's official rider guide says "Shoes and shirts must be worn at all times", so plan on your child wearing shoes both when measured and when riding, and measure at home in the same shoes. Do not count on a hairstyle or hat to add height, and expect a check at each ride.</p>
<h2>If your child is near the line</h2><ul><li>Measure at home against a wall, standing straight with heels flat, in the shoes they will wear. Round down, not up.</li>
<li>Ask staff to measure at the entrance before you join a long queue.</li><li>Have a plan B nearby, such as a family coaster with a lower requirement. Our <a href="/height-checker/">height checker</a> shows what a given height can ride at every park we cover.</li>
<li>Ask about rider swap (also called child swap or rider switch) where the park offers it, so adults can take turns without queuing twice.</li></ul>
<h2>Ride-alone minimum vs companion range</h2><p>Many rides have two numbers. The ride-alone minimum is the height to ride without an adult; the lower companion range means the child can ride only with a supervising companion. Universal Orlando defines a Supervising Companion as "someone who is 14 years of age or older and meets all other attraction ridership requirements", for children under its 48 in (122 cm) ride-alone height. Of the {len(hr)} coasters on {BRAND} with a verified height rule, {acc} publish a companion range. Companion rules differ by park, so check each ride's page.</p>
<h2>Why height requirements exist</h2><p>A rider has to be tall enough for the restraint to hold them properly and for their body to be braced against the ride's forces. Universal Orlando's guide says that for most rides you "must be able to independently maintain an upright position, and brace and support your torso, neck, and head while absorbing sudden and dramatic movements". That is why the number is fixed per ride, and why some rides also have a maximum height. See <a href="/guides/can-you-be-too-tall-for-a-roller-coaster/">can you be too tall for a roller coaster?</a></p>
<h2>The most common height requirements</h2><p>Across the coasters we cover, the most common ride-alone minimums at parks that publish inches are {", ".join(f"{h} in ({n} coasters)" for h, n in inch)}. At parks that publish centimetres they are {", ".join(f"{h} cm ({n} coasters)" for h, n in cmc)}.</p>
<h2>Height guides</h2><ul><li><a href="/guides/roller-coasters-for-36-inch-kids/">Coasters for 36-inch kids</a></li><li><a href="/guides/roller-coasters-for-42-inch-kids/">Coasters for 42-inch kids</a></li><li><a href="/guides/roller-coasters-for-48-inch-kids/">Coasters for 48-inch kids</a></li><li><a href="/guides/roller-coasters-for-54-inch-kids/">Coasters for 54-inch kids</a></li></ul>'''
    faqs = [("How do theme parks measure height for rides?", "At each ride entrance with a measuring stick, and sometimes again before boarding. Walt Disney World's official planDisney panel says Cast Members at rides with height restrictions have measuring sticks at the entrances."),
            ("Do kids get measured with shoes on?", "Plan on it. Universal Orlando's official rider guide says shoes must be worn at all times, so children wear shoes both when measured and when riding. Measure at home in the same shoes."),
            ("Can my child ride if they are half an inch short?", "No. Walt Disney World's planDisney panel says height restrictions are strictly enforced even for a tiny difference, and other parks apply their posted minimums too."),
            ("What is a supervising companion?", "At Universal Orlando, someone 14 or older who meets all other ride requirements and rides with a child under the 48 in ride-alone height. Other parks set their own rules.")]
    qpage("roller-coaster-height-requirements-explained", f"Roller Coaster Height Requirements Explained | {BRAND}", "How theme parks measure riders, shoes, what to do if your child is near the line, companion rules and the most common coaster height requirements.",
          "Roller coaster height requirements explained", "parks measure riders at each ride entrance with a measuring stick and enforce the posted number strictly, even for a fraction of an inch. Many rides also have a lower height range that can ride with a supervising companion.",
          body, faqs, "How parks measure, and what to do near the line.", sources=[PLANDISNEY, PLANDISNEY2, UOR_GUIDE, UOR_HEIGHTS], related=[("/height-checker/", "Ride height checker"), ("/guides/can-you-be-too-tall-for-a-roller-coaster/", "Can you be too tall?"), ("/guides/best-first-roller-coasters/", "Best first roller coasters"), ("/guides/roller-coasters-for-48-inch-kids/", "Coasters for 48-inch kids")])

def fti(inches): f, i = divmod(round(inches), 12); return f"{f} ft {i} in" if i else f"{f} ft"
def too_tall_page():
    mx = sorted([c for c in _hr_coasters() if c["hr"].get("max")], key=lambda c: (hin(c["hr"], "max"), c["name"]))
    rows = "".join(f'<tr><th scope="row"><a href="{coaster_path(c)}">{E(c["name"])}</a></th><td>{E(pk(c)["short"])}</td><td data-v="{round(hin(c["hr"], "max"), 2)}">{hs(c["hr"], "max")}</td><td>{hs(c["hr"])}</td></tr>' for c in mx)
    adult = [c for c in mx if hin(c["hr"], "max") >= 66]; kid = [c for c in mx if hin(c["hr"], "max") < 66]
    lo_i = min(hin(c["hr"], "max") for c in adult); hi_i = max(hin(c["hr"], "max") for c in adult)
    rng = f"{fti(lo_i)} to {fti(hi_i)} ({round(lo_i * 2.54)} to {round(hi_i * 2.54)} cm)"
    body = f'''<h2>Yes, some coasters have a maximum height</h2><p>Most roller coasters have only a minimum height, but some also set a maximum. Of the {len(_hr_coasters())} coasters on {BRAND} with a verified height rule, <strong>{len(mx)} publish a maximum rider height</strong>. They fall into two groups:</p><ul>
<li><strong>Kids' coasters</strong> ({len(kid)} on our list) with a low maximum.</li>
<li><strong>Coasters with an adult-size limit</strong> ({len(adult)} on our list), ranging from {rng}.</li></ul>
<h2>Why tall riders are limited</h2><p>A shoulder harness or vest has to sit correctly and lock at the right point, and very tall riders may not fit it properly. On some coasters, especially inverted, flying and tight indoor rides, the clearance between a rider's head, feet or legs and the structure is part of the design. Universal Orlando's official rider guide notes on one attraction that "People of extreme height should see an Attendant", and provides test seats at the entrance of several rides.</p>
<h2>Too big rather than too tall</h2><p>Body shape matters as much as height. Universal Orlando's rider guide says "Guests who do not fit properly within any safety restraint will not be permitted to ride." If a ride has a test seat, use it before queuing.</p>
<h2>Every coaster with a maximum height on {BRAND}</h2><p>Lowest maximum first. Each links to the ride's page with the official source.</p><div class="tablewrap"><table class="list sortable"><thead><tr><th scope="col">Coaster</th><th scope="col">Park</th><th scope="col">Maximum height</th><th scope="col">Minimum height</th></tr></thead><tbody>{rows}</tbody></table></div>'''
    faqs = [("Can you be too tall for a roller coaster?", f"Yes, on some rides. {len(mx)} of the coasters on {BRAND} with verified height rules publish a maximum rider height; on coasters with an adult-size limit it ranges from {rng}."),
            ("Do all roller coasters have a maximum height?", "No. Most have only a minimum. Check each ride's page for a published maximum, and try the test seat where one is provided."),
            ("Why do roller coasters have a maximum height?", "So that shoulder harnesses and vests fit correctly and riders' heads and limbs stay clear of the structure."),
            ("Is 6 ft 5 in too tall for roller coasters?", f"For most coasters, no. Some rides set a maximum in the range {rng}, and body shape and restraint fit also matter, so check the ride's page and try the test seat.")]
    qpage("can-you-be-too-tall-for-a-roller-coaster", f"Can You Be Too Tall for a Roller Coaster? Max Heights | {BRAND}", f"Yes, some coasters have a maximum rider height. See all {len(mx)} coasters on Coaster Map with an official maximum, why limits exist and tips for tall riders.",
          "Can you be too tall for a roller coaster?", f"yes, on some rides. {len(mx)} of the coasters we cover publish a maximum rider height: low limits on some kids' coasters, and limits from {rng} on others, usually because of shoulder harnesses or tight clearances.",
          body, faqs, "Every coaster with a maximum rider height.", sources=[UOR_GUIDE], related=[("/guides/roller-coaster-height-requirements-explained/", "Height requirements explained"), ("/guides/how-do-roller-coaster-restraints-work/", "How restraints work"), ("/height-checker/", "Ride height checker"), ("/guides/what-is-an-inverted-roller-coaster/", "What is an inverted coaster?")], items=mx[:50])

def stuck_page():
    long_ = sorted([c for c in ALL if c["length"]], key=lambda c: -c["length"])[:6]
    body = f'''<h2>Why coasters stop</h2><p>A roller coaster's control system watches sensors all along the track. If anything is outside the expected range, such as a train running slower than it should, a sensor not reporting, high wind or a problem in the station, the system stops trains at the next safe point. Stopping is the designed response to a fault, not the fault itself.</p>
<h2>Where a train stops</h2><p>The track is divided into blocks separated by brakes, and only one train is allowed in a block at a time. When the system stops, trains halt on block brakes or the lift hill, so they cannot reach each other. On a lift hill, the anti-rollback ratchet holds the train in place. Coasters are designed with enough speed through every inversion, so stops happen on brakes and lifts rather than upside down.</p>
<h2>What happens next</h2><p>Usually the ride is restarted after staff check the system, and trains continue to the station. If not, staff walk riders off the train. Universal Orlando's official rider guide warns: "If an evacuation of an attraction or venue is required, Guests may be required to navigate stairs, narrow walkways, or ladders." It adds: "Please have a member of your party assist you, or wait in the ride vehicle for assistance."</p>
<h2>If you are on a stopped coaster</h2><ul><li>Stay seated with your restraint locked.</li><li>Keep hands, feet and belongings inside the car.</li><li>Wait for instructions from ride staff, and do not try to climb out.</li><li>If you have a medical need, tell staff when they reach you.</li></ul>
<h2>Longest coasters we cover</h2><p>Long coasters have more blocks and more places to stop along the way:</p>{clist(long_, lambda c: f": {c['length']:,} ft")}'''
    faqs = [("What happens if a roller coaster gets stuck?", "Trains stop on block brakes or the lift hill, where they are held in place. Staff restart the ride or walk riders off using stairs and walkways."),
            ("Can a roller coaster stop upside down?", "Coasters are designed with enough speed through each inversion, and stops happen on brakes or lift hills rather than in loops."),
            ("Why do roller coasters stop on the lift hill?", "The control system stops trains at safe points if a sensor reports anything unexpected. The anti-rollback ratchet holds the train on the lift.")]
    qpage("what-happens-if-a-roller-coaster-gets-stuck", f"What Happens If a Roller Coaster Gets Stuck? | {BRAND}", "Why roller coasters stop, where trains stop, whether a coaster can stop upside down, how evacuations work and what to do if you are on a stopped ride.",
          "What happens if a roller coaster gets stuck?", "the ride's control system stops trains at safe points, on brakes or the lift hill, where they are held in place. Staff then restart the ride or walk riders off using stairs and walkways. Stay seated and wait for instructions.",
          body, faqs, "Why coasters stop and how evacuations work.", sources=[UOR_GUIDE], related=[("/guides/how-do-roller-coaster-brakes-work/", "How brakes work"), ("/guides/how-do-roller-coasters-work/", "How roller coasters work"), ("/guides/how-to-not-be-scared-of-roller-coasters/", "How to not be scared"), ("/guides/longest-roller-coasters/", "Longest roller coasters")])

def motion_page():
    spin = [c for c in ALL if "Spinning Cars" in c["tags"]][:10]
    body = f'''<p class="note"><strong>General information only.</strong> This page summarises public health guidance and park safety rules. It is not medical advice. Talk to a doctor or pharmacist before taking any medicine, and follow the warning signs at each ride.</p>
<h2>Why coasters can make you feel sick</h2><p>Motion sickness happens when the signals from your eyes, inner ear and body do not match. Coasters with spinning cars, backwards sections, dark indoor sections or screens are common triggers, because what you see and what you feel disagree. Universal Orlando's warning symbols include "Do not ride if you are susceptible to motion sickness or dizziness" on rides where that applies.</p>
<h2>What public health guidance says</h2><p>The US Centers for Disease Control and Prevention (CDC) travel guidance on motion sickness suggests, among other steps, looking at the horizon, staying hydrated, limiting alcoholic and caffeinated drinks, eating small amounts of food frequently, avoiding smoking and distracting yourself, for example with music. The CDC Yellow Book says habituation, gradual repeated exposure to the motion, is the most effective countermeasure, that sleep deprivation can make motion sickness worse, and that medicine is most effective when taken before the motion starts rather than after symptoms begin. The CDC notes many motion sickness medicines cause drowsiness and says to talk to a healthcare professional about whether to use them.</p>
<h2>Practical tips at the park</h2><ul><li>Sit in the middle of the train and face forward. Look ahead, not at the floor.</li><li>Take breaks between rides and drink water.</li><li>Skip spinning coasters and shuttle coasters, which run backwards, if they trouble you.</li><li>Build up gradually across the day, starting with a gentle coaster.</li></ul>
<h2>Spinning coasters to approach with care</h2><p>On these coasters the cars spin freely, a common motion sickness trigger:</p>{clist(spin, withhr)}'''
    faqs = [("How do you avoid motion sickness on roller coasters?", "Sit in the middle facing forward, look ahead, avoid spinning and backwards rides if they trouble you, stay hydrated and take breaks. CDC guidance adds looking at the horizon and limiting alcohol and caffeine. Ask a doctor or pharmacist about medicine."),
            ("Why do roller coasters make me sick?", "Motion sickness happens when your eyes and inner ear send conflicting signals, which is common on spinning, backwards and dark rides."),
            ("Can you take motion sickness medicine before a theme park?", "The CDC says medicine is most effective before the motion starts and that many such medicines cause drowsiness. Talk to a healthcare professional before using any medicine.")]
    qpage("roller-coaster-motion-sickness", f"Roller Coaster Motion Sickness: Causes and Tips | {BRAND}", "Why roller coasters cause motion sickness, what CDC guidance says about preventing it, and practical seat and ride tips. General information only.",
          "Roller coaster motion sickness: causes and tips", "motion sickness on coasters comes from your eyes and inner ear disagreeing, especially on spinning, backwards and dark rides. Sit in the middle facing forward, look ahead, stay hydrated and take breaks. Ask a doctor or pharmacist before taking any medicine.",
          body, faqs, "CDC guidance plus seat and ride tips.", sources=[CDC_TRAVEL, CDC_YB, UOR_GUIDE], related=[("/guides/best-seat-on-a-roller-coaster/", "Best seat on a roller coaster"), ("/guides/what-is-a-spinning-roller-coaster/", "What is a spinning coaster?"), ("/guides/roller-coasters-and-health-conditions/", "Roller coasters and health conditions"), ("/guides/best-first-roller-coasters/", "Best first roller coasters")])

def health_page():
    body = f'''<p class="note"><strong>General information only.</strong> This page quotes official park safety rules. It is not medical advice. If you have a health condition or are pregnant, talk to your doctor before your visit and always follow the warning signs at each ride and the instructions of ride staff.</p>
<h2>What parks say</h2><p>Parks post health warnings at ride entrances, and the warnings differ from ride to ride. Universal Orlando's official Guide for Rider Safety and Accessibility is a clear example. Its warning symbols include:</p><ul>
<li>"Do not ride if you have a history of heart conditions or abnormal blood pressure."</li>
<li>"Do not ride if you have back, neck, or similar physical conditions."</li>
<li>"Do not ride if you have unhealed surgery or fractures."</li>
<li>"Do not ride if you have weakened bones or muscles."</li>
<li>"Do not ride if you are an expectant mother."</li>
<li>"Do not ride if you are susceptible to motion sickness or dizziness."</li>
<li>"Do not ride if you have other conditions which may be aggravated by this ride."</li></ul>
<p>The same guide says: "You know your physical conditions and limitations; Universal Orlando does not. If you suspect your health could be at risk for any reason, or you could aggravate a pre-existing condition of any kind, do not experience the attraction." It also says that for most rides you "must be able to independently maintain an upright position, and brace and support your torso, neck, and head while absorbing sudden and dramatic movements throughout the experience."</p>
<h2>Pregnancy</h2><p>Universal Orlando's symbol for expectant mothers ("Do not ride if you are an expectant mother") appears on the rides where it applies, and other parks post their own warnings at ride entrances. Check the sign at each ride and ask your doctor.</p>
<h2>Heart, blood pressure, back and neck</h2><p>Coasters subject riders to sudden acceleration, braking and changes in direction, which is why parks warn riders with heart conditions, abnormal blood pressure, back or neck conditions, or unhealed surgery or fractures. On {BRAND}, each coaster page shows RCDB's intensity class and, where the park publishes it, the park's own thrill rating, but these are not a substitute for the park's warning sign or a doctor's advice.</p>
<h2>Before you go</h2><ul><li>Read the park's rider safety or accessibility guide for each ride you plan to ride.</li><li>Talk to your doctor if you have any condition on the warning lists.</li><li>At the park, read the sign at each ride entrance and ask staff if anything is unclear.</li></ul>'''
    faqs = [("Can you ride roller coasters while pregnant?", "Parks warn against it. Universal Orlando's official rider guide, for example, uses the warning \"Do not ride if you are an expectant mother\" on rides where it applies. Follow each ride's sign and your doctor's advice."),
            ("Can you ride roller coasters with a heart condition?", "Parks warn against it on many rides. Universal Orlando's guide says \"Do not ride if you have a history of heart conditions or abnormal blood pressure.\" Talk to your doctor and follow each ride's sign."),
            ("Can you ride roller coasters with back problems?", "Many rides carry a warning such as Universal Orlando's \"Do not ride if you have back, neck, or similar physical conditions.\" Follow each ride's sign and your doctor's advice.")]
    qpage("roller-coasters-and-health-conditions", f"Roller Coasters, Pregnancy and Health: What Parks Say | {BRAND}", "What official park safety rules say about riding roller coasters while pregnant or with heart, blood pressure, back or neck conditions. General information only.",
          "Roller coasters, pregnancy and health conditions: what parks say", "parks warn expectant mothers and riders with heart conditions, abnormal blood pressure, back or neck problems, or unhealed surgery not to ride many coasters. This is general information only: follow the warning sign at each ride and your doctor's advice.",
          body, faqs, "Official park warnings, quoted.", sources=[UOR_GUIDE], related=[("/guides/roller-coaster-motion-sickness/", "Roller coaster motion sickness"), ("/guides/best-first-roller-coasters/", "Best first roller coasters"), ("/guides/most-intense-roller-coasters/", "Most intense roller coasters"), ("/guides/how-do-roller-coaster-restraints-work/", "How restraints work")])

REC_SPEED = [("1st", [("Falcons Flight", None)], "Six Flags Qiddiya City", "Saudi Arabia", 155.3), ("2nd", [("Top Thrill 2", "cedar-point")], "Cedar Point", "US (Ohio)", 120), ("3rd", [("Red Force", "ferrari-land")], "Ferrari Land", "Spain", 111.8),
 ("4th", [("Steel Dragon 2000", None), ("Fury 325", "carowinds")], "Nagashima Spa Land; Carowinds", "Japan; US (North Carolina)", 95), ("5th", [("Millennium Force", "cedar-point")], "Cedar Point", "US (Ohio)", 93), ("6th", [("Leviathan", "canadas-wonderland")], "Canada's Wonderland", "Canada", 92),
 ("7th", [("Orion", "kings-island")], "Kings Island", "US (Ohio)", 91), ("8th", [("Pantherian", "kings-dominion")], "Kings Dominion", "US (Virginia)", 90), ("9th", [("Hyperion", "energylandia")], "Energylandia", "Poland", 88.2), ("10th", [("Tormenta Rampaging Run", "six-flags-over-texas")], "Six Flags Over Texas", "US (Texas)", 87)]
REC_HEIGHT = [("1st", [("Falcons Flight", None)], "Six Flags Qiddiya City", "Saudi Arabia", 534.8), ("2nd", [("Top Thrill 2", "cedar-point")], "Cedar Point", "US (Ohio)", 420), ("3rd", [("Red Force", "ferrari-land")], "Ferrari Land", "Spain", 367.3),
 ("4th", [("Fury 325", "carowinds")], "Carowinds", "US (North Carolina)", 325), ("5th", [("Steel Dragon 2000", None)], "Nagashima Spa Land", "Japan", 318.2), ("6th", [("Millennium Force", "cedar-point")], "Cedar Point", "US (Ohio)", 310),
 ("7th", [("Tormenta Rampaging Run", "six-flags-over-texas")], "Six Flags Over Texas", "US (Texas)", 309), ("8th", [("Leviathan", "canadas-wonderland")], "Canada's Wonderland", "Canada", 306), ("9th", [("Pantherian", "kings-dominion")], "Kings Dominion", "US (Virginia)", 305), ("10th", [("Orion", "kings-island")], "Kings Island", "US (Ohio)", 287)]
def records_page():
    def nm(lst): return " and ".join(clk(n, p) if p else E(n) for n, p in lst)
    def table(rows, unit):
        return '<div class="tablewrap"><table class="list"><thead><tr><th scope="col">RCDB rank</th><th scope="col">Coaster</th><th scope="col">Park</th><th scope="col">Country</th><th scope="col">' + unit + '</th></tr></thead><tbody>' + "".join(
            f'<tr><td>{r}</td><th scope="row">{nm(l)}</th><td>{E(p)}</td><td>{E(co)}</td><td>{(f"{v:g} mph ({round(v * 1.609)} km/h)" if unit == "Top speed" else f"{v:g} ft ({round(v * 0.3048)} m)")}</td></tr>' for r, l, p, co, v in rows) + "</tbody></table></div>"
    body = f'''<p>These tables copy RCDB's Record Holders rankings for operating roller coasters, last verified {CHECKED}. RCDB does not assign ranks to coasters that are not operating, so closed rides and rides not yet open are left out. Records change when new rides open, so check the date above. Where we cover a coaster, its name links to our page with its height requirement.</p>
<h2>Fastest roller coasters in the world</h2>{table(REC_SPEED, "Top speed")}
<h2>Tallest roller coasters in the world</h2>{table(REC_HEIGHT, "Height")}
<h2>Other world records on RCDB</h2><ul><li><strong>Longest:</strong> Falcons Flight at Six Flags Qiddiya City, 13,943.6 ft (4,250 m), ahead of Steel Dragon 2000 at 8,133.2 ft and {clk("Beast", "kings-island")} at Kings Island at 7,361 ft.</li>
<li><strong>Biggest drop:</strong> {clk("Top Thrill 2", "cedar-point")} at Cedar Point, 400 ft (122 m), ahead of {clk("Red Force", "ferrari-land")} at 345 ft.</li>
<li><strong>Most inversions:</strong> {clk("Smiler", "alton-towers")} at Alton Towers, 14.</li>
<li><strong>Steepest:</strong> TMNT Shellraiser at Nickelodeon Universe in New Jersey, 121.5 degrees, then {clk("Takabisha")} at Fuji-Q Highland at 121 degrees and {clk("Green Lantern Coaster")} at Warner Bros. Movie World at 120.5 degrees.</li></ul>
<h2>Records among the coasters we cover</h2><p>Our ranking guides list the leaders among the {len(ALL)} coasters on {BRAND}, each with its height requirement: <a href="/guides/fastest-roller-coasters/">fastest</a>, <a href="/guides/tallest-roller-coasters/">tallest</a>, <a href="/guides/longest-roller-coasters/">longest</a>, <a href="/guides/steepest-roller-coasters/">steepest</a> and <a href="/guides/roller-coasters-with-the-most-inversions/">most inversions</a>.</p>
<h2>Height classes</h2><p>Coasters 200 ft or taller are called hypercoasters, 300 ft or taller giga coasters, and 400 ft or taller strata coasters. See <a href="/guides/what-is-a-hypercoaster/">what is a hypercoaster?</a></p>'''
    faqs = [("What is the fastest roller coaster in the world?", f"Falcons Flight at Six Flags Qiddiya City in Saudi Arabia, at 155.3 mph (250 km/h), according to RCDB's record holders list for operating coasters, last verified {CHECKED}."),
            ("What is the tallest roller coaster in the world?", f"Falcons Flight at Six Flags Qiddiya City, at 534.8 ft (163 m), according to RCDB, last verified {CHECKED}. Top Thrill 2 at Cedar Point is second at 420 ft."),
            ("What is the fastest roller coaster in the US?", f"Top Thrill 2 at Cedar Point, Ohio, at 120 mph, according to RCDB's record holders list, last verified {CHECKED}."),
            ("Which roller coaster has the most inversions?", f"The Smiler at Alton Towers, with 14, according to RCDB, last verified {CHECKED}.")]
    qpage("world-record-roller-coasters", f"World Record Roller Coasters: Fastest, Tallest & More | {BRAND}", "The fastest, tallest, longest and steepest roller coasters in the world and the most inversions, from RCDB's record holders, with a last verified date.",
          "World record roller coasters", f"the fastest and tallest roller coaster in the world is Falcons Flight at Six Flags Qiddiya City in Saudi Arabia: 155.3 mph and 534.8 ft, according to RCDB (last verified {CHECKED}). In the US, Top Thrill 2 at Cedar Point leads at 120 mph and 420 ft.",
          body, faqs, "Fastest, tallest, longest and steepest, from RCDB.", sources=[RCDB_REC], group="Records", related=[("/guides/fastest-roller-coasters/", "Fastest roller coasters we cover"), ("/guides/tallest-roller-coasters/", "Tallest roller coasters we cover"), ("/guides/what-is-a-hypercoaster/", "What is a hypercoaster?"), ("/guides/how-do-roller-coaster-launches-work/", "How launches work")])

GLOSSARY = [
 ("Airtime", "The moment you lift out of your seat, held in by your restraint, when forces drop below zero g.", "/guides/what-is-airtime-on-a-roller-coaster/"),
 ("Anti-rollback", "The ratchet on a lift hill that stops a train rolling backwards; it makes the clacking sound.", "/guides/how-do-roller-coasters-work/"),
 ("B&M", "Bolliger & Mabillard, a Swiss coaster manufacturer.", "/guides/bolliger-mabillard-roller-coasters/"),
 ("Banked turn", "A turn tilted towards its centre so riders are pushed into the seat rather than sideways."),
 ("Block brake", "A brake that divides the track into sections so only one train is in each section at a time.", "/guides/how-do-roller-coaster-brakes-work/"),
 ("Boomerang", "A Vekoma shuttle coaster model that runs its looping course forwards, then backwards.", "/guides/what-is-a-shuttle-roller-coaster/"),
 ("Brake run", "The section of brakes that slows the train before the station.", "/guides/how-do-roller-coaster-brakes-work/"),
 ("Camelback", "A large, rounded hill designed for floater airtime."),
 ("Catch car", "On cable and hydraulic launches, the car that hooks the train, pulls it to speed and lets go.", "/guides/how-do-roller-coaster-launches-work/"),
 ("Chain lift", "A moving chain under the track that pulls the train up the lift hill.", "/guides/how-do-roller-coasters-work/"),
 ("Cobra roll", "A two-inversion element shaped like a cobra's hood that reverses the train's direction."),
 ("Corkscrew", "An inversion where the track twists through 360 degrees as it moves forward."),
 ("Dive coaster", "A coaster with wide trains that pause at the top of a vertical drop.", "/guides/what-is-a-dive-coaster/"),
 ("Dive loop", "An inversion that rises, twists and dives down, the reverse of an immelmann."),
 ("Ejector airtime", "Strong, sharp airtime that pushes you up into your restraint.", "/guides/what-is-airtime-on-a-roller-coaster/"),
 ("Family coaster", "A coaster built for children and adults to ride together.", "/guides/what-is-a-family-roller-coaster/"),
 ("Floater airtime", "Gentle, sustained airtime close to zero g.", "/guides/what-is-airtime-on-a-roller-coaster/"),
 ("Flying coaster", "A coaster where riders lie face down, parallel to the track.", "/guides/what-is-a-flying-roller-coaster/"),
 ("G-force", "The force on a rider compared with normal gravity; 1 g is sitting still.", "/guides/why-your-stomach-drops-on-a-roller-coaster/"),
 ("Giga coaster", "A coaster with a height or drop of 300 to 399 feet.", "/guides/what-is-a-hypercoaster/"),
 ("Heartline roll", "A roll where the track rotates around the rider's heart line, so the body stays centred."),
 ("Helix", "A long, spiralling turn of 360 degrees or more, often with sustained g-forces."),
 ("Hybrid coaster", "A coaster with steel track on a wooden-style structure, or a wooden coaster retracked in steel.", "/guides/what-is-a-hybrid-roller-coaster/"),
 ("Hypercoaster", "A coaster with a height or drop of at least 200 feet.", "/guides/what-is-a-hypercoaster/"),
 ("Immelmann", "An inversion with a half loop up followed by a half twist, named after a flying manoeuvre."),
 ("Inversion", "Any element that turns riders upside down.", "/guides/roller-coasters-with-the-most-inversions/"),
 ("Inverted coaster", "A coaster where the train hangs below the track and riders' feet dangle.", "/guides/what-is-an-inverted-roller-coaster/"),
 ("Lap bar", "A restraint that lowers across the thighs or hips.", "/guides/how-do-roller-coaster-restraints-work/"),
 ("Launch", "Acceleration that replaces a lift hill, using magnets, hydraulics, air or tyres.", "/guides/how-do-roller-coaster-launches-work/"),
 ("Lift hill", "The climb at the start of most coasters, using a chain, cable or tyres.", "/guides/how-do-roller-coasters-work/"),
 ("LIM and LSM", "Linear induction and linear synchronous motors, electromagnetic launch systems.", "/guides/how-do-roller-coaster-launches-work/"),
 ("Magnetic brakes", "Brakes that slow the train with eddy currents, without contact.", "/guides/how-do-roller-coaster-brakes-work/"),
 ("Mine train", "A family coaster themed to a runaway mining train, usually with no inversions."),
 ("OTSR", "Over-the-shoulder restraint: a harness that comes down over the shoulders.", "/guides/how-do-roller-coaster-restraints-work/"),
 ("Outlaw hill", "A small, sudden hill designed for a quick moment of ejector airtime."),
 ("Overbanked turn", "A turn banked beyond 90 degrees, so riders tilt partly upside down without fully inverting."),
 ("Pretzel loop", "A loop on a flying coaster where riders dive down on their backs and pull up face down, with strong g-forces.", "/guides/what-is-a-flying-roller-coaster/"),
 ("Rider swap", "A system at many parks where adults take turns riding while one waits with a child, without queuing twice. Also called child swap or rider switch.", "/guides/roller-coaster-height-requirements-explained/"),
 ("Rollback", "When a launched train does not clear a tall tower and rolls back to the launch track.", "/guides/how-do-roller-coaster-launches-work/"),
 ("Shuttle coaster", "A coaster that runs its course forwards and then backwards rather than completing a circuit.", "/guides/what-is-a-shuttle-roller-coaster/"),
 ("Side friction wheels", "Wheels on the side of the rail that stop the train moving sideways.", "/guides/how-do-roller-coasters-stay-on-the-track/"),
 ("SLC", "Suspended Looping Coaster, a Vekoma inverted coaster model.", "/guides/vekoma-roller-coasters/"),
 ("Spinning coaster", "A coaster whose cars rotate freely as they travel.", "/guides/what-is-a-spinning-roller-coaster/"),
 ("Stall", "An inversion held slowly at the top so riders hang in their restraints."),
 ("Strata coaster", "A coaster with a height or drop of at least 400 feet.", "/guides/world-record-roller-coasters/"),
 ("Top hat", "A tall tower element, usually on a launch coaster, where the track climbs vertically and drops straight back down."),
 ("Trim brake", "A brake partway through a course that takes off a little speed.", "/guides/how-do-roller-coaster-brakes-work/"),
 ("Upstop wheels", "Wheels under the rail that stop the train lifting off the track.", "/guides/how-do-roller-coasters-stay-on-the-track/"),
 ("Vertical loop", "A full loop where the train turns upside down; modern loops are teardrop shaped.", "/guides/how-do-roller-coasters-stay-on-the-track/"),
 ("Wild mouse", "A compact coaster with single cars and sharp, unbanked hairpin turns.", "/guides/what-is-a-wild-mouse-coaster/"),
 ("Wing coaster", "A coaster with seats on either side of the track and nothing above or below.", "/guides/what-is-a-wing-coaster/"),
 ("Wooden coaster", "A coaster with track made of laminated wood.", "/guides/what-is-a-wooden-roller-coaster/"),
 ("Zero-g roll", "A twisting inversion over a hill where riders feel close to weightless while upside down."),
]
def glossary_page():
    gp = {u for u, *_ in GUIDES}
    def dd(t, d, u=None): return f'<dt id="{slugify(t)}">{E(t)}</dt><dd>{E(d)}' + (f' <a href="{u}">Read more</a>.' if u and u in gp else "") + "</dd>"
    letters = sorted({t[0].upper() for t, *_ in GLOSSARY})
    body = '<p>Jump to: ' + " · ".join(f'<a href="#letter-{l.lower()}">{l}</a>' for l in letters) + '</p>'
    for l in letters: body += f'<h2 id="letter-{l.lower()}">{l}</h2><dl>' + "".join(dd(*g) for g in GLOSSARY if g[0][0].upper() == l) + "</dl>"
    faqs = [("What is airtime on a roller coaster?", GLOSSARY[0][1]), ("What is an inversion on a roller coaster?", "Any element that turns riders upside down, such as a loop, corkscrew or zero-g roll."), ("What is a giga coaster?", "A roller coaster with a height or drop of 300 to 399 feet. Coasters of 200 ft or more are hypercoasters and 400 ft or more strata coasters.")]
    qpage("roller-coaster-glossary", f"Roller Coaster Glossary: {len(GLOSSARY)} Terms Explained | {BRAND}", f"A plain-English roller coaster glossary: {len(GLOSSARY)} terms from airtime and anti-rollback to zero-g roll, with links to detailed explainers.",
          "Roller coaster glossary", f"this glossary explains {len(GLOSSARY)} roller coaster terms in plain English, from airtime and block brakes to inversions, launches and the zero-g roll, with links to our detailed explainers.",
          body, faqs, f"{len(GLOSSARY)} coaster terms in plain English.", related=[("/guides/roller-coaster-types/", "Roller coaster types"), ("/guides/how-do-roller-coasters-work/", "How roller coasters work"), ("/guides/roller-coaster-manufacturers/", "Roller coaster manufacturers")])

MAKERS = [
 ("Vekoma", "vekoma", "Vekoma", "Vlodrop, Netherlands", 1926, None, "/6836.htm", "Vekoma is one of the most prolific coaster builders, known for family coasters, the Boomerang shuttle and the Suspended Looping Coaster (SLC), as well as launched and family boomerang designs."),
 ("Bolliger & Mabillard", "bolliger-mabillard", "Bolliger & Mabillard (B&M)", "Monthey, Switzerland", 1988, None, "/6831.htm", "Bolliger & Mabillard, usually called B&M, is a Swiss firm known for smooth steel coasters: inverted coasters, hypercoasters, dive coasters, wing coasters, floorless and flying coasters."),
 ("Intamin Amusement Rides", "intamin", "Intamin", "Schaan, Liechtenstein", 1967, None, "/6837.htm", "Intamin has built many record-breaking coasters, including hydraulic and LSM launch coasters, giga coasters and wooden coasters with prefabricated track."),
 ("Mack Rides GmbH & Co KG", "mack-rides", "Mack Rides", "Waldkirch, Germany", 1780, None, "/6856.htm", "Mack Rides is a German family company known for launched coasters, mega coasters, family coasters, wild mouse rides and water coasters."),
 ("Arrow Dynamics", "arrow-dynamics", "Arrow Dynamics", "Clearfield, Utah, United States", 1945, 2002, "/6835.htm", "Arrow Dynamics built many classic mine trains, corkscrews and looping coasters on tubular steel track. RCDB lists the company as defunct."),
 ("Premier Rides", "premier-rides", "Premier Rides", "Baltimore, Maryland, United States", 1994, None, "/6848.htm", "Premier Rides is known for LIM and LSM launch coasters, including indoor launched coasters and Sky Rocket designs."),
 ("Rocky Mountain Coasters", "rocky-mountain-construction", "Rocky Mountain Construction (RMC)", "Hayden, Idaho, United States", 2001, None, "/10583.htm", "Rocky Mountain Construction, listed on RCDB as Rocky Mountain Coasters, is best known for I-Box steel track that turns wooden coasters into hybrids, and for Raptor single-rail coasters. Its rides are known for airtime."),
 ("Gerstlauer Amusement Rides GmbH", "gerstlauer", "Gerstlauer", "Münsterhausen, Germany", 1981, None, "/6948.htm", "Gerstlauer is a German manufacturer known for Euro-Fighter coasters with beyond-vertical drops, infinity coasters, spinning coasters and family coasters."),
]
def maker_path(c):
    for mk, slug, label, *_ in MAKERS:
        if c["make"] == mk: return f"/guides/{slug}-roller-coasters/", f"{label} roller coasters"
    return None
def maker_pages():
    from collections import Counter
    hub = []
    for mk, slug, label, hq, since, until, rid, blurb in MAKERS:
        cs = sorted([c for c in ALL if c["make"] == mk], key=lambda c: -(c["height"] or 0))
        if len(cs) < 3: continue
        parks = sorted({pk(c)["name"] for c in cs})
        models = Counter(c["model"] for c in cs if c["model"]).most_common(5)
        tall = max((c for c in cs if c["height"]), key=lambda c: c["height"], default=None)
        fast = max((c for c in cs if c["speed"]), key=lambda c: c["speed"], default=None)
        inv = max((c for c in cs if c["inversions"]), key=lambda c: c["inversions"], default=None)
        hrs = [c for c in cs if c["hr"]]; lo = min(hrs, key=lambda c: hin(c["hr"]), default=None)
        yrs = sorted(int(year(c)) for c in cs if year(c))
        rcdb_line = f"RCDB lists {label} as based in {hq}" + (f", operating from {since} to {until}" if until else f", in business since {since}") + "."
        body = (f'<h2>About {E(label)}</h2><p>{E(blurb)} {E(rcdb_line)}</p><h2>{E(label)} coasters by the numbers</h2><ul><li><strong>{len(cs)}</strong> coasters on {BRAND} at <strong>{len(parks)}</strong> parks.</li>'
                + (f'<li>Opened between {yrs[0]} and {yrs[-1]}.</li>' if yrs else "") + (f'<li>Tallest: {clink(tall)}, {ftm(tall["height"])}.</li>' if tall else "") + (f'<li>Fastest: {clink(fast)}, {mphk(fast["speed"])}.</li>' if fast else "")
                + (f'<li>Most inversions: {clink(inv)}, {inv["inversions"]}.</li>' if inv else "") + (f'<li>Lowest height requirement: {clink(lo)}, {hs(lo["hr"])}.</li>' if lo else "") + "</ul>"
                + ('<h2>Most common models</h2><ul>' + "".join(f"<li>{E(m)}: {n}</li>" for m, n in models) + "</ul>" if models else "")
                + f'<h2>Every {E(label)} coaster on {BRAND}</h2>{coaster_table(cs, show_park=True)}<p>Manufacturer, model and statistics come from each coaster\'s RCDB entry; see the <a href="https://rcdb.com{rid}" rel="nofollow noopener" target="_blank">RCDB page for {E(label)}</a> for its full worldwide list.</p>')
        faqs = [(f"Who is {label}?", f"{blurb} {rcdb_line}"), (f"How many {label} roller coasters are on Coaster Map?", f"{len(cs)}, at {len(parks)} parks, as of {CHECKED}.")]
        if tall: faqs.append((f"What is the tallest {label} roller coaster on Coaster Map?", f"{tall['name']} at {pk(tall)['name']}, {ftm(tall['height'])} according to RCDB."))
        title = f"{label} Roller Coasters: Every Ride & Height Rule | {BRAND}"
        if len(title) > 70: title = f"{label} Roller Coasters | {BRAND}"
        qpage(f"{slug}-roller-coasters", title, f"Who {label} is and all {len(cs)} {label} roller coasters on Coaster Map, with height requirements, stats, models and the tallest and fastest.",
              f"{label} roller coasters", f"{E(label)} is a coaster manufacturer based in {E(hq)}. {BRAND} covers <strong>{len(cs)} {E(label)} coasters</strong> at {len(parks)} parks" + (f", the tallest being {clink(tall)} at {ftm(tall['height'])}" if tall else "") + ".",
              body, faqs, f"{len(cs)} coasters at {len(parks)} parks.", sources=[(f"RCDB: {label}", "https://rcdb.com" + rid)], group="Manufacturers",
              related=[("/guides/roller-coaster-manufacturers/", "All roller coaster manufacturers")] + [(f"/guides/{s}-roller-coasters/", f"{l} roller coasters") for m, s, l, *_ in MAKERS if s != slug][:5], items=cs[:50])
        hub.append((slug, label, hq, since, until, len(cs), len(parks), tall))
    allc = Counter(c["make"] for c in ALL if c["make"])
    rows = "".join(f'<tr><th scope="row"><a href="/guides/{s}-roller-coasters/">{E(l)}</a></th><td>{E(h)}</td><td>{si}{"" if not u else f" to {u}"}</td><td>{n}</td><td>{np_}</td><td>{clink(t, False) if t else ""}</td></tr>' for s, l, h, si, u, n, np_, t in hub)
    others = [f"{E(m)} ({n})" for m, n in allc.most_common() if m not in {x[0] for x in MAKERS}][:12]
    body = f'''<p>A small number of specialist companies design and build most roller coasters. The table covers the manufacturers with the most coasters on {BRAND}, with headquarters and founding year as listed on RCDB, and links to a page for each with every ride we cover.</p>
<div class="tablewrap"><table class="list"><thead><tr><th scope="col">Manufacturer</th><th scope="col">Based in</th><th scope="col">In business (RCDB)</th><th scope="col">Coasters on {BRAND}</th><th scope="col">Parks</th><th scope="col">Tallest we cover</th></tr></thead><tbody>{rows}</tbody></table></div>
<h2>How a coaster gets built</h2><p>A park usually chooses a manufacturer and works with its engineers on a layout that fits the site, budget and target riders. Some firms sell standard models, such as Vekoma's Boomerang or junior coasters, which are built many times; others mostly build custom layouts. The manufacturer designs the track, trains and control system, and the ride is assembled on site on new foundations. Rides are tested, often with weighted dummies in the seats, before riders board.</p>
<h2>Other manufacturers on {BRAND}</h2><p>{", ".join(others)}.</p>'''
    faqs = [("Who makes the most roller coasters?", f"Among the coasters on {BRAND}, Vekoma leads with {allc.get('Vekoma', 0)}, followed by Bolliger & Mabillard with {allc.get('Bolliger & Mabillard', 0)} and Intamin with {allc.get('Intamin Amusement Rides', 0)}, as of {CHECKED}."),
            ("What are the main roller coaster manufacturers?", "Bolliger & Mabillard, Intamin, Vekoma, Mack Rides, Gerstlauer, Rocky Mountain Construction and Premier Rides are among the best-known active manufacturers; Arrow Dynamics built many classic coasters and is listed by RCDB as defunct."),
            ("Where are B&M roller coasters made?", "RCDB lists Bolliger & Mabillard as based in Monthey, Switzerland.")]
    qpage("roller-coaster-manufacturers", f"Roller Coaster Manufacturers: B&M, Intamin, RMC & More | {BRAND}", "Who builds roller coasters: B&M, Intamin, Vekoma, Mack, Gerstlauer, RMC, Premier and Arrow, with headquarters, founding years and every ride we cover.",
          "Roller coaster manufacturers", f"most coasters come from a handful of specialists. Among the {len(ALL)} coasters on {BRAND}, Vekoma built {allc.get('Vekoma', 0)}, Bolliger & Mabillard {allc.get('Bolliger & Mabillard', 0)}, Intamin {allc.get('Intamin Amusement Rides', 0)} and Mack Rides {allc.get('Mack Rides GmbH & Co KG', 0)}.",
          body, faqs, "Who builds coasters, with every ride we cover.", sources=[RCDB_SRC], group="Manufacturers", related=[("/guides/how-do-roller-coasters-work/", "How roller coasters work"), ("/guides/roller-coaster-types/", "Roller coaster types"), ("/guides/roller-coaster-glossary/", "Roller coaster glossary")])

def build_explainers():
    fear_page(); stomach_page(); airtime_page(); work_page(); track_page(); launch_page(); brakes_page(); restraint_page(); seat_page()
    heights_explained_page(); too_tall_page(); stuck_page(); motion_page(); health_page(); records_page(); maker_pages(); glossary_page()
