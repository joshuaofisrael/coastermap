# Evergreen guide pages built only from verified site data. Exec'd inside build.py's namespace.
GUIDES = []  # (path, title, blurb, group)
REGION_PARKS = {}
REGION = {"US": "North America", "CA": "North America", "DE": "Europe", "GB": "Europe", "ES": "Europe", "NL": "Europe", "SE": "Europe", "JP": "Asia", "CN": "Asia", "HK": "Asia", "FR": "Europe"}
def pk(c): return park_of(c)
def mtr(v): return f"{round(v * 0.3048):,} m"
def kmh(v): return f"{round(v * 1.609)} km/h"
def ftm(v): return f"{ft(v)} ({mtr(v)})" if v else "n/a"
def mphk(v): return f"{mph(v)} ({kmh(v)})" if v else "n/a"
def byline(): return f'<p class="byline">By the {BRAND} editorial team · Last verified {CHECKED} · <a href="/methodology/">How we verify</a></p>'
def clink(c, park=True): return f'<a href="{coaster_path(c)}">{E(c["name"])}</a>' + (f' <span class="muted">({E(pk(c)["name"])})</span>' if park else "")
def hreq(c): return hs(c["hr"]) if c["hr"] else "not verified"
def article_ld(path, title, desc):
    return {"@context": "https://schema.org", "@type": "Article", "headline": title.split(" | ")[0], "description": desc, "url": url(path), "dateModified": TODAY,
            "author": {"@type": "Organization", "name": f"{BRAND} editorial team", "url": url("/about/")}, "publisher": {"@type": "Organization", "name": BRAND, "url": BASE_URL, "logo": {"@type": "ImageObject", "url": url("/logo.png")}}}
def itemlist_ld(name, cs):
    return {"@context": "https://schema.org", "@type": "ItemList", "name": name, "numberOfItems": len(cs),
            "itemListElement": [{"@type": "ListItem", "position": i + 1, "url": url(coaster_path(c)), "name": c["name"]} for i, c in enumerate(cs)]}
def guide(path, title, desc, h1, body_html, faqs, group, blurb, cs_for_list=None, related=()):
    if len(title) > 70: raise SystemExit("title too long: " + title)
    rel = "".join(f'<li><a href="{u}">{E(t)}</a></li>' for u, t in related)
    body = (f'<article class="guide"><h1>{E(h1)}</h1>{byline()}{body_html}{faq_html(faqs)}'
            + (f'<section aria-labelledby="rel-h"><h2 id="rel-h">Related guides</h2><ul class="cols">{rel}</ul></section>' if rel else "")
            + f'<section class="sources"><h2>How this guide is built</h2><p>Everything on this page is generated from the facts on Coaster Map: height requirements from each park\'s official page and ride statistics from the <a href="https://rcdb.com/" rel="nofollow noopener" target="_blank">Roller Coaster DataBase</a>, last verified {CHECKED}. It covers the {len(PARKS)} parks we document, not every coaster in the world. Each coaster page links its sources. See <a href="/methodology/">sources and methods</a>.</p></section></article>')
    ld = [article_ld(path, title, desc), faq_ld(faqs)] + ([itemlist_ld(h1, cs_for_list)] if cs_for_list else [])
    write(path, page(path, title, desc, body, ld, [("/", "Home"), ("/guides/", "Guides"), (path, h1)]))
    GUIDES.append((path, h1, blurb, group))

# ---------- height guides ----------
HEIGHTS = (36, 42, 48, 54)
def height_guides():
    for H in HEIGHTS:
        path = f"/guides/roller-coasters-for-{H}-inch-kids/"
        alone = [c for c in ALL if c["hr"] and hin(c["hr"]) <= H + 1e-9 and not (c["hr"].get("max") and hin(c["hr"], "max") < H)]
        comp = [c for c in ALL if c["hr"] and c["hr"].get("acc_min") and hin(c["hr"], "acc_min") <= H + 1e-9 < hin(c["hr"]) + 1e-9 and hin(c["hr"]) > H + 1e-9]
        soon = sorted([c for c in ALL if c["hr"] and H + 1e-9 < hin(c["hr"]) <= H + 2 + 1e-9 and c not in comp], key=lambda c: hin(c["hr"]))
        byp = {}
        for c in alone: byp.setdefault(c["park"], []).append(c)
        sec = ""
        for p in PARKS:
            cs = sorted(byp.get(p["slug"], []), key=lambda c: -(c["height"] or 0))
            if cs: sec += f'<h3><a href="/parks/{p["slug"]}/">{E(p["name"])}</a> ({len(cs)})</h3><ul>' + "".join(f'<li>{clink(c, False)}: minimum {hshort(c["hr"])}' + (f' (maximum {hshort(c["hr"], "max")})' if c["hr"].get("max") else "") + '</li>' for c in cs) + "</ul>"
        compl = "".join(f'<li>{clink(c)}: {rngs(c["hr"])} with a companion, {hs(c["hr"])} alone</li>' for c in sorted(comp, key=lambda c: (pk(c)["name"], c["name"])))
        soonl = "".join(f'<li>{clink(c)}: {hs(c["hr"])}</li>' for c in soon[:30])
        biggest = max(alone, key=lambda c: c["height"] or 0, default=None)
        fastest = max(alone, key=lambda c: c["speed"] or 0, default=None)
        parks_n = len(byp)
        cmH = round(H * 2.54)
        intro = f'''<p class="answer">A child who is <strong>{H} inches ({cmH} cm)</strong> tall meets the ride-alone height on <strong>{len(alone)} of the {sum(1 for c in ALL if c["hr"])} coasters</strong> with a verified height rule on Coaster Map, across {parks_n} parks. A further {len(comp)} can be ridden with a companion. The lists below are grouped by park.</p>
<p>Height rules are set by each park and the ride's manufacturer, based on how the restraint fits and the forces on the ride, not on age or bravery. A child exactly at the posted minimum can ride; a child even slightly under it will be turned away at the measuring post, so it is worth measuring at home in the shoes they will wear. Parks outside North America publish their rules in centimetres. We compare against the official centimetre figure, which is why a ride listed at 107 cm does not appear on the 42-inch list (42 inches is 106.7 cm).</p>'''
        if biggest: intro += f'<p>At {H} inches the tallest coaster on the list is {clink(biggest)} at {ftm(biggest["height"])}' + (f', and the fastest is {clink(fastest)} at {mphk(fastest["speed"])}.' if fastest and fastest is not biggest else '.') + '</p>'
        body = intro + f'<section aria-labelledby="alone-h"><h2 id="alone-h">Coasters a {H}-inch rider can ride alone</h2>{sec or "<p>None of the coasters we cover allow riders this short to ride alone.</p>"}</section>'
        if compl: body += f'<section aria-labelledby="comp-h"><h2 id="comp-h">Coasters a {H}-inch rider can ride with a companion</h2><p>These rides let shorter children ride if an older companion rides with them. The companion\'s minimum age differs by park and is given on each coaster page.</p><ul>{compl}</ul></section>'
        if soonl: body += f'<section aria-labelledby="soon-h"><h2 id="soon-h">Just out of reach: up to 2 inches more</h2><p>Coasters whose ride-alone minimum is just above {H} inches (up to {H + 2} in, about {round((H + 2) * 2.54)} cm):</p><ul>{soonl}</ul></section>'
        body += '<p>For a personal list by exact height, park and unit, use the <a href="/height-checker/">ride height checker</a>.</p>'
        faqs = [(f"How many roller coasters can a {H}-inch child ride?", f"On Coaster Map, a {H}-inch ({cmH} cm) rider meets the ride-alone minimum on {len(alone)} coasters and can ride {len(comp)} more with a companion, based on official park rules last verified {CHECKED}."),
                ("Do kids get measured with shoes on?", "Yes, parks measure guests as they arrive at the ride, normally in the shoes they are wearing. Thick soles or hairstyles that add height may be checked, and staff have the final say."),
                ("Can a child ride if they are just under the height?", "No. The posted minimum is a safety limit tied to how the restraint fits, so ride staff do not make exceptions. Some family coasters offer a lower limit when riding with a companion; those are listed separately above.")]
        if biggest: faqs.append((f"What is the biggest coaster a {H}-inch child can ride?", f"By height, {biggest['name']} at {pk(biggest)['name']}, which is {ft(biggest['height'])} tall (RCDB) with a ride-alone minimum of {hshort(biggest['hr'])}."))
        title = f"Roller Coasters a {H}-Inch ({cmH} cm) Child Can Ride | {BRAND}"
        desc = f"Every coaster a {H}-inch ({cmH} cm) child can ride alone or with a companion at {parks_n} theme parks, from official height rules."
        rel = [(f"/guides/roller-coasters-for-{x}-inch-kids/", f"Coasters for {x}-inch kids") for x in HEIGHTS if x != H] + [("/guides/best-first-roller-coasters/", "Best first roller coasters")]
        guide(path, title, desc, f"Roller coasters a {H}-inch ({cmH} cm) child can ride", body, faqs, "By height", f"What a {H}-inch ({cmH} cm) rider can ride, park by park.", alone[:100] if len(alone) <= 100 else None, rel)

# ---------- record rankings ----------
RANK = [
 ("tallest", "height", "Tallest", "height", lambda c: ftm(c["height"]), "Height is the coaster's highest point above the ground, as listed on RCDB. A coaster with a drop into a trench or tunnel can have a longer drop than its height.", "tall"),
 ("fastest", "speed", "Fastest", "top speed", lambda c: mphk(c["speed"]), "Top speed is the maximum speed listed on RCDB, usually reached at the bottom of the first drop or the end of a launch.", "fast"),
 ("longest", "length", "Longest", "track length", lambda c: ftm(c["length"]), "Track length is the length of the circuit listed on RCDB. Long coasters are not always the longest rides; launches, brakes and lift speeds change the ride time.", "long"),
 ("most-inversions", "inversions", "Most inversions on", "inversions", lambda c: str(c["inversions"]), "An inversion is any point where riders turn upside down, such as a loop, corkscrew, cobra roll or zero-g roll. The count is from RCDB.", "inv"),
 ("steepest", "angle", "Steepest", "drop angle", lambda c: f'{c["angle"]}°', "Drop angle is the steepest angle of descent listed on RCDB. Anything over 90 degrees is a beyond-vertical drop that curls back under the hill.", "steep"),
]
def ranking_guides():
    for slug, key, word, label, fmt, expl, _ in RANK:
        cs = sorted([c for c in ALL if c[key]], key=lambda c: (-c[key], c["name"]))
        top = cs[:25]
        path = f"/guides/{slug}-roller-coasters/" if slug != "most-inversions" else "/guides/roller-coasters-with-the-most-inversions/"
        rows = "".join(f'<tr><td>{i + 1}</td><th scope="row"><a href="{coaster_path(c)}">{E(c["name"])}</a></th><td>{E(pk(c)["name"])}</td><td>{E(fmt(c))}</td><td>{E(hreq(c))}</td></tr>' for i, c in enumerate(top))
        reg = ""
        for r in ("North America", "Europe", "Asia"):
            rc = [c for c in cs if REGION.get(pk(c)["country"]) == r]
            if rc: reg += f'<li>{r}: {clink(rc[0])}, {E(fmt(rc[0]))}</li>'
        lead = top[0]
        H1 = f"{word} roller coasters" if slug != "most-inversions" else "Roller coasters with the most inversions"
        body = f'''<p class="answer">The {"coaster with the most inversions" if slug == "most-inversions" else word.lower() + " roller coaster"} on Coaster Map is <strong>{clink(lead)}</strong> at <strong>{E(fmt(lead))}</strong>. Below are the top {len(top)} of the {len(cs)} coasters we cover that have a {label} figure on RCDB, with each ride's height requirement so you can see who can ride.</p>
<p>{expl} Records change slowly, but they do change when a park opens a new ride or a record holder closes, so check the date at the top of this guide.</p>
<section aria-labelledby="top-h"><h2 id="top-h">Top {len(top)} by {label}</h2><div class="tablewrap"><table class="list"><thead><tr><th scope="col">Rank</th><th scope="col">Coaster</th><th scope="col">Park</th><th scope="col">{E(label.capitalize())}</th><th scope="col">Height requirement</th></tr></thead><tbody>{rows}</tbody></table></div></section>
<section aria-labelledby="reg-h"><h2 id="reg-h">Leader by region</h2><ul>{reg}</ul></section>'''
        tall_kid = min((c for c in top if c["hr"]), key=lambda c: hin(c["hr"]), default=None)
        faqs = [(f"What is the {word.lower()} roller coaster on Coaster Map?" if slug != "most-inversions" else "Which roller coaster has the most inversions on Coaster Map?", f"{lead['name']} at {pk(lead)['name']}, with a {label} of {fmt(lead)} according to RCDB, last verified {CHECKED}.")]
        if tall_kid: faqs.append((f"Which of these coasters has the lowest height requirement?", f"Of the top {len(top)}, {tall_kid['name']} at {pk(tall_kid)['name']} has the lowest ride-alone minimum, {hs(tall_kid['hr'])}."))
        faqs.append(("Is this every coaster in the world?", f"No. It ranks the {len(cs)} coasters with a {label} figure at the {len(PARKS)} parks Coaster Map covers. RCDB lists records for every coaster worldwide."))
        TT = H1.replace("roller coasters", "Roller Coasters").replace("with the most inversions", "With the Most Inversions")
        title = f"{TT}: Top {len(top)} Ranked | {BRAND}" if len(f"{TT}: Top {len(top)} Ranked | {BRAND}") <= 70 else f"{TT} | {BRAND}"
        desc = f"The {len(top)} {H1.lower()} at {len(PARKS)} major theme parks, ranked by {label} from RCDB, with height requirements for each."
        rel = [(f"/guides/{s}-roller-coasters/" if s != "most-inversions" else "/guides/roller-coasters-with-the-most-inversions/", (f"{w} roller coasters" if s != "most-inversions" else "Most inversions")) for s, _, w, *_ in RANK if s != slug] + [("/guides/most-intense-roller-coasters/", "Most intense roller coasters")]
        guide(path, title, desc, H1, body, faqs, "Records", f"Top {len(top)} by {label}.", top, rel)

def intense_guide():
    cs = sorted([c for c in ALL if c["gforce"]], key=lambda c: (-c["gforce"], -(c["speed"] or 0)))[:25]
    ext = [c for c in ALL if c["scale"] == "Extreme"]
    rows = "".join(f'<tr><td>{i + 1}</td><th scope="row"><a href="{coaster_path(c)}">{E(c["name"])}</a></th><td>{E(pk(c)["name"])}</td><td>{c["gforce"]} g</td><td>{E(mphk(c["speed"]))}</td><td>{c["inversions"] if c["inversions"] is not None else "n/a"}</td><td>{E(hreq(c))}</td></tr>' for i, c in enumerate(cs))
    steep = sorted([c for c in ALL if c["angle"] and c["angle"] > 90], key=lambda c: -c["angle"])
    body = f'''<p class="answer">"Scary" means different things to different riders, so this guide uses measurable signs of intensity. By the peak g-force RCDB lists, the most intense coaster on Coaster Map is <strong>{clink(cs[0])}</strong> at <strong>{cs[0]["gforce"]} g</strong>. RCDB classes {len(ext)} of the {len(ALL)} coasters we cover as "extreme".</p>
<p>G-force measures how hard the ride pushes you into your seat; 1 g is what you feel standing still. Sustained forces of 4 g or more are what make some riders grey out briefly in the bottom of a loop. Other things that make a ride feel intense are not captured by one number: a beyond-vertical drop, long stretches of airtime that lift you out of the seat, riding in the dark, or having your legs dangle with nothing underneath. Many of the most frightening rides for first-timers are not the fastest; anticipation, height and the unknown do most of the work.</p>
<section aria-labelledby="g-h"><h2 id="g-h">Highest g-forces</h2><div class="tablewrap"><table class="list"><thead><tr><th scope="col">Rank</th><th scope="col">Coaster</th><th scope="col">Park</th><th scope="col">Peak g-force</th><th scope="col">Top speed</th><th scope="col">Inversions</th><th scope="col">Height requirement</th></tr></thead><tbody>{rows}</tbody></table></div><p class="note">Only coasters with a g-force figure on RCDB are ranked.</p></section>'''
    if steep: body += '<section aria-labelledby="st-h"><h2 id="st-h">Beyond-vertical drops</h2><p>These coasters drop at more than 90 degrees, so the track curls back under the top of the hill:</p><ul>' + "".join(f'<li>{clink(c)}: {c["angle"]}°</li>' for c in steep) + "</ul></section>"
    body += '<section aria-labelledby="tip-h"><h2 id="tip-h">How to work up to the big ones</h2><p>Most riders build up in steps: a family coaster with no inversions, then a coaster with one or two smooth inversions, then a hypercoaster with airtime, then launches and the highest g-forces. Riding in the middle of the train softens both the drop and the airtime; the back row is the most intense on most drops and the front gives the best view. Our <a href="/guides/best-first-roller-coasters/">first coasters guide</a> lists gentle starting points at every park.</p></section>'
    faqs = [("What is the most intense roller coaster on Coaster Map?", f"By RCDB's listed peak g-force, {cs[0]['name']} at {pk(cs[0])['name']}, at {cs[0]['gforce']} g."),
            ("What makes a roller coaster scary?", "Height, steep or beyond-vertical drops, strong g-forces, airtime that lifts you from the seat, darkness and open-feeling seats such as wing, floorless and inverted coasters. Speed alone matters less than most people expect."),
            ("Where is the most intense seat?", "On most coasters the back row feels the strongest over the first drop and airtime hills, because the train pulls the rear cars over the crest at speed. The front row gives the clearest view. The middle is the gentlest.")]
    guide("/guides/most-intense-roller-coasters/", f"Most Intense Roller Coasters by G-Force | {BRAND}", f"The most intense roller coasters at {len(PARKS)} major theme parks, ranked by peak g-force from RCDB, with beyond-vertical drops and height rules.", "Most intense roller coasters", body, faqs, "Records", "Ranked by peak g-force, plus beyond-vertical drops.", cs, [("/guides/tallest-roller-coasters/", "Tallest roller coasters"), ("/guides/fastest-roller-coasters/", "Fastest roller coasters"), ("/guides/steepest-roller-coasters/", "Steepest roller coasters"), ("/guides/best-first-roller-coasters/", "Best first roller coasters")])

def first_timer_guide():
    sec = ""; picks_all = []
    for p in PARKS:
        cands = [c for c in p["coasters"] if c["hr"] and c["inversions"] == 0 and c["scale"] in ("Kiddie", "Family")]
        cands.sort(key=lambda c: (hin(c["hr"]), c["speed"] or 0))
        picks = cands[:2]
        if not picks:
            cands = [c for c in p["coasters"] if c["hr"] and c["inversions"] == 0]
            cands.sort(key=lambda c: (c["speed"] or 99, hin(c["hr"])))
            picks = cands[:1]
        if picks:
            picks_all += picks
            sec += f'<h3><a href="/parks/{p["slug"]}/">{E(p["name"])}</a></h3><ul>' + "".join(f'<li>{clink(c, False)}: {hshort(c["hr"])} minimum, ' + (f'{mphk(c["speed"])}, ' if c["speed"] else "") + 'no inversions</li>' for c in picks) + "</ul>"
    body = f'''<p class="answer">The best first roller coaster is a family coaster with <strong>no inversions, a low height requirement and a modest top speed</strong>. Below we pick up to two at each of the {len(PARKS)} parks we cover, chosen only from verified facts: no inversions on RCDB, RCDB's kiddie or family class where available, then the lowest official height requirement.</p>
<h2>What makes a good first coaster</h2><p>First-time and nervous riders usually do best on rides that build confidence: a short lift, gentle curves and small drops, a lap bar rather than an over-the-shoulder restraint, and no inversions. Mine train and family coasters are designed for exactly this. Watching the ride from the queue for a few cycles helps, as does picking a ride with a short queue so the wait does not build anticipation.</p>
<h2>Tips for nervous riders</h2><ul><li>Sit in the middle of the train, where drops and airtime feel softest.</li><li>Keep your head back against the headrest and hold the lap bar or grab handles, and breathe out on the drops.</li><li>Ride during the day; dark sections and night rides feel faster.</li><li>Step up gradually: a family coaster, then one with a single smooth inversion, then bigger rides.</li><li>If you change your mind in the queue, tell a team member; many coasters have an exit before the boarding platform.</li></ul>
<section aria-labelledby="picks-h"><h2 id="picks-h">First coaster picks at each park</h2>{sec}</section>'''
    faqs = [("What is a good first roller coaster for a child?", "A family coaster with no inversions and a height requirement your child clearly meets. Each park's pick above meets those criteria, using official height rules."),
            ("Are roller coasters with no inversions less scary?", "Usually, yes. Going upside down is the step many first-timers fear most, though a coaster can still be intense through height, speed or airtime without any inversions."),
            ("Which seat is least scary?", "The middle of the train. The front gives a full view of the drop and the back is whipped over hills fastest, so the middle feels the gentlest on most coasters.")]
    guide("/guides/best-first-roller-coasters/", f"Best First Roller Coasters for Kids and Nervous Riders | {BRAND}"[:200], f"Gentle first roller coasters at {len(PARKS)} theme parks: no inversions, low height rules and modest speeds, from verified data.", "Best first roller coasters for kids and nervous riders", body, faqs, "For families", "Gentle starter coasters at every park, plus tips.", None, [("/guides/roller-coasters-for-42-inch-kids/", "Coasters for 42-inch kids"), ("/guides/roller-coasters-for-48-inch-kids/", "Coasters for 48-inch kids"), ("/guides/what-is-a-family-roller-coaster/", "What is a family roller coaster?"), ("/guides/most-intense-roller-coasters/", "Most intense roller coasters")])

# ---------- regions ----------
STATES = {"FL": "Florida", "CA": "California", "PA": "Pennsylvania", "TX": "Texas", "MO": "Missouri", "OH": "Ohio", "VA": "Virginia"}
COUNTRIES = {"GB": "the United Kingdom", "DE": "Germany", "ES": "Spain", "JP": "Japan", "FR": "France", "CA": "Canada"}
def region_guides():
    groups = [(f"roller-coasters-in-{n.lower()}", n, [p for p in PARKS if p["country"] == "US" and p["state"] == s]) for s, n in STATES.items()]
    groups += [(f"roller-coasters-in-{n.replace('the ', '').lower().replace(' ', '-')}", n, [p for p in PARKS if p["country"] == k]) for k, n in COUNTRIES.items()]
    for slug, name, ps in groups:
        if len(ps) < 2: continue
        cs = [c for p in ps for c in p["coasters"]]
        tall = max((c for c in cs if c["height"]), key=lambda c: c["height"]); fast = max((c for c in cs if c["speed"]), key=lambda c: c["speed"])
        low = min((c for c in cs if c["hr"]), key=lambda c: hin(c["hr"]), default=None)
        most = max(ps, key=lambda p: len(p["coasters"]))
        inv = max((c for c in cs if c["inversions"]), key=lambda c: c["inversions"], default=None)
        wood = [c for c in cs if c["material"] == "Wood"]
        Name = name[0].upper() + name[1:]
        plist = "".join(f'<li><a href="/parks/{p["slug"]}/">{E(p["name"])}</a> ({E(p["loc"])}): {len(p["coasters"])} coaster{"s" if len(p["coasters"]) != 1 else ""}</li>' for p in sorted(ps, key=lambda p: -len(p["coasters"])))
        body = f'''<p class="answer">Coaster Map covers <strong>{len(cs)} roller coasters at {len(ps)} parks in {E(name)}</strong>. The tallest is {clink(tall)} at {ftm(tall["height"])} and the fastest is {clink(fast)} at {mphk(fast["speed"])}.''' + (f' The lowest height requirement is {hs(low["hr"])}, on {clink(low)}.' if low else "") + f'''</p>
<p>{E(most["name"])} has the most coasters of the {E(name)} parks we cover, with {len(most["coasters"])}.''' + (f' The coaster with the most inversions is {clink(inv)}, with {inv["inversions"]}.' if inv else "") + (f' {len(wood)} of the coasters are wooden.' if wood else " None of them are wooden.") + f''' Use the park guides for maps, the full height lists and where to sit on each ride.</p>
<section aria-labelledby="pl-h"><h2 id="pl-h">Theme parks in {E(name)} on Coaster Map</h2><ul>{plist}</ul></section>
<section aria-labelledby="all-h"><h2 id="all-h">Every coaster we cover in {E(name)}</h2>{coaster_table(sorted(cs, key=lambda c: -(c["height"] or 0)), show_park=True)}</section>'''
        faqs = [(f"How many roller coasters are in {name}?", f"Coaster Map covers {len(cs)} operating roller coasters at {len(ps)} major parks in {name}, from RCDB's operating lists last verified {CHECKED}. Smaller parks and fairs add more."),
                (f"What is the tallest roller coaster in {name}?", f"Of the parks we cover, {tall['name']} at {pk(tall)['name']}, at {ft(tall['height'])} tall (RCDB)."),
                (f"What is the fastest roller coaster in {name}?", f"Of the parks we cover, {fast['name']} at {pk(fast)['name']}, with a top speed of {mph(fast['speed'])} (RCDB)."),
                (f"Which park in {name} has the most roller coasters?", f"Of the parks we cover, {most['name']}, with {len(most['coasters'])} operating coasters.")]
        path = f"/guides/{slug}/"
        title = f"Roller Coasters in {Name}: Parks, Heights & Records | {BRAND}"
        if len(title) > 70: title = f"Roller Coasters in {Name} | {BRAND}"
        rel = [(f"/guides/{s}/", f"Roller coasters in {n}") for s, n, pp in groups if s != slug and len(pp) >= 2][:6]
        REGION_PARKS[path] = {p["slug"] for p in ps}
        guide(path, title, f"All {len(cs)} roller coasters at {len(ps)} major theme parks in {name}, with the tallest, fastest and lowest height requirements.", f"Roller coasters in {name}", body, faqs, "By place", f"{len(cs)} coasters at {len(ps)} parks.", None, rel)

# ---------- coaster types / glossary ----------
def launched(c): return bool(c["model"] and re.search(r"Launch|Accelerator|Impulse|Sky Rocket|Catapult", c["model"]))
TYPES = [
 ("what-is-a-wooden-roller-coaster", "wooden roller coaster", lambda c: c["material"] == "Wood",
  "A wooden roller coaster runs on a track built from layers of laminated wood, with steel running plates for the wheels, usually on a wooden or steel support structure. Wooden coasters were the first kind of modern coaster and many classics from the 1920s still operate.",
  "Wooden track flexes slightly, so wooden coasters feel looser and louder than steel: lateral jolts in the turns, a rattling roar and sudden pops of airtime over the hills. Riders love them for that wild, out-of-control feeling; others find them rough.",
  "Most wooden coasters suit riders who like airtime more than inversions. Very few wooden coasters go upside down."),
 ("what-is-a-hybrid-roller-coaster", "hybrid roller coaster", lambda c: "Hybrid" in c["tags"],
  "A hybrid roller coaster combines a wooden-style structure with steel track, or replaces an old wooden track with a steel rail system such as I-Box or Topper track. RCDB tags these rides as hybrid.",
  "Hybrids keep the out-of-control feel and airtime of a wooden coaster but run far smoother, which lets designers add steep drops, overbanked turns and even inversions that a traditional wooden track could not handle.",
  "If you enjoy airtime but find classic wooden coasters too rough, a hybrid is a good next step."),
 ("what-is-a-launch-coaster", "launch coaster", launched,
  "A launch coaster starts with a burst of speed instead of a slow lift hill. Hydraulic, pneumatic or electromagnetic (LSM or LIM) systems accelerate the train along a straight section of track, sometimes from a standstill to highway speed in a couple of seconds. Our examples are coasters whose RCDB model name identifies a launch system.",
  "The launch pushes you back into the seat and takes away the slow build-up of a lift hill. Some launch coasters have several launches, launch backwards, or launch straight up a vertical tower and drop back down.",
  "Many riders find the launch less scary than a big lift hill because it is over so quickly; others find the sudden acceleration the most intense part of any ride."),
 ("what-is-a-hypercoaster", "hypercoaster", lambda c: c["height"] and c["height"] >= 200,
  "A hypercoaster is a roller coaster with a height or drop of at least 200 feet (about 61 m). Coasters between 300 and 399 feet are often called giga coasters, and those 400 feet or taller strata coasters. Hypercoasters are built for speed and airtime rather than inversions. Our examples are coasters at least 200 feet tall on RCDB.",
  "Expect a long, tall lift or launch, a huge first drop and a series of hills that lift you out of your seat. Most use lap bars so the airtime feels stronger.",
  "Hypercoasters are big but often smooth; riders who are fine with height and speed but not inversions often love them."),
 ("what-is-an-inverted-roller-coaster", "inverted roller coaster", lambda c: "Inverted" in c["tags"],
  "On an inverted roller coaster the train runs below the track, with the seats hanging from the wheel carriers and riders' feet dangling freely. RCDB tags these as inverted. They usually include several loops, rolls and corkscrews.",
  "With nothing below your feet the ride feels more exposed and the inversions swing you around the track rather than over it. Ride positions on the outside of each row feel the most open.",
  "Inverted coasters suit riders already comfortable going upside down. Family inverted coasters without inversions also exist."),
 ("what-is-a-wing-coaster", "wing coaster", lambda c: "Wing" in c["tags"],
  "On a wing coaster the seats sit on either side of the track, like the wings of a plane, with nothing above or below the riders. RCDB tags these as wing coasters.",
  "Wing seats give a feeling of flying beside the track, and the slow rolls and near-miss elements, such as passing close to a building or rock, make the most of it. The outer seats feel the most exposed.",
  "Wing coasters usually feel smooth and graceful rather than violent, though most still go upside down."),
 ("what-is-a-flying-roller-coaster", "flying roller coaster", lambda c: "Flying" in c["tags"],
  "A flying roller coaster holds riders lying face down, parallel to the track, like Superman flying. Riders board sitting up and the seats tilt forward before the lift. RCDB tags these as flying.",
  "Lying face down gives a strong sensation of flying through the turns, and a pretzel loop (diving down into a loop while lying on your back or front) can bring some of the strongest g-forces on any ride.",
  "Flying coasters suit riders who are comfortable with inversions and the unusual position; the harness and vest hold you firmly."),
 ("what-is-a-dive-coaster", "dive coaster", lambda c: bool(c["model"] and "Dive" in c["model"]),
  "A dive coaster has wide trains with few rows that pause at the top of a vertical or near-vertical drop, holding riders over the edge for a few seconds before releasing them. Our examples are coasters with a dive coaster model on RCDB.",
  "The hold at the edge is the defining moment: riders look straight down before the drop. After that, dive coasters are usually smooth, with big turns and an immelmann or two.",
  "Riders who dread the first drop find the pause the hardest part; once past it, dive coasters are gentle on the body."),
 ("what-is-a-spinning-roller-coaster", "spinning roller coaster", lambda c: "Spinning Cars" in c["tags"],
  "On a spinning roller coaster each car can rotate freely on its own axis as it travels along the track, so riders spin depending on the weight in the car and the forces in each turn. RCDB tags these as having spinning cars.",
  "No two rides feel quite the same: a car loaded unevenly spins more. Spinning coasters are usually compact with tight turns and small drops.",
  "They suit families and riders who enjoy spinning rides; those who get motion sick should be cautious."),
 ("what-is-a-wild-mouse-coaster", "wild mouse coaster", lambda c: "Wild Mouse" in c["tags"],
  "A wild mouse coaster uses small, single cars on a compact track with sharp, unbanked hairpin turns and short steep drops. RCDB tags these rides as wild mouse.",
  "Because the cars hang out over the track before turning, riders feel as though the car will run off the edge at each corner. The drops are short but sudden.",
  "A classic family-to-thrill step up: no inversions, but more jolting than most family coasters."),
 ("what-is-a-family-roller-coaster", "family roller coaster", lambda c: c["scale"] == "Family",
  "A family roller coaster is designed so children and adults can ride together: a lower height requirement, moderate speeds and drops, and usually no inversions. RCDB classes each coaster on a scale of kiddie, family, thrill or extreme; our examples are those RCDB classes as family.",
  "Family coasters range from gentle mine trains to fast launches with small inversions, so check the stats and height rule on each ride's page.",
  "They are the best place for a first coaster and for mixed groups."),
 ("what-is-a-shuttle-roller-coaster", "shuttle roller coaster", lambda c: "Shuttle" in c["tags"],
  "A shuttle roller coaster does not complete a full circuit. The train runs forwards through the course and then back through it in reverse, as on a Boomerang, or launches up a tower and falls back. RCDB tags these as shuttle coasters.",
  "Riding the same elements backwards is disorienting because you cannot see what is coming. Shuttle coasters are usually short but intense.",
  "Riders who dislike surprises may prefer a conventional circuit coaster."),
]
def type_guides():
    for slug, name, test, d1, d2, d3 in TYPES:
        cs = [c for c in ALL if test(c)]
        if len(cs) < 3: continue
        hrs = [c for c in cs if c["hr"]]
        lo = min(hrs, key=lambda c: hin(c["hr"]), default=None); hi = max(hrs, key=lambda c: hin(c["hr"]), default=None)
        tall = max((c for c in cs if c["height"]), key=lambda c: c["height"], default=None); fast = max((c for c in cs if c["speed"]), key=lambda c: c["speed"], default=None)
        art = "an" if name[0] in "aeiou" else "a"
        body = f'''<p class="answer">{E(d1)}</p>
<h2>What it feels like</h2><p>{E(d2)}</p><h2>Who it suits</h2><p>{E(d3)}</p>
<h2>{E(name.capitalize())}s by the numbers</h2><p>Coaster Map covers <strong>{len(cs)} {E(name)}s</strong> at {len({c["park"] for c in cs})} parks.''' + (f' Height requirements range from {hs(lo["hr"])} on {clink(lo)} to {hs(hi["hr"])} on {clink(hi)}.' if lo and hi and lo is not hi else "") + (f' The tallest is {clink(tall)} at {ftm(tall["height"])}' if tall else "") + (f' and the fastest is {clink(fast)} at {mphk(fast["speed"])}.' if fast else ".") + f'''</p>
<section aria-labelledby="ex-h"><h2 id="ex-h">Every {E(name)} on Coaster Map</h2>{coaster_table(sorted(cs, key=lambda c: -(c["height"] or 0)), show_park=True)}</section>'''
        faqs = [(f"What is {art} {name}?", d1), (f"What does {art} {name} feel like?", d2)]
        if lo: faqs.append((f"What is the lowest height requirement for {art} {name}?", f"Of the {name}s we cover, {lo['name']} at {pk(lo)['name']} has the lowest ride-alone minimum, {hs(lo['hr'])}."))
        title = f"What Is {art} {name.title()}? Explained, With Examples | {BRAND}"
        if len(title) > 70: title = f"What Is {art} {name.title()}? | {BRAND}"
        rel = [(f"/guides/{s}/", f"What is {('an' if n[0] in 'aeiou' else 'a')} {n}?") for s, n, *_ in TYPES if s != slug][:8] + [("/guides/roller-coaster-types/", "All roller coaster types")]
        guide(f"/guides/{slug}/", title, f"What {art} {name} is, what it feels like and who it suits, with all {len(cs)} examples on Coaster Map and their height rules.", f"What is {art} {name}?", body, faqs, "Coaster types", f"{len(cs)} examples, with height rules.", None, rel)

def types_hub():
    items = [(u, t, b) for u, t, b, g in GUIDES if g == "Coaster types"]
    body = '<p class="answer">Roller coasters are grouped by what the track is made of, how the train gets its speed, and how riders sit. This page links our plain-English explainer for each type, with every example we cover and its height requirement.</p><h2>Track material</h2><p>Wooden coasters run on laminated wood track and feel loose and lively; steel coasters run on tubular or box steel track and allow smooth inversions; hybrids mix the two.</p><h2>How the ride starts</h2><p>Most coasters use a chain or cable lift hill. Launch coasters fire the train along the track instead, and shuttle coasters run the course forwards and then backwards.</p><h2>How you sit</h2><p>Sit-down coasters are the most common. On inverted coasters you hang below the track, on wing coasters you sit beside it, on flying coasters you lie face down, and on spinning coasters your car rotates.</p><h2>Explainers</h2><ul>' + "".join(f'<li><a href="{u}">{E(t)}</a>: {E(b)}</li>' for u, t, b in items) + "</ul>"
    faqs = [("What are the main types of roller coaster?", "By material: wooden, steel and hybrid. By how they start: lift hill, launch or shuttle. By seating: sit-down, inverted, wing, flying, floorless, stand-up, dive and spinning. Size classes include hyper (200 ft or more), giga (300 ft or more) and strata (400 ft or more) coasters."),
            ("Which type of roller coaster is the least intense?", "Family coasters and mine trains, which usually have no inversions and low height requirements.")]
    guide("/guides/roller-coaster-types/", f"Roller Coaster Types Explained: A Plain-English Guide | {BRAND}", "Wooden, hybrid, launch, hyper, inverted, wing, flying, dive, spinning, wild mouse, family and shuttle coasters explained, with examples.", "Roller coaster types explained", body, faqs, "Coaster types hub", "Every type, explained.", None, [])

def guides_hub():
    order = ["By height", "For families", "Records", "By place", "Coaster types hub", "Coaster types"]
    names = {"By height": "Height requirement guides", "For families": "For families and first-timers", "Records": "Records and rankings", "By place": "Roller coasters by state and country", "Coaster types hub": "Roller coaster types", "Coaster types": "Type explainers"}
    sec = ""
    for g in order:
        items = [x for x in GUIDES if x[3] == g]
        if items: sec += f'<section><h2>{names[g]}</h2><ul>' + "".join(f'<li><a href="{u}">{E(t)}</a>: {E(b)}</li>' for u, t, b, _ in items) + "</ul></section>"
    body = f'<h1>Roller coaster guides</h1>{byline()}<p class="answer">Answers to the questions people ask before a park day: what a child of a given height can ride, which coasters are the tallest, fastest and most intense, where to start if you are nervous, and what each type of coaster is like. Every guide is built from the official height rules and RCDB statistics on Coaster Map, so each fact links back to its source.</p>{sec}'
    write("/guides/", page("/guides/", f"Roller Coaster Guides: Heights, Records & Types | {BRAND}", "Evergreen roller coaster guides: height requirements by child height, tallest and fastest coasters, first-timer picks, coasters by state and coaster types explained.", body, None, [("/", "Home"), ("/guides/", "Guides")]))

def type_links(c):
    out = []
    for slug, name, test, *_ in TYPES:
        if any(s == f"/guides/{slug}/" for s, *_ in GUIDES) and test(c): out.append((f"/guides/{slug}/", f"What is {('an' if name[0] in 'aeiou' else 'a')} {name}?"))
    return out
def build_guides():
    height_guides(); ranking_guides(); intense_guide(); first_timer_guide(); region_guides(); type_guides(); types_hub(); guides_hub()
