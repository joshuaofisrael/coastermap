# ---------- per-coaster data-driven writing (batch 10) ----------
import hashlib, math
def poss(s): return E(s) + ("'" if s.endswith("s") else "'s")
def _pick(c, key, opts):
    h = int(hashlib.md5((c["park"] + c["slug"] + key).encode()).hexdigest(), 16)
    return opts[h % len(opts)]
def _ord(n): return ordinal(n) if n > 1 else ""
GENERIC_MODELS = {None, "Custom", "Wooden Coasters / Custom", "Other"}
def model_family(c):
    m = c["model"]
    if not m or m in GENERIC_MODELS or m.endswith("/ Custom") or "Custom" in m: return []
    return [x for x in ALL if x["model"] == m and x["make"] == c["make"]]

def feel_html(c):
    p = park_of(c); n = E(c["name"]); out = []
    H, D, S, L, I, A, G = c["height"], c["drop"], c["speed"], c["length"], c["inversions"], c["angle"], c["gforce"]
    s = []
    if H and L:
        r = L / H
        if r >= 30: s.append(_pick(c, "lay", [f"With {L:,} ft of track for a {H} ft structure, {n} is a long, low-slung ride: most of the time is spent carving through turns and small hills rather than on one big plunge.", f"{n} spreads {L:,} ft of track across a layout only {H} ft tall, so expect a ride that keeps moving through turns and hills instead of saving everything for one drop."]))
        elif r <= 9: s.append(_pick(c, "lay", [f"{n} packs its {L:,} ft of track into a tall, compact footprint ({H} ft high), so the big moments come quickly and close together.", f"For a {H} ft ride, {L:,} ft of track is short: {n} is compact and vertical, with little time between its main elements."]))
        else: s.append(_pick(c, "lay", [f"At {H} ft tall with {L:,} ft of track, {n} balances height and length: a main drop followed by a full circuit of hills and turns.", f"{n} pairs a {H} ft structure with {L:,} ft of track, a classic proportion that gives a clear first drop and a full layout after it."]))
    if H and D and D > H + 5: s.append(f"Its {D} ft drop is longer than its {H} ft height, which means the first drop falls below the level where it starts, into a trench, tunnel or down a hillside.")
    elif H and D and not launched(c) and D < H * 0.7 and H > 30: s.append(f"RCDB lists a {D} ft drop against a {H} ft height, so the first drop does not fall the full height of the structure.")
    if S and D and D > 20:
        vff = math.sqrt(2 * 9.81 * D * 0.3048) * 2.237
        if launched(c) and S > vff * 1.15: s.append(f"A free fall of {D} ft would give about {round(vff)} mph; {n} reaches {S} mph because its launch adds the speed rather than the drop.")
    if A and A > 90: s.append(f"The steepest drop is {A}°, past vertical, so riders tip slightly beyond straight down.")
    elif A and A >= 80: s.append(f"At {A}°, the steepest drop is close to vertical.")
    if I and L:
        dens = I / (L / 1000)
        if dens >= 2.5: s.append(f"With {I} inversions in {L:,} ft, it flips riders roughly every {round(L / I):,} ft, one of the denser inversion sequences you will find.")
        elif I >= 1: s.append(f"It goes upside down {I} time{'s' if I != 1 else ''} across {L:,} ft of track, so inversions are spaced out between other elements.")
    if G:
        gs = sorted(x["gforce"] for x in ALL if x["gforce"]); med = gs[len(gs) // 2]
        s.append(f"RCDB lists a peak force of {G} g, " + ("above" if G > med else "below" if G < med else "level with") + f" the {med} g median for coasters on {BRAND} with a g-force figure.")
    if s: out.append("<p>" + " ".join(s) + "</p>")
    # history and park context
    t = []
    yrs = [(x, year(x)) for x in p["coasters"] if year(x)]
    if year(c) and len(yrs) > 2:
        order = sorted(yrs, key=lambda z: (z[1], z[0]["slug"]))
        k = [z[0] for z in order].index(c) + 1
        if k == 1: t.append(f"Opened in {year(c)}, it is the oldest of the {len(yrs)} coasters we list at {E(p['name'])}.")
        elif k == len(order): t.append(f"Opened in {year(c)}, it is the newest of the {len(yrs)} coasters we list at {E(p['name'])}.")
        else: t.append(f"Opened in {year(c)}, it is the {ordinal(k)} oldest of the {len(yrs)} coasters we list at {E(p['name'])}.")
    if c["former"]: t.append(f"It has run under other names ({E(', then '.join(c['former']))}), so older guides and photos may use those.")
    fam = model_family(c)
    if len(fam) > 1:
        others = [x for x in fam if x is not c]
        fy = sorted(((year(x) or "9999", x["park"], x["slug"], x) for x in fam), key=lambda z: z[:3])
        rank = [z[3] for z in fy].index(c) + 1
        ph = [x for x in fam if x["hr"]]
        same = [x for x in others if x["hr"] and c["hr"] and abs(hin(x["hr"]) - hin(c["hr"])) < 0.6]
        msg = f"It is one of {len(fam)} rides on {BRAND} built to {E(c['make'])}'s {E(c['model'])} design" + (f", and the {'first' if rank == 1 else 'most recent' if rank == len(fam) else ordinal(rank)} of them to open" if year(c) else "") + ". "
        msg += "Others include " + andlist([f'<a href="{coaster_path(x)}">{E(x["name"])}</a> at {E(park_of(x)["short"])}' for x in others[:4]]) + "."
        if c["hr"] and len(ph) > 1:
            diff = [x for x in ph if x is not c and abs(hin(x["hr"]) - hin(c["hr"])) >= 0.6]
            if diff: msg += f" Height rules for this model differ by park: {E(p['short'])} sets {hshort(c['hr'])}, while " + andlist([f"{E(park_of(x)['short'])} sets {hshort(x['hr'])}" for x in diff[:3]]) + "."
            elif same: msg += f" Every listed park with a verified rule sets the same minimum, {hshort(c['hr'])}."
        t.append(msg)
    if t: out.append("<p>" + " ".join(t) + "</p>")
    # height rule context
    u = []
    if c["hr"]:
        ph = [x for x in p["coasters"] if x["hr"]]
        if len(ph) > 2:
            mins = sorted(hin(x["hr"]) for x in ph); me = hin(c["hr"])
            if me >= mins[-1] - 1e-9: u.append(f"Its {hshort(c['hr'])} minimum is the strictest at {E(p['short'])}" + ("" if mins.count(mins[-1]) == 1 else f", shared with {mins.count(mins[-1]) - 1} other coaster{'s' if mins.count(mins[-1]) > 2 else ''}") + ".")
            elif me <= mins[0] + 1e-9: u.append(f"Its {hshort(c['hr'])} minimum is the lowest of any coaster at {E(p['short'])}" + ("" if mins.count(mins[0]) == 1 else f" (tied with {mins.count(mins[0]) - 1} other{'s' if mins.count(mins[0]) > 2 else ''})") + ", which makes it a natural first coaster there.")
            else:
                can = len([m for m in mins if m <= me + 1e-9]) - 1
                u.append(f"A rider who just meets its {hshort(c['hr'])} minimum can also ride {can} other coaster{'s' if can != 1 else ''} at {E(p['short'])}, out of {len(ph) - 1} with verified rules.")
        if c["scale"]:
            cls = [hin(x["hr"]) for x in ALL if x["hr"] and x["scale"] == c["scale"]]
            if len(cls) > 10:
                cls.sort(); med = cls[len(cls) // 2]; me = hin(c["hr"])
                cmp_ = "higher than is typical" if me > med + 0.6 else "lower than is typical" if me < med - 0.6 else "about typical"
                u.append(f"Among {c['scale'].lower()}-class coasters on {BRAND} the median ride-alone minimum is about {round(med)} in ({round(med * 2.54)} cm), so this rule is {cmp_} for its class.")
        if c["hr"].get("acc_min"): u.append(f"Children from {rngs(c['hr'])} can ride with a companion, so a family can often ride together before a child is old enough to ride alone.")
    if u: out.append("<p>" + " ".join(u) + "</p>")
    w = where_html(c)
    if w: out.append(w)
    if not out: return ""
    return f'<section aria-labelledby="feel-h"><h2 id="feel-h">What riding {n} is like</h2>{"".join(out)}<p class="note">Written from RCDB statistics and the park\'s published height rule; it describes the layout, not a review.</p></section>'

def _dist(a, b):
    R = 6371000; f1, f2 = math.radians(a["lat"]), math.radians(b["lat"]); dl = math.radians(b["lon"] - a["lon"]); df_ = f2 - f1
    x = math.sin(df_ / 2) ** 2 + math.cos(f1) * math.cos(f2) * math.sin(dl / 2) ** 2
    return 2 * R * math.asin(math.sqrt(x))
def _bearing_word(c, lat, lon):
    dy = c["lat"] - lat; dx = (c["lon"] - lon) * math.cos(math.radians(lat))
    ang = (math.degrees(math.atan2(dx, dy)) + 360) % 360
    return ["north", "north-east", "east", "south-east", "south", "south-west", "west", "north-west"][int((ang + 22.5) // 45) % 8]
def where_html(c):
    p = park_of(c)
    if not c["lat"]: return ""
    pts = [x for x in p["coasters"] if x["lat"] and x is not c]
    if not pts: return ""
    s = []
    allp = pts + [c]
    if len(allp) >= 3:
        la = sum(x["lat"] for x in allp) / len(allp); lo = sum(x["lon"] for x in allp) / len(allp)
        d0 = _dist(c, {"lat": la, "lon": lo})
        if d0 > 80: s.append(f"Going by RCDB's map positions, {E(c['name'])} sits on the {_bearing_word(c, la, lo)} side of {poss(p['short'])} coaster line-up.")
        else: s.append(f"Going by RCDB's map positions, {E(c['name'])} sits near the middle of {poss(p['short'])} coaster line-up.")
    near = sorted(pts, key=lambda x: _dist(c, x))[:2]
    d = _dist(c, near[0])
    s.append(f'The nearest other coaster is <a href="{coaster_path(near[0])}">{E(near[0]["name"])}</a>, roughly {max(10, round(d / 10) * 10):,} m away' + (f' ({hshort(near[0]["hr"])} minimum)' if near[0]["hr"] else "") + (", so the two are easy to ride back to back." if d < 300 else "."))
    if len(near) > 1:
        d2 = _dist(c, near[1]); s.append(f'Next closest is <a href="{coaster_path(near[1])}">{E(near[1]["name"])}</a> at about {max(10, round(d2 / 10) * 10):,} m.')
    return "<p>" + " ".join(s) + " Distances are straight-line estimates from map coordinates, not walking routes.</p>"

def clone_faqs(c):
    fam = [x for x in (model_family(c) or [x for x in ALL if x["name"] == c["name"]]) if x is not c and x["park"] != c["park"]]
    if not fam: return []
    p = park_of(c); o = sorted(fam, key=lambda x: (year(x) or "9999", x["park"]))[0]; op = park_of(o)
    bits = []
    if c["model"] and c["model"] == o["model"]: bits.append(f"Both are {c['make']} {c['model']} coasters on RCDB")
    else: bits.append(f"They share a name but are separate rides")
    if year(c) and year(o): bits.append(f"the {p['short']} ride opened in {year(c)} and the {op['short']} ride in {year(o)}")
    if c["hr"] and o["hr"]:
        if abs(hin(c["hr"]) - hin(o["hr"])) < 0.6: bits.append(f"both list a {hshort(c['hr'])} minimum")
        else: bits.append(f"{p['short']} sets {hshort(c['hr'])} and {op['short']} sets {hshort(o['hr'])}")
    if c["height"] and o["height"] and c["height"] != o["height"]: bits.append(f"RCDB lists heights of {c['height']} ft and {o['height']} ft")
    return [(f"Is {c['name']} at {p['short']} the same as {o['name']} at {op['short']}?", "; ".join(bits) + ".")]
