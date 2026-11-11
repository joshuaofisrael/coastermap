# ---------- per-coaster ride system, element list, trains and extra FAQs (batch 11) ----------
# Data: rcdb_details.json (built by details.py from cached RCDB coaster pages) and raw RCDB stats in rcdb.json.
_RAW = {}
for _p in json.load(open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "rcdb.json"))).values():
    for _c in _p["coasters"]: _RAW[_c["rcdb_url"]] = _c
_DX = json.load(open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "rcdb_details.json")))
for _c in ALL:
    _r = _RAW.get(_c["rcdb_url"], {}); _c["dx"] = _DX.get(_c["rcdb_url"].rsplit("/", 1)[1].split(".")[0], {})
    _d = (_r.get("stats", {}).get("Duration") or [None])[0]
    _m = re.match(r"(\d+):(\d\d)", _d or ""); _c["duration"] = (int(_m.group(1)) * 60 + int(_m.group(2))) if _m and (int(_m.group(1)) or int(_m.group(2))) else None
    _c["xstats"] = {k: _r.get("st", {}).get(k) for k in ("Airtime Points", "Bank Angle", "Crossings") if _r.get("st", {}).get(k)}
    if _c["dx"].get("former"):  # RCDB lists former names newest first; show them oldest first
        _f = []
        for _nm, *_ in reversed(_c["dx"]["former"]):
            if _nm and _nm not in (_c["rcdb_name"], _c["name"], "Etymology", "Name") and _nm not in _f: _f.append(_nm)
        _c["former"] = _f or None
    _a = (_c["dx"].get("arrangement") or "")
    _m = re.search(r"total of (\d+) riders", _a); _c["per_train"] = int(_m.group(1)) if _m and not _c["dx"].get("train_note") else None
    if _c["dx"].get("train_note"): _c["dx"].pop("arrangement", None)  # RCDB notes qualify the seat count, so leave the train layout out
    _m = re.search(r"(\d[\d,]*) riders per hour", _c["dx"].get("capacity") or ""); _c["capacity"] = int(_m.group(1).replace(",", "")) if _m else None

GLOSS = {"Chain Lift Hill": "chain-lift", "Vertical Chain Lift Hill": "chain-lift", "Loop": "vertical-loop", "Corkscrew": "corkscrew", "Double Corkscrew": "corkscrew",
         "Zero-G Roll": "zero-g-roll", "Zero-G Roll (variant)": "zero-g-roll", "Cobra Roll": "cobra-roll", "Block Brake": "block-brake", "Immelmann": "immelmann",
         "Jr. Immelmann": "immelmann", "Dive Loop": "dive-loop", "Helix": "helix", "Heartline Roll": "heartline-roll", "Over-Banked Curve": "overbanked-turn",
         "Zero-G Stall": "stall", "Top Hat - Outside": "top-hat", "Top Hat - Inside": "top-hat", "Pretzel Loop": "pretzel-loop", "Catch Car Lift Hill": "catch-car",
         "Booster Wheel Lift Hill": "lift-hill", "Cable Lift Hill": "lift-hill", "LSM Launch": "lim-and-lsm", "LIM Launch": "lim-and-lsm",
         "LSM Launch (rolling)": "lim-and-lsm", "LSM Launch (multi-pass)": "lim-and-lsm", "LIM Launch (multi-pass)": "lim-and-lsm", "Hydraulic Launch": "launch",
         "Tire Propelled Launch": "launch", "Tire Propelled Launch (rolling)": "launch", "Electric Winch Launch": "launch", "Flywheel Launch": "launch"}
LIFT_WORDS = {"Chain Lift Hill": "a chain lift hill", "Booster Wheel Lift Hill": "a lift hill driven by rubber booster wheels", "Cable Lift Hill": "a cable lift hill",
              "Vertical Chain Lift Hill": "a vertical chain lift", "Catch Car Lift Hill": "a catch-car lift hill", "LSM Lift Hill": "a magnetic (LSM) lift hill",
              "Elevator Lift": "an elevator lift", "Spiral Lift": "a spiral lift", "Catch Car Vertical Lift": "a vertical catch-car lift"}
def _launch_word(n):
    base = {"LSM": "a linear synchronous motor (LSM) launch", "LIM": "a linear induction motor (LIM) launch", "Hydraulic": "a hydraulic launch",
            "Tire": "a tyre-driven launch", "Electric": "an electric winch launch", "Flywheel": "a flywheel launch", "Compressed": "a compressed-air launch", "Pneumatic": "a compressed-air launch"}
    w = next((v for k, v in base.items() if n.startswith(k)), "a launch")
    if "(rolling)" in n: w += " that starts while the train is already moving"
    if "(multi-pass)" in n: w += " that the train passes through more than once"
    return w
def _el_li(name, extra, k):
    g = GLOSS.get(name)
    t = f'<a href="/guides/roller-coaster-glossary/#{g}">{E(name)}</a>' if g else E(name)
    if extra: t += f' <span class="muted">({E(extra)})</span>'
    if k > 1: t += f' <span class="muted">×{k}</span>'
    return f"<li>{t}</li>"
def propulsion(c):
    els = [e[0] for e in c["dx"].get("elements", [])]
    lifts = [e for e in els if e in LIFT_WORDS]; launches = [e for e in els if "Launch" in e]; boosts = [e for e in els if "Boost" in e]
    return lifts, launches, boosts
def prop_sentence(c):
    n = E(c["name"]); lifts, launches, boosts = propulsion(c); s = []
    ex = {e[0]: e[1] for e in c["dx"].get("elements", []) if e[1]}
    if launches:
        u = list(dict.fromkeys(launches))
        s.append(f"{n} starts with " + andlist([_launch_word(x) for x in u]) + (f" ({len(launches)} launch sections listed)" if len(launches) > 1 else "") + " rather than relying only on gravity from a lift.")
    if lifts:
        u = list(dict.fromkeys(lifts))
        s.append((_pick(c, "lft", ["Trains climb ", "The ride begins with ", "To gain height it uses "]) if not launches else "It also uses ") + andlist([LIFT_WORDS[x] + (f' ({ex[x]})' if ex.get(x) else "") for x in u]) + ".")
    if boosts:
        s.append(f"RCDB also lists {pl(len(boosts), 'booster section')} ({E(andlist(list(dict.fromkeys(boosts))))}) that add speed mid-course.")
    return " ".join(s)

def kidfit(c):
    h = c["hr"]
    if not h: return ""
    alone = [H for H in HEIGHTS if can(c, H)]; comp = [H for H in HEIGHTS if can_acc(c, H)]
    bits = []
    if alone: bits.append(f'it appears on our <a href="/guides/roller-coasters-for-{alone[0]}-inch-kids/">{alone[0]}-inch</a> list' + (f' and every taller list ({", ".join(str(x) for x in alone[1:])} in)' if len(alone) > 1 else "") + " as a ride-alone coaster")
    if comp: bits.append(f'a child of {andlist([str(x) for x in comp])} in fits its companion band, so they can ride with an adult rather than alone')
    if not alone and not comp: bits.append(f"its {hshort(h)} minimum is above all four of our kid-height lists (36, 42, 48 and 54 in), so it is for older children, teens and adults")
    return _pick(c, "kfx", ["On kid height: ", "For families checking heights: ", "Kid-height check: "]) + "; ".join(bits) + "."

def specs_html(c):
    dx = c["dx"]; n = E(c["name"]); p = park_of(c); parts = []
    ps = prop_sentence(c)
    els = dx.get("elements") or []
    if els:
        grp = []
        for nm, ex in els:
            if grp and grp[-1][0] == nm and grp[-1][1] == ex: grp[-1][2] += 1
            else: grp.append([nm, ex, 1])
        intro = f"RCDB lists one element for {n}:" if len(els) == 1 else _pick(c, "elx", [f"RCDB lists {pl(len(els), 'track element')} for {n}, shown here in the order RCDB lists them:",
                                  f"These are the {pl(len(els), 'element')} RCDB records on {poss(c['name'])} track, in RCDB's order:",
                                  f"Element by element, as listed on RCDB ({pl(len(els), 'entry', 'entries')}):"])
        parts.append(f"<p>{ps}</p>" if ps else "")
        parts.append(f'<p>{intro}</p><ol class="els">' + "".join(_el_li(a, b, k) for a, b, k in grp) + "</ol>")
        if c["twin"] and len(grp) < len(els) + 1: parts.append('<p class="note">It has two tracks, and RCDB may list an element once for each track.</p>')
        if c["inversions"]: parts.append(f'<p class="note">RCDB counts {c["inversions"]} inversion{"s" if c["inversions"] != 1 else ""} in total; some elements, such as a cobra roll, turn riders over more than once.</p>' if any(e[0] in ("Cobra Roll", "Batwing", "Double Corkscrew", "Double In-Line Twist", "Interlocking Corkscrews", "Sea Serpent", "Pretzel Knot") for e in els) else "")
    elif ps: parts.append(f"<p>{ps}</p>")
    rows = []
    if dx.get("arrangement"): rows.append(("Trains", dx["arrangement"]))
    if c["per_train"]: rows.append(("Riders per train", str(c["per_train"])))
    if dx.get("restraints"): rows.append(("Restraints", ", ".join(dx["restraints"])))
    if c["capacity"]: rows.append(("Hourly capacity (RCDB)", f'{c["capacity"]:,} riders per hour'))
    for k, v in c["xstats"].items(): rows.append((k, v))
    if dx.get("designers"): rows.append(("Designer" + ("s" if len(dx["designers"]) > 1 else ""), ", ".join(dx["designers"])))
    rel = [r for r in dx.get("relocations", []) if r[0] != p["name"] and r[0] != c["park_name"]]
    if rel: rows.append(("Previous locations", "; ".join(f"{a} (as {b})" for a, b in rel)))
    if rows:
        parts.append(f'<h3>{n} trains and ride system</h3><table class="stats"><tbody>' + "".join(f'<tr><th scope="row">{E(k)}</th><td>{E(v)}</td></tr>' for k, v in rows) + "</tbody></table>")
    if rel:
        parts.append(f"<p>{n} has been relocated: RCDB records it operating at " + andlist([f"{E(a)} as {E(b)}" for a, b in rel]) + f" before {E(p['short'])}.</p>")
    kf = kidfit(c)
    if kf: parts.append(f"<p>{kf}</p>")
    same_make = [x for x in ALL if x["make"] and x["make"] == c["make"] and x["park"] != c["park"] and x not in model_family(c)]
    if same_make and c["make"]:
        top = sorted(same_make, key=lambda x: (sim_dist(c, x), x["park"], x["slug"]))[:14]
        hsh = int(hashlib.md5((c["park"] + c["slug"] + "mk").encode()).hexdigest(), 16)
        pick = sorted(top, key=lambda x: int(hashlib.md5((str(hsh) + x["park"] + x["slug"]).encode()).hexdigest(), 16))[:4]
        mp = maker_path(c)
        parts.append(f"<p>{_pick(c, 'mkx', ['Other ' + E(c['make']) + ' coasters on ' + BRAND + ': ', 'More rides from ' + E(c['make']) + ' at other parks we cover: ', 'Elsewhere, ' + E(c['make']) + ' also built '])}" + andlist([f'<a href="{coaster_path(x)}">{E(x["name"])}</a> ({E(park_of(x)["short"])})' for x in pick]) + (f'. See <a href="{mp[0]}">all {E(c["make"])} coasters</a>.' if mp else ".") + "</p>")
    body = "".join(x for x in parts if x)
    if not body: return ""
    return f'<section aria-labelledby="spec-h"><h2 id="spec-h">{n} layout, trains and ride system</h2>{body}<p class="note">From the {rcdb_link(c)}; elements are RCDB\'s list, not a ride-by-ride account.</p></section>'

def detail_faqs(c):
    q = []; n = c["name"]; dx = c["dx"]
    if c["duration"]:
        m, s = divmod(c["duration"], 60)
        t = (f"{m} minute{'s' if m != 1 else ''}" if m else "") + (" " if m and s else "") + (f"{s} second{'s' if s != 1 else ''}" if s else "")
        q.append((f"How long is the ride on {n}?", f"RCDB lists a ride time of {t}" + (f" over {c['length']:,} ft of track" if isinstance(c["length"], int) else (f" over {c['length']} ft of track" if c["length"] else "")) + "."))
    elif c["length"]:
        q.append((f"How long is the track on {n}?", f"RCDB lists {c['length']:,} ft ({round(c['length'] * 0.3048):,} m) of track." if isinstance(c["length"], int) else f"RCDB lists {c['length']} ft of track."))
    lifts, launches, boosts = propulsion(c)
    if launches: q.append((f"Does {n} launch?", f"Yes. RCDB lists " + andlist([_launch_word(x) for x in dict.fromkeys(launches)]) + "."))
    elif lifts: q.append((f"How does {n} get up its first hill?", "RCDB lists " + andlist([LIFT_WORDS[x] for x in dict.fromkeys(lifts)]) + "; it has no launch."))
    if c["per_train"]: q.append((f"How many people ride {n} at once?", _pick(c, "fqt", [f"Up to {c['per_train']} per train, going by RCDB's train layout.", f"Each train carries {c['per_train']} riders, according to RCDB.", f"RCDB's train details give {c['per_train']} seats per train."]) + (f" RCDB lists an hourly capacity of about {c['capacity']:,} riders." if c["capacity"] else "")))
    if dx.get("restraints"): q.append((f"What restraints does {n} use?", f"RCDB lists: {', '.join(dx['restraints']).lower()}."))
    s, inv, h = c["scale"], c["inversions"], c["hr"]
    if s:
        facts_ = [f"RCDB classes it as {s.lower()}"]
        if inv is not None: facts_.append("it has no inversions" if inv == 0 else f"it goes upside down {inv} time{'s' if inv != 1 else ''}")
        if c["speed"]: facts_.append(f"it tops out at {c['speed']} mph")
        if h: facts_.append(f"the minimum height is {hshort(h)}")
        gentle = s in ("Kiddie", "Family") and not inv
        q.append((f"Is {n} good for first-time riders?", "On the numbers: " + "; ".join(facts_) + ". " + ("Those are the marks of a first-coaster ride: a gentle class and no inversions." if gentle else "Most first-timers start with a family-class ride with no inversions, so this is better as a step up than a first coaster." if s in ("Thrill", "Extreme") else "It is a small coaster, but it does turn riders upside down, so check that a nervous rider is happy with that.")))
    if dx.get("relocations"):
        rel = [r for r in dx["relocations"] if r[0] != c["park_name"]]
        if rel: q.append((f"Where did {n} operate before?", "RCDB records it at " + "; ".join(f"{a} (as {b})" for a, b in rel) + "."))
    return q
