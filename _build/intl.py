# International parks (expansion batch 5, 10 Nov 2026). Heights are the park's official metric rules, stored in cm (unit="cm").
def EP(slug): return ("Europa-Park, official attraction page", f"https://www.europapark.de/en/theme-park/attractions/{slug}")
def PH(path): return ("Phantasialand, official attraction page", f"https://www.phantasialand.de/en/theme-park/{path}/")
AT = ("Alton Towers Resort, Height Restrictions page", "https://www.altontowers.com/plan-your-visit/resort-information/height-restrictions/")
ATS = ("Alton Towers Resort help centre, height restrictions article", "https://support.altontowers.com/hc/en-us/articles/16003545905309-What-are-the-height-restrictions-for-your-Rides-and-Attractions")
TP = ("Thorpe Park Resort, Ride Restrictions Guide (PDF)", "https://www.thorpepark.com/media/cfqjphft/bodymeasurementsv3.pdf")
BP = ("Pleasure Beach Resort, Height Restrictions page", "https://www.blackpoolpleasurebeach.com/height-restrictions/")
PA = ("PortAventura World, PortAventura Park height requirements page", "https://www.portaventuraworld.com/en/rides/requirements")
FL = ("PortAventura World, Ferrari Land height requirements page", "https://www.portaventuraworld.com/en/ferrari-land/rides/requirements")
def EF(slug): return ("Efteling, official attraction page", f"https://www.efteling.com/en/park/attractions/{slug}")
def LB(slug): return ("Liseberg, official ride page", f"https://www.liseberg.se/en/park/rides-attractions/{slug}/")
def FQ(slug): return ("Fuji-Q Highland, official attraction page", f"https://www.fujiq.jp/en/attraction/{slug}.html")
TDR = ("Tokyo Disney Resort, official FAQ on attractions with height requirements", "https://faq-en.tokyodisneyresort.jp/answer/683f07a485e09d45dfdde8ec/")
def SH(slug): return ("Shanghai Disney Resort, official attraction page", f"https://www.shanghaidisneyresort.com/en/{slug}/")
def M(**k): return dict(unit="cm", **k)
A16 = "Riders below the ride-alone height must be accompanied by an adult aged 16 or over."
HP_INTL = {
 ("europa-park", "Matterhorn Blitz"): M(min=130, acc_min=120, acc_max=130, src=EP("matterhorn-blitz")),
 ("europa-park", "Euro Mir"): M(min=130, max=195, src=EP("euro-mir")),
 ("europa-park", "Eurosat - CanCan Coaster"): M(min=130, acc_min=120, acc_max=130, max=195, src=EP("eurosat-cancan-coaster")),
 ("europa-park", "Schweizer Bobbahn"): M(min=130, acc_min=120, acc_max=130, src=EP("swiss-bob-run")),
 ("europa-park", "Silver Star"): M(min=140, src=EP("silver-star")),
 ("europa-park", "Poseidon"): M(min=130, acc_min=120, acc_max=130, src=EP("water-rollercoaster-poseidon")),
 ("europa-park", "Atlantica SuperSplash"): M(min=130, acc_min=100, acc_max=130, src=EP("atlantica-supersplash")),
 ("europa-park", "Pegasus"): M(min=130, acc_min=100, acc_max=130, src=EP("pegasus")),
 ("europa-park", "blue fire Megacoaster"): M(min=130, src=EP("blue-fire-megacoaster")),
 ("europa-park", "Voltron"): M(min=130, src=EP("voltron-nevera-powered-rimac")),
 ("europa-park", "Wodan Timbur Coaster"): M(min=130, acc_min=120, acc_max=130, src=EP("wodan-timburcoaster")),
 ("europa-park", "Arthur"): M(min=120, acc_min=100, acc_max=120, src=EP("arthur")),
 ("europa-park", "Ba-a-a-Express"): M(min=120, acc_min=90, acc_max=120, src=EP("ba-express")),
 ("europa-park", "Alpenexpress Enzian"): M(min=130, acc_min=90, acc_max=130, src=EP("alpine-express-enzian")),
 ("phantasialand", "Colorado Adventure"): M(min=120, acc_min=100, acc_max=120, src=PH("one-of-a-kind-attractions/colorado-adventure")),
 ("phantasialand", "Crazy Bats"): M(min=120, acc_min=100, acc_max=120, src=PH("one-of-a-kind-attractions/crazy-bats")),
 ("phantasialand", "Winjas"): M(min=140, acc_min=120, acc_max=140, max=200, note="Children under 6 may not ride; children aged 6 to 10 must ride with an adult.", src=PH("one-of-a-kind-attractions/winjas-fear-force")),
 ("phantasialand", "Black Mamba"): M(min=140, max=195, note="Children under 10 may not ride.", src=PH("one-of-a-kind-attractions/black-mamba")),
 ("phantasialand", "Taron"): M(min=140, acc_min=130, acc_max=140, src=PH("one-of-a-kind-attractions/taron")),
 ("phantasialand", "Raik"): M(min=120, acc_min=100, acc_max=120, src=PH("one-of-a-kind-attractions/raik")),
 ("phantasialand", "F.L.Y."): M(min=140, acc_min=130, acc_max=140, note="Children aged 8 to 10 must ride with an adult; children over 10 who meet the height may ride alone.", src=PH("rookburgh/f-l-y")),
 ("alton-towers", "Nemesis Reborn"): M(min=140, src=AT), ("alton-towers", "Oblivion"): M(min=140, src=AT),
 ("alton-towers", "Runaway Mine Train"): M(min=130, acc_min=110, acc_max=130, note=A16, src=AT),
 ("alton-towers", "Spinball Whizzer"): M(min=120, max=195, src=AT), ("alton-towers", "Rita"): M(min=140, max=195, src=AT),
 ("alton-towers", "Th13teen"): M(min=120, max=196, src=AT), ("alton-towers", "Smiler"): M(min=140, src=AT),
 ("alton-towers", "Octonauts Rollercoaster Adventure"): M(min=110, acc_min=90, acc_max=110, note=A16, src=AT),
 ("alton-towers", "Wicker Man"): M(min=120, src=AT), ("alton-towers", "Galactica"): M(min=140, src=AT),
 ("alton-towers", "Bluey the Ride: Here come the grannies!"): M(min=110, acc_min=90, acc_max=110, note=A16, src=ATS),
 ("thorpe-park", "Walking Dead - The Ride"): M(min=140, note="The park's ride guide lists an age requirement of 13+.", src=TP),
 ("thorpe-park", "Flying Fish"): M(min=110, acc_min=90, acc_max=110, note=A16, src=TP),
 ("thorpe-park", "Colossus"): M(min=140, max=196, src=TP), ("thorpe-park", "Nemesis Inferno"): M(min=140, src=TP),
 ("thorpe-park", "Stealth"): M(min=140, max=196, src=TP),
 ("thorpe-park", "Saw - The Ride"): M(min=140, note="The park's ride guide lists an age requirement of 13+.", src=TP),
 ("thorpe-park", "Swarm"): M(min=140, max=195, src=TP), ("thorpe-park", "Hyperia"): M(min=130, src=TP),
 ("blackpool-pleasure-beach", "Big One"): M(min=132, src=BP), ("blackpool-pleasure-beach", "Revolution"): M(min=127, src=BP),
 ("blackpool-pleasure-beach", "Avalanche"): M(min=132, acc_min=112, acc_max=132, note="Below 132 cm, riders must be with a responsible person aged 12 or over who meets the height requirement.", src=BP),
 ("blackpool-pleasure-beach", "Grand National"): M(min=140, src=BP), ("blackpool-pleasure-beach", "Nickelodeon Streak"): M(min=117, src=BP),
 ("blackpool-pleasure-beach", "Steeplechase"): M(min=127, src=BP), ("blackpool-pleasure-beach", "Infusion"): M(min=132, max=200, src=BP),
 ("blackpool-pleasure-beach", "Icon"): M(min=130, src=BP),
 ("portaventura-park", "Stampida"): M(min=120, src=PA), ("portaventura-park", "Dragon Khan"): M(min=140, max=195, src=PA),
 ("portaventura-park", "Tomahawk"): M(min=105, max=185, src=PA), ("portaventura-park", "Diablo - Tren de la Mina"): M(min=140, acc_min=110, acc_max=140, src=PA),
 ("portaventura-park", "Tami-Tami"): M(min=130, acc_min=100, acc_max=130, src=PA), ("portaventura-park", "Furius Baco"): M(min=140, max=195, src=PA),
 ("portaventura-park", "Shambhala"): M(min=140, src=PA),
 ("ferrari-land", "Red Force"): M(min=140, max=195, src=FL), ("ferrari-land", "Junior Red Force"): M(min=120, acc_min=95, acc_max=120, max=195, src=FL),
 ("efteling", "Python"): M(min=120, src=EF("python")), ("efteling", "Vogel Rok"): M(min=120, src=EF("vogel-rok")),
 ("efteling", "Vliegende Hollander"): M(min=120, src=EF("de-vliegende-hollander")),
 ("efteling", "Joris en de Draak"): M(min=120, acc_min=110, acc_max=120, note=A16, src=EF("joris-en-de-draak")),
 ("efteling", "Baron 1898"): M(min=132, src=EF("baron-1898")),
 ("efteling", "Max + Moritz"): M(min=130, acc_min=90, acc_max=130, note=A16, src=EF("max-moritz")),
 ("liseberg", "Lisebergbanan"): M(min=130, acc_min=110, acc_max=130, src=LB("lisebergbanan")),
 ("liseberg", "Rabalder"): M(min=110, acc_min=90, acc_max=110, src=LB("rabalder")), ("liseberg", "Stampbanan"): M(min=110, acc_min=90, acc_max=110, src=LB("stampbanan")),
 ("liseberg", "Helix"): M(min=130, note="Riders must also be at least 7 years old.", src=LB("helix")),
 ("liseberg", "Valkyria"): M(min=132, max=195, note="Riders must also be at least 7 years old.", src=LB("valkyria")),
 ("liseberg", "Luna"): M(min=120, acc_min=95, acc_max=120, note="Riders must also be at least 6 years old, or 3 with an adult.", src=LB("luna")),
 ("liseberg", "Balder"): M(min=130, note="Riders must also be at least 7 years old.", src=LB("balder")),
 ("fuji-q-highland", "Fujiyama"): M(min=130, acc_min=110, acc_max=130, note="Riders between 110 and 130 cm must be accompanied by someone of junior high school age or older. Not available to guests over 65.", src=FQ("fujiyama")),
 ("fuji-q-highland", "Eejanaika"): M(min=125, max=200, note="Not available to guests over 55.", src=FQ("eejanaika")),
 ("fuji-q-highland", "Takabisha"): M(min=125, note="Not available to guests over 55.", src=FQ("takabisha")),
 ("fuji-q-highland", "Zokkon"): M(min=120, max=195, note="Not available to guests over 65.", src=FQ("zokkon")),
 ("fuji-q-highland", "Gaspard et Lisa - Voyage Dans Le Ciel"): M(min=110, acc_min=100, acc_max=110, note="Riders must be under 190 cm.", src=FQ("lisagas_soratabi")),
 ("tokyo-disneyland", "Big Thunder Mountain"): M(min=102, src=TDR), ("tokyo-disneyland", "Gadget's Go Coaster"): M(min=90, src=TDR),
 ("tokyo-disneysea", "Flounder's Flying Fish Coaster"): M(min=90, src=TDR), ("tokyo-disneysea", "Raging Spirits"): M(min=117, max=195, src=TDR),
 ("shanghai-disneyland", "TRON Lightcycle Power Run"): M(min=122, src=SH("experience/attraction/tron-lightcycle-power-run")),
 ("shanghai-disneyland", "Seven Dwarfs Mine Train"): M(min=97, src=SH("attractions/seven-dwarfs-mine-train")),
 ("shanghai-disneyland", "Rex's Racer"): M(min=120, src=SH("experience/attraction/rexs-rc-racer")),
}
INTL_PARKS = [
 dict(slug="europa-park", name="Europa-Park", short="Europa-Park", loc="Rust, Germany", state="Baden-Württemberg", country="DE", official="https://www.europapark.de/en", group="Europa-Park Resort"),
 dict(slug="phantasialand", name="Phantasialand", short="Phantasialand", loc="Brühl, Germany", state="North Rhine-Westphalia", country="DE", official="https://www.phantasialand.de/en/", group="Phantasialand"),
 dict(slug="alton-towers", name="Alton Towers", short="Alton Towers", loc="Alton, England", state="Staffordshire", country="GB", official="https://www.altontowers.com/", group="Merlin Entertainments"),
 dict(slug="thorpe-park", name="Thorpe Park", short="Thorpe Park", loc="Chertsey, England", state="Surrey", country="GB", official="https://www.thorpepark.com/", group="Merlin Entertainments"),
 dict(slug="blackpool-pleasure-beach", name="Blackpool Pleasure Beach", short="Blackpool Pleasure Beach", loc="Blackpool, England", state="Lancashire", country="GB", official="https://www.blackpoolpleasurebeach.com/", group="Pleasure Beach Resort"),
 dict(slug="portaventura-park", name="PortAventura Park", short="PortAventura Park", loc="Salou, Spain", state="Catalonia", country="ES", official="https://www.portaventuraworld.com/en/portaventura-park", group="PortAventura World"),
 dict(slug="ferrari-land", name="Ferrari Land", short="Ferrari Land", loc="Salou, Spain", state="Catalonia", country="ES", official="https://www.portaventuraworld.com/en/ferrari-land", group="PortAventura World"),
 dict(slug="efteling", name="Efteling", short="Efteling", loc="Kaatsheuvel, Netherlands", state="North Brabant", country="NL", official="https://www.efteling.com/en", group="Efteling"),
 dict(slug="liseberg", name="Liseberg", short="Liseberg", loc="Gothenburg, Sweden", state="Västra Götaland", country="SE", official="https://www.liseberg.se/en/", group="Liseberg"),
 dict(slug="fuji-q-highland", name="Fuji-Q Highland", short="Fuji-Q Highland", loc="Fujiyoshida, Japan", state="Yamanashi", country="JP", official="https://www.fujiq.jp/en/", group="Fujikyu"),
 dict(slug="tokyo-disneyland", name="Tokyo Disneyland", short="Tokyo Disneyland", loc="Urayasu, Japan", state="Chiba", country="JP", official="https://www.tokyodisneyresort.jp/en/tdl/", group="Tokyo Disney Resort"),
 dict(slug="tokyo-disneysea", name="Tokyo DisneySea", short="Tokyo DisneySea", loc="Urayasu, Japan", state="Chiba", country="JP", official="https://www.tokyodisneyresort.jp/en/tds/", group="Tokyo Disney Resort"),
 dict(slug="shanghai-disneyland", name="Shanghai Disneyland", short="Shanghai Disneyland", loc="Shanghai, China", state="Shanghai", country="CN", official="https://www.shanghaidisneyresort.com/en/", group="Shanghai Disney Resort"),
]
DISPLAY_INTL = {
 ("europa-park", "Eurosat - CanCan Coaster"): "Eurosat CanCan Coaster", ("europa-park", "Schweizer Bobbahn"): "Swiss Bob Run",
 ("europa-park", "blue fire Megacoaster"): "Blue Fire Megacoaster", ("europa-park", "Wodan Timbur Coaster"): "Wodan Timburcoaster",
 ("europa-park", "Voltron"): "Voltron Nevera", ("europa-park", "Alpenexpress Enzian"): "Alpine Express Enzian",
 ("phantasialand", "Winjas"): "Winja's Fear & Force",
 ("alton-towers", "Th13teen"): "TH13TEEN", ("alton-towers", "Smiler"): "The Smiler",
 ("alton-towers", "Bluey the Ride: Here come the grannies!"): "Bluey the Ride: Here Come the Grannies!",
 ("thorpe-park", "Walking Dead - The Ride"): "The Walking Dead: The Ride", ("thorpe-park", "Saw - The Ride"): "SAW: The Ride", ("thorpe-park", "Swarm"): "The Swarm",
 ("blackpool-pleasure-beach", "Big One"): "The Big One", ("blackpool-pleasure-beach", "Icon"): "ICON",
 ("portaventura-park", "Diablo - Tren de la Mina"): "El Diablo: Tren de la Mina", ("portaventura-park", "Uncharted: The Enigma of Penitence"): "Uncharted: The Enigma of Penitence",
 ("efteling", "Vliegende Hollander"): "De Vliegende Hollander",
 ("fuji-q-highland", "Gaspard et Lisa - Voyage Dans Le Ciel"): "Gaspard et Lisa: Voyage Dans Le Ciel",
 ("shanghai-disneyland", "Rex's Racer"): "Rex's RC Racer",
}
