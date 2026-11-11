#!/usr/bin/env python3
"""Coaster Map static site builder. Run from repo root: python3 _build/build.py"""
import os, json, html, datetime, re, sys
sys.path.insert(0, os.path.dirname(__file__))
from data import load, CHECKED, slugify
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BASE_URL = "https://coastermap.com/"
BRAND = "Coaster Map"
TODAY = "2026-11-10"
INDEXNOW_KEY = "fe204aafdcd4bf6d890c7776842749c0"
CF_BEACON_TOKEN = "eac63f2b5dbc4539a2d95249baab6472"  # shared JI Ventures Analytics 2 token, requestHost match (both CF accounts at site limit)
GSC_TOKEN = ""  # Search Console HTML tag content, optional (Domain property via DNS TXT preferred)
SIGNUP_ENDPOINT = "https://coastermap-signups.joshofisrael.workers.dev/subscribe"
FORM_ENDPOINT = "https://formsubmit.co/4497ee41a1200e746e967998473d21da"
LEGAL_LINE = "© 2026 Joshua Israel Ventures LLC. All rights reserved. Coaster Map is a trade name of Joshua Israel Ventures LLC, a Florida limited liability company."
E = html.escape
PARKS = load()
ALL = [c for p in PARKS for c in p["coasters"]]
PAGES = []  # (path, lastmod)

def url(path): return BASE_URL + path.lstrip("/")
def write(path, content):
    fp = os.path.join(ROOT, path.lstrip("/"))
    if path.endswith("/"): fp = os.path.join(fp, "index.html")
    os.makedirs(os.path.dirname(fp), exist_ok=True)
    open(fp, "w").write(content)

NAV = [("/", "Home"), ("/parks/", "Parks"), ("/map/", "Coaster map"), ("/height-checker/", "Height checker"), ("/guides/", "Guides"), ("/quiz/", "Coaster quiz"), ("/coasters/", "All coasters")]
LOGO = '<svg width="34" height="34" viewBox="0 0 64 64" aria-hidden="true" focusable="false"><rect width="64" height="64" rx="14" fill="#fca311"/><path d="M6 46 C14 10, 22 10, 28 34 S40 58, 46 22 S56 18, 58 30" fill="none" stroke="#14213d" stroke-width="5" stroke-linecap="round"/><circle cx="46" cy="22" r="4" fill="#b3001b"/></svg>'

def signup_box():
    return f'''<section class="signup" aria-labelledby="signup-h"><h2 id="signup-h">New coaster alerts</h2>
<p>Get a short email when we add a park or a new coaster opens. No spam; unsubscribe anytime.</p>
<form class="signup-form" action="{SIGNUP_ENDPOINT}" method="POST">
<label for="su-email" class="vh">Email address</label><input id="su-email" type="email" name="email" required autocomplete="email" placeholder="you@example.com">
<input type="text" name="company" class="hp" tabindex="-1" autocomplete="off" aria-hidden="true">
<label class="consent"><input type="checkbox" name="consent" value="yes" required> Email me new-coaster alerts from Coaster Map. I can unsubscribe anytime (see our <a href="/privacy/">privacy policy</a>).</label>
<button class="btn" type="submit">Sign up</button><p class="form-status" role="status" hidden></p></form></section>'''

def clip_desc(d, n=158):
    if len(d) <= n: return d
    cut = d[:n]; i = cut.rfind(". ")
    if i > 90: return cut[:i + 1]
    return cut[:cut.rfind(" ")].rstrip(",;:") + "."
def page(path, title, desc, body, jsonld=None, crumbs=None, extra_head="", modified=TODAY, noindex=False, legal=False):
    desc = clip_desc(desc)
    canon = url(path)
    if not noindex: PAGES.append((path, modified))
    ld = [{"@context": "https://schema.org", "@type": "WebSite", "name": BRAND, "url": BASE_URL,
           "publisher": {"@type": "Organization", "name": BRAND, "url": BASE_URL, "logo": url("/logo.png")}}] if path == "/" else []
    if crumbs:
        ld.append({"@context": "https://schema.org", "@type": "BreadcrumbList", "itemListElement": [
            {"@type": "ListItem", "position": i + 1, "name": n, "item": url(u)} for i, (u, n) in enumerate(crumbs)]})
    if jsonld: ld += jsonld if isinstance(jsonld, list) else [jsonld]
    ldhtml = "".join(f'<script type="application/ld+json">{json.dumps(x, ensure_ascii=False)}</script>' for x in ld)
    nav = "".join(f'<a href="{u}"' + (' aria-current="page"' if u == path else "") + f'>{n}</a>' for u, n in NAV)
    bc = ""
    if crumbs:
        bc = '<nav class="crumbs" aria-label="Breadcrumb"><ol>' + "".join(
            (f'<li><a href="{u}">{E(n)}</a></li>' if i < len(crumbs) - 1 else f'<li aria-current="page">{E(n)}</li>') for i, (u, n) in enumerate(crumbs)) + "</ol></nav>"
    gsc = f'<meta name="google-site-verification" content="{GSC_TOKEN}">' if (GSC_TOKEN and path == "/") else ""
    beacon = f"<!-- Cloudflare Web Analytics --><script defer src='https://static.cloudflareinsights.com/beacon.min.js' data-cf-beacon='{{\"token\": \"{CF_BEACON_TOKEN}\"}}'></script><!-- End Cloudflare Web Analytics -->" if CF_BEACON_TOKEN else ""
    return f'''<!doctype html>
<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<title>{E(title)}</title><meta name="description" content="{E(desc)}"><link rel="canonical" href="{canon}">
<meta name="robots" content="{"noindex" if noindex else "index, follow, max-image-preview:large"}">
<meta property="og:type" content="website"><meta property="og:site_name" content="{BRAND}"><meta property="og:title" content="{E(title)}"><meta property="og:description" content="{E(desc)}"><meta property="og:url" content="{canon}"><meta property="og:image" content="{url('/og.png')}"><meta name="twitter:card" content="summary_large_image">
<link rel="icon" href="/favicon.svg" type="image/svg+xml"><link rel="stylesheet" href="/assets/style.css?v=2">{gsc}{extra_head}{ldhtml}
</head><body><a class="skip" href="#main">Skip to content</a>
<header class="site"><div class="wrap"><a class="brand" href="/">{LOGO}<span>{BRAND}</span></a><nav class="main" aria-label="Main">{nav}</nav></div></header>
<main id="main" class="wrap">{bc}{body}<!-- ad-slot: below-content (reserved for future use; no ad code) -->{signup_box()}</main>
<footer class="site"><div class="wrap"><p class="fbrand"><strong>{BRAND}</strong>: roller coasters at the big theme parks, mapped and explained with height requirements and stats from official park pages and the Roller Coaster DataBase. Not affiliated with any park. Ride rules change, so always check with the park.</p>
<section class="contact-us" aria-labelledby="contact-us"><h2 id="contact-us">Contact us</h2><p>Corrections, questions or a park you want next? Use our <a href="/contact/">contact form</a>.</p></section>
<p class="flinks"><a href="/about/">About</a> | <a href="/methodology/">Sources and methods</a> | <a href="/terms/">Terms of use</a> | <a href="/privacy/">Privacy</a> | <a href="/disclaimer/">Disclaimer</a> | <a href="/ad-disclosure/">Advertising disclosure</a> | <a href="/copyright/">Copyright and DMCA</a> | <a href="/credits/">Credits</a> | <a href="/contact/">Contact</a></p>
{f'<p class="legal-line">{LEGAL_LINE}</p>' if legal else ''}</div></footer>
<script src="/assets/site.js?v=2" defer></script>{beacon}
</body></html>'''

# ---------- helpers ----------
def ft(v): return f"{v:,} ft" if isinstance(v, int) else (f"{v} ft" if v is not None else None)
def mph(v): return f"{v} mph" if v is not None else None
def cm(inches): return round(inches * 2.54)
def _n(x): x = round(x, 1); return str(int(x)) if x == int(x) else str(x)
def metric(h): return h.get("unit") == "cm"
def hs(h, k="min"):
    v = h[k]
    return f'{v} cm (about {_n(v / 2.54)} in)' if metric(h) else f'{v} in ({cm(v)} cm)'
def hshort(h, k="min"): return f'{h[k]} cm' if metric(h) else f'{h[k]} in'
def hin(h, k="min"): return h[k] / 2.54 if metric(h) else h[k]
def rngs(h): return (f'{h["acc_min"]} to {h["acc_max"]} cm (about {_n(h["acc_min"] / 2.54)} to {_n(h["acc_max"] / 2.54)} in)' if metric(h) else f'{h["acc_min"]} to {h["acc_max"]} in ({cm(h["acc_min"])} to {cm(h["acc_max"])} cm)')
def date_h(d):
    if not d: return None
    parts = d.split("-")
    months = "Jan Feb Mar Apr May Jun Jul Aug Sep Oct Nov Dec".split()
    if len(parts) == 3: return f"{int(parts[2])} {months[int(parts[1]) - 1]} {parts[0]}"
    if len(parts) == 2: return f"{months[int(parts[1]) - 1]} {parts[0]}"
    return parts[0]
def year(c): return c["opened"][:4] if c["opened"] else None
def hr_text(c, short=False):
    h = c["hr"]
    if not h: return None
    s = hs(h)
    if h.get("acc_min"):
        s += f'; {rngs(h)} may ride with a companion' if not short else f' ({hshort(h, "acc_min")} with a companion)'
    return s
def src_link(s): return f'<a href="{s[1]}" rel="nofollow noopener" target="_blank">{E(s[0])}</a>'
def rcdb_link(c): return f'<a href="{c["rcdb_url"]}" rel="nofollow noopener" target="_blank">RCDB entry for {E(c["rcdb_name"])}</a>'
def coaster_path(c): return f'/parks/{c["park"]}/{c["slug"]}/'
def park_of(c): return next(p for p in PARKS if p["slug"] == c["park"])

TYPE_EXPLAIN = {
 "Inverted": "On an inverted coaster the seats hang below the track, so riders' feet dangle free with nothing beneath them.",
 "Suspended": "On a suspended coaster the cars hang below the track on pivots and swing outward through the turns.",
 "Wing": "On a wing coaster the seats stick out on either side of the track, so the outer riders have nothing above or below them.",
 "Flying": "On a flying coaster riders are tipped forward so they travel face down under the track, as if flying.",
 "Stand Up": "On a stand-up coaster riders travel standing, supported by a bicycle-style seat and a shoulder harness.",
 "Floorless": "The train has no floor, so riders' feet hang just above the track.",
 "Spinning Cars": "The cars can spin freely as they travel, so no two rides feel quite the same.",
 "Hybrid": "It is a hybrid coaster, mixing wooden and steel construction.",
 "Wood": "It is a wooden coaster, with a wooden track structure.",
 "Twin": "It runs on two tracks side by side.",
 "Enclosed": "Most or all of the ride is indoors.",
 "Dark Ride": "It combines coaster sections with themed show scenes, like a dark ride.",
 "Straddled Seating": "Riders straddle their seats, motorbike style.",
 "Single Rail": "Riders sit single file on a train that runs on one narrow rail.",
 "Terrain": "The layout follows the natural hillside terrain.",
 "Rocking Cars": "The cars rock from side to side as the train takes the curves.",
 "Onboard Sound": "The train has an onboard soundtrack.",
}
LAUNCH_MODELS = ("LSM Launch", "Accelerator", "Sky Rocket")

def class_word(c):
    h = c["height"] or 0
    if h >= 400: return "strata coaster (a coaster 400 ft or taller)"
    if h >= 300: return "giga coaster (300 to 399 ft tall)"
    if h >= 200: return "hyper coaster (200 to 299 ft tall)"
    return None

def intensity(c):
    """Return (label, sentence) from verified data only."""
    s, h = c["scale"], c["hr"]
    bits = []
    if s: bits.append(f'RCDB classes it as a{"n" if s[0] in "AEIOU" else ""} <strong>{s.lower()}</strong> coaster')
    if h and h.get("thrill"): bits.append(f'{E(c["park_name"])} rates it <strong>{h["thrill"]} out of 5</strong> on its own thrill scale')
    label = {"Kiddie": "Gentle (kiddie)", "Family": "Mild (family)", "Thrill": "Moderate (thrill)", "Extreme": "Intense (extreme)"}.get(s, "Not rated")
    return label, ("; ".join(bits) + ".") if bits else ""

def best_seat(c):
    t = c["tags"]
    if "Spinning Cars" in t:
        return "Seat choice matters less on a spinning coaster: how much the car spins depends on how the weight is spread around it, so every ride is different."
    if any(x in t for x in ("Enclosed", "Dark Ride")):
        return "Because much of the ride is themed or in the dark, the front rows give the clearest view of the show scenes and effects, while the back rows feel the drops a little more."
    if c["design"] in ("Inverted", "Wing", "Flying") or "Floorless" in t:
        return _pick(c, "seat", ["The front row gives an unobstructed view, which is the main reason riders choose it on this style of coaster. Outer seats feel more open; the back row is pulled over the drops faster and so tends to give the strongest drop sensation.", "On this style of coaster, the front row has nothing in your line of sight, and the outermost seats feel the most exposed. Riders after the strongest drops pick the back row, which is pulled over each crest faster.", "Choose an outside seat for the most open feeling and the front row for a clear view; the back row feels the drops hardest because the train pulls it over the top at speed."])
    if c["scale"] in ("Kiddie", "Family"):
        return "On a small coaster any seat works. The front row gives the best view."
    return _pick(c, "seat", ["For the strongest airtime, sit near the back: the cars ahead pull the back of the train over each crest faster, so you leave your seat sooner on the drops. For the best view of what is coming, sit in the front row.", "The back rows get pulled over each hill at speed, which gives the sharpest drops and most airtime; the front row trades some of that for a clear view of the track ahead.", "Pick the front row for the view and the back rows for airtime: the train drags the rear cars over every crest faster than the front."])

def suits(c):
    h, s, inv = c["hr"], c["scale"], c["inversions"]
    parts = []
    if s in ("Kiddie", "Family"): parts.append("young riders taking their first coasters and adults riding with them")
    elif s == "Thrill": parts.append("riders who enjoy speed and turns but may not want the biggest drops in the park")
    elif s == "Extreme": parts.append("confident thrill seekers who are comfortable with big forces")
    if inv == 0: parts.append("riders who prefer not to go upside down")
    elif inv: parts.append(f"riders happy to go upside down {inv} time{'s' if inv != 1 else ''}")
    out = "It suits " + " and ".join(parts) + "." if parts else ""
    if h: out += f' Riders must be at least {hs(h)} tall' + (f', or {rngs(h)} with a companion' if h.get("acc_min") else "") + (f', and no taller than {hs(h, "max")}' if h.get("max") else "") + "."
    return out

def describe(c):
    p = park_of(c)
    mat = c["material"].lower() if c["material"] else ""
    design = {"Sit Down": "sit-down", "Inverted": "inverted", "Suspended": "suspended", "Wing": "wing", "Flying": "flying", "Stand Up": "stand-up"}.get(c["design"], "")
    kind = " ".join(x for x in [mat, design] if x) + " roller coaster"
    s1 = f'{E(c["name"])} is a{"n" if kind[0] in "aeiou" else ""} {kind} at {E(p["name"])} in {E(p["loc"])}'
    if c["make"]: s1 += f', built by {E(c["make"])}'
    s1 += "" if s1.endswith(".") else "."
    sents = [s1]
    if c["opened"]:
        if c["former"]:
            sents.append(f'It first opened {"on " + date_h(c["opened"]) if len(c["opened"]) > 4 else "in " + c["opened"]} and was previously known as {E(" and later ".join(c["former"]))}.')
        else:
            sents.append(f'It opened on {date_h(c["opened"])}.' if len(c["opened"]) > 4 else f'It opened in {c["opened"]}.')
    stat = []
    if c["height"]: stat.append(f'stands {ft(c["height"])} tall')
    if c["drop"]: stat.append(f'drops {ft(c["drop"])}')
    if c["speed"]: stat.append(f'reaches {mph(c["speed"])}')
    if c["length"]: stat.append(f'runs {ft(c["length"])} of track')
    if stat:
        sents.append("The ride " + (", ".join(stat[:-1]) + " and " + stat[-1] if len(stat) > 1 else stat[0]) + (" on each track" if c["twin"] else "") + ".")
    cw = class_word(c)
    if cw: sents.append(f"That height makes it a {cw}.")
    if c["model"] and any(m in c["model"] for m in LAUNCH_MODELS): sents.append("Instead of a slow chain lift, trains are launched up to speed.")
    for t in c["tags"]:
        if t in TYPE_EXPLAIN and t != "Twin" or (t == "Twin"):
            if t in TYPE_EXPLAIN: sents.append(TYPE_EXPLAIN[t])
    if c["design"] in TYPE_EXPLAIN: sents.append(TYPE_EXPLAIN[c["design"]])
    if c["inversions"]: sents.append(f'It turns riders upside down {c["inversions"]} time{"s" if c["inversions"] != 1 else ""}.')
    elif c["inversions"] == 0: sents.append("It does not turn riders upside down.")
    if c["angle"] and c["angle"] >= 90: sents.append(f'Its steepest drop is {c["angle"]}°, ' + ("past vertical." if c["angle"] > 90 else "straight down."))
    seen, out = set(), []
    for s in sents:
        if s not in seen: seen.add(s); out.append(s)
    return " ".join(out)

def stat_rows(c):
    h = c["hr"]
    rows = []
    if h:
        rows.append(("Minimum height", hs(h)))
        if h.get("acc_min"): rows.append(("With a companion", rngs(h)))
        if h.get("max"): rows.append(("Maximum height", hs(h, "max")))
        if h.get("note"): rows.append(("Other rider rules", h["note"]))
        if h.get("thrill"): rows.append(("Park thrill rating", f'{h["thrill"]} of 5'))
    else:
        rows.append(("Minimum height", "Not clearly published by the park. Check the sign at the ride entrance."))
    for k, v in [("Height", ft(c["height"])), ("Drop", ft(c["drop"])), ("Top speed", mph(c["speed"])), ("Track length", ft(c["length"])),
                 ("Inversions", c["inversions"]), ("Steepest drop angle", f'{c["angle"]}°' if c["angle"] else None), ("Max g-force", c["gforce"]),
                 ("Ride time", f'{c["duration"] // 60}:{c["duration"] % 60:02d}' if c.get("duration") else None), ("Opened", date_h(c["opened"])), ("Manufacturer", c["make"]), ("Model", c["model"]), ("Type", ", ".join(c["tags"]))]:
        if v not in (None, ""): rows.append((k, str(v)))
    return rows

def faq_items(c):
    q = []
    h = c["hr"]
    if h:
        a = f'Riders must be at least {hs(h)} tall to ride {c["name"]}'
        if h.get("acc_min"): a += f', or {rngs(h)} with a companion'
        if h.get("max"): a += f'. The maximum rider height is {hs(h, "max")}'
        if h.get("note"): a += ". " + h["note"].rstrip(".")
        a += f', according to {h["src"][0]} (checked {CHECKED}). Requirements can change, so confirm at the ride entrance.'
        q.append((f'What is the height requirement for {c["name"]}?', a))
    if c["height"]: q.append((f'How tall is {c["name"]}?', f'{c["name"]} is {ft(c["height"])} tall' + (f', with a drop of {ft(c["drop"])}' if c["drop"] else "") + ', according to RCDB.'))
    if c["speed"]: q.append((f'How fast does {c["name"]} go?', f'Its top speed is {mph(c["speed"])} ({round(c["speed"] * 1.609)} km/h), according to RCDB.'))
    if c["inversions"] is not None: q.append((f'Does {c["name"]} go upside down?', (f'Yes. It has {c["inversions"]} inversion' + ("s" if c["inversions"] != 1 else "") + '.') if c["inversions"] else 'No. It has no inversions.'))
    lab, sent = intensity(c)
    if sent: q.append((f'Is {c["name"]} scary?', f'It depends on the rider, but on intensity: {re.sub("<[^>]+>", "", sent)} ' + ({"Kiddie": "It is one of the gentlest coasters you can ride.", "Family": "It is built for families.", "Thrill": "Expect a lively ride that stops short of the most extreme coasters.", "Extreme": "That is RCDB's most intense class."}.get(c["scale"], ""))))
    if c["opened"]: q.append((f'When did {c["name"]} open?', f'{c["name"]} opened {"on " + date_h(c["opened"]) if len(c["opened"]) > 4 else "in " + c["opened"]}' + (f' (previously known as {" and later ".join(c["former"])})' if c["former"] else "") + '.'))
    if c["make"]: q.append((f'Who built {c["name"]}?', f'{c["name"]} was manufactured by {c["make"]}' + ("" if c["make"].endswith(".") else ".")))
    q += detail_faqs(c)
    q += clone_faqs(c)
    return q

def before_ride(c):
    p = park_of(c); h = c["hr"]; li = []
    if h: li.append(f'Measure first: the ride-alone minimum is {hs(h)}' + (f', and riders from {rngs(h)} need a companion' if h.get("acc_min") else "") + '. Height is checked at the entrance, so ask the ride team before you queue if your child is close.')
    else: li.append(f'We could not verify an official height rule for {E(c["name"])}, so check the sign at the entrance or the <a href="{p["official"]}" rel="nofollow noopener" target="_blank">{E(p["name"])} site</a>.')
    if h and h.get("max"): li.append(f'Tall riders: the maximum is {hs(h, "max")}. See <a href="/guides/can-you-be-too-tall-for-a-roller-coaster/">can you be too tall?</a>')
    if h and h.get("note"): li.append(E(h["note"]))
    if "Spinning Cars" in c["tags"] or "Shuttle" in c["tags"]: li.append('If you get motion sick, note that this ride ' + ("spins" if "Spinning Cars" in c["tags"] else "runs backwards") + '. See our <a href="/guides/roller-coaster-motion-sickness/">motion sickness tips</a>.')
    elif c["inversions"]: li.append(f'Secure glasses, phones and loose items before the {c["inversions"]} inversion' + ("s" if c["inversions"] != 1 else "") + '; the park posts its loose-article rules at the ride.')
    else: li.append('Loose items, health warnings and accessibility rules are set by the park and posted at the ride.')
    li.append(f'Opening times and ride status: check the {E(p["name"])} app or <a href="{p["official"]}" rel="nofollow noopener" target="_blank">official site</a> on the day.')
    return "".join(f"<li>{x}</li>" for x in li)

def faq_html(items):
    return '<section class="faq" aria-labelledby="faq-h"><h2 id="faq-h">Frequently asked questions</h2>' + "".join(f'<details><summary>{E(a)}</summary><p>{E(b)}</p></details>' for a, b in items) + "</section>"
def faq_ld(items):
    return {"@context": "https://schema.org", "@type": "FAQPage", "mainEntity": [{"@type": "Question", "name": a, "acceptedAnswer": {"@type": "Answer", "text": b}} for a, b in items]}

def map_block(points, height=380, id="map"):
    pts = [dict(n=c["name"], p=c["park_name"], u=coaster_path(c), lat=c["lat"], lon=c["lon"], h=hshort(c["hr"]) if c["hr"] else None, s=c["scale"]) for c in points if c["lat"]]
    return (f'<div class="map" id="{id}" style="height:{height}px" role="region" aria-label="Interactive map of coaster locations"></div>'
            f'<p class="note">Pins show approximate ride positions from RCDB map coordinates. Map data © <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors. A text list of every coaster is below the map.</p>'
            f'<script type="application/json" id="{id}-data">{json.dumps(pts, ensure_ascii=False)}</script>')
LEAFLET_HEAD = '<link rel="stylesheet" href="/assets/leaflet.css"><script src="/assets/leaflet.js" defer></script>'

# ---------- coaster pages ----------
def related_html(c=None, p=None):
    gp = {u for u, *_ in GUIDES}
    links = []
    park = p or park_of(c)
    if c:
        links += type_links(c)
        h = c["hr"]
        if h:
            for H in HEIGHTS:
                if hin(h) <= H + 1e-9: links.append((f"/guides/roller-coasters-for-{H}-inch-kids/", f"Coasters for {H}-inch kids")); break
    for u, t, b, g in GUIDES:
        if g == "By place" and park["slug"] in REGION_PARKS.get(u, ()): links.append((u, t))
    if c:
        mp = maker_path(c)
        if mp: links.append(mp)
        links += [("/guides/best-seat-on-a-roller-coaster/", "Best seat on a roller coaster")]
        if c["hr"] and c["hr"].get("max"): links.append(("/guides/can-you-be-too-tall-for-a-roller-coaster/", "Can you be too tall for a coaster?"))
        if launched(c): links.append(("/guides/how-do-roller-coaster-launches-work/", "How roller coaster launches work"))
        if "Spinning Cars" in c["tags"]: links.append(("/guides/roller-coaster-motion-sickness/", "Roller coaster motion sickness"))
        if c.get("inversions"): links.append(("/guides/how-do-roller-coaster-restraints-work/", "How coaster restraints work"))
        else: links.append(("/guides/how-do-roller-coasters-stay-on-the-track/", "How coasters stay on the track"))
        if (c.get("height") or 0) >= 150 or "Wood" in c["tags"]: links.append(("/guides/what-is-airtime-on-a-roller-coaster/", "What is airtime?"))
        if (c.get("height") or 0) >= 100: links.append(("/guides/why-your-stomach-drops-on-a-roller-coaster/", "Why your stomach drops"))
        if (c.get("speed") or 0) >= 55 or (c.get("inversions") or 0) >= 3: links.append(("/guides/roller-coasters-and-health-conditions/", "Coasters and health conditions"))
        if launched(c) or (c.get("speed") or 0) >= 60: links.append(("/guides/how-do-roller-coaster-brakes-work/", "How coaster brakes work"))
    if p: links += [("/guides/roller-coaster-height-requirements-explained/", "Height requirements explained"), ("/guides/how-to-not-be-scared-of-roller-coasters/", "How to not be scared of coasters")]
    if p: links += [("/guides/best-first-roller-coasters/", "Best first roller coasters"), ("/guides/roller-coasters-for-48-inch-kids/", "Coasters for 48-inch kids"), ("/guides/tallest-roller-coasters/", "Tallest roller coasters")]
    if p: links += [("/guides/roller-coaster-glossary/", "Roller coaster glossary"), ("/guides/what-happens-if-a-roller-coaster-gets-stuck/", "What happens if a coaster gets stuck"), ("/guides/world-record-roller-coasters/", "World record roller coasters")]
    links = [(u, t) for u, t in dict.fromkeys(links) if u in gp]
    if not links: return ""
    return '<section aria-labelledby="rg-h"><h2 id="rg-h">Related guides</h2><ul class="cols">' + "".join(f'<li><a href="{u}">{E(t)}</a></li>' for u, t in links) + "</ul></section>"

def coaster_page(c):
    p = park_of(c)
    path = coaster_path(c)
    h = c["hr"]
    lab, isent = intensity(c)
    answer = []
    if h: answer.append(f'<strong>Height requirement: {hs(h)}</strong>' + (f', or {rngs(h)} with a companion' if h.get("acc_min") else ""))
    if c["speed"]: answer.append(f'top speed {mph(c["speed"])}')
    if c["height"]: answer.append(f'{ft(c["height"])} tall')
    if c["inversions"] is not None: answer.append(f'{c["inversions"]} inversion{"s" if c["inversions"] != 1 else ""}')
    if year(c): answer.append(f'opened {year(c)}')
    rows = "".join(f'<tr><th scope="row">{E(k)}</th><td>{E(v)}</td></tr>' for k, v in stat_rows(c))
    faqs = faq_items(c)
    siblings = [x for x in p["coasters"] if x is not c]
    sib = "".join(f'<li><a href="{coaster_path(x)}">{E(x["name"])}</a>' + (f' <span class="muted">({hshort(x["hr"])})</span>' if x["hr"] else "") + '</li>' for x in siblings)
    srcs = [f'<li>{rcdb_link(c)}: stats, opening date, manufacturer, type and map position.</li>']
    if h: srcs.append(f'<li>{src_link(h["src"])}: height requirement' + (", thrill rating" if h.get("thrill") else "") + f' (checked {CHECKED}).</li>')
    srcs.append(f'<li><a href="{p["official"]}" rel="nofollow noopener" target="_blank">{E(p["name"])} official site</a>: hours, closures and current ride rules.</li>')
    if c["opened"] and h and h.get("introduced") and h["introduced"] != c["opened"][:4]:
        srcs.append(f'<li>Note: the park\'s ride page lists {h["introduced"]} as the year this ride was introduced; RCDB dates the opening of this coaster to {date_h(c["opened"])}.</li>')
    mp = map_block([c], 300, "map") if c["lat"] else ""
    body = f'''<article class="coaster"><h1>{E(c["name"])}</h1><p class="sub">{E(p["name"])} · {E(p["loc"])}</p>{byline()}
<p class="answer">{"; ".join(answer)}.</p>
<p>{describe(c)}</p>
{feel_html(c)}
{specs_html(c)}
<div class="grid2"><section aria-labelledby="stats-h"><h2 id="stats-h">{E(c["name"])} stats</h2><table class="stats"><tbody>{rows}</tbody></table>
{"<p class='note'>" + E(c["name"]) + " has two tracks; RCDB figures above are for one track.</p>" if c["twin"] else ""}</section>
<section aria-labelledby="int-h"><h2 id="int-h">How intense is it?</h2><p class="pill">{E(lab)}</p><p>{isent}</p>
<h2>Who is it for?</h2><p>{E(suits(c))}</p>
<h2>Best seat to ride</h2><p>{E(best_seat(c))}</p>
<p class="note">General guidance from how this style of coaster moves, not a park rule. See <a href="/guides/best-seat-on-a-roller-coaster/">best seat on a roller coaster</a>.</p></section></div>
{compare_html(c)}
{mp}
<section aria-labelledby="tips-h"><h2 id="tips-h">Before you ride {E(c["name"])}</h2><ul>{before_ride(c)}</ul>
<p>Planning for a child? The <a href="/height-checker/">ride height checker</a> shows every coaster they can ride at {E(p["short"])}.</p></section>
{faq_html(faqs)}
<section aria-labelledby="more-h"><h2 id="more-h">More coasters at {E(p["name"]) if siblings else E(p["group"])}</h2>{f'<ul class="cols">{sib}</ul>' if siblings else '<ul class="cols">' + "".join(f'<li><a href="{coaster_path(x)}">{E(x["name"])}</a> <span class="muted">({E(x["park_name"])}{", " + hshort(x["hr"]) if x["hr"] else ""})</span></li>' for x in ALL if park_of(x)["group"] == p["group"] and x is not c) + '</ul>'}<p><a href="/parks/{p["slug"]}/">See the full {E(p["name"])} coaster guide and map</a></p></section>
{related_html(c=c)}<section class="sources" aria-labelledby="src-h"><h2 id="src-h">Sources</h2><ul>{srcs and "".join(srcs)}</ul><p class="note">Last checked {CHECKED}. Found an error? <a href="/contact/">Tell us</a>.</p></section></article>'''
    dparts = [x for x in [h and f'height requirement {hshort(h)}', mph(c["speed"]) and "top speed " + mph(c["speed"]), ft(c["height"]) and ft(c["height"]) + " tall"] if x]
    desc = f'{c["name"]} at {p["name"]}' + (": " + ", ".join(dparts) if dparts else "") + ". How intense it is, best seat and who it suits."
    if sum(1 for x in ALL if x["name"] == c["name"]) > 1:  # same ride name at more than one park
        title = f'{c["name"]} at {p["short"]}: Height Requirement & Stats | {BRAND}'
        if len(title) > 70: title = f'{c["name"]} at {p["short"]}: Height & Stats | {BRAND}'
        if len(title) > 70: title = f'{c["name"]} at {p["short"]}: Heights & Stats | {BRAND}'
        if len(title) > 70: title = f'{c["name"]} at {p["short"]} | {BRAND}'
        if len(title) > 70: title = f'{c["name"]}, {p["short"]} | {BRAND}'
    else:
        title = f'{c["name"]}: Height Requirement, Stats & Best Seat | {BRAND}'
        if len(title) > 70: title = f'{c["name"]} Height Requirement & Stats | {BRAND}'
        if len(title) > 70: title = f'{c["name"]} Guide | {BRAND}'
    ld = [{"@context": "https://schema.org", "@type": "TouristAttraction", "name": c["name"], "description": re.sub("<[^>]+>", "", describe(c))[:300],
           "url": url(path), "isAccessibleForFree": False, "touristType": lab,
           "containedInPlace": {"@type": "AmusementPark", "name": p["name"], "url": p["official"]},
           **({"geo": {"@type": "GeoCoordinates", "latitude": c["lat"], "longitude": c["lon"]}} if c["lat"] else {}),
           "publisher": {"@type": "Organization", "name": BRAND, "url": BASE_URL}}, faq_ld(faqs)]
    write(path, page(path, title, desc, body, ld, [("/", "Home"), ("/parks/", "Parks"), (f'/parks/{p["slug"]}/', p["name"]), (path, c["name"])], LEAFLET_HEAD if c["lat"] else ""))

def coaster_table(cs, show_park=False):
    head = "<tr><th scope='col'>Coaster</th>" + ("<th scope='col'>Park</th>" if show_park else "") + "<th scope='col'>Min height</th><th scope='col'>Height</th><th scope='col'>Top speed</th><th scope='col'>Inversions</th><th scope='col'>Intensity</th><th scope='col'>Opened</th></tr>"
    rows = ""
    for c in cs:
        rows += (f'<tr><th scope="row"><a href="{coaster_path(c)}">{E(c["name"])}</a></th>' + (f'<td>{E(park_of(c)["short"])}</td>' if show_park else "")
                 + f'<td data-v="{round(hin(c["hr"]), 2) if c["hr"] else 999}">{hshort(c["hr"]) if c["hr"] else "check park"}</td><td data-v="{c["height"] or 0}">{ft(c["height"]) or "n/a"}</td>'
                 f'<td data-v="{c["speed"] or 0}">{mph(c["speed"]) or "n/a"}</td><td>{c["inversions"] if c["inversions"] is not None else "n/a"}</td><td>{E(c["scale"] or "")}</td><td>{year(c) or ""}</td></tr>')
    return f'<div class="tablewrap"><table class="list sortable"><thead>{head}</thead><tbody>{rows}</tbody></table></div><p class="note">n/a means RCDB lists no figure. Tap a column heading to sort.</p>'

def park_page(p):
    path = f'/parks/{p["slug"]}/'
    cs = p["coasters"]
    n = len(cs)
    tall = max((c for c in cs if c["height"]), key=lambda c: c["height"], default=None)
    fast = max((c for c in cs if c["speed"]), key=lambda c: c["speed"], default=None)
    lowest = min((c for c in cs if c["hr"]), key=lambda c: hin(c["hr"]), default=None)
    noinv = [c for c in cs if c["inversions"] == 0]
    bands = [(0, 42, "Under 42 in (107 cm)"), (42, 48, "42 to 47 in (107 to 121 cm)"), (48, 52, "48 to 51 in (122 to 131 cm)"), (52, 999, "52 in (132 cm) and up")]
    band_html = ""
    for lo, hi, label in bands:
        b = sorted([c for c in cs if c["hr"] and lo <= round(hin(c["hr"]), 6) < hi], key=lambda c: hin(c["hr"]))
        if b: band_html += f'<h3>{label}</h3><ul>' + "".join(f'<li><a href="{coaster_path(c)}">{E(c["name"])}</a>: {hshort(c["hr"])}</li>' for c in b) + "</ul>"
    unv = [c for c in cs if not c["hr"]]
    if unv: band_html += "<h3>Height requirement not yet verified</h3><ul>" + "".join(f'<li><a href="{coaster_path(c)}">{E(c["name"])}</a></li>' for c in unv) + "</ul>"
    lead = f'{E(p["name"])}' + (f' (formerly {E(p["former"])})' if p.get("former") else "") + f' in {E(p["loc"])} has <strong>{n} operating roller coaster{"s" if n != 1 else ""}</strong> listed on RCDB as of {CHECKED}.'
    if tall: lead += f' The tallest is <a href="{coaster_path(tall)}">{E(tall["name"])}</a> at {ft(tall["height"])}'
    if fast: lead += (f' and the fastest is <a href="{coaster_path(fast)}">{E(fast["name"])}</a> at {mph(fast["speed"])}' if fast is not tall else ", which is also the fastest at " + mph(fast["speed"])) 
    lead += "."
    if lowest: lead += f' The lowest height requirement is {hs(lowest["hr"])}, for <a href="{coaster_path(lowest)}">{E(lowest["name"])}</a>.'
    fm = p.get("former")
    faqs = []
    if fm: faqs.append((f'Is {p["name"]} the same park as {fm}?', f'Yes. {p["name"]} in {p["loc"]} is the park formerly called {fm}; {p["former_note"]} (checked {CHECKED}).'))
    faqs += [(f'How many roller coasters does {p["name"]} have?', f'{p["name"]} has {n} operating roller coaster{"s" if n != 1 else ""} according to RCDB, checked {CHECKED}.')]
    if tall: faqs.append((f'What is the tallest roller coaster at {p["name"]}?', f'{tall["name"]}, at {ft(tall["height"])} tall (RCDB).'))
    if fast: faqs.append((f'What is the fastest roller coaster at {p["name"]}?', f'{fast["name"]}, with a top speed of {mph(fast["speed"])} (RCDB).'))
    if lowest: faqs.append((f'What is the easiest coaster for kids at {p["name"]}?', f'By height requirement, {lowest["name"]} has the lowest minimum at {hs(lowest["hr"])}. Check the park for companion rules.'))
    for th in (42, 48):
        ok = [c["name"] for c in cs if c["hr"] and hin(c["hr"]) <= th + 1e-9]
        if ok: faqs.append((f'Which {p["name"]} coasters can a {th}-inch child ride?', f'Based on official minimum heights checked {CHECKED}: ' + ", ".join(ok) + '. Some rides also need a companion below a certain height; confirm at the ride.'))
    if noinv: faqs.append((f'Which coasters at {p["name"]} do not go upside down?', ", ".join(c["name"] for c in noinv) + " have no inversions, per RCDB."))
    srcset = sorted({c["hr"]["src"] for c in cs if c["hr"]})
    body = f'''<h1>{E(p["name"])} roller coasters</h1><p class="sub">{("Formerly " + E(p["former"]) + " · ") if p.get("former") else ""}{E(p["loc"])} · {n} coaster{"s" if n != 1 else ""}</p>{byline()}
<p class="answer">{lead}</p>
{map_block(cs, 440)}
<h2>Every coaster at {E(p["name"])}</h2>{coaster_table(sorted(cs, key=lambda c: -(c["height"] or 0)))}
<section aria-labelledby="hb-h"><h2 id="hb-h">{E(p["name"])} coasters by height requirement</h2>{band_html}<p>Want a personal list? Use the <a href="/height-checker/">ride height checker</a>.</p></section>
{faq_html(faqs)}
{related_html(p=p)}<section class="sources"><h2>Sources</h2><ul><li><a href="{p["rcdb_url"]}" rel="nofollow noopener" target="_blank">RCDB: {E(p["name"])}</a>: operating coaster list, stats and map positions.</li>{"".join(f"<li>{src_link(s)}: height requirements (checked {CHECKED}).</li>" for s in srcset if not (s[1].startswith("https://www.sixflags.com") or ".enchantedparks.com/rides-and-experiences/" in s[1]))}{"<li>" + E(p["name"]) + " official ride pages on " + ("sixflags.com" if p["official"].startswith("https://www.sixflags.com") else p["official"].split("/")[2]) + ": height requirements and thrill ratings (linked on each coaster page, checked " + CHECKED + ").</li>" if any(c["hr"] and (c["hr"]["src"][1].startswith("https://www.sixflags.com") or ".enchantedparks.com/rides-and-experiences/" in c["hr"]["src"][1]) for c in cs) else ""}<li><a href="{p["official"]}" rel="nofollow noopener" target="_blank">{E(p["name"])} official site</a></li></ul></section>'''
    ld = [{"@context": "https://schema.org", "@type": "AmusementPark", "name": p["name"], "url": p["official"], **({"alternateName": p["former"]} if p.get("former") else {}), "address": {"@type": "PostalAddress", "addressLocality": p["loc"].split(", ")[-2], "addressRegion": p["state"], "addressCountry": p["country"]}},
          {"@context": "https://schema.org", "@type": "ItemList", "name": f'Roller coasters at {p["name"]}', "numberOfItems": n,
           "itemListElement": [{"@type": "ListItem", "position": i + 1, "url": url(coaster_path(c)), "name": c["name"]} for i, c in enumerate(cs)]}, faq_ld(faqs)]
    title = f'{p["name"]} Roller Coasters: Heights, Stats & Map | {BRAND}' if not p.get("former") else f'{p["name"]} ({p["former"]}) Coasters | {BRAND}'
    if len(title) > 70: title = f'{p["short"]} Roller Coasters: Heights & Map | {BRAND}'
    if len(title) > 70: title = f'{p["short"]} Coasters: Heights & Map | {BRAND}'
    write(path, page(path, title, (f'All {n} roller coasters at {p["name"]}' if n != 1 else f'The roller coaster at {p["name"]}') + (f', formerly {p["former"]},' if p.get("former") else "") + ' with height requirements, top speeds, intensity and an interactive map.', body, ld, [("/", "Home"), ("/parks/", "Parks"), (path, p["name"])], LEAFLET_HEAD))

def parks_index():
    cards = "".join(f'<li class="card"><h2><a href="/parks/{p["slug"]}/">{E(p["name"])}</a></h2><p>{("Formerly " + E(p["former"]) + ", ") if p.get("former") else ""}{E(p["loc"])}</p><p><strong>{len(p["coasters"])} coaster{"s" if len(p["coasters"]) != 1 else ""}</strong>' + (f'; tallest {E(max((c for c in p["coasters"] if c["height"]), key=lambda c: c["height"])["name"])}' if any(c["height"] for c in p["coasters"]) else "") + '.</p></li>' for p in PARKS)
    body = f'<h1>Theme park coaster guides</h1><p class="answer">Coaster Map covers {len(PARKS)} major theme parks so far, with {len(ALL)} roller coasters. Each guide lists every operating coaster with its height requirement, stats and map position. Each park guide also ranks its coasters by intensity and suggests first-timer picks.</p><ul class="cards">{cards}</ul>'
    write("/parks/", page("/parks/", f"Theme Park Roller Coaster Guides by Park | {BRAND}", f"Roller coaster guides for {len(PARKS)} theme parks, including Walt Disney World, Disneyland Resort, Universal Orlando, Six Flags, Cedar Point, Kings Island, SeaWorld, Busch Gardens, Hersheypark and Dollywood.", body, None, [("/", "Home"), ("/parks/", "Parks")]))

def all_coasters():
    body = f'<h1>All roller coasters on Coaster Map</h1><p class="answer">{len(ALL)} roller coasters across {len(PARKS)} parks, sorted tallest first. Height requirements come from official park pages; stats come from RCDB.</p>{coaster_table(sorted(ALL, key=lambda c: -(c["height"] or 0)), True)}'
    write("/coasters/", page("/coasters/", f"All Roller Coasters: Height Requirements & Stats | {BRAND}", f"Compare {len(ALL)} theme park roller coasters by height requirement, height, top speed and inversions.", body, None, [("/", "Home"), ("/coasters/", "All coasters")]))

def map_page():
    opts = "".join(f'<option value="{E(p["name"])}">{E(p["name"])}</option>' for p in PARKS)
    body = f'<h1>Roller coaster map</h1><p class="answer">Every coaster we cover, on one map. Zoom into a park to see where each ride sits, then open a pin for its height requirement and full guide.</p><p><label for="park-filter">Show park: </label><select id="park-filter" data-map="map"><option value="">All parks</option>{opts}</select></p>{map_block(ALL, 560)}<h2>Parks on the map</h2><ul>' + "".join(f'<li><a href="/parks/{p["slug"]}/">{E(p["name"])}</a> ({len(p["coasters"])} coaster{"s" if len(p["coasters"]) != 1 else ""})</li>' for p in PARKS) + "</ul>"
    write("/map/", page("/map/", f"Theme Park Roller Coaster Map | {BRAND}", f"Interactive map of {len(ALL)} roller coasters at Disney, Universal, Six Flags, Cedar Point, Kings Island, SeaWorld, Busch Gardens, Hersheypark, Dollywood, Knott's and more parks.", body, None, [("/", "Home"), ("/map/", "Coaster map")], LEAFLET_HEAD))

def tool_data():
    return json.dumps([dict(n=c["name"], p=c["park_name"], ps=c["park"], u=coaster_path(c), min=c["hr"]["min"] if c["hr"] else None,
        am=c["hr"]["acc_min"] if c["hr"] else None, ax=c["hr"]["acc_max"] if c["hr"] else None, mx=c["hr"]["max"] if c["hr"] else None, mu=("cm" if c["hr"] and metric(c["hr"]) else None),
        s=c["scale"], i=c["inversions"], h=c["height"], v=c["speed"], y=year(c)) for c in ALL], ensure_ascii=False)

def height_checker():
    opts = "".join(f'<option value="{p["slug"]}">{E(p["name"])}</option>' for p in PARKS)
    body = f'''<h1>Ride height checker: which coasters can my child ride?</h1>
<p class="answer">Enter your child's height and pick a park. We'll list every coaster they are tall enough for, the ones they can ride with a companion, and the ones to save for next year. Height rules come from official park pages, checked {CHECKED}.</p>
<form id="hc" class="tool" onsubmit="return false"><div class="row"><label for="hc-h">Height</label><input id="hc-h" type="number" inputmode="decimal" min="20" max="250" step="0.5" required>
<label for="hc-u" class="vh">Unit</label><select id="hc-u"><option value="in">inches</option><option value="cm">cm</option></select></div>
<div class="row"><label for="hc-p">Park</label><select id="hc-p"><option value="">All parks</option>{opts}</select></div><button class="btn" type="submit">Check rides</button></form>
<div id="hc-out" aria-live="polite"></div>
<p class="note"><strong>Always confirm at the ride.</strong> Parks measure at the entrance, rules change, and a ride can refuse anyone for safety reasons. Coasters with no verified requirement are listed separately so you can ask the park.</p>
<h2>How height requirements work</h2><p>Each coaster has a minimum height set by the park and the ride maker. Some family coasters let shorter children ride with a companion (an adult or older rider), and a few kiddie coasters also have a maximum height. Our checker uses only those official numbers.</p>
<script type="application/json" id="coaster-data">{tool_data()}</script>'''
    faqs = [("Where is height checked?", "At the ride entrance, by the park's ride team. Rules on footwear and re-measuring vary by park, so ask the ride team if your child is close to the line."),
            ("Where do these height requirements come from?", f"From each park's official ride pages, ride guides or FAQs (for Universal Orlando parks, Visit Orlando's official coaster guide), all checked {CHECKED}. Each coaster page links its exact source, and our sources and methods page lists them all."),
            ("Does the checker work in centimetres?", "Yes. Choose cm or inches. Parks in Europe and Asia publish rules in centimetres, and the checker compares your child's height against that official centimetre figure, so a rider exactly at the line is shown as able to ride in either unit."),
            ("What does ride with a companion mean?", "Some family coasters let a shorter child ride if an adult or older rider sits with them. The checker lists these separately, with the companion height range the park gives. Who counts as a companion (age or height) is set by each park.")]
    body += faq_html(faqs)
    write("/height-checker/", page("/height-checker/", f"Ride Height Checker: Coasters Your Child Can Ride | {BRAND}", "Enter your child's height in inches or cm and see which roller coasters they can ride at Disney, Universal, Six Flags, Cedar Point, Kings Island, SeaWorld, Busch Gardens, Hersheypark, Dollywood, Knott's and more.", body, [faq_ld(faqs), {"@context": "https://schema.org", "@type": "WebApplication", "name": "Coaster Map ride height checker", "applicationCategory": "TravelApplication", "operatingSystem": "Any", "offers": {"@type": "Offer", "price": "0", "priceCurrency": "USD"}, "url": url("/height-checker/")}], [("/", "Home"), ("/height-checker/", "Height checker")]))

def quiz():
    opts = "".join(f'<option value="{p["slug"]}">{E(p["name"])}</option>' for p in PARKS)
    body = f'''<h1>Which roller coaster should you ride?</h1>
<p class="answer">Answer four quick questions and we'll match you with coasters that fit your height, your nerve and your park, using official height rules and RCDB stats only.</p>
<form id="qz" class="tool" onsubmit="return false">
<div class="row"><label for="qz-p">Which park?</label><select id="qz-p"><option value="">Any park</option>{opts}</select></div>
<div class="row"><label for="qz-h">Your height (inches)</label><input id="qz-h" type="number" min="30" max="90" step="0.5" required></div>
<fieldset><legend>How brave are you feeling?</legend>
<label><input type="radio" name="qz-t" value="gentle" checked> Gentle: first coasters, small drops</label>
<label><input type="radio" name="qz-t" value="moderate"> Moderate: speed and turns, nothing too wild</label>
<label><input type="radio" name="qz-t" value="max"> Bring it on: the biggest and fastest</label></fieldset>
<fieldset><legend>Going upside down?</legend><label><input type="radio" name="qz-i" value="no" checked> No thanks</label><label><input type="radio" name="qz-i" value="yes"> Yes please</label></fieldset>
<button class="btn" type="submit">Find my coaster</button></form><div id="qz-out" aria-live="polite"></div>
<h2 id="tg-h">Coaster trivia: which is taller?</h2>
<p>Two coasters, one question. Pick the taller one. Heights are from RCDB.</p>
<div id="tg" class="tool" aria-labelledby="tg-h"><p id="tg-q"></p><div id="tg-btns" class="btnrow"></div><p id="tg-msg" aria-live="polite"></p><p>Score: <span id="tg-s">0</span> · Best streak: <span id="tg-b">0</span></p></div>
<script type="application/json" id="coaster-data">{tool_data()}</script>
<section><h2>How the quiz picks your coasters</h2>
<p>The quiz works through the same verified data as the rest of Coaster Map. First it removes every coaster your height does not meet, using each park's official minimum (and any maximum). Then it matches your answer on bravery to our intensity labels, which are worked out from each ride's RCDB height, speed, inversions and type, the same way for every park. If you say no to going upside down, any coaster with an inversion is dropped.</p>
<p>The results are a starting point, not a promise. Two rides with the same numbers can feel very different, so read the "How intense is it?" and "Who is it for?" notes on each coaster page before you queue.</p>
<p>New to coasters? Our <a href="/guides/best-first-roller-coasters/">best first roller coasters</a> guide explains how to build up from a family coaster, and the <a href="/guides/roller-coaster-types/">roller coaster types</a> guide explains launches, inverts, wooden coasters and more. For the trivia game, the <a href="/guides/tallest-roller-coasters/">tallest roller coasters</a> list is a good cheat sheet.</p></section>'''
    qf = [("Is the quiz based on real ride rules?", "Yes. It only uses height rules from official park sources and stats from RCDB. Coasters without a verified height rule are left out of the matches."),
          ("Why didn't my favourite coaster come up?", "It may be outside the thrill level you chose, have an inversion when you said no to going upside down, or have no verified height rule on Coaster Map yet."),
          ("Where do the trivia heights come from?", "From RCDB, the Roller Coaster DataBase. Height is the coaster's highest point above the ground.")]
    body += faq_html(qf)
    write("/quiz/", page("/quiz/", f"Which Roller Coaster Should You Ride? Quiz | {BRAND}", "A quick quiz that matches you with theme park roller coasters by height, thrill level and inversions, plus a coaster height trivia game.", body, [faq_ld(qf)], [("/", "Home"), ("/quiz/", "Coaster quiz")]))

def home():
    tallest = sorted([c for c in ALL if c["height"]], key=lambda c: -c["height"])[:5]
    fastest = sorted([c for c in ALL if c["speed"]], key=lambda c: -c["speed"])[:5]
    kid = sorted([c for c in ALL if c["hr"]], key=lambda c: hin(c["hr"]))[:6]
    li = lambda cs, f: "".join(f'<li><a href="{coaster_path(c)}">{E(c["name"])}</a> <span class="muted">({E(park_of(c)["short"])}, {f(c)})</span></li>' for c in cs)
    cards = "".join(f'<li class="card"><h3><a href="/parks/{p["slug"]}/">{E(p["name"])}</a></h3><p>{len(p["coasters"])} coaster{"s" if len(p["coasters"]) != 1 else ""} · {E(p["loc"].split(", ")[-1])}</p></li>' for p in PARKS)
    body = f'''<section class="hero"><h1>Every roller coaster at the big theme parks, mapped and explained</h1>
<p class="answer">Coaster Map answers the questions you have in the queue: <strong>how tall do you have to be, how fast does it go, how scary is it and where should you sit?</strong> {len(ALL)} coasters at {len(PARKS)} parks so far, with height rules from official park pages and stats from the Roller Coaster DataBase.</p>
<p class="btnrow"><a class="btn" href="/height-checker/">Check what my child can ride</a> <a class="btn alt" href="/map/">Open the coaster map</a> <a class="btn alt" href="/quiz/">Take the coaster quiz</a></p></section>
<h2>Park guides</h2><ul class="cards">{cards}</ul>
<div class="grid3"><section><h2>Tallest coasters</h2><ol>{li(tallest, lambda c: ft(c["height"]))}</ol></section>
<section><h2>Fastest coasters</h2><ol>{li(fastest, lambda c: mph(c["speed"]))}</ol></section>
<section><h2>Lowest height requirements</h2><ol>{li(kid, lambda c: hshort(c["hr"]))}</ol></section></div>
<section><h2>Popular guides</h2><ul class="cols"><li><a href="/guides/roller-coasters-for-42-inch-kids/">Coasters for 42-inch kids</a></li><li><a href="/guides/roller-coasters-for-48-inch-kids/">Coasters for 48-inch kids</a></li><li><a href="/guides/best-first-roller-coasters/">Best first roller coasters</a></li><li><a href="/guides/tallest-roller-coasters/">Tallest roller coasters</a></li><li><a href="/guides/fastest-roller-coasters/">Fastest roller coasters</a></li><li><a href="/guides/most-intense-roller-coasters/">Most intense roller coasters</a></li><li><a href="/guides/roller-coaster-types/">Roller coaster types explained</a></li><li><a href="/guides/how-to-not-be-scared-of-roller-coasters/">How to not be scared of roller coasters</a></li><li><a href="/guides/best-seat-on-a-roller-coaster/">Best seat on a roller coaster</a></li><li><a href="/guides/world-record-roller-coasters/">World record roller coasters</a></li><li><a href="/guides/roller-coaster-manufacturers/">Roller coaster manufacturers</a></li><li><a href="/guides/roller-coaster-glossary/">Roller coaster glossary</a></li><li><a href="/guides/">All guides</a></li></ul></section>
<section><h2>How we check facts</h2><p>Every height requirement links to the park page it came from, and every stat links to its RCDB entry. If we can't verify a number, we leave it out rather than guess. Read our <a href="/methodology/">sources and methods</a>.</p></section>'''
    write("/", page("/", f"{BRAND}: Roller Coaster Height Requirements, Stats & Maps", f"Height requirements, stats, intensity and best seats for {len(ALL)} roller coasters at Disney, Universal, Six Flags, Cedar Point, Kings Island, SeaWorld, Busch Gardens, Hersheypark, Dollywood, Knott's and more, with interactive park maps.", body))

def simple(path, title, desc, h1, inner, crumbs_name=None, legal=False, noindex=False):
    body = f'<article class="prose"><h1>{E(h1)}</h1>{inner}' + (f'<p class="legal-line">{LEGAL_LINE}</p>' if legal else "") + "</article>"
    write(path, page(path, title, desc, body, None, [("/", "Home"), (path, crumbs_name or h1)], legal=False, noindex=noindex))

def _affil():
    names = []
    for p in PARKS:
        for n in (p["name"], p["group"]):
            if n not in names: names.append(n)
    for n in ("Six Flags", "United Parks & Resorts", "Herschend Family Entertainment", "Oriental Land Company", "Ferrari"):
        if n not in names: names.append(n)
    return ", ".join(names)
def about_legal():
    global AFFIL
    AFFIL = _affil()
    simple("/about/", f"About {BRAND}", "What Coaster Map is, how we pick and check coaster facts, and what is coming next.", "About Coaster Map", f'''
<p>Coaster Map is an independent guide to the roller coasters at the world's big theme parks. Our goal is simple: one clear page for every coaster, answering the questions families and thrill seekers actually ask, such as the height requirement, how intense the ride is, and where to sit, plus a map of where each coaster sits in its park.</p>
<h2>What we cover</h2><p>We now cover {len(PARKS)} parks and {len(ALL)} coasters: {", ".join(p["name"] for p in PARKS[:-1])} and {PARKS[-1]["name"]}. We add parks when we can verify their height rules on official park sources, and we leave out any rule we cannot verify.</p>
<h2>How we work</h2><p>Height requirements come from official park pages. Ride statistics, opening dates, manufacturers and map positions come from the Roller Coaster DataBase (RCDB). We write every description ourselves. If a fact can't be verified, we leave it out. See <a href="/methodology/">sources and methods</a>.</p>
<h2>Independence</h2><p>Coaster Map is not affiliated with, endorsed by or sponsored by any park, operator or ride manufacturer. Park and ride names are used only to identify the rides we describe.</p>
<p>Spotted something out of date? <a href="/contact/">Let us know</a> and we'll check it.</p>''')
    simple("/methodology/", f"Sources and Methods | {BRAND}", "Where Coaster Map's height requirements, ride stats and map positions come from, and how often we check them.", "Sources and methods", f'''
<h2>Height requirements</h2><p>From official park pages: sixflags.com ride pages for {", ".join(p["name"] for p in PARKS if p["official"].startswith("https://www.sixflags.com"))}; the Enchanted Parks ride pages for Worlds of Fun, Valleyfair, Michigan's Adventure and Mid America Adventure; disneyworld.disney.go.com attraction pages for Magic Kingdom, EPCOT, Disney's Hollywood Studios and Disney's Animal Kingdom; Disneyland Resort attraction pages on disneyparks.disney.go.com for Disneyland Park and Disney California Adventure Park; the Busch Gardens Tampa Bay, Busch Gardens Williamsburg and SeaWorld Orlando roller coaster pages and ride pages, and the SeaWorld San Diego and SeaWorld San Antonio rides pages; dollywood.com, silverdollarcity.com, kennywood.com, lakecompounce.com and holidayworld.com ride pages; and, for Universal Studios Hollywood, the park's official Guide for Rider Safety and Accessibility. Outside North America we use each park's own official pages or guides: Europa-Park, Phantasialand, Efteling, Liseberg, Fuji-Q Highland and Shanghai Disneyland attraction pages; the Alton Towers and Pleasure Beach Resort (Blackpool) height restriction pages; Thorpe Park's official Ride Restrictions Guide; PortAventura World's height requirement pages for PortAventura Park and Ferrari Land; and Tokyo Disney Resort's official FAQ on attractions with height requirements. These parks set their rules in centimetres, so we show the official centimetre figure first with an approximate inch conversion, and the height checker compares your child's height against the rule in its own unit, so there is no rounding error at the line. Where a park adds an age rule or a companion age, we note it on the coaster page. Hersheypark groups rides by height category (for example 42 to 48 in) and its ride pages do not print the numbers, so for Hersheypark we use its official 2026 roller coaster guide on hersheypa.com and list the lowest height category allowed to ride. Where a park sets a companion rule (a shorter child may ride with someone older), we show both heights; companion age rules vary by park, so check at the ride. Universal Orlando's own ride pages could not be read by our checker, so for Epic Universe, Islands of Adventure and Universal Studios Florida we use Visit Orlando's roller coaster guide (Orlando's official tourism organisation, updated 1 Jun 2026) and will switch to Universal's pages when we can confirm them. The Barnstormer's requirement is also from Visit Orlando. All were checked {CHECKED}. Where no official figure was found ({", ".join(c["name"] for c in ALL if not c["hr"])}), we say so instead of guessing.</p>
<h2>Ride stats and positions</h2><p>Height, drop, speed, length, inversions, drop angle, g-force, opening date, manufacturer, model, type and map coordinates come from each coaster's <a href="https://rcdb.com/" rel="nofollow noopener">RCDB</a> entry. Our park lists include operating coasters only, as listed on RCDB on {CHECKED}. Dates of a ride's first opening follow RCDB; where a park dates a rebuilt version differently, the coaster page notes it.</p>
<h2>Intensity, who it suits and best seat</h2><p>Intensity labels use RCDB's scale (kiddie, family, thrill, extreme) and, where the park publishes one, the park's own thrill rating. "Who it suits" is drawn from those labels, the height rules and the number of inversions. Seat advice is general guidance based on how each style of coaster moves (for example, back rows crest drops faster); it is not a park rule.</p>
<h2>Maps</h2><p>Maps use <a href="https://leafletjs.com/">Leaflet</a> with tiles and map data © <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors. Pins are approximate.</p>
<h2>Updates</h2><p>Rules change, rides close and new coasters open. We re-check pages regularly and date every check. <a href="/contact/">Report an error</a>.</p>''', "Sources and methods")
    simple("/credits/", f"Credits | {BRAND}", "Credits and licences for software, map data and graphics used on Coaster Map.", "Credits", '''
<ul><li>Maps: <a href="https://leafletjs.com/">Leaflet</a> 1.9.4 (BSD 2-Clause licence, © Volodymyr Agafonkin and CloudMade), served from this site.</li>
<li>Map tiles and data: © <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors, available under the Open Database Licence.</li>
<li>Ride statistics and coordinates: facts compiled from the <a href="https://rcdb.com/" rel="nofollow noopener">Roller Coaster DataBase</a>, linked on every coaster page.</li>
<li>Logo and graphics: original artwork made for Coaster Map. The site uses no ride photos and no park or ride logos.</li>
<li>Height requirements: each park's official ride pages, guides or FAQs, credited and linked on every coaster page and listed on our <a href="/methodology/">sources and methods</a> page.</li>
<li>Writing: every description, explainer and guide is written by the Coaster Map editorial team. We do not copy park marketing text; short factual rules (such as a minimum height) are reported in our own words with a link to the source.</li></ul>
<h2>Park and ride names</h2><p>Park, ride and company names are trademarks of their owners and are used only to identify the rides we describe. Coaster Map is not affiliated with any of them.</p>
<h2>Corrections</h2><p>If you own or operate a park and see an out-of-date rule, please use our <a href="/contact/">contact form</a> and we will re-check the official source.</p>''')
    contact_inner = f'''<p>Questions, corrections or a park you'd like us to cover next? Send us a message and we'll reply by email. We read every correction and fix verified errors quickly.</p>
<h2>Reporting a correction</h2><p>The fastest way to get a fix is to include the page address, what looks wrong and a link to the official park page that shows the correct rule. We only change a height requirement when we can confirm it on an official park source, and we update the "last verified" date on the page when we do.</p>
<h2>Press, partnerships and parks</h2><p>Parks, operators and media can use the same form. Coaster Map does not accept payment for coverage or for changes to descriptions.</p>
<p class="form-status" id="contact-status" role="status" hidden></p>
<form class="contact" id="contact-form" action="{FORM_ENDPOINT}" method="POST">
<input type="hidden" name="_subject" value="Coaster Map contact"><input type="hidden" name="_template" value="table">
<input type="hidden" name="_next" value="https://coastermap.com/contact/?sent=1">
<input type="text" name="_honey" class="hp" tabindex="-1" autocomplete="off" aria-hidden="true">
<input type="hidden" name="_captcha" value="false">
<label for="name">Name</label><input id="name" type="text" name="name" required autocomplete="name">
<label for="email">Email</label><input id="email" type="email" name="email" required autocomplete="email">
<label for="message">Message</label><textarea id="message" name="message" rows="6" required></textarea>
<button class="btn" type="submit">Send message</button></form>
<p class="note">Messages are delivered by FormSubmit (formsubmit.co), a form-to-email service. See our <a href="/privacy/">privacy policy</a>.</p>'''
    simple("/contact/", f"Contact {BRAND}", "Contact Coaster Map with questions, corrections or park requests.", "Contact us", contact_inner, "Contact")
    simple("/newsletter/thanks/", f"Thanks for signing up | {BRAND}", "Coaster Map sign-up confirmation.", "Thanks for signing up", '<p id="nl-msg">You are on the list for new-coaster alerts. You can unsubscribe at any time.</p><p><a href="/">Back to Coaster Map</a></p>', "Sign-up", noindex=True)
    L = lambda: f'<p class="legal-line">{LEGAL_LINE}</p>'
    legal = {
    "/terms/": ("Terms of Use", f'''<p>Last updated {date_h(TODAY)}. These terms govern your use of coastermap.com ("Coaster Map", "we", "us"). Coaster Map is a trade name of Joshua Israel Ventures LLC, a Florida limited liability company. By using the site you agree to these terms.</p>
<h2>Information only</h2><p>Coaster Map provides general information about amusement rides for planning purposes. It is not safety, medical or professional advice. Ride rules, height requirements, health restrictions and operating status are set by each park and can change at any time. Always follow the park's posted rules and ride staff instructions. Do not rely on this site to decide whether a ride is safe for you or your child.</p>
<h2>Accuracy</h2><p>We work to keep information accurate and cite our sources, but we make no warranty that any information is complete, current or error free. Figures may differ from those posted at the park.</p>
<h2>Acceptable use</h2><p>You may view and share links to our pages for personal, non-commercial use. You may not scrape the site in bulk, republish our original text or data compilations without permission, misuse the contact or sign-up forms, or try to disrupt the site.</p>
<h2>Intellectual property</h2><p>Original text, design, data compilations and graphics on this site belong to Joshua Israel Ventures LLC. Park, ride and company names and trademarks belong to their owners and are used only to identify the rides described. Their use does not imply affiliation or endorsement.</p>
<h2>Third-party links and services</h2><p>We link to park websites, RCDB and other sources, and use third-party services (OpenStreetMap tiles, Cloudflare, FormSubmit). We are not responsible for their content or practices.</p>
<h2>Disclaimer of warranties and limitation of liability</h2><p>The site is provided "as is" and "as available". To the fullest extent permitted by law, Joshua Israel Ventures LLC disclaims all warranties, express or implied, and will not be liable for any indirect, incidental, special, consequential or punitive damages, or any loss or injury arising from your use of the site or any ride. Our total liability for any claim relating to the site is limited to US$100.</p>
<h2>Indemnity</h2><p>You agree to indemnify Joshua Israel Ventures LLC against claims arising from your misuse of the site or breach of these terms.</p>
<h2>Governing law</h2><p>These terms are governed by the laws of the State of Florida, United States, without regard to conflict-of-law rules. Any dispute will be resolved in the state or federal courts located in Florida, and you consent to their jurisdiction.</p>
<h2>Changes</h2><p>We may update these terms. The date above shows the latest version. Questions: use our <a href="/contact/">contact form</a>.</p>'''),
    "/privacy/": ("Privacy Policy", f'''<p>Last updated {date_h(TODAY)}. This policy explains how Coaster Map (coastermap.com), a trade name of Joshua Israel Ventures LLC, a Florida limited liability company, handles information.</p>
<h2>Analytics</h2><p>We use Cloudflare Web Analytics to count page views. It does not use cookies or local storage and does not track you across sites; it records basic, aggregated information such as the page visited, referrer, browser type and country.</p>
<h2>Contact form</h2><p>If you use the contact form, your name, email address and message are sent through FormSubmit (formsubmit.co), a form-to-email service, so we can reply. We use them only to respond and keep them only as long as needed.</p>
<h2>Email sign-up</h2><p>If you sign up for new-coaster alerts, we store your email address, the date and your consent in a database run on Cloudflare Workers. We use it only to send Coaster Map updates, never sell it, and delete it when you unsubscribe or ask us to. Every email will include a way to unsubscribe.</p>
<h2>Maps</h2><p>Interactive maps load tiles from OpenStreetMap's servers, which receive your IP address and browser details as part of the request. See the <a href="https://osmfoundation.org/wiki/Privacy_Policy">OpenStreetMap Foundation privacy policy</a>.</p>
<h2>Games and tools</h2><p>The height checker and quiz run in your browser. Your answers are not sent to us. The trivia game may save your best streak in your browser's local storage.</p>
<h2>Advertising</h2><p>To keep Coaster Map free, we show or may show ads served by Google (including Google AdSense) and other third-party advertising partners. Third-party vendors, including Google, use cookies to serve ads based on a user's prior visits to this website or other websites. Google's use of advertising cookies enables it and its partners to serve ads to you based on your visit to this site and/or other sites on the Internet.</p>
<p>You can opt out of personalised advertising by visiting <a href="https://www.google.com/settings/ads" rel="nofollow noopener" target="_blank">Google Ads Settings</a>, and you can opt out of some third-party vendors' use of cookies for personalised advertising at <a href="https://www.aboutads.info/choices/" rel="nofollow noopener" target="_blank">aboutads.info/choices</a> or, in Europe, <a href="https://www.youronlinechoices.eu/" rel="nofollow noopener" target="_blank">youronlinechoices.eu</a>. Learn more in <a href="https://policies.google.com/technologies/ads" rel="nofollow noopener" target="_blank">how Google uses cookies in advertising</a>. Where the law requires it (for example in the European Economic Area, the United Kingdom and Switzerland), we will ask for your consent through a certified consent management platform before any advertising cookies are set, and you can change your choice at any time.</p>
<h2>Cookies and similar technologies</h2><p>Cookies are small text files a website stores in your browser. Coaster Map itself sets no cookies for analytics. Advertising partners, if ads are shown, may set cookies or use similar identifiers as described above. The trivia game may store your best score in your browser's local storage, which never leaves your device. You can block or delete cookies in your browser settings; the site works without them.</p>
<h2>Hosting</h2><p>The site is hosted on GitHub Pages, which may log IP addresses for security and operations.</p>
<h2>Your rights</h2><p>You can ask us to access, correct or delete personal information we hold about you via the <a href="/contact/">contact form</a>. Residents of some US states and other countries may have additional rights, which we will honour.</p>
<h2>Children</h2><p>The site is for a general audience and is not directed to children under 13. We do not knowingly collect personal information from children. The height checker does not collect or store a child's height.</p>
<h2>Changes</h2><p>We will post any changes here with a new date.</p>'''),
    "/disclaimer/": ("Disclaimer", f'''<p>Last updated {date_h(TODAY)}.</p>
<h2>Not affiliated with any park</h2><p>Coaster Map is an independent site. It is not affiliated with, endorsed by or sponsored by any of the parks or operators it covers, including {E(AFFIL)}, by any ride manufacturer, or by the Roller Coaster DataBase. All park, ride and company names, logos and trademarks belong to their owners and are used only to identify the rides described.</p>
<h2>Ride rules change: check with the park</h2><p>Height requirements, maximum heights, companion rules, health and accessibility restrictions, opening dates and ride status are set by each park and can change without notice. The figures on this site were correct on the source page on the date shown, but the park's posted rules and ride staff always take priority. Check the park's official website or app before your visit and confirm at the ride entrance.</p>
<h2>No safety or medical advice</h2><p>Nothing on this site is safety, medical or professional advice. Descriptions of intensity, "who it suits" and seat suggestions are general opinions to help planning. Riders with health conditions, pregnancy, injuries or other concerns should follow the park's posted warnings and consult a doctor.</p>
<h2>Accuracy and corrections</h2><p>We cite our sources and leave out what we cannot verify, but errors can happen. Please <a href="/contact/">report errors</a> and we will correct verified mistakes promptly.</p>
<h2>Limitation of liability</h2><p>To the extent permitted by law, Joshua Israel Ventures LLC is not liable for any loss or injury arising from reliance on this site. See our <a href="/terms/">terms of use</a>.</p>'''),
    "/copyright/": ("Copyright and DMCA Policy", f'''<p>Last updated {date_h(TODAY)}. Original text, design, data compilations and graphics on Coaster Map are owned by Joshua Israel Ventures LLC. Facts such as ride statistics are cited to their sources. The site uses no ride photos at launch; any future images will be our own, licensed or properly credited.</p>
<h2>Reporting infringement</h2><p>If you believe material on this site infringes your copyright, send a notice through our <a href="/contact/">contact form</a> with: (1) your name and contact details; (2) a description of the copyrighted work; (3) the URL of the material on our site; (4) a statement that you have a good-faith belief the use is not authorised by the owner, its agent or the law; (5) a statement, under penalty of perjury, that the information is accurate and you are the owner or authorised to act for the owner; and (6) your physical or electronic signature. We will review notices promptly and remove or disable material where appropriate.</p>
<h2>Counter-notice</h2><p>If material you provided was removed and you believe this was a mistake, you may send a counter-notice through the contact form with the details required by 17 U.S.C. § 512(g).</p>
<h2>Repeat infringers</h2><p>We will act against repeat infringement where appropriate.</p>'''),
    "/ad-disclosure/": ("Advertising and Affiliate Disclosure", f'''<p>Last updated {date_h(TODAY)}. Coaster Map is free to use. To pay for running it, we plan to show advertising, for example through Google AdSense or a managed ad network. At the moment the site shows no ads and contains no affiliate links.</p>
<p>When ads appear they will be clearly separate from our content and labelled as advertising. Advertisers will have no influence over our coaster descriptions, ratings or recommendations. If we ever add affiliate links (for example to tickets or hotels), we may earn a commission at no extra cost to you, and we will label those links.</p>
<h2>How ads would be chosen</h2><p>Ads from networks such as Google AdSense are picked automatically by the network, sometimes based on cookies, as explained in our <a href="/privacy/">privacy policy</a>. We do not choose individual advertisers, and an ad appearing on a page is not an endorsement by Coaster Map. Ads will never be placed inside height tables or made to look like ride information.</p>
<h2>Editorial independence</h2><p>Stats come from RCDB and height rules from official park sources, as described on our <a href="/methodology/">sources and methods</a> page. Intensity labels, seat tips and "who it suits" notes are our own editorial guidance, written the same way for every coaster whatever its park.</p>
<p>No park, operator or ride manufacturer pays for coverage on Coaster Map. Questions: use our <a href="/contact/">contact form</a>.</p>'''),
    }
    for pth, (t, inner) in legal.items():
        body = f'<article class="prose"><h1>{E(t)}</h1>{inner}{L()}</article>'
        write(pth, page(pth, f"{t} | {BRAND}", f"{t} for Coaster Map (coastermap.com), the independent guide to theme park roller coasters.", body, None, [("/", "Home"), (pth, t)], legal=False))

def not_found():
    body = '<h1>Page not found</h1><p>That page has moved or never existed. Try the <a href="/parks/">park guides</a>, the <a href="/coasters/">full coaster list</a> or the <a href="/map/">coaster map</a>.</p>'
    html_ = page("/404.html", f"Page not found | {BRAND}", "Page not found.", body, noindex=True)
    open(os.path.join(ROOT, "404.html"), "w").write(html_)

def extras():
    open(os.path.join(ROOT, "CNAME"), "w").write("coastermap.com\n")
    open(os.path.join(ROOT, f"{INDEXNOW_KEY}.txt"), "w").write(INDEXNOW_KEY)
    bots = ["*", "Googlebot", "Bingbot", "Mediapartners-Google", "OAI-SearchBot", "ChatGPT-User", "GPTBot", "PerplexityBot", "Perplexity-User", "ClaudeBot", "Claude-SearchBot", "Claude-User", "Google-Extended", "Applebot", "Applebot-Extended", "DuckAssistBot", "Amazonbot", "CCBot"]
    open(os.path.join(ROOT, "robots.txt"), "w").write("".join(f"User-agent: {b}\nAllow: /\n\n" for b in bots) + f"Sitemap: {BASE_URL}sitemap.xml\n")
    sm = '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n' + "".join(f"<url><loc>{url(p)}</loc><lastmod>{m}</lastmod></url>\n" for p, m in PAGES) + "</urlset>\n"
    open(os.path.join(ROOT, "sitemap.xml"), "w").write(sm)
    llms = [f"# {BRAND}", "", f"> Coaster Map (coastermap.com) maps and describes the roller coasters at major theme parks: height requirements (from official park pages), stats (from RCDB), intensity, who each ride suits and seat guidance. {len(ALL)} coasters at {len(PARKS)} parks as of {CHECKED}.", "",
            "Not affiliated with any park. Ride rules change; confirm with the park.", "", "## Tools", f"- [Ride height checker]({url('/height-checker/')})", f"- [Coaster map]({url('/map/')})", f"- [Which coaster should you ride? quiz]({url('/quiz/')})", f"- [All coasters]({url('/coasters/')})", f"- [Sources and methods]({url('/methodology/')})", "", "## Parks"]
    for p in PARKS:
        llms.append(f"- [{p['name']}]({url('/parks/' + p['slug'] + '/')}): {len(p['coasters'])} coasters")
        for c in p["coasters"]:
            llms.append(f"  - [{c['name']}]({url(coaster_path(c))})" + (f": min height {hshort(c['hr'])}" if c["hr"] else ""))
    open(os.path.join(ROOT, "llms.txt"), "w").write("\n".join(llms) + "\n")
    open(os.path.join(ROOT, "favicon.svg"), "w").write(LOGO.replace('width="34" height="34" ', 'xmlns="http://www.w3.org/2000/svg" ').replace(' aria-hidden="true" focusable="false"', ""))

exec(compile(open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "guides.py")).read(), "guides.py", "exec"))
exec(compile(open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "parkguide.py")).read(), "parkguide.py", "exec"))
exec(compile(open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "explainers.py")).read(), "explainers.py", "exec"))
exec(compile(open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "coasterplus.py")).read(), "coasterplus.py", "exec"))
exec(compile(open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "specs.py")).read(), "specs.py", "exec"))

if __name__ == "__main__":
    build_guides()
    for p in PARKS:
        for c in p["coasters"]: coaster_page(c)
        park_page(p)
    parks_index(); all_coasters(); map_page(); height_checker(); quiz(); home(); about_legal(); not_found(); extras()
    print(len(PAGES), "pages")
