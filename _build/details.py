"""Extract extra RCDB fields (elements, restraints, capacity, designer, relocations, per-track names) from cached RCDB coaster pages
into rcdb_details.json. Run: python3 _build/details.py  (reads /workspace/coastermap-data/raw/<id>.html)."""
import re, json, os, html as H
HERE = os.path.dirname(os.path.abspath(__file__))
RAW = "/workspace/coastermap-data/raw"
def tx(s): return re.sub(r"\s+", " ", H.unescape(re.sub("<[^>]+>", " ", s))).strip()
def rows(tbl): return re.findall(r"<tr><th>([^<]+)<td>(.*?)(?=<tr>|</tbody>|</table>)", tbl, re.S)
def sect(c, name):
    i = c.find(f"<h3>{name}</h3>")
    if i < 0: return ""
    return c[i:c.find("</section>", i)]
rc = json.load(open(os.path.join(HERE, "rcdb.json")))
out = {}
for park in rc.values():
    for co in park["coasters"]:
        cid = co["rcdb_id"]; fn = f"{RAW}/{cid}.html"
        if not os.path.exists(fn): continue
        c = open(fn).read(); d = {}
        tr = sect(c, "Tracks")
        # track names (dual/racing coasters list one column per track)
        hdr = re.search(r"<thead>(.*?)</thead>", tr, re.S)
        if hdr: d["tracks"] = [tx(x) for x in re.findall(r"<th>(.*?)(?=<th>|</tr>|</thead>)", hdr.group(1)) if tx(x)]
        for k, v in rows(tr):
            if k == "Elements":
                els = []
                for seg in re.split(r"<br>", v):
                    m = re.search(r"<a href=/\d+\.htm>([^<]+)</a>", seg)
                    if not m: continue
                    pre, post = tx(seg[:m.start()]), tx(seg[m.end():])
                    extra = ", ".join(x for x in [pre, post] if x)
                    els.append([H.unescape(m.group(1)), extra or None])
                d["elements"] = els
        trn = sect(c, "Trains")
        for k, v in rows(trn):
            if k == "Restraints": d["restraints"] = [tx(x) for x in re.findall(r"<li>(.*?)(?=<li>|</ul>)", v)] or [tx(v)]
            if k == "Arrangement": d["arrangement"] = tx(v)
        det = sect(c, "Details")
        for k, v in rows(det):
            if k == "Capacity": d["capacity"] = tx(v)
            if k in ("Designer", "Designers"): d["designers"] = [tx(x) for x in re.findall(r"<li>(.*?)(?=<li>|</ul>)", v)] or [tx(v)]
            if k == "Relocations":
                d["relocations"] = [[tx(a), tx(b)] for a, b in re.findall(r"<a href=/\d+\.htm>([^<]+)</a> as <a href=/\d+\.htm>([^<]+)</a>", v)]
            if k in ("Installer", "Installers"): d["installer"] = tx(v)
        m = re.search(r"<th>Former names?<td>(.*?)(?=<tr>|</table>)", c, re.S)
        if m:
            fl = []
            for seg in re.split(r"<br>", m.group(1)):
                if not tx(seg): continue
                nm = tx(re.sub(r"\(.*$", "", seg, flags=re.S))
                ys = re.findall(r'datetime="(\d{4})', seg)
                fl.append([nm, ys[0] if ys else None, ys[1] if len(ys) > 1 else None])
            d["former"] = fl
        nt = sect(c, "Notes")
        if nt and re.search(r"\bseats?\b|\bseated\b|\briders?\b|\bpassengers?\b|\brows?\b", tx(nt), re.I): d["train_note"] = True
        out[str(cid)] = d
json.dump(out, open(os.path.join(HERE, "rcdb_details.json"), "w"), indent=1, ensure_ascii=False)
from collections import Counter
print(len(out), Counter(k for d in out.values() for k in d))
print(Counter(e[0] for d in out.values() for e in d.get("elements", [])).most_common(80))
print(Counter(r for d in out.values() for r in d.get("restraints", [])))
