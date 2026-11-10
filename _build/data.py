"""Merge verified data into one coaster list. Sources: RCDB (stats, opening, make, coordinates),
official park pages (height requirements), Visit Orlando (official Orlando tourism board) where park
pages could not be read. Checked 10 Nov 2026. Never add a number that is not in a source."""
import json, re, os, unicodedata
HERE = os.path.dirname(__file__)
CHECKED = "10 Nov 2026"
VO = ("Visit Orlando, Orlando Roller Coaster Guide (updated 1 Jun 2026)", "https://www.visitorlando.com/blog/post/orlando-roller-coaster-guide/")
BG = ("Busch Gardens Tampa Bay, Roller Coasters page", "https://buschgardens.com/tampa/roller-coasters/")
def dz(slug): return ("Walt Disney World, official attraction page", f"https://disneyworld.disney.go.com/attractions/magic-kingdom/{slug}/")
PARKS = [
 dict(slug="cedar-point", name="Cedar Point", short="Cedar Point", loc="Sandusky, Ohio", state="OH", country="US", official="https://www.sixflags.com/cedarpoint", group="Six Flags (formerly Cedar Fair)"),
 dict(slug="six-flags-magic-mountain", name="Six Flags Magic Mountain", short="Magic Mountain", loc="Valencia, California", state="CA", country="US", official="https://www.sixflags.com/magicmountain", group="Six Flags"),
 dict(slug="magic-kingdom", name="Magic Kingdom", short="Magic Kingdom", loc="Lake Buena Vista, Florida", state="FL", country="US", official="https://disneyworld.disney.go.com/destinations/magic-kingdom/", group="Walt Disney World"),
 dict(slug="epic-universe", name="Universal Epic Universe", short="Epic Universe", loc="Orlando, Florida", state="FL", country="US", official="https://www.universalorlando.com/web/en/us/theme-parks/epic-universe", group="Universal Orlando Resort"),
 dict(slug="islands-of-adventure", name="Universal Islands of Adventure", short="Islands of Adventure", loc="Orlando, Florida", state="FL", country="US", official="https://www.universalorlando.com/web/en/us/theme-parks/islands-of-adventure", group="Universal Orlando Resort"),
 dict(slug="universal-studios-florida", name="Universal Studios Florida", short="Universal Studios Florida", loc="Orlando, Florida", state="FL", country="US", official="https://www.universalorlando.com/web/en/us/theme-parks/universal-studios-florida", group="Universal Orlando Resort"),
 dict(slug="busch-gardens-tampa-bay", name="Busch Gardens Tampa Bay", short="Busch Gardens Tampa", loc="Tampa, Florida", state="FL", country="US", official="https://buschgardens.com/tampa/", group="United Parks & Resorts"),
]
DISPLAY = {"Barnstormer": "The Barnstormer", "Incredible Hulk": "The Incredible Hulk Coaster", "VelociCoaster": "Jurassic World VelociCoaster"}
# Height requirements (inches) for non Six Flags parks, as read on the cited page on CHECKED.
H = {
 "Space Mountain": dict(min=44, src=dz("space-mountain")),
 "Big Thunder Mountain Railroad": dict(min=38, src=dz("big-thunder-mountain-railroad")),
 "Seven Dwarfs Mine Train": dict(min=38, src=dz("seven-dwarfs-mine-train")),
 "TRON Lightcycle / Run": dict(min=48, src=dz("tron-lightcycle-run")),
 "Barnstormer": dict(min=35, src=VO),
 "Stardust Racers": dict(min=48, src=VO), "Hiccup's Wing Gliders": dict(min=40, src=VO),
 "Curse of the Werewolf": dict(min=40, src=VO), "Mine-Cart Madness": dict(min=40, src=VO),
 "Flight of the Hippogriff": dict(min=36, src=VO), "VelociCoaster": dict(min=51, src=VO),
 "Hagrid's Magical Creatures Motorbike Adventure": dict(min=48, src=VO), "Incredible Hulk": dict(min=54, src=VO),
 "Harry Potter and the Escape from Gringotts": dict(min=42, src=VO), "Trolls Trollercoaster": dict(min=36, src=VO),
 "Revenge of the Mummy": dict(min=48, src=VO),
 "Montu": dict(min=54, src=BG), "SheiKra": dict(min=54, src=BG), "Air Grover": dict(min=38, src=BG),
 "Cheetah Hunt": dict(min=48, src=BG), "Cobra's Curse": dict(min=48, acc_min=42, acc_max=48, src=BG),
 "Tigris": dict(min=54, src=BG), "Iron Gwazi": dict(min=48, src=BG), "Phoenix Rising": dict(min=42, src=BG),
}
def slugify(s):
    s = unicodedata.normalize("NFKD", s).encode("ascii", "ignore").decode().lower().replace("'", "").replace("’", "")
    return re.sub(r"[^a-z0-9]+", "-", s).strip("-")
def num(v):
    if v is None: return None
    m = re.match(r"([\d.]+)", v); 
    if not m: return None
    x = float(m.group(1)); return int(x) if x == int(x) else x
def load():
    rc = json.load(open(os.path.join(HERE, "rcdb.json")))
    sf = json.load(open(os.path.join(HERE, "sf_heights.json")))
    parks = []
    for p in PARKS:
        r = rc[p["slug"]]; p = dict(p, rcdb_url=r["rcdb_url"], coasters=[])
        for c in r["coasters"]:
            n = c["name"]; st = c.get("st", {})
            tags = [t for t in c["tags"] if t not in ("Roller Coaster",)]
            scale = next((t for t in tags if t in ("Kiddie", "Family", "Thrill", "Extreme")), None)
            material = next((t for t in tags if t in ("Steel", "Wood")), None)
            former = None
            if c.get("former"):
                former = [x.strip() for x in re.split(r"\(\s*to\s*\)", c["former"]) if x.strip() and x.strip() != n]
            hr = None
            if n in sf and sf[n]:
                s = sf[n]; hr = dict(min=int(s["min"]), acc_min=s["acc_min"] and int(s["acc_min"]), acc_max=s["acc_max"] and int(s["acc_max"]),
                                     max=s["max"] and int(s["max"]), src=(f"{p['name']}, official ride page", s["url"]), thrill=s["thrill"] and int(s["thrill"]), introduced=s.get("introduced"))
            elif n in H:
                hr = {**dict(acc_min=None, acc_max=None, max=None, thrill=None), **H[n]}
            model = c.get("model")
            if model: model = re.sub(r"^(All Models|Other) / ", "", model)
            co = dict(
                name=DISPLAY.get(n, n), rcdb_name=n, slug=slugify(DISPLAY.get(n, n)), park=p["slug"], park_name=p["name"],
                rcdb_url=c["rcdb_url"], opened=c["opened"], make=c["make"], model=model, tags=tags, scale=scale, material=material,
                design=next((t for t in tags if t in ("Sit Down", "Inverted", "Suspended", "Wing", "Flying", "Stand Up")), None),
                height=num(st.get("Height")), drop=num(st.get("Drop")), speed=num(st.get("Speed")), length=num(st.get("Length")),
                inversions=num(st.get("Inversions")), angle=num(st.get("Vertical Angle")), gforce=num(st.get("G-Force")),
                twin=("Twin" in tags), lat=c["lat"], lon=c["lon"], former=former, hr=hr, trains=c.get("trains"))
            p["coasters"].append(co)
        parks.append(p)
    return parks
if __name__ == "__main__":
    for p in load():
        for c in p["coasters"]: print(p["slug"], c["slug"], c["hr"] and c["hr"]["min"], c["scale"], c["former"])
