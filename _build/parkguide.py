# Per-park "height requirements and ride guide" (replaces the old park page) and per-coaster comparisons.
# Exec'd inside build.py's namespace after guides.py.
SCALE_N = {"Kiddie": 0, "Family": 1, "Thrill": 2, "Extreme": 3}
def iscore(c):
    s = SCALE_N.get(c["scale"])
    if s is None: s = 0.5 if (c["height"] or 0) < 40 else 1.5 if (c["height"] or 0) < 120 else 2.5
    ht = min(c["height"], 420) / 420 * 30 if c["height"] else None
    sp = min(c["speed"], 130) / 130 * 30 if c["speed"] else None
    size = (ht + sp) if ht is not None and sp is not None else 2 * (ht if ht is not None else sp if sp is not None else 0)
    return (s * 100 + size + min(c["inversions"] or 0, 10) * 2.5 + (6 if launched(c) else 0) + (5 if (c["angle"] or 0) > 90 else 0) + c["slug"].__len__() * 1e-6)
def ilabel(c): return intensity(c)[0]
def hb(H): return f"{H} in ({cm(H)} cm)"
def can(c, H): h = c["hr"]; return bool(h) and hin(h) <= H + 1e-9 and not (h.get("max") and hin(h, "max") < H - 1e-9)
def can_acc(c, H): h = c["hr"]; return bool(h) and not can(c, H) and h.get("acc_min") is not None and h.get("acc_min") and hin(h, "acc_min") <= H + 1e-9 <= hin(h, "acc_max") + 2e-9
def andlist(xs): xs = list(xs); return xs[0] if len(xs) == 1 else ", ".join(xs[:-1]) + " and " + xs[-1] if xs else ""
def pl(n, w, ws=None): return f"{n} {w if n == 1 else (ws or w + 's')}"
def facts(c):
    b = []
    if c["height"]: b.append(ft(c["height"]) + " tall")
    if c["speed"]: b.append(mph(c["speed"]))
    if c["inversions"]: b.append(pl(c["inversions"], "inversion"))
    elif c["inversions"] == 0: b.append("no inversions")
    if c["gforce"]: b.append(f'{c["gforce"]} g')
    return ", ".join(b)
def pct(v, arr): return round(100 * sum(1 for x in arr if x < v) / len(arr)) if arr else 0

def park_analysis(p):
    cs = p["coasters"]; n = len(cs); out = []
    sc = {k: sum(1 for c in cs if c["scale"] == k) for k in SCALE_N}
    fam = sc["Kiddie"] + sc["Family"]; ext = sc["Extreme"]
    site_ext = round(100 * sum(1 for c in ALL if c["scale"] == "Extreme") / len(ALL))
    if n >= 3:
        mix = "family-leaning" if fam > n / 2 else "thrill-heavy" if ext + sc["Thrill"] > n * 0.6 and ext >= 2 else "balanced"
        out.append(f'RCDB classes {pl(fam, "coaster")} here as kiddie or family, {sc["Thrill"]} as thrill and {ext} as extreme, which makes {E(p["name"])} a <strong>{mix}</strong> park for roller coasters. '
                   + (f'Extreme coasters make up {round(100 * ext / n)}% of its lineup, against {site_ext}% across all {len(PARKS)} parks on {BRAND}.' if ext else f'None of its coasters are classed as extreme, against {site_ext}% of coasters across all {len(PARKS)} parks on {BRAND}.'))
    hv = sorted(hin(c["hr"]) for c in cs if c["hr"])
    if len(hv) >= 3:
        site = sorted(hin(c["hr"]) for c in ALL if c["hr"])
        med, smed = hv[len(hv) // 2], site[len(site) // 2]
        cmp_ = "higher than" if med > smed + 0.5 else "lower than" if med < smed - 0.5 else "about the same as"
        big = sum(1 for v in hv if v >= 48 - 1e-9)
        out.append(f'The typical (median) height requirement here is about {_n(med)} in, {cmp_} the {_n(smed)} in typical across the site, and {big} of the {len(hv)} coasters with a verified rule need a rider of at least 48 in (122 cm).')
    inv = [c for c in cs if c["inversions"]]; wood = [c for c in cs if c["material"] == "Wood" or "Wood" in c["tags"]]; lau = [c for c in cs if launched(c)]
    bits = []
    if n > 1: bits.append(f'{len(inv)} of the {n} go upside down' if inv else f'none of the {n} go upside down')
    if wood: bits.append(f'{pl(len(wood), "is a wooden coaster", "are wooden coasters")} ({andlist(E(c["name"]) for c in wood[:4])})')
    if lau: bits.append(f'{pl(len(lau), "uses", "use")} a launch instead of a lift hill ({andlist(E(c["name"]) for c in lau[:4])})')
    if bits: out.append("Of the ride types, " + "; ".join(bits) + ".")
    mk = {}
    for c in cs:
        if c["make"]: mk[c["make"]] = mk.get(c["make"], 0) + 1
    if mk and n >= 3:
        m, k = max(mk.items(), key=lambda x: (x[1], x[0]))
        if k >= 2: out.append(f'The most common builder is {E(m)}, with {k} of the coasters.')
    old = min((c for c in cs if c["opened"]), key=lambda c: c["opened"], default=None)
    if old and n > 1: out.append(f'The longest-serving coaster in the lineup is <a href="{coaster_path(old)}">{E(old["name"])}</a>, which opened in {old["opened"][:4]}.')
    for key, word in (("height", "tallest"), ("speed", "fastest")):
        top = sorted([c for c in ALL if c[key]], key=lambda c: -c[key])
        for c in cs:
            if c[key] and c in top[:15]:
                r = top.index(c) + 1
                out.append(f'<a href="{coaster_path(c)}">{E(c["name"])}</a> is the {"" if r == 1 else ordinal(r) + " "}{word} of the {len(top)} coasters on {BRAND} with a listed {"height" if key == "height" else "top speed"}.'); break
    if any(c["hr"] and metric(c["hr"]) for c in cs):
        out.append(f'{E(p["name"])} publishes its height rules in centimetres. We show the official centimetre figure with an inch conversion, and every list on this page compares in centimetres, so a child exactly at the line counts as tall enough.')
    return out
def ordinal(n): return f'{n}{"th" if 10 <= n % 100 <= 20 else {1: "st", 2: "nd", 3: "rd"}.get(n % 10, "th")}'

def ladder(cs):
    v = sorted([c for c in cs if c["hr"]], key=iscore)
    if len(v) < 2: return []
    first = next((c for c in v if c["inversions"] == 0), v[0])
    rest = [c for c in v if c is not first]
    mid = [c for c in rest if iscore(c) > iscore(first) and c["scale"] != "Extreme"]
    step = mid[len(mid) // 2] if mid else None
    big = v[-1] if v[-1] not in (first, step) else None
    out = [("Start here", first, "the gentlest coaster here by our intensity ranking" + (", with no inversions" if first["inversions"] == 0 else ""))]
    if step: out.append(("Step up", step, "a bigger ride that stops short of the park's most extreme coasters"))
    if big: out.append(("The big one", big, "the most intense coaster in the park"))
    return out

def park_page(p):
    path = f'/parks/{p["slug"]}/'
    cs = p["coasters"]; n = len(cs); PN = E(p["name"])
    ver = [c for c in cs if c["hr"]]
    tall = max((c for c in cs if c["height"]), key=lambda c: c["height"], default=None)
    fast = max((c for c in cs if c["speed"]), key=lambda c: c["speed"], default=None)
    lowest = min(ver, key=lambda c: hin(c["hr"]), default=None)
    highest = max(ver, key=lambda c: hin(c["hr"]), default=None)
    ranked = sorted(cs, key=lambda c: -iscore(c))
    noinv = [c for c in cs if c["inversions"] == 0]
    cnt = {H: [c for c in cs if can(c, H)] for H in HEIGHTS}
    fm = p.get("former")
    # lead
    lead = f'{PN}' + (f' (formerly {E(fm)})' if fm else "") + f' in {E(p["loc"])} has <strong>{pl(n, "operating roller coaster")}</strong> on RCDB.'
    if lowest and highest and lowest is not highest:
        lead += f' Height requirements run from <strong>{hs(lowest["hr"])}</strong> on <a href="{coaster_path(lowest)}">{E(lowest["name"])}</a> to <strong>{hs(highest["hr"])}</strong> on <a href="{coaster_path(highest)}">{E(highest["name"])}</a>.'
    elif lowest: lead += f' The height requirement is <strong>{hs(lowest["hr"])}</strong> on <a href="{coaster_path(lowest)}">{E(lowest["name"])}</a>.'
    if ver and n > 1: lead += " Riding alone, a 42-inch (107 cm) child can ride " + f'{len(cnt[42])}, a 48-inch (122 cm) child {len(cnt[48])} and a 54-inch (137 cm) rider {len(cnt[54])} of them.'
    # table of heights
    def hrow(c):
        h = c["hr"]
        return (f'<tr><th scope="row"><a href="{coaster_path(c)}">{E(c["name"])}</a></th><td>{E(hs(h)) if h else "Not verified"}</td><td>{E(rngs(h)) if h and h.get("acc_min") else "None"}</td>'
                f'<td>{E(hs(h, "max")) if h and h.get("max") else "None"}</td><td>{E(ilabel(c))}</td><td>{c["inversions"] if c["inversions"] is not None else "n/a"}</td></tr>')
    hsort = sorted(cs, key=lambda c: (0, hin(c["hr"])) if c["hr"] else (1, 0))
    notes = [c for c in ver if c["hr"].get("note")]
    htable = ('<div class="tablewrap"><table class="list"><thead><tr><th scope="col">Coaster</th><th scope="col">Ride alone</th><th scope="col">With a companion</th><th scope="col">Maximum</th><th scope="col">Intensity</th><th scope="col">Inversions</th></tr></thead><tbody>'
              + "".join(hrow(c) for c in hsort) + "</tbody></table></div>")
    if notes: htable += "<h3>Other rider rules stated by the park</h3><ul>" + "".join(f'<li><a href="{coaster_path(c)}">{E(c["name"])}</a>: {E(c["hr"]["note"])}</li>' for c in notes) + "</ul>"
    unv = [c for c in cs if not c["hr"]]
    if unv: htable += f'<p class="note">We could not verify a height rule on an official {PN} source for {andlist(E(c["name"]) for c in unv)}, so ' + ("it is" if len(unv) == 1 else "they are") + ' left out of the height lists below. Ask the park before you queue.</p>'
    # bands
    bands = ""; prev = set(); gains = []
    if ver and n > 1:
        for H in HEIGHTS:
            ok = cnt[H]; acc = [c for c in cs if can_acc(c, H)]; new = [c for c in ok if c["slug"] not in prev]
            gains.append((len(new), H, new))
            too = [c for c in ver if not can(c, H) and not can_acc(c, H) and hin(c["hr"]) > H]
            s = f'<h3>{hb(H)} tall</h3><p>'
            if ok:
                s += f'A {H}-inch rider meets the ride-alone minimum on <strong>{len(ok)} of {len(ver)}</strong> coasters with a verified rule'
                s += (f', {len(new)} more than at the height below: ' + andlist(f'<a href="{coaster_path(c)}">{E(c["name"])}</a>' for c in new) + ".") if new and prev else (": " + andlist(f'<a href="{coaster_path(c)}">{E(c["name"])}</a>' for c in ok) + ".")
            else: s += f'A {H}-inch rider is below the ride-alone minimum on every coaster here.'
            if acc: s += " With a companion they can also ride " + andlist(f'<a href="{coaster_path(c)}">{E(c["name"])}</a> ({rngs(c["hr"])})' for c in acc) + "."
            if too: s += f' Still too short for {pl(len(too), "coaster")}' + (f', the nearest being {E(min(too, key=lambda c: hin(c["hr"]))["name"])} at {hs(min(too, key=lambda c: hin(c["hr"]))["hr"])}.' if too else ".")
            else: s += " That covers every coaster with a verified rule here."
            bands += s + "</p>"; prev = {c["slug"] for c in ok}
        g = max(gains, key=lambda x: (x[0], -x[1]))
        if g[0]: bands = f'<p>At {PN} the biggest single step is reaching <strong>{hb(g[1])}</strong>, which opens up {pl(g[0], "more coaster")}' + (" than the height below" if g[1] != HEIGHTS[0] else "") + '. Measure at home in the shoes your child will wear, since parks measure at the ride entrance and a child even slightly under the line is turned away.</p>' + bands
        maxs = [c for c in ver if c["hr"].get("max")]
        if maxs: bands += "<h3>Maximum heights</h3><p>Some rides are built for children and have an upper limit: " + andlist(f'<a href="{coaster_path(c)}">{E(c["name"])}</a> (up to {hs(c["hr"], "max")})' for c in maxs) + ". Taller riders are turned away for restraint fit, not age.</p>"
    accs = [c for c in ver if c["hr"].get("acc_min")]
    comp = ""
    if accs or notes:
        comp = f'<section aria-labelledby="cmp-h"><h2 id="cmp-h">Companion rules at {PN}</h2><p>These are the rules {PN} states on its official pages for riding with a companion or other conditions. Who counts as a companion (age or height) is set by the park; check the linked source for the exact wording.</p><ul>'
        comp += "".join(f'<li><a href="{coaster_path(c)}">{E(c["name"])}</a>: riders {rngs(c["hr"])} tall must ride with a companion.</li>' for c in accs)
        comp += "".join(f'<li><a href="{coaster_path(c)}">{E(c["name"])}</a>: {E(c["hr"]["note"])}</li>' for c in notes if c not in accs) + "</ul></section>"
    # intensity ranking
    rk = "".join(f'<li><a href="{coaster_path(c)}">{E(c["name"])}</a> <span class="muted">{E(ilabel(c))}' + (f' · {facts(c)}' if facts(c) else "") + "</span></li>" for c in ranked)
    rank_html = (f'<section aria-labelledby="rk-h"><h2 id="rk-h">{PN} roller coasters ranked, most intense first</h2>'
                 f'<p>We rank the coasters by intensity using only measurable facts: RCDB\'s kiddie, family, thrill or extreme class first, then height, top speed, inversions, launches and beyond-vertical drops. It is a guide to how hard each ride hits, not a review of how good it is.</p><ol>{rk}</ol>'
                 + (f'<p>By this measure the scariest coaster at {PN} is <a href="{coaster_path(ranked[0])}">{E(ranked[0]["name"])}</a> and the gentlest is <a href="{coaster_path(ranked[-1])}">{E(ranked[-1]["name"])}</a>.</p>' if n > 1 else "") + "</section>")
    # records
    recs = []
    for lab, key, fmt in (("Tallest", "height", ftm), ("Fastest", "speed", mphk), ("Longest track", "length", lambda v: f"{ft(v)}"), ("Most inversions", "inversions", lambda v: str(v)), ("Steepest drop", "angle", lambda v: f"{v}°"), ("Highest g-force", "gforce", lambda v: f"{v} g")):
        top = max((c for c in cs if c[key]), key=lambda c: c[key], default=None)
        if top: recs.append(f'<tr><th scope="row">{lab}</th><td><a href="{coaster_path(top)}">{E(top["name"])}</a></td><td>{E(fmt(top[key]))}</td></tr>')
    rec_html = f'<section aria-labelledby="rec-h"><h2 id="rec-h">Tallest, fastest and longest at {PN}</h2><div class="tablewrap"><table class="list"><thead><tr><th scope="col">Record</th><th scope="col">Coaster</th><th scope="col">Figure (RCDB)</th></tr></thead><tbody>{"".join(recs)}</tbody></table></div></section>' if recs and n > 1 else ""
    # first-timers
    lad = ladder(cs)
    ft_html = ""
    if lad:
        ft_html = f'<section aria-labelledby="ft-h"><h2 id="ft-h">Best coasters at {PN} for first-timers</h2><p>Nervous riders usually do best working up in steps. Here is a three-step plan for {PN}, picked from our intensity ranking and the official height rules:</p><ol>'
        ft_html += "".join(f'<li><strong>{st}:</strong> <a href="{coaster_path(c)}">{E(c["name"])}</a>, {why} ({hshort(c["hr"])} minimum' + (f'; {facts(c)}' if facts(c) else "") + ").</li>" for st, c, why in lad)
        ft_html += '</ol><p>Sit in the middle of the train for the softest ride, and watch a few cycles from the queue first. Our <a href="/guides/best-first-roller-coasters/">best first roller coasters</a> guide has more tips.</p></section>'
    analysis = park_analysis(p)
    ana_html = f'<section aria-labelledby="an-h"><h2 id="an-h">What the coasters at {PN} are like</h2>' + "".join(f"<p>{x}</p>" for x in analysis) + "</section>" if analysis else ""
    # FAQ
    faqs = []
    if fm: faqs.append((f'Is {p["name"]} the same park as {fm}?', f'Yes. {p["name"]} in {p["loc"]} is the park formerly called {fm}; {p["former_note"]} (checked {CHECKED}).'))
    if ver: faqs.append((f'What are the height requirements at {p["name"]}?', (f'Roller coaster height requirements at {p["name"]} run from {hs(lowest["hr"])} ({lowest["name"]}) to {hs(highest["hr"])} ({highest["name"]}), according to official park sources checked {CHECKED}.' if lowest is not highest else f'{lowest["name"]} requires riders to be at least {hs(lowest["hr"])}, according to the park (checked {CHECKED}).') + " Rules are checked at each ride entrance."))
    faqs.append((f'How many roller coasters does {p["name"]} have?', f'{p["name"]} has {pl(n, "operating roller coaster")} according to RCDB, checked {CHECKED}.'))
    if n > 1: faqs.append((f'What is the scariest roller coaster at {p["name"]}?', f'By our intensity ranking, which uses RCDB class, height, speed, inversions and launches, it is {ranked[0]["name"]}' + (f' ({facts(ranked[0])})' if facts(ranked[0]) else "") + '.'))
    if tall: faqs.append((f'What is the tallest roller coaster at {p["name"]}?', f'{tall["name"]}, at {ft(tall["height"])} tall (RCDB).'))
    if fast: faqs.append((f'What is the fastest roller coaster at {p["name"]}?', f'{fast["name"]}, with a top speed of {mph(fast["speed"])} (RCDB).'))
    if lad: faqs.append((f'What is the best coaster at {p["name"]} for first-timers?', f'{lad[0][1]["name"]} is the gentlest coaster here by our intensity ranking, with a {hs(lad[0][1]["hr"])} minimum height.'))
    for th in (42, 48):
        ok = [c["name"] for c in cnt[th]]
        if ver and n > 1: faqs.append((f'What can a {th}-inch child ride at {p["name"]}?', (f'Riding alone, a {th}-inch ({cm(th)} cm) child meets the official minimum on: ' + ", ".join(ok) + '.' if ok else f'No coaster here has a ride-alone minimum of {th} in or less.') + (" With a companion they can also ride " + ", ".join(c["name"] for c in cs if can_acc(c, th)) + "." if any(can_acc(c, th) for c in cs) else "")))
    if noinv and n > 1: faqs.append((f'Which coasters at {p["name"]} do not go upside down?', ", ".join(c["name"] for c in noinv) + " have no inversions, per RCDB."))
    srcset = sorted({c["hr"]["src"] for c in ver})
    body = f'''<h1>{PN} height requirements and roller coasters ranked</h1><p class="sub">{("Formerly " + E(fm) + " · ") if fm else ""}{E(p["loc"])} · {pl(n, "coaster")}</p>{byline()}
<p class="answer">{lead}</p>
{ana_html}
<section aria-labelledby="hr-h"><h2 id="hr-h">{PN} height requirements for every coaster</h2>{htable}</section>
{f'<section aria-labelledby="hb-h"><h2 id="hb-h">What can my child ride at {PN}? By height</h2>{bands}<p>For a personal list, try the <a href="/height-checker/">ride height checker</a>.</p></section>' if bands else ""}
{comp}
{rank_html if n > 1 else ""}
{ft_html}
{rec_html}
{map_block(cs, 440)}
<h2>Every coaster at {PN}: full stats</h2>{coaster_table(sorted(cs, key=lambda c: -(c["height"] or 0)))}
{group_html(p)}
{faq_html(faqs)}
{related_html(p=p)}<section class="sources"><h2>Sources</h2><ul><li><a href="{p["rcdb_url"]}" rel="nofollow noopener" target="_blank">RCDB: {PN}</a>: operating coaster list, stats and map positions.</li>{"".join(f"<li>{src_link(s)}: height requirements (checked {CHECKED}).</li>" for s in srcset)}<li><a href="{p["official"]}" rel="nofollow noopener" target="_blank">{PN} official site</a>: hours and ride status.</li></ul><p class="note">Intensity labels, rankings and first-timer picks are {BRAND} editorial guidance built from the facts above, not park rules. Last checked {CHECKED}.</p></section>'''
    old_ld = PARK_LD(p)
    ld = [*old_ld, {"@context": "https://schema.org", "@type": "ItemList", "name": f'{p["name"]} roller coasters ranked by intensity', "numberOfItems": n, "itemListOrder": "https://schema.org/ItemListOrderDescending",
           "itemListElement": [{"@type": "ListItem", "position": i + 1, "url": url(coaster_path(c)), "name": c["name"]} for i, c in enumerate(ranked)]}, faq_ld(faqs)]
    title = None
    if n == 1 and not fm: TT = [f'{p["name"]} Height Requirements & Roller Coaster Guide | {BRAND}', f'{p["short"]} Height Requirements & Coaster Guide | {BRAND}', f'{p["short"]} Height Requirements | {BRAND}']
    else: TT = None
    for t in TT or ([f'{p["name"]} Height Requirements & Coasters Ranked | {BRAND}', f'{p["short"]} Height Requirements & Coasters Ranked | {BRAND}', f'{p["short"]} Height Requirements & Coasters Ranked',
               f'{p["short"]} Height Requirements & Ride Guide | {BRAND}', f'{p["short"]} Height Requirements | {BRAND}'] if not fm else
              [f'{p["name"]} (ex {fm}) Height Requirements', f'{p["name"]} Height Requirements & Coasters Ranked']):
        if len(t) <= 70: title = t; break
    desc = (f'Height requirements for all {n} roller coasters at {p["name"]}' if n > 1 else f'Height requirement for the roller coaster at {p["name"]}') + (f' (formerly {fm})' if fm else "") + (', what 42 and 48-inch kids can ride, coasters ranked by intensity and first-timer picks.' if n > 1 else ", with stats and who it suits.")
    write(path, page(path, title, desc, body, ld, [("/", "Home"), ("/parks/", "Parks"), (path, p["name"])]))

# ---------- coaster comparisons ----------
def sim_dist(a, b):
    d = abs((a["height"] or 0) - (b["height"] or 0)) / 60 + abs((a["speed"] or 0) - (b["speed"] or 0)) / 15 + abs((a["inversions"] or 0) - (b["inversions"] or 0)) / 2
    d += 0 if a["scale"] == b["scale"] else 2
    d += 0 if a["material"] == b["material"] else 1.5
    d += 0 if a["design"] == b["design"] else 1
    d += 0 if launched(a) == launched(b) else 1.5
    d -= 0.8 if a["make"] and a["make"] == b["make"] else 0
    d -= 0.8 if a["model"] and a["model"] == b["model"] else 0
    return d
def shared(a, b):
    s = []
    if a["model"] and a["model"] == b["model"] and a["make"] == b["make"]: s.append(f'the same {E(a["make"])} {E(a["model"])} model')
    elif a["make"] and a["make"] == b["make"]: s.append(f'also built by {E(a["make"])}')
    if a["material"] == "Wood" and b["material"] == "Wood": s.append("also wooden")
    if launched(a) and launched(b): s.append("also launched")
    if a["design"] == b["design"] and a["design"] not in (None, "", "Sit Down"): s.append(f'also {E(a["design"].lower())}')
    if a["scale"] == b["scale"] and a["scale"]: s.append(f'same {E(a["scale"].lower())} class')
    return s[:2]
def compare_html(c):
    p = park_of(c); cs = p["coasters"]; out = []
    sib = sorted(cs, key=iscore)
    if len(cs) > 1:
        i = sib.index(c); r = len(cs) - i
        txt = f'On our intensity ranking {E(c["name"])} is <strong>number {r} of {len(cs)}</strong> at {E(p["name"])}, where 1 is the most intense.'
        if c["height"]:
            hl = sorted([x for x in cs if x["height"]], key=lambda x: -x["height"])
            txt += f' It is the {"tallest" if hl[0] is c else ordinal(hl.index(c) + 1) + " tallest"} of the park\'s {len(hl)} coasters with a listed height.'
        out.append(f"<p>{txt}</p>")
        nb = []
        if i > 0: lo = sib[i - 1]; nb.append(f'If it sounds like too much, the next gentler coaster here is <a href="{coaster_path(lo)}">{E(lo["name"])}</a>' + (f' ({facts(lo)}' + (f'; {hshort(lo["hr"])} minimum' if lo["hr"] else "") + ")" if facts(lo) else "") + ".")
        if i < len(sib) - 1: hi = sib[i + 1]; nb.append(f'Ready for more? The next step up is <a href="{coaster_path(hi)}">{E(hi["name"])}</a>' + (f' ({facts(hi)}' + (f'; {hshort(hi["hr"])} minimum' if hi["hr"] else "") + ")" if facts(hi) else "") + ".")
        if nb: out.append("<p>" + " ".join(nb) + "</p>")
    hs_ = [x["height"] for x in ALL if x["height"]]; ss = [x["speed"] for x in ALL if x["speed"]]
    bits = []
    if c["height"]: bits.append(f'taller than {pct(c["height"], hs_)}%')
    if c["speed"]: bits.append(f'faster than {pct(c["speed"], ss)}%')
    if bits: out.append(_pick(c, "acr", [f'<p>Across all {len(ALL)} coasters on {BRAND}, {E(c["name"])} is {andlist(bits)} of those with a listed figure.</p>', f'<p>Measured against every coaster on {BRAND} with a listed figure, {E(c["name"])} is {andlist(bits)} of them.</p>', f'<p>Site-wide, {E(c["name"])} is {andlist(bits)} of the {len(ALL)} coasters we cover that have a listed figure.</p>']))
    others = sorted([x for x in ALL if x["park"] != c["park"] and x is not c and x["name"] != c["name"]], key=lambda x: (sim_dist(c, x), x["park"], x["slug"]))
    fam = {id(x) for x in model_family(c)}
    others = [x for x in others if id(x) not in fam] or others
    picks, seenp = [], set()
    local = [x for x in others if c["lat"] and x["lat"] and _dist(c, x) < 700000]
    for x in local[:1] + others:
        if x["park"] in seenp: continue
        picks.append(x); seenp.add(x["park"])
        if len(picks) == 3: break
    if picks:
        li = "".join(f'<li><a href="{coaster_path(x)}">{E(x["name"])}</a> at <a href="/parks/{x["park"]}/">{E(park_of(x)["name"])}</a>: ' + "; ".join(shared(c, x) + ([facts(x)] if facts(x) else [])) + (f'; {hshort(x["hr"])} minimum' if x["hr"] else "") + "</li>" for x in picks)
        out.append(f'<h3>If you liked {E(c["name"])}, try</h3><p>{_pick(c, "lk", ["The closest matches at other parks on " + BRAND + ", by type, class, builder, height, speed and inversions, with one pick within about 700 km where there is one:", "Similar rides elsewhere on " + BRAND + ", matched on type, class, builder, size and inversions (the first is the nearest good match within about 700 km, where there is one):"])}</p><ul>{li}</ul>')
    return f'<section aria-labelledby="cmpx-h"><h2 id="cmpx-h">How {E(c["name"])} compares</h2>' + "".join(out) + "</section>"
def PARK_LD(p):
    return [{"@context": "https://schema.org", "@type": "AmusementPark", "name": p["name"], "url": p["official"], **({"alternateName": p["former"]} if p.get("former") else {}),
             "address": {"@type": "PostalAddress", "addressLocality": p["loc"].split(", ")[-2], "addressRegion": p["state"], "addressCountry": p["country"]}}]

def group_html(p):
    sib = [q for q in PARKS if q["group"] == p["group"] and q is not p]
    if not sib: return ""
    allp = [p] + sib
    def rng(q):
        v = [c for c in q["coasters"] if c["hr"]]
        if not v: return "not verified"
        lo, hi = min(v, key=lambda c: hin(c["hr"])), max(v, key=lambda c: hin(c["hr"]))
        return hshort(lo["hr"]) if lo is hi else f'{hshort(lo["hr"])} to {hshort(hi["hr"])}'
    rows = "".join(f'<tr><th scope="row">' + (E(q["name"]) if q is p else f'<a href="/parks/{q["slug"]}/">{E(q["name"])}</a>') + f'</th><td>{len(q["coasters"])}</td><td>{E(rng(q))}</td><td>{sum(1 for c in q["coasters"] if can(c, 42))}</td><td>{sum(1 for c in q["coasters"] if can(c, 48))}</td></tr>' for q in allp)
    t42 = sum(1 for q in allp for c in q["coasters"] if can(c, 42)); t48 = sum(1 for q in allp for c in q["coasters"] if can(c, 48)); tot = sum(len(q["coasters"]) for q in allp)
    resort = any(w in p["group"] for w in ("Resort", "World", "Walt Disney"))
    intro = (f'{E(p["name"])} is one of {len(allp)} {E(p["group"])} parks on {BRAND}. Across all of them there are {tot} coasters; a 42-inch (107 cm) child can ride {t42} alone and a 48-inch (122 cm) child {t48}, so if your family is splitting days between parks, this table shows where shorter riders get the most choice.'
             if resort else f'{E(p["name"])} is one of {len(allp)} {E(p["group"])} parks on {BRAND}. The table compares their coaster lineups and how many rides shorter children can take on alone.')
    return f'<section aria-labelledby="grp-h"><h2 id="grp-h">How {E(p["name"])} compares with other {E(p["group"])} parks</h2><p>{intro}</p><div class="tablewrap"><table class="list"><thead><tr><th scope="col">Park</th><th scope="col">Coasters</th><th scope="col">Height range</th><th scope="col">Rides at 42 in</th><th scope="col">Rides at 48 in</th></tr></thead><tbody>{rows}</tbody></table></div></section>'
