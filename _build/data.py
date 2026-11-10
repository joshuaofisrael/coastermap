"""Merge verified data into one coaster list. Sources: RCDB (stats, opening, make, coordinates),
official park pages (height requirements), Visit Orlando (official Orlando tourism board) where park
pages could not be read. Checked 10 Nov 2026. Never add a number that is not in a source."""
import json, re, os, unicodedata
HERE = os.path.dirname(__file__)
CHECKED = "10 Nov 2026"
VO = ("Visit Orlando, Orlando Roller Coaster Guide (updated 1 Jun 2026)", "https://www.visitorlando.com/blog/post/orlando-roller-coaster-guide/")
BG = ("Busch Gardens Tampa Bay, Roller Coasters page", "https://buschgardens.com/tampa/roller-coasters/")
def dz(slug, park="magic-kingdom"): return ("Walt Disney World, official attraction page", f"https://disneyworld.disney.go.com/attractions/{park}/{slug}/")
SWO = ("SeaWorld Orlando, Roller Coasters page", "https://seaworld.com/orlando/roller-coasters/")
def sw(slug, title): return (f"SeaWorld Orlando, {title} ride page", f"https://seaworld.com/orlando/roller-coasters/{slug}")
BGW = ("Busch Gardens Williamsburg, Roller Coasters page", "https://buschgardens.com/williamsburg/roller-coasters/")
HP = ("Hershey Entertainment & Resorts, Hersheypark Roller Coaster Guide 2026 (lowest height category that may ride)", "https://stories.hersheypa.com/hersheypark-roller-coaster-guide-2026/")
def dw(slug): return ("Dollywood, official ride page", f"https://www.dollywood.com/themepark/rides/{slug}/")
PARKS = [
 dict(slug="cedar-point", name="Cedar Point", short="Cedar Point", loc="Sandusky, Ohio", state="OH", country="US", official="https://www.sixflags.com/cedarpoint", group="Six Flags (formerly Cedar Fair)"),
 dict(slug="six-flags-magic-mountain", name="Six Flags Magic Mountain", short="Magic Mountain", loc="Valencia, California", state="CA", country="US", official="https://www.sixflags.com/magicmountain", group="Six Flags"),
 dict(slug="magic-kingdom", name="Magic Kingdom", short="Magic Kingdom", loc="Lake Buena Vista, Florida", state="FL", country="US", official="https://disneyworld.disney.go.com/destinations/magic-kingdom/", group="Walt Disney World"),
 dict(slug="epic-universe", name="Universal Epic Universe", short="Epic Universe", loc="Orlando, Florida", state="FL", country="US", official="https://www.universalorlando.com/web/en/us/theme-parks/epic-universe", group="Universal Orlando Resort"),
 dict(slug="islands-of-adventure", name="Universal Islands of Adventure", short="Islands of Adventure", loc="Orlando, Florida", state="FL", country="US", official="https://www.universalorlando.com/web/en/us/theme-parks/islands-of-adventure", group="Universal Orlando Resort"),
 dict(slug="universal-studios-florida", name="Universal Studios Florida", short="Universal Studios Florida", loc="Orlando, Florida", state="FL", country="US", official="https://www.universalorlando.com/web/en/us/theme-parks/universal-studios-florida", group="Universal Orlando Resort"),
 dict(slug="busch-gardens-tampa-bay", name="Busch Gardens Tampa Bay", short="Busch Gardens Tampa", loc="Tampa, Florida", state="FL", country="US", official="https://buschgardens.com/tampa/", group="United Parks & Resorts"),
 # Added 10 Nov 2026 (expansion batch 1, see expansion-log.md)
 dict(slug="epcot", name="EPCOT", short="EPCOT", loc="Lake Buena Vista, Florida", state="FL", country="US", official="https://disneyworld.disney.go.com/destinations/epcot/", group="Walt Disney World"),
 dict(slug="hollywood-studios", name="Disney's Hollywood Studios", short="Hollywood Studios", loc="Lake Buena Vista, Florida", state="FL", country="US", official="https://disneyworld.disney.go.com/destinations/hollywood-studios/", group="Walt Disney World"),
 dict(slug="animal-kingdom", name="Disney's Animal Kingdom", short="Animal Kingdom", loc="Lake Buena Vista, Florida", state="FL", country="US", official="https://disneyworld.disney.go.com/destinations/animal-kingdom/", group="Walt Disney World"),
 dict(slug="seaworld-orlando", name="SeaWorld Orlando", short="SeaWorld Orlando", loc="Orlando, Florida", state="FL", country="US", official="https://seaworld.com/orlando/", group="United Parks & Resorts"),
 dict(slug="kings-island", name="Kings Island", short="Kings Island", loc="Mason, Ohio", state="OH", country="US", official="https://www.sixflags.com/kingsisland", group="Six Flags (formerly Cedar Fair)"),
 dict(slug="busch-gardens-williamsburg", name="Busch Gardens Williamsburg", short="Busch Gardens Williamsburg", loc="Williamsburg, Virginia", state="VA", country="US", official="https://buschgardens.com/williamsburg/", group="United Parks & Resorts"),
 dict(slug="hersheypark", name="Hersheypark", short="Hersheypark", loc="Hershey, Pennsylvania", state="PA", country="US", official="https://www.hersheypark.com/", group="Hershey Entertainment & Resorts"),
 dict(slug="knotts-berry-farm", name="Knott's Berry Farm", short="Knott's", loc="Buena Park, California", state="CA", country="US", official="https://www.sixflags.com/knotts", group="Six Flags (formerly Cedar Fair)"),
 dict(slug="dollywood", name="Dollywood", short="Dollywood", loc="Pigeon Forge, Tennessee", state="TN", country="US", official="https://www.dollywood.com/themepark/", group="Herschend Family Entertainment"),
 dict(slug="six-flags-great-adventure", name="Six Flags Great Adventure", short="Great Adventure", loc="Jackson, New Jersey", state="NJ", country="US", official="https://www.sixflags.com/greatadventure", group="Six Flags"),
]
ORIGINAL = {"cedar-point", "six-flags-magic-mountain", "magic-kingdom", "epic-universe", "islands-of-adventure", "universal-studios-florida", "busch-gardens-tampa-bay"}
DISPLAY = {"Barnstormer": "The Barnstormer", "Incredible Hulk": "The Incredible Hulk Coaster", "VelociCoaster": "Jurassic World VelociCoaster",
 "Rock ‘n Roller Coaster Starring The Muppets": "Rock 'n' Roller Coaster Starring The Muppets", "Beast": "The Beast", "Racer": "The Racer", "Bat": "The Bat",
 "Great Pumpkin Coaster": "The Great Pumpkin Coaster", "Big Bad Wolf: The Wolf’s Revenge": "The Big Bad Wolf: The Wolf's Revenge", "Joker": "The Joker",
 "Dark Knight": "The Dark Knight Coaster", "Flash: Vertical Velocity": "The Flash: Vertical Velocity", "Woodstock’s Air Rail": "Woodstock's Air Rail",
 "Snoopy’s Tenderpaw Twister Coaster": "Snoopy's Tenderpaw Twister Coaster"}
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
# Height requirements for parks added in the expansion, keyed by (park slug, RCDB name), as read on the cited page on CHECKED.
# Six Flags (ex Cedar Fair) parks Kings Island, Knott's and Great Adventure come from sf_heights_new.json (sixflags.com ride pages).
HP2 = {
 ("epcot", "Guardians of the Galaxy: Cosmic Rewind"): dict(min=42, src=dz("guardians-of-the-galaxy-cosmic-rewind", "epcot")),
 ("hollywood-studios", "Rock ‘n Roller Coaster Starring The Muppets"): dict(min=48, src=dz("rock-and-roller-coaster-starring-muppets", "hollywood-studios")),
 ("hollywood-studios", "Slinky Dog Dash"): dict(min=38, src=dz("slinky-dog-dash", "hollywood-studios")),
 ("animal-kingdom", "Expedition Everest"): dict(min=44, src=dz("expedition-everest", "animal-kingdom")),
 ("seaworld-orlando", "Kraken"): dict(min=54, src=SWO), ("seaworld-orlando", "Mako"): dict(min=54, src=SWO),
 ("seaworld-orlando", "Manta"): dict(min=54, src=SWO), ("seaworld-orlando", "Ice Breaker"): dict(min=48, src=SWO),
 ("seaworld-orlando", "Journey to Atlantis"): dict(min=42, src=SWO), ("seaworld-orlando", "Super Grover's Box Car Derby"): dict(min=38, src=SWO),
 ("seaworld-orlando", "Pipeline: The Surf Coaster"): dict(min=54, max=78, src=sw("pipeline", "Pipeline: The Surf Coaster")),
 ("seaworld-orlando", "Penguin Trek"): dict(min=42, max=78, src=sw("penguin-trek", "Penguin Trek")),
 ("busch-gardens-williamsburg", "Big Bad Wolf: The Wolf’s Revenge"): dict(min=42, max=77, src=BGW),
 ("busch-gardens-williamsburg", "Alpengeist"): dict(min=54, src=BGW), ("busch-gardens-williamsburg", "Apollo's Chariot"): dict(min=52, src=BGW),
 ("busch-gardens-williamsburg", "Griffon"): dict(min=54, src=BGW), ("busch-gardens-williamsburg", "InvadR"): dict(min=46, src=BGW),
 ("busch-gardens-williamsburg", "Loch Ness Monster"): dict(min=48, src=BGW), ("busch-gardens-williamsburg", "Pantheon"): dict(min=52, src=BGW),
 ("busch-gardens-williamsburg", "Tempesto"): dict(min=54, src=BGW), ("busch-gardens-williamsburg", "Verbolten"): dict(min=48, src=BGW),
 ("busch-gardens-williamsburg", "DarKoaster"): dict(min=48, max=77, src=("Busch Gardens Williamsburg, DarKoaster ride page", "https://buschgardens.com/williamsburg/roller-coasters/darkoaster")),
 ("busch-gardens-williamsburg", "Grover's Alpine Express"): dict(min=41, acc_min=38, acc_max=41, src=("Busch Gardens Williamsburg, Grover's Alpine Express ride page", "https://buschgardens.com/williamsburg/rides/grovers-alpine-express")),
 ("hersheypark", "Comet"): dict(min=42, src=HP), ("hersheypark", "Trailblazer"): dict(min=36, src=HP), ("hersheypark", "Sooperdooperlooper"): dict(min=42, src=HP),
 ("hersheypark", "Jolly Rancher Remix"): dict(min=48, src=HP), ("hersheypark", "Great Bear"): dict(min=54, src=HP), ("hersheypark", "Wild Mouse"): dict(min=48, src=HP),
 ("hersheypark", "Lightning Racer"): dict(min=48, src=HP), ("hersheypark", "Fahrenheit"): dict(min=54, src=HP), ("hersheypark", "Skyrush"): dict(min=54, src=HP),
 ("hersheypark", "Cocoa Cruiser"): dict(min=36, src=HP), ("hersheypark", "Laff Trakk"): dict(min=42, src=HP), ("hersheypark", "Candymonium"): dict(min=54, src=HP),
 ("hersheypark", "Wildcat's Revenge"): dict(min=48, src=HP), ("hersheypark", "Storm Runner"): dict(min=54, src=HP),
 ("dollywood", "Blazing Fury"): dict(min=42, src=dw("blazing-fury")), ("dollywood", "Tennessee Tornado"): dict(min=48, src=dw("tennessee-tornado")),
 ("dollywood", "Thunderhead"): dict(min=48, src=dw("thunderhead")), ("dollywood", "Mystery Mine"): dict(min=48, src=dw("mystery-mine")),
 ("dollywood", "FireChaser Express"): dict(min=48, acc_min=39, acc_max=48, src=dw("firechaser-express")),
 ("dollywood", "Wild Eagle"): dict(min=50, max=78, src=dw("wild-eagle")), ("dollywood", "Lightning Rod"): dict(min=48, src=dw("lightningrod")),
 ("dollywood", "Whistle Punk Chaser"): dict(min=42, acc_min=36, acc_max=42, src=dw("whistle-punk-chaser")),
 ("dollywood", "Dragonflier"): dict(min=48, acc_min=39, acc_max=48, max=81, src=dw("dragonflier")),
 ("dollywood", "Big Bear Mountain"): dict(min=48, acc_min=39, acc_max=48, src=dw("big-bear-mountain")),
 ("dollywood", "NightFlight Expedition"): dict(min=39, src=("Dollywood, NightFlight Expedition page", "https://www.dollywood.com/themepark/rides/nightflight-expedition/")),
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
    sfn = json.load(open(os.path.join(HERE, "sf_heights_new.json")))
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
            s = sfn.get(f'{p["slug"]}|{n}') if p["slug"] not in ORIGINAL else sf.get(n)
            if s:
                hr = dict(min=int(s["min"]), acc_min=s["acc_min"] and int(s["acc_min"]), acc_max=s["acc_max"] and int(s["acc_max"]),
                                     max=s["max"] and int(s["max"]), src=(f"{p['name']}, official ride page", s["url"]), thrill=s["thrill"] and int(s["thrill"]), introduced=s.get("introduced"))
            elif (p["slug"], n) in HP2:
                hr = {**dict(acc_min=None, acc_max=None, max=None, thrill=None), **HP2[(p["slug"], n)]}
            elif p["slug"] in ORIGINAL and n in H:
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
