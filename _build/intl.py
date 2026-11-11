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

# ---- Batch 6 (10 Nov 2026): rendered with a headless browser where the official pages need JavaScript ----
def USJ(slug): return ("Universal Studios Japan, official attraction page", f"https://www.usj.co.jp/web/en/us/attractions/{slug}")
def HK(slug): return ("Hong Kong Disneyland, official attraction page", f"https://www.hongkongdisneyland.com/attractions/{slug}/")
DLPA = ("Disneyland Paris, official attractions page (height filter)", "https://www.disneylandparis.com/en-gb/attractions/")
LR = ("La Ronde, official All Rides page", "https://laronde.com/en/attraction/")
def KN(slug): return ("Knoebels, official ride page", f"https://knoebels.com/ride/{slug}/")
CS = "Universal Studios Japan lists this ride on its Child Switch (rider swap) page."
JH = "Supervising companions must be of junior high school age or older."
HP_B6 = {
 ("universal-studios-japan", "Flying Dinosaur"): M(min=132, max=198, note=CS, src=USJ("the-flying-dinosaur")),
 ("universal-studios-japan", "Hollywood Dream: The Ride"): M(min=132, note="The Backdrop version, which runs backwards, has the same height rule. " + CS, src=USJ("hollywood-dream-the-ride")),
 ("universal-studios-japan", "Flight of the Hippogriff"): M(min=122, acc_min=92, acc_max=122, max=195, note=JH + " " + CS, src=USJ("flight-of-the-hippogriff")),
 ("universal-studios-japan", "Mine Cart Madness"): M(min=122, acc_min=107, acc_max=122, note=JH + " " + CS, src=USJ("donkey-kong-country-ride")),
 ("universal-studios-japan", "Snoopy's Flying Ace Adventure"): M(min=122, acc_min=92, acc_max=122, note=JH + " " + CS, src=USJ("snoopys-flying-ace-adventure")),
 ("hong-kong-disneyland", "Hyperspace Mountain"): M(min=102, src=HK("hyperspace-mountain")),
 ("hong-kong-disneyland", "Big Grizzly Mountain Runaway Mine Cars"): M(min=112, src=HK("big-grizzly-mountain-runaway-mine-cars")),
 ("hong-kong-disneyland", "RC Racer"): M(min=120, src=HK("rc-racer")),
 ("hong-kong-disneyland", "Wandering Oaken’s Sliding Sleighs"): M(min=95, src=HK("wandering-oakens-sliding-sleighs")),
 ("disneyland-paris", "Big Thunder Mountain"): M(min=102, src=DLPA),
 ("disneyland-paris", "Indiana Jones et le Temple du Péril"): M(min=140, src=DLPA),
 ("disneyland-paris", "Star Wars Hyperspace Mountain: Rebel Mission"): M(min=120, src=DLPA),
 ("disney-adventure-world", "RC Racer"): M(min=120, src=DLPA),
 ("disney-adventure-world", "Avengers Assemble: Flight Force"): M(min=120, src=DLPA),
 ("la-ronde", "Monstre"): dict(min=54, thrill=5, src=LR),
 ("la-ronde", "Boomerang"): dict(min=48, thrill=5, src=LR),
 ("la-ronde", "Dragon"): dict(min=52, acc_min=42, acc_max=52, thrill=3, src=LR),
 ("la-ronde", "Marche du Mille-pattes"): dict(min=42, acc_min=36, acc_max=42, thrill=2, src=LR),
 ("la-ronde", "Vampire"): dict(min=54, thrill=5, src=LR),
 ("la-ronde", "Toboggan Nordique"): dict(min=48, acc_min=42, acc_max=48, thrill=4, src=LR),
 ("la-ronde", "Goliath"): dict(min=54, thrill=5, src=LR),
 ("la-ronde", "Ednör - L'Attaque"): dict(min=52, thrill=5, src=LR),
 ("knoebels", "Phoenix"): dict(min=48, acc_min=42, acc_max=48, src=KN("phoenix")),
 ("knoebels", "Twister"): dict(min=42, src=KN("twister")),
 ("knoebels", "Impulse"): dict(min=52, acc_min=48, acc_max=52, src=KN("impulse")),
 ("knoebels", "Black Diamond"): dict(min=42, src=KN("black-diamond")),
 ("knoebels", "Flying Turns"): dict(min=48, acc_min=42, acc_max=48, src=KN("flying-turns")),
 ("knoebels", "Kozmo's Kurves"): dict(min=36, src=KN("kozmos-kurves")),
}
HP_INTL.update(HP_B6)
INTL_PARKS += [
 dict(slug="knoebels", name="Knoebels Amusement Resort", short="Knoebels", loc="Elysburg, Pennsylvania", state="PA", country="US", official="https://knoebels.com/", group="Knoebels"),
 dict(slug="la-ronde", name="La Ronde", short="La Ronde", loc="Montréal, Canada", state="Quebec", country="CA", official="https://laronde.com/en/", group="Enchanted Parks"),
 dict(slug="universal-studios-japan", name="Universal Studios Japan", short="Universal Studios Japan", loc="Osaka, Japan", state="Osaka", country="JP", official="https://www.usj.co.jp/web/en/us", group="Universal Studios Japan"),
 dict(slug="hong-kong-disneyland", name="Hong Kong Disneyland", short="Hong Kong Disneyland", loc="Lantau Island, Hong Kong", state="Hong Kong", country="HK", official="https://www.hongkongdisneyland.com/", group="Hong Kong Disneyland Resort"),
 dict(slug="disneyland-paris", name="Disneyland Park (Paris)", short="Disneyland Paris", loc="Marne-la-Vallée, France", state="Île-de-France", country="FR", official="https://www.disneylandparis.com/en-gb/", group="Disneyland Paris"),
 dict(slug="disney-adventure-world", name="Disney Adventure World", short="Disney Adventure World", loc="Marne-la-Vallée, France", state="Île-de-France", country="FR", official="https://www.disneylandparis.com/en-gb/", group="Disneyland Paris", former="Walt Disney Studios Park", former_note="RCDB lists the park's former name as Walt Disney Studios Park, and Disneyland Paris's official attractions page lists it as Disney Adventure World"),
]
DISPLAY_INTL.update({("la-ronde", "Monstre"): "Le Monstre", ("la-ronde", "Marche du Mille-pattes"): "La Marche du Mille-pattes", ("la-ronde", "Ednör - L'Attaque"): "Ednör",
 ("universal-studios-japan", "Flying Dinosaur"): "The Flying Dinosaur", ("disneyland-paris", "Indiana Jones et le Temple du Péril"): "Indiana Jones and the Temple of Peril",
 ("disneyland-paris", "Casey Jr., Le Petit Train du Cirque"): "Casey Jr., le Petit Train du Cirque"})

# ---- Batch 7 (10 Nov 2026): remaining major US parks ----
LG = ("Lagoon, official Rides & Attractions page", "https://www.lagoonpark.com/rides-and-attractions")
SW = ("Silverwood, official Size Guide", "https://www.silverwoodthemepark.com/rides/size-guide.php")
def LLF(s): return ("Legoland Florida, official ride page", f"https://www.legoland.com/florida/things-to-do/theme-park/rides-attractions/{s}/")
def LLC(s): return ("Legoland California, official ride page", f"https://www.legoland.com/california/things-to-do/theme-park/rides/{s}/")
def LLN(s): return ("Legoland New York, official ride page", f"https://www.legoland.com/new-york/things-to-do/theme-park/rides-attractions/{s}/")
def EG(s): return ("Elitch Gardens, official attraction page", f"https://elitchgardens.com/attractions/{s}/")
HP_B7 = {
 ("lagoon", "Spider"): dict(min=50, acc_min=46, acc_max=50, src=LG),
 ("lagoon", "Colossus the Fire Dragon"): dict(min=50, acc_min=46, acc_max=50, src=LG),
 ("lagoon", "Wild Mouse"): dict(min=50, acc_min=46, acc_max=50, src=LG),
 ("lagoon", "Roller Coaster"): dict(min=50, acc_min=46, acc_max=50, src=LG),
 ("lagoon", "Wicked"): dict(min=50, acc_min=46, acc_max=50, note="Riders 46 to 50 in must ride in a designated seat.", src=LG),
 ("lagoon", "Primordial"): dict(min=48, acc_min=36, acc_max=48, src=LG),
 ("lagoon", "Bombora"): dict(min=48, acc_min=36, acc_max=48, src=LG),
 ("lagoon", "Cannibal"): dict(min=48, src=LG),
 ("lagoon", "Bat"): dict(min=42, src=LG),
 ("silverwood", "Tremors"): dict(min=48, acc_min=42, acc_max=48, src=SW),
 ("silverwood", "Aftershock"): dict(min=54, max=80, src=SW),
 ("silverwood", "Krazy Koaster"): dict(min=48, acc_min=36, acc_max=48, src=SW),
 ("silverwood", "Stunt Pilot"): dict(min=48, src=SW),
 ("silverwood", "Timber Terror"): dict(min=48, acc_min=42, acc_max=48, src=SW),
 ("silverwood", "Corkscrew"): dict(min=48, src=SW),
 ("legoland-florida", "Dragon"): dict(min=48, acc_min=40, acc_max=48, note="Companions must be at least 14 years old.", src=LLF("the-dragon")),
 ("legoland-florida", "Coastersaurus"): dict(min=42, src=LLF("coastersaurus")),
 ("legoland-florida", "Great Lego Race"): dict(min=48, acc_min=42, acc_max=48, note="Companions must be at least 14 years old and at least 48 in tall.", src=LLF("the-great-lego-race")),
 ("legoland-florida", "Galacticoaster"): dict(min=48, acc_min=36, acc_max=48, src=LLF("galacticoaster")),
 ("legoland-california", "Dragon"): dict(min=48, acc_min=40, acc_max=48, note="Companions must be at least 14 years old and at least 48 in tall.", src=LLC("the-dragon")),
 ("legoland-california", "Coastersaurus"): dict(min=48, acc_min=36, acc_max=48, note="Companions must be adults aged 18 or older.", src=LLC("coastersaurus")),
 ("legoland-california", "Technic Coaster"): dict(min=48, acc_min=42, acc_max=48, note="Riders must be at least 4 years old, and at least 6 to ride alone.", src=LLC("lego-technic-coaster")),
 ("legoland-california", "Galacticoaster"): dict(min=48, acc_min=36, acc_max=48, max=78, src=LLC("galacticoaster")),
 ("legoland-new-york", "Dragon"): dict(min=48, acc_min=42, acc_max=48, max=76, note="Riders must be at least 4 years old; under 6 they must ride with a companion aged 14 or older.", src=LLN("the-dragon")),
 ("legoland-new-york", "Dragon's Apprentice"): dict(min=42, acc_min=36, acc_max=42, src=LLN("dragon-s-apprentice")),
 ("elitch-gardens", "Sidewinder"): dict(min=48, src=EG("sidewinder")),
 ("elitch-gardens", "Twister III: Storm Chaser"): dict(min=48, src=EG("twisteriii")),
 ("elitch-gardens", "Mind Eraser"): dict(min=52, max=80, src=EG("mind-eraser")),
 ("elitch-gardens", "Boomerang"): dict(min=48, src=EG("boomerang")),
 ("elitch-gardens", "Blazin' Buckaroo"): dict(min=42, acc_min=36, acc_max=42, src=EG("blazin-buckaroo")),
}
HP_INTL.update(HP_B7)
INTL_PARKS += [
 dict(slug="lagoon", name="Lagoon", short="Lagoon", loc="Farmington, Utah", state="UT", country="US", official="https://www.lagoonpark.com/", group="Lagoon"),
 dict(slug="silverwood", name="Silverwood Theme Park", short="Silverwood", loc="Athol, Idaho", state="ID", country="US", official="https://www.silverwoodthemepark.com/", group="Silverwood"),
 dict(slug="legoland-florida", name="Legoland Florida", short="Legoland Florida", loc="Winter Haven, Florida", state="FL", country="US", official="https://www.legoland.com/florida/", group="Merlin Entertainments"),
 dict(slug="legoland-california", name="Legoland California", short="Legoland California", loc="Carlsbad, California", state="CA", country="US", official="https://www.legoland.com/california/", group="Merlin Entertainments"),
 dict(slug="legoland-new-york", name="Legoland New York", short="Legoland New York", loc="Goshen, New York", state="NY", country="US", official="https://www.legoland.com/new-york/", group="Merlin Entertainments"),
 dict(slug="great-escape", name="Great Escape", short="Great Escape", loc="Queensbury, New York", state="NY", country="US", official="https://greatescapeparks.enchantedparks.com/", group="Enchanted Parks", former="Six Flags Great Escape", former_note="sixflags.com/greatescape redirects to the Enchanted Parks site, and RCDB lists the park as Great Escape"),
 dict(slug="elitch-gardens", name="Elitch Gardens", short="Elitch Gardens", loc="Denver, Colorado", state="CO", country="US", official="https://elitchgardens.com/", group="Elitch Gardens"),
]
DISPLAY_INTL.update({("legoland-florida", "Dragon"): "The Dragon", ("legoland-california", "Dragon"): "The Dragon", ("legoland-new-york", "Dragon"): "The Dragon",
 ("legoland-florida", "Great Lego Race"): "The Great LEGO Race", ("legoland-california", "Technic Coaster"): "LEGO Technic Coaster", ("great-escape", "Bobcat"): "The Bobcat"})

# ---- Batch 8 (10 Nov 2026): major international parks ----
def EL(s): return ("Energylandia, official attraction page", f"https://energylandia.pl/en/attractions/{s}/")
GL = ("Gardaland, official Rides page", "https://www.gardaland.it/en/explore-gardaland/gardaland-park/rides/")
def HPK(s): return ("Heide Park, official ride page", f"https://www.heide-park.de/en/explore/attractions-shows-entertainment/rides-attractions/{s}/")
def MPG(s): return ("Movie Park Germany, official attraction page", f"https://www.movieparkgermany.de/en/erlebnisse/attraktionen/{s}")
def WH(s): return ("Walibi Holland, official attraction page", f"https://www.walibi.nl/en/park/attractions/{s}")
def WB(s): return ("Walibi Belgium, official attraction page", f"https://www.walibi.be/en/explore-the-park/{s}")
def PA(s): return ("Parc Astérix, official attraction page", f"https://www.parcasterix.fr/en/attractions/{s}")
def FW(s): return ("Ferrari World Abu Dhabi, official ride page", f"https://www.ferrariworldabudhabi.com/en/rides/{s}")
def MW(s): return ("Warner Bros. Movie World, official attraction page", f"https://movieworld.com.au/attractions/{s}")
def DW(s): return ("Dreamworld, official ride page", f"https://www.dreamworld.com.au/rides-and-attractions/{s}/")
def USS(s): return ("Universal Studios Singapore, official ride page", f"https://www.rwsentosa.com/en/play/universal-studios-singapore/rides/{s}")
HP_B8 = {
 ("energylandia", "Energuś"): M(min=120, acc_min=100, acc_max=120, src=EL("little-kids-zone/energus-roller-coaster")),
 ("energylandia", "Viking Roller Coaster"): M(min=140, note="Riders must be at least 12 years old.", src=EL("extreme-zone/viking-rollercoaster")),
 ("energylandia", "Roller Coaster Mayan"): M(min=140, src=EL("extreme-zone/rollercoaster-mayan")),
 ("energylandia", "Dragon Roller Coaster"): M(min=130, acc_min=120, acc_max=130, src=EL("family-zone/rmf-dragon-roller-coaster")),
 ("energylandia", "Formuła"): M(min=140, acc_min=120, acc_max=140, src=EL("extreme-zone/formula-1-roller-coaster")),
 ("energylandia", "Boomerang"): M(min=120, acc_min=100, acc_max=120, src=EL("family-zone/boomerang")),
 ("energylandia", "Speed"): M(min=140, max=195, src=EL("extreme-zone/water-coaster-speed")),
 ("energylandia", "Hyperion"): M(min=140, max=195, src=EL("extreme-zone/pepsi-hyperion")),
 ("energylandia", "Zadra"): M(min=140, src=EL("dragon-zone/zadra")),
 ("energylandia", "Frida"): M(min=120, acc_min=100, acc_max=120, src=EL("dragon-zone/frida")),
 ("energylandia", "Abyssus"): M(min=140, acc_min=120, acc_max=140, src=EL("aqualantis/abyssus")),
 ("energylandia", "Light Explorers"): M(min=120, acc_min=100, acc_max=120, src=EL("aqualantis/light-explorers")),
 ("gardaland", "Blue Tornado"): M(min=140, max=200, src=GL),
 ("gardaland", "Shaman"): M(min=120, max=205, src=GL),
 ("gardaland", "Ortobruco Tour"): M(min=120, acc_min=100, acc_max=120, src=GL),
 ("gardaland", "Mammut"): M(min=130, acc_min=110, acc_max=130, src=GL),
 ("gardaland", "Raptor"): M(min=140, max=195, src=GL),
 ("gardaland", "Oblivion - The Black Hole"): M(min=140, max=195, src=GL),
 ("gardaland", "Dragon Rush"): M(min=130, acc_min=110, acc_max=130, max=200, src=GL),
 ("heide-park", "Bobbahn"): M(min=120, note="Riders must be at least 6 years old.", src=HPK("bobbahn")),
 ("heide-park", "Big Loop"): M(min=120, max=195, src=HPK("big-loop")),
 ("heide-park", "Toxic Garden"): M(min=130, max=195, note="Riders must be at least 10 years old.", src=HPK("toxic-garden-heide-park-resort")),
 ("heide-park", "Colossos - Kampf der Giganten"): M(min=140, max=195, note="Riders must be at least 10 years old.", src=HPK("colossos-kampf-der-giganten")),
 ("heide-park", "Desert Race"): M(min=140, max=195, src=HPK("desert-race")),
 ("heide-park", "Indy-Blitz"): M(min=100, note="Children under 8 years and under 120 cm must ride with an adult.", src=HPK("indy-blitz")),
 ("heide-park", "Flug der Dämonen"): M(min=140, max=195, src=HPK("flug-der-daemonen")),
 ("heide-park", "Krake"): M(min=140, max=195, src=HPK("krake")),
 ("movie-park-germany", "Ghost Chasers"): M(min=120, max=195, src=MPG("ghost-chasers")),
 ("movie-park-germany", "Bandit"): M(min=120, src=MPG("the-bandit")),
 ("movie-park-germany", "Backyardigans: Mission to Mars"): M(min=135, acc_min=90, acc_max=135, src=MPG("backyardigans-mission-to-mars")),
 ("movie-park-germany", "Iron Claw"): M(min=130, max=195, src=MPG("ironclaw")),
 ("movie-park-germany", "Jimmy Neutron's Atomic Flyer"): M(min=130, acc_min=95, acc_max=130, max=205, src=MPG("jimmy-neutrons-atomic-flyer")),
 ("movie-park-germany", "Van Helsing's Factory"): M(min=120, src=MPG("vanhelsings-factory")),
 ("movie-park-germany", "Star Trek: Operation Enterprise"): M(min=130, src=MPG("star-trek-operation-enterprise")),
 ("movie-park-germany", "Studio Tour"): M(min=130, acc_min=110, acc_max=130, src=MPG("movie-park-studio-tour")),
 ("walibi-holland", "Xpress: Platform 13"): M(min=120, src=WH("xpress-platform-13")),
 ("walibi-holland", "Condor"): M(min=140, src=WH("condor")),
 ("walibi-holland", "Speed of Sound"): M(min=120, src=WH("speed-sound")),
 ("walibi-holland", "Drako"): M(min=120, acc_min=90, acc_max=120, src=WH("drako")),
 ("walibi-holland", "Goliath"): M(min=140, src=WH("goliath")),
 ("walibi-holland", "Lost Gravity"): M(min=140, src=WH("lost-gravity")),
 ("walibi-holland", "Untamed"): M(min=120, src=WH("untamed")),
 ("walibi-holland", "Eat My Dust"): M(min=105, acc_min=90, acc_max=105, src=WH("eat-my-dust")),
 ("walibi-holland", "YoY"): M(min=120, src=WH("yoy/thrill")),
 ("walibi-belgium", "Mecalodon"): M(min=120, acc_min=100, acc_max=120, src=WB("attractions-family/mecalodon")),
 ("walibi-belgium", "Pulsar"): M(min=120, src=WB("attractions-thrills/pulsar")),
 ("walibi-belgium", "Tiki-Waka"): M(min=120, acc_min=100, acc_max=120, src=WB("attractions-family/tiki-waka")),
 ("walibi-belgium", "Fun Pilot"): M(min=120, acc_min=90, acc_max=120, src=WB("attractions-kids/fun-pilot")),
 ("walibi-belgium", "Kondaa"): M(min=130, max=195, src=WB("attractions-thrills/kondaa")),
 ("walibi-belgium", "Turbine"): M(min=140, acc_min=130, acc_max=140, src=WB("attractions-thrills/turbine")),
 ("walibi-belgium", "Vampire"): M(min=130, max=195, src=WB("attractions-thrills/vampire")),
 ("walibi-belgium", "Calamity Mine"): M(min=120, acc_min=100, acc_max=120, src=WB("attractions-family/calamity-mine")),
 ("walibi-belgium", "Cobra"): M(min=130, src=WB("attractions-thrills/cobra")),
 ("walibi-belgium", "Loup-Garou"): M(min=120, src=WB("attractions-thrills/loup-garou")),
 ("parc-asterix", "Tonnerre 2 Zeus"): M(min=120, src=PA("thrill/thunder-2-zeus")),
 ("parc-asterix", "OzIris"): M(min=130, src=PA("thrill/osiris-convolvulis")),
 ("parc-asterix", "Pégase Express"): M(min=130, acc_min=100, acc_max=130, src=PA("family/the-pegasus-express")),
 ("parc-asterix", "Cétautomatix"): M(min=100, src=PA("family/fulliautomatix")),
 ("parc-asterix", "Vol D'Icare"): M(min=130, acc_min=100, acc_max=130, src=PA("family/icaruss-flight")),
 ("parc-asterix", "Trace Du Hourra"): M(min=130, acc_min=120, acc_max=130, src=PA("thrill/the-hurrah-trail")),
 ("ferrari-world", "Flying Aces"): M(min=130, max=196, src=FW("flying-aces")),
 ("ferrari-world", "Mission Ferrari"): M(min=130, src=FW("mission-ferrari")),
 ("ferrari-world", "Turbo Track"): M(min=130, max=196, src=FW("turbo-track")),
 ("ferrari-world", "Fiorano GT Challenge"): M(min=130, max=195, src=FW("fiorano-gt-challenge")),
 ("ferrari-world", "Formula Rossa Junior"): M(min=90, src=FW("formula-rossa-junior")),
 ("warner-bros-movie-world", "DC Rivals HyperCoaster"): M(min=130, note="Riders must be at least 7 years old.", src=MW("dc-rivals-hypercoaster")),
 ("warner-bros-movie-world", "Green Lantern Coaster"): M(min=140, src=MW("green-lantern-coaster")),
 ("warner-bros-movie-world", "Road Runner Roller Coaster"): M(min=120, acc_min=110, acc_max=120, src=MW("road-runner-rollercoaster")),
 ("warner-bros-movie-world", "Superman Escape"): M(min=140, max=196, src=MW("superman-escape")),
 ("dreamworld", "Gold Coaster"): M(min=120, max=205, note="Riders must be at least 10 years old.", src=DW("the-gold-coaster")),
 ("dreamworld", "Jungle Rush"): M(min=120, acc_min=95, acc_max=120, max=205, src=DW("jungle-rush")),
 ("dreamworld", "Kenny's Forest Flyer"): M(min=130, acc_min=110, acc_max=130, max=195, src=DW("kennys-forest-flyer")),
 ("dreamworld", "Steel Taipan"): M(min=130, max=200, src=DW("steel-taipan")),
 ("dreamworld", "Big Red Boat"): M(min=105, acc_min=90, acc_max=105, src=DW("big-red-boat-coaster")),
 ("universal-studios-singapore", "Enchanted Airways"): M(min=122, acc_min=92, acc_max=122, max=205, src=USS("enchanted-airways")),
 ("universal-studios-singapore", "Revenge of the Mummy"): M(min=122, src=USS("revenge-of-the-mummy")),
 ("universal-studios-singapore", "Battlestar Galactica"): M(min=125, src=USS("battlestar-galactica-human-vs-cylon")),
 ("universal-studios-singapore", "Canopy Flyer"): M(min=122, acc_min=92, acc_max=122, src=USS("canopy-flyer")),
 ("universal-studios-singapore", "Puss In Boots’ Giant Journey"): M(min=122, acc_min=102, acc_max=122, src=USS("puss-in-boots-giant-journey")),
}
HP_INTL.update(HP_B8)
INTL_PARKS += [
 dict(slug="energylandia", name="Energylandia", short="Energylandia", loc="Zator, Poland", state="Lesser Poland", country="PL", official="https://energylandia.pl/en/", group="Energylandia"),
 dict(slug="gardaland", name="Gardaland", short="Gardaland", loc="Castelnuovo del Garda, Italy", state="Veneto", country="IT", official="https://www.gardaland.it/en/", group="Merlin Entertainments"),
 dict(slug="heide-park", name="Heide Park Resort", short="Heide Park", loc="Soltau, Germany", state="Lower Saxony", country="DE", official="https://www.heide-park.de/en/", group="Merlin Entertainments"),
 dict(slug="movie-park-germany", name="Movie Park Germany", short="Movie Park Germany", loc="Bottrop, Germany", state="North Rhine-Westphalia", country="DE", official="https://www.movieparkgermany.de/en", group="Parques Reunidos"),
 dict(slug="walibi-holland", name="Walibi Holland", short="Walibi Holland", loc="Biddinghuizen, Netherlands", state="Flevoland", country="NL", official="https://www.walibi.nl/en", group="Compagnie des Alpes"),
 dict(slug="walibi-belgium", name="Walibi Belgium", short="Walibi Belgium", loc="Wavre, Belgium", state="Walloon Brabant", country="BE", official="https://www.walibi.be/en", group="Compagnie des Alpes"),
 dict(slug="parc-asterix", name="Parc Astérix", short="Parc Astérix", loc="Plailly, France", state="Hauts-de-France", country="FR", official="https://www.parcasterix.fr/en", group="Compagnie des Alpes"),
 dict(slug="ferrari-world", name="Ferrari World Abu Dhabi", short="Ferrari World", loc="Abu Dhabi, United Arab Emirates", state="Abu Dhabi", country="AE", official="https://www.ferrariworldabudhabi.com/en", group="Miral"),
 dict(slug="warner-bros-movie-world", name="Warner Bros. Movie World", short="Movie World", loc="Oxenford, Australia", state="Queensland", country="AU", official="https://movieworld.com.au/", group="Village Roadshow Theme Parks"),
 dict(slug="dreamworld", name="Dreamworld", short="Dreamworld", loc="Coomera, Australia", state="Queensland", country="AU", official="https://www.dreamworld.com.au/", group="Dreamworld"),
 dict(slug="universal-studios-singapore", name="Universal Studios Singapore", short="Universal Studios Singapore", loc="Sentosa, Singapore", state="Singapore", country="SG", official="https://www.rwsentosa.com/en/play/universal-studios-singapore", group="Resorts World Sentosa"),
]
DISPLAY_INTL.update({("gardaland", "Oblivion - The Black Hole"): "Oblivion: The Black Hole", ("heide-park", "Colossos - Kampf der Giganten"): "Colossos: Kampf der Giganten",
 ("universal-studios-singapore", "Puss In Boots’ Giant Journey"): "Puss In Boots' Giant Journey", ("universal-studios-singapore", "Battlestar Galactica"): "Battlestar Galactica: Human vs. Cylon",
 ("parc-asterix", "Trace Du Hourra"): "La Trace du Hourra", ("parc-asterix", "Vol D'Icare"): "Vol d'Icare", ("dreamworld", "Gold Coaster"): "The Gold Coaster"})

# ---- Batch 10: regional parks (Indiana Beach, Adventureland, Wild Adventures, Waldameer, Six Flags Mexico) ----
def IB(s): return ("Indiana Beach, official ride page", f"https://www.indianabeach.com/rides/{s}/")
def AL(s): return ("Adventureland, official ride page", f"https://www.adventurelandpark.com/discover-the-park/adventureland-rides/{s}/")
def WA(s): return ("Wild Adventures, official ride page", f"https://www.wildadventures.com/explore-the-park/rides/{s}/")
def WL(s): return ("Waldameer, official attraction page", f"https://waldameer.com/park-attractions/{s}/")
def SM(s): return ("Six Flags Mexico, official attraction page", f"https://www.sixflags.com/mexico/attractions/{s}")
HP_B10 = {
 ("indiana-beach", "Hoosier Hurricane"): dict(min=48, src=IB("hoosier-hurricane")),
 ("indiana-beach", "Tig'rr"): dict(min=54, src=IB("tigrr")),
 ("indiana-beach", "Lost Coaster of Superstition Mountain"): dict(min=48, src=IB("lost-coaster")),
 ("indiana-beach", "Cornball Express"): dict(min=46, src=IB("cornball-express")),
 ("indiana-beach", "Steel Hawg"): dict(min=48, note="Riders may not sit on another rider's lap.", src=IB("steel-hawg")),
 ("indiana-beach", "All American Triple Loop"): dict(min=59, max=77, src=IB("all-american-triple-loop")),
 ("indiana-beach", "Cyclone"): dict(min=48, src=IB("cyclone")),
 ("adventureland-iowa", "Outlaw"): dict(min=48, src=AL("outlaw")),
 ("adventureland-iowa", "Monster"): dict(min=48, src=AL("monster")),
 ("adventureland-iowa", "Phoenix"): dict(min=48, src=AL("phoenix")),
 ("adventureland-iowa", "Dragon Slayer"): dict(min=48, max=77, src=AL("dragon-slayer")),
 ("adventureland-iowa", "Flying Viking"): dict(min=48, acc_min=36, acc_max=48, note="Riders 36 to 48 in must ride with a supervising companion at least 48 in tall.", src=AL("flying-viking")),
 ("adventureland-iowa", "Tornado"): dict(min=48, src=AL("tornado")),
 ("wild-adventures", "Boomerang"): dict(min=48, src=WA("boomerang")),
 ("wild-adventures", "Twisted Typhoon"): dict(min=52, src=WA("twisted-typhoon")),
 ("wild-adventures", "Outpost Express"): dict(min=44, acc_min=36, acc_max=44, note="Riders 36 to 44 in must ride with someone at least 14 years old.", src=WA("outpost-express")),
 ("wild-adventures", "Marsh Mayhem"): dict(min=50, acc_min=46, acc_max=50, note="Riders 46 to 50 in must ride with someone at least 14 years old.", src=WA("marsh-mayhem")),
 ("wild-adventures", "Swamp Thing"): dict(min=44, max=78, src=WA("swamp-thing")),
 ("waldameer", "Comet"): dict(min=46, acc_min=36, acc_max=46, note="Riders 36 to 46 in must sit next to a supervising companion.", src=WL("comet")),
 ("waldameer", "Ravine Flyer 3"): dict(min=40, src=WL("ravine-flyer-3")),
 ("waldameer", "Ravine Flyer II"): dict(min=48, src=WL("ravine-flyer-ii")),
 ("waldameer", "Steel Dragon"): dict(min=50, acc_min=46, acc_max=50, max=78, src=WL("steel-dragon")),
 ("waldameer", "Whirlwind"): dict(min=48, acc_min=36, acc_max=48, max=77, src=WL("whirlwind")),
 ("six-flags-mexico", "Tsunami"): M(min=120, acc_min=105, acc_max=120, src=SM("tsunami")),
 ("six-flags-mexico", "Batgirl Batarang"): M(min=120, src=SM("batgirl-batarang")),
 ("six-flags-mexico", "Batman The Ride"): M(min=130, src=SM("batman-ride-7")),
 ("six-flags-mexico", "Superman el Último Escape"): M(min=130, src=SM("superman-el-ultimo-escape")),
 ("six-flags-mexico", "Dark Knight"): M(min=120, acc_min=105, acc_max=120, src=SM("dark-knight-coaster-3")),
 ("six-flags-mexico", "Joker"): M(min=120, acc_min=105, acc_max=120, src=SM("the-joker")),
 ("six-flags-mexico", "Medusa Steel Coaster"): M(min=130, src=SM("medusa-steel-coaster")),
 ("six-flags-mexico", "Wonder Woman"): M(min=122, src=SM("wonder-woman-coaster")),
 ("six-flags-mexico", "Speedway Stunt Coaster"): M(min=120, acc_min=95, acc_max=120, src=SM("speedway-stunt-coaster")),
}
HP_INTL.update(HP_B10)
INTL_PARKS += [
 dict(slug="indiana-beach", name="Indiana Beach", short="Indiana Beach", loc="Monticello, Indiana", state="IN", country="US", official="https://www.indianabeach.com/", group="Indiana Beach"),
 dict(slug="adventureland-iowa", name="Adventureland Park", short="Adventureland", loc="Altoona, Iowa", state="IA", country="US", official="https://www.adventurelandpark.com/", group="Palace Entertainment"),
 dict(slug="wild-adventures", name="Wild Adventures Theme Park", short="Wild Adventures", loc="Valdosta, Georgia", state="GA", country="US", official="https://www.wildadventures.com/", group="Palace Entertainment"),
 dict(slug="waldameer", name="Waldameer Park", short="Waldameer", loc="Erie, Pennsylvania", state="PA", country="US", official="https://waldameer.com/", group="Waldameer"),
 dict(slug="six-flags-mexico", name="Six Flags Mexico", short="Six Flags Mexico", loc="Mexico City, Mexico", state="Mexico City", country="MX", official="https://www.sixflags.com/mexico", group="Six Flags"),
]
DISPLAY_INTL.update({("six-flags-mexico", "Joker"): "The Joker", ("six-flags-mexico", "Dark Knight"): "Dark Knight Coaster", ("six-flags-mexico", "Wonder Woman"): "Wonder Woman Coaster"})
CB = ("Canobie Lake Park, official attraction page", "https://www.canobie.com/park-attractions/{}/")
def CBs(s): return (CB[0], CB[1].format(s))
FSO = ("Fun Spot America Orlando, official roller coasters page", "https://fun-spot.com/orlando/roller-coasters/")
FSK = ("Fun Spot America Kissimmee, official roller coasters page", "https://fun-spot.com/kissimmee/kissimmee-roller-coasters/")
HP_B10b = {
 ("canobie-lake-park", "Untamed"): dict(min=48, src=CBs("untamed")),
 ("canobie-lake-park", "Yankee Cannonball"): dict(min=48, src=CBs("yankee-cannonball")),
 ("canobie-lake-park", "Dragon"): dict(min=42, note="The park says riders under 42 in may ride with a supervising companion.", src=CBs("dragon-coaster")),
 ("fun-spot-orlando", "White Lightning"): dict(min=46, src=FSO),
 ("fun-spot-orlando", "Freedom Flyer"): dict(min=52, acc_min=38, acc_max=52, note="Riders 38 to 52 in must ride with an adult.", src=FSO),
 ("fun-spot-orlando", "Sea Serpent"): dict(min=36, src=FSO),
 ("fun-spot-kissimmee", "Mine Blower"): dict(min=48, src=FSK),
 ("fun-spot-kissimmee", "Galaxy Spin"): dict(min=48, acc_min=42, acc_max=48, note="Riders 42 to 48 in must ride with an adult.", src=FSK),
 ("fun-spot-kissimmee", "Sea Serpent"): dict(min=36, src=FSK),
 ("fun-spot-kissimmee", "Hurricane"): dict(min=42, src=FSK),
}
HP_INTL.update(HP_B10b)
INTL_PARKS += [
 dict(slug="canobie-lake-park", name="Canobie Lake Park", short="Canobie Lake", loc="Salem, New Hampshire", state="NH", country="US", official="https://www.canobie.com/", group="Canobie Lake Park"),
 dict(slug="fun-spot-orlando", name="Fun Spot America Orlando", short="Fun Spot Orlando", loc="Orlando, Florida", state="FL", country="US", official="https://fun-spot.com/orlando/", group="Fun Spot America Theme Parks"),
 dict(slug="fun-spot-kissimmee", name="Fun Spot America Kissimmee", short="Fun Spot Kissimmee", loc="Kissimmee, Florida", state="FL", country="US", official="https://fun-spot.com/kissimmee/", group="Fun Spot America Theme Parks"),
]

# ---- Batch 10d: Europe and US additions ----
def TV(s): return ("Toverland, official ride page", f"https://www.toverland.com/en/rides/{s}")
def CH(s): return ("Chessington World of Adventures, official ride page", f"https://www.chessington.com/explore/theme-park-zoo/rides-attractions/{s}/")
def GL(s): return ("Gröna Lund, official ride page", f"https://www.gronalund.com/en/rides/{s}")
def TI(s): return ("Tivoli Gardens, official ride page", f"https://www.tivoli.dk/en/rides/{s}")
def LM(s): return ("Linnanmäki, official ride page", f"https://www.linnanmaki.fi/en/ride/{s}/")
FL = ("Flamingo Land, official ride restrictions page", "https://www.flamingoland.co.uk/plan-your-visit/ride-restrictions/")
def MP(s): return ("Morey's Piers, official ride page", f"https://www.moreyspiers.com/moreys-rides/{s}/")
def PW(s): return ("Parque Warner Madrid, official attraction page", f"https://www.parquewarner.com/en/experiencias/atracciones/{s}")
HP_B10d = {
 ("toverland", "Toos-Express"): M(min=120, acc_min=90, acc_max=120, src=TV("toos-express")),
 ("toverland", "Booster Bike"): M(min=140, src=TV("booster-bike")),
 ("toverland", "Troy"): M(min=120, src=TV("troy")),
 ("toverland", "Dwervelwind"): M(min=120, acc_min=100, acc_max=120, note="Riders 100 to 120 cm must ride with an adult (16+).", src=TV("dwervelwind")),
 ("toverland", "Fēnix"): M(min=132, max=195, src=TV("fenix")),
 ("chessington", "Dragon's Fury"): M(min=120, max=195, src=CH("dragons-fury")),
 ("chessington", "Mandrill Mayhem"): M(min=120, max=195, src=CH("mandrill-mayhem")),
 ("chessington", "Chase's Mountain Mission"): M(min=110, acc_min=90, acc_max=110, note="Riders 90 to 110 cm must ride with an adult (16+).", src=CH("chases-mountain-mission")),
 ("chessington", "Vampire"): M(min=130, acc_min=110, acc_max=130, note="Riders 110 to 130 cm must ride with an adult aged 16+.", src=CH("vampire")),
 ("chessington", "Rattlesnake"): M(min=140, max=196, src=CH("rattlesnake")),
 ("grona-lund", "Kvasten"): M(min=120, acc_min=110, acc_max=120, note="Riders must also be at least 4 years old.", src=GL("kvasten")),
 ("grona-lund", "Insane"): M(min=140, max=195, src=GL("insane")),
 ("grona-lund", "Twister"): M(min=120, src=GL("twister")),
 ("grona-lund", "Monster"): M(min=140, src=GL("monster")),
 ("tivoli-gardens", "Dæmonen"): M(min=132, src=TI("the-demon")),
 ("tivoli-gardens", "Kamelen"): M(min=120, acc_min=100, acc_max=120, note="Riders 100 to 120 cm must ride with a paying companion aged at least 14.", src=TI("the-camel-trail")),
 ("linnanmaki", "Linnunrata"): M(min=120, max=195, note="Riders must be over 6 to ride without a guardian.", src=LM("linnunrata-extra")),
 ("linnanmaki", "Vuoristorata"): M(min=140, acc_min=120, acc_max=140, note="Riders 120 to 140 cm must ride with a guardian.", src=LM("vuoristorata")),
 ("linnanmaki", "Pikajuna"): M(min=130, acc_min=100, acc_max=130, note="Riding without a guardian also requires being over 10.", src=LM("pikajuna")),
 ("linnanmaki", "Tulireki"): M(min=140, acc_min=120, acc_max=140, note="Riding alone requires being over 8; riding with a guardian requires being over 6.", src=LM("tulireki")),
 ("linnanmaki", "Kirnu"): M(min=140, max=195, src=LM("kirnu")),
 ("linnanmaki", "Salama"): M(min=140, acc_min=120, acc_max=140, max=195, src=LM("salama")),
 ("linnanmaki", "Ukko"): M(min=140, src=LM("ukko")),
 ("linnanmaki", "Taiga"): M(min=140, max=195, src=LM("taiga")),
 ("flamingo-land", "Mumbo Jumbo"): M(min=122, src=FL),
 ("flamingo-land", "Hero"): M(min=127, src=FL),
 ("flamingo-land", "Twistosaurus"): M(min=105, src=FL),
 ("flamingo-land", "Sik"): M(min=140, max=195, src=FL),
 ("flamingo-land", "Velocity"): M(min=140, max=198, src=FL),
 ("flamingo-land", "Kumali"): M(min=130, src=FL),
 ("moreys-piers", "Great Nor'Easter"): dict(min=52, max=79, src=MP("the-great-noreaster")),
 ("moreys-piers", "Sea Serpent"): dict(min=48, max=81, src=MP("sea-serpent")),
 ("moreys-piers", "Rollies Coaster"): dict(min=50, acc_min=44, acc_max=50, max=75, note="Riders 44 to 50 in must ride with an adult.", src=MP("rollies-coaster")),
 ("moreys-piers", "Doo Wopper"): dict(min=48, acc_min=36, acc_max=48, src=MP("doo-wopper")),
 ("moreys-piers", "Wild Whizzer"): dict(min=48, acc_min=36, acc_max=48, max=77, src=MP("wild-whizzer")),
 ("moreys-piers", "Runaway Tram"): dict(min=48, acc_min=40, acc_max=48, src=MP("runaway-tram")),
 ("parque-warner-madrid", "Shadows of Arkham"): M(min=132, src=PW("batman-arkham-asylum")),
 ("parque-warner-madrid", "Superman / la Atracción de Acero"): M(min=132, src=PW("superman-atraccion-de-acero")),
 ("parque-warner-madrid", "Coaster Express"): M(min=121, max=197, src=PW("coaster-express")),
 ("parque-warner-madrid", "Stunt Fall"): M(min=137, max=195, src=PW("stunt-fall-new")),
 ("parque-warner-madrid", "Batman Gotham City Escape"): M(min=140, max=195, src=PW("Batman-Gotham-City-Escape")),
}
HP_INTL.update(HP_B10d)
INTL_PARKS += [
 dict(slug="toverland", name="Toverland", short="Toverland", loc="Sevenum, Netherlands", state="Limburg", country="NL", official="https://www.toverland.com/en/", group="Toverland"),
 dict(slug="chessington", name="Chessington World of Adventures", short="Chessington", loc="Chessington, England", state="Greater London", country="GB", official="https://www.chessington.com/", group="Merlin Entertainments"),
 dict(slug="grona-lund", name="Gröna Lund", short="Gröna Lund", loc="Stockholm, Sweden", state="Stockholm", country="SE", official="https://www.gronalund.com/en", group="Parks and Resorts Scandinavia"),
 dict(slug="tivoli-gardens", name="Tivoli Gardens", short="Tivoli", loc="Copenhagen, Denmark", state="Capital Region", country="DK", official="https://www.tivoli.dk/en", group="Tivoli"),
 dict(slug="linnanmaki", name="Linnanmäki", short="Linnanmäki", loc="Helsinki, Finland", state="Uusimaa", country="FI", official="https://www.linnanmaki.fi/en/", group="Linnanmäki"),
 dict(slug="flamingo-land", name="Flamingo Land", short="Flamingo Land", loc="Kirby Misperton, England", state="North Yorkshire", country="GB", official="https://www.flamingoland.co.uk/", group="Flamingo Land"),
 dict(slug="moreys-piers", name="Morey's Piers", short="Morey's Piers", loc="Wildwood, New Jersey", state="NJ", country="US", official="https://www.moreyspiers.com/", group="Morey's Piers"),
 dict(slug="parque-warner-madrid", name="Parque Warner Madrid", short="Parque Warner", loc="San Martín de la Vega, Spain", state="Madrid", country="ES", official="https://www.parquewarner.com/en", group="Parques Reunidos"),
]
DISPLAY_INTL.update({("moreys-piers", "Great Nor'Easter"): "The Great Nor'Easter", ("moreys-piers", "Rollies Coaster"): "Rollie's Coaster", ("parque-warner-madrid", "Superman / la Atracción de Acero"): "Superman: La Atracción de Acero"})

# ---- Batch 10e: Särkänniemi, Seabreeze, Santa Cruz Beach Boardwalk, Luna Park (Coney Island) ----
def SK(s): return ("Särkänniemi, official ride page", f"https://sarkanniemi.fi/en/rides/{s}")
SB = ("Seabreeze, official ride requirements page", "https://seabreeze.com/plan-your-visit/ride-requirements/")
SC = ("Santa Cruz Beach Boardwalk, official height requirements page", "https://beachboardwalk.com/rides/height-requirements/")
def LP(s): return ("Luna Park in Coney Island, official ride page", f"https://lunaparknyc.com/rides/{s}/")
HP_B10e = {
 ("sarkanniemi", "MotoGee"): M(min=120, src=SK("Motogee")),
 ("sarkanniemi", "Hype"): M(min=140, src=SK("hype")),
 ("sarkanniemi", "Konect"): M(min=120, acc_min=100, acc_max=120, note="Riders 100 to 120 cm must ride with an adult; riding without an adult also requires being at least 6.", src=SK("konect")),
 ("sarkanniemi", "Tornado"): M(min=140, src=SK("tornado")),
 ("seabreeze", "Jack Rabbit"): dict(min=48, src=SB),
 ("seabreeze", "Bobsleds"): dict(min=48, acc_min=38, acc_max=48, note="Riders 38 to 48 in must ride with a responsible person who meets the ride criteria.", src=SB),
 ("seabreeze", "Bear Trax"): dict(min=36, note="Guests over 58 in must ride with a child in their party.", src=SB),
 ("seabreeze", "Whirlwind"): dict(min=48, src=SB),
 ("santa-cruz-beach-boardwalk", "Giant Dipper"): dict(min=50, src=SC),
 ("santa-cruz-beach-boardwalk", "Undertow"): dict(min=48, max=77, src=SC),
 ("santa-cruz-beach-boardwalk", "Sea Serpent"): dict(min=48, acc_min=34, acc_max=48, note="Riders 34 to 48 in may ride with a chaperone.", src=SC),
 ("luna-park-coney-island", "Cyclone"): dict(min=54, src=LP("coney-island-cyclone")),
 ("luna-park-coney-island", "Thunderbolt"): dict(min=50, src=LP("thunderbolt")),
 ("luna-park-coney-island", "Tickler"): dict(min=48, acc_min=42, acc_max=48, src=LP("the-tickler")),
 ("luna-park-coney-island", "Circus Coaster"): dict(min=48, acc_min=36, acc_max=48, src=LP("circus-coaster")),
 ("luna-park-coney-island", "Soarin' Eagle"): dict(min=52, src=LP("soarin-eagle")),
 ("luna-park-coney-island", "Steeplechase"): dict(min=48, src=LP("steeplechase")),
 ("luna-park-coney-island", "Mini Mouse"): dict(min=48, src=LP("mini-mouse")),
}
HP_INTL.update(HP_B10e)
INTL_PARKS += [
 dict(slug="sarkanniemi", name="Särkänniemi", short="Särkänniemi", loc="Tampere, Finland", state="Pirkanmaa", country="FI", official="https://sarkanniemi.fi/en/", group="Särkänniemi"),
 dict(slug="seabreeze", name="Seabreeze Amusement Park", short="Seabreeze", loc="Rochester, New York", state="NY", country="US", official="https://seabreeze.com/", group="Seabreeze"),
 dict(slug="santa-cruz-beach-boardwalk", name="Santa Cruz Beach Boardwalk", short="Santa Cruz Beach Boardwalk", loc="Santa Cruz, California", state="CA", country="US", official="https://beachboardwalk.com/", group="Santa Cruz Seaside Company"),
 dict(slug="luna-park-coney-island", name="Luna Park in Coney Island", short="Luna Park", loc="Brooklyn, New York", state="NY", country="US", official="https://lunaparknyc.com/", group="Central Amusement International"),
]
DISPLAY_INTL.update({("luna-park-coney-island", "Cyclone"): "Coney Island Cyclone", ("luna-park-coney-island", "Tickler"): "The Tickler"})

# ---- Batch 10f: Dutch Wonderland, Idlewild ----
def DW(s): return ("Dutch Wonderland, official attraction page", f"https://www.dutchwonderland.com/discover-the-park/attractions/{s}/")
def IW(s): return ("Idlewild & SoakZone, official attraction page", f"https://www.idlewild.com/discover-the-park/attractions/{s}/")
HP_B10f = {
 ("dutch-wonderland", "Kingdom Coaster"): dict(min=46, src=DW("kingdom-coaster")),
 ("dutch-wonderland", "Joust"): dict(min=42, acc_min=36, acc_max=42, note="Riders under 42 in must ride with a responsible rider at least 18 years old.", src=DW("joust-family-coaster")),
 ("dutch-wonderland", "Merlin's Mayhem"): dict(min=39, max=78, src=DW("merlins-mayhem")),
 ("idlewild", "Wild Mouse"): dict(min=48, src=IW("wild-mouse")),
 ("idlewild", "Rollo Coaster"): dict(min=42, note="The park lists an adult companion as required.", src=IW("rollo-coaster")),
}
HP_INTL.update(HP_B10f)
INTL_PARKS += [
 dict(slug="dutch-wonderland", name="Dutch Wonderland", short="Dutch Wonderland", loc="Lancaster, Pennsylvania", state="PA", country="US", official="https://www.dutchwonderland.com/", group="Palace Entertainment"),
 dict(slug="idlewild", name="Idlewild & SoakZone", short="Idlewild", loc="Ligonier, Pennsylvania", state="PA", country="US", official="https://www.idlewild.com/", group="Palace Entertainment"),
]

# ---- Batch 11b (10 Nov 2026): Six Flags Qiddiya City, Legoland Windsor/Deutschland/Billund, Mirabilandia, Tripsdrill, Djurs Sommerland, Drayton Manor, TusenFryd, Bobbejaanland, Skyline Park ----
def SFQ(s): return ("Six Flags Qiddiya City, official ride accessibility guide (PDF)", f"https://sixflagsqiddiyacity.com/content/dam/sixflags/en/pdfs/accessibility/rides/Accessibility%20Guide%20-%20{s}_r.pdf")
LLW = ("Legoland Windsor, official height restrictions page", "https://www.legoland.co.uk/plan-your-day/useful-guides/height-restrictions/")
LLD = ("Legoland Deutschland, official age and height restrictions (PDF)", "https://www.legoland.de/media/4l5pfnue/legoland-altersbeschraenkungen-groe%C3%9Fenbeschraenkungen.pdf")
def LLB(s): return ("Legoland Billund, official ride page", f"https://www.legoland.dk/en/explore/the-park/attractions/{s}/")
def MIR(s): return ("Mirabilandia, official attraction page", f"https://www.mirabilandia.it/en/attivita/attrazioni/{s}")
def TD(s): return ("Erlebnispark Tripsdrill, official attraction page", f"https://tripsdrill.de/en/theme-park/attractions/detail-page/{s}")
def DJ(s): return ("Djurs Sommerland, official ride page", f"https://www.djurssommerland.dk/en/rides/{s}/")
def DM(s): return ("Drayton Manor, official ride page", f"https://www.draytonmanor.co.uk/attraction-details/{s}")
def TF(s): return ("TusenFryd, official attraction page", f"https://www.tusenfryd.no/en/attraksjoner/{s}")
def BJ(s): return ("Bobbejaanland, official attraction page", f"https://www.bobbejaanland.be/parkactiviteiten/attracties/{s}")
def SKP(s): return ("Skyline Park, official attraction page", f"https://www.skylinepark.de/attraktionen/{s}/")
Q130 = "Riders under 130 cm must ride with an adult companion."
HP_B11b = {
 ("six-flags-qiddiya-city", "Falcons Flight"): M(min=130, max=196, src=SFQ("Falcons%20Flight")),
 ("six-flags-qiddiya-city", "Sea Stallion"): M(min=130, acc_min=120, acc_max=130, max=195, note=Q130 + " The park recommends a minimum age of 6.", src=SFQ("Sea%20Stallion")),
 ("six-flags-qiddiya-city", "Saw Mill Falls"): M(min=130, acc_min=100, acc_max=130, note=Q130 + " Recommended minimum age: 5 with an adult, 8 unaccompanied.", src=SFQ("Saw%20Mill%20Falls")),
 ("six-flags-qiddiya-city", "Twilight Express"): M(min=130, acc_min=95, acc_max=130, max=205, note=Q130 + " Recommended minimum age: 4 with an adult, 8 unaccompanied.", src=SFQ("Twilight%20Express")),
 ("six-flags-qiddiya-city", "Adrena-Line"): M(min=130, acc_min=105, acc_max=130, max=205, note=Q130 + " Recommended minimum age: 4 with an adult, 8 unaccompanied.", src=SFQ("Adrena-Line")),
 ("six-flags-qiddiya-city", "Iron Rattler"): M(min=130, acc_min=120, acc_max=130, max=205, note=Q130 + " Recommended minimum age to ride unaccompanied: 10.", src=SFQ("Iron%20Rattler")),
 ("six-flags-qiddiya-city", "Spitfire"): M(min=130, acc_min=105, acc_max=130, note=Q130, src=SFQ("Spitfire")),
 ("six-flags-qiddiya-city", "Colossus"): M(min=130, acc_min=120, acc_max=130, max=190, note=Q130, src=SFQ("Colossus")),
 ("legoland-windsor", "Dragon"): M(min=130, acc_min=100, acc_max=130, note="Riders under 130 cm must be accompanied by a responsible person at least 16 years old.", src=LLW),
 ("legoland-windsor", "Dragon's Apprentice"): M(min=130, acc_min=90, acc_max=130, note="Riders under 130 cm must be accompanied by a responsible person at least 16 years old.", src=LLW),
 ("legoland-windsor", "DUPLO Dino Coaster"): M(min=90, src=LLW),
 ("legoland-windsor", "Minifigure Speedway"): M(min=105, src=LLW),
 ("legoland-deutschland", "Das Große LEGO Rennen"): M(min=120, acc_min=110, acc_max=120, note="Minimum age 4 with an adult, 6 without.", src=LLD),
 ("legoland-deutschland", "Feuerdrache"): M(min=120, acc_min=110, acc_max=120, note="Minimum age 6 with an adult, 8 without.", src=LLD),
 ("legoland-deutschland", "Drachenjagd"): M(min=120, acc_min=100, acc_max=120, note="Minimum age 4 with an adult, 6 without.", src=LLD),
 ("legoland-deutschland", "Maximus - Der Flug des Wächters"): M(min=130, acc_min=120, acc_max=130, max=200, note="Minimum age 6 with an adult, 8 without.", src=LLD),
 ("legoland-billund", "Dragen"): M(min=120, acc_min=100, acc_max=120, note="Riders 100 to 120 cm must be accompanied by a responsible adult.", src=LLB("the-dragon")),
 ("legoland-billund", "X-treme Racers"): M(min=120, max=195, src=LLB("x-treme-racers")),
 ("legoland-billund", "Polar X-plorer"): M(min=130, acc_min=120, acc_max=130, note="Riders 120 to 130 cm must be accompanied by a responsible adult.", src=LLB("polar-x-plorer")),
 ("legoland-billund", "Flying Eagle"): M(min=120, acc_min=100, acc_max=120, note="Riders 100 to 120 cm must be accompanied by a responsible adult.", src=LLB("flying-eagle")),
 ("legoland-billund", "Minifigure Speedway"): M(min=130, acc_min=110, acc_max=130, note="Riders 110 to 130 cm must be accompanied by a responsible adult.", src=LLB("minifigure-speedway")),
 ("mirabilandia", "Katun"): M(min=140, src=MIR("katun")),
 ("mirabilandia", "iSpeed"): M(min=140, max=195, src=MIR("ispeed")),
 ("mirabilandia", "Divertical"): M(min=130, note="The park requires an adult companion for riders between 8 and 10 years old.", src=MIR("divertical")),
 ("mirabilandia", "Cowabunga Carts"): M(min=90, note="The park requires an adult companion for riders under 8 years old and under 110 cm.", src=MIR("cowabunga-carts")),
 ("mirabilandia", "PAW Patrol To The Rescue"): M(min=90, note="The park requires an adult companion for riders under 8 years old.", src=MIR("paw-patrol-to-the-rescue")),
 ("mirabilandia", "Gold Digger"): M(min=90, note="The park requires an adult companion for riders between 3 and 10 years old.", src=MIR("gold-digger")),
 ("mirabilandia", "Rexplorer"): M(min=90, note="The park requires an adult companion for riders between 3 and 10 years old.", src=MIR("rexplorer")),
 ("mirabilandia", "Master Thai"): M(min=120, note="The park requires an adult companion for riders between 6 and 8 years old.", src=MIR("master-thai")),
 ("mirabilandia", "Desmo Race"): M(min=120, max=195, note="The park requires an adult companion for riders under 10 years old and under 140 cm, and lists a maximum weight of 135 kg.", src=MIR("desmo-race")),
 ("tripsdrill", "Karacho"): M(min=125, max=195, note="Minimum age 8 with an adult, 11 to ride alone.", src=TD("karacho")),
 ("tripsdrill", "Mammut"): M(min=120, note="Minimum age 6 with an adult, 8 to ride alone.", src=TD("mammut")),
 ("tripsdrill", "G'sengte Sau"): M(min=100, note="Minimum age 4 with an adult, 8 to ride alone.", src=TD("gsengte-sau")),
 ("tripsdrill", "Volldampf"): M(min=95, note="Minimum age 4 with an adult, 8 to ride alone.", src=TD("volldampf")),
 ("tripsdrill", "Hals-über-Kopf"): M(min=120, note="Minimum age 6 with an adult, 8 to ride alone.", src=TD("hals-ueber-kopf")),
 ("djurs-sommerland", "Thor's Hammer"): M(min=130, acc_min=100, acc_max=130, note="Children under 130 cm must be accompanied and under adult supervision.", src=DJ("vikingeland/thors-hammer")),
 ("djurs-sommerland", "Piraten"): M(min=140, max=196, src=DJ("piratland/piraten")),
 ("djurs-sommerland", "Skatteøen"): M(min=130, acc_min=110, acc_max=130, src=DJ("piratland/skatteoeen")),
 ("djurs-sommerland", "Juvelen"): M(min=132, acc_min=120, acc_max=132, src=DJ("mexicoland/juvelen")),
 ("djurs-sommerland", "Vilde Hønsejagt"): M(min=120, acc_min=90, acc_max=120, src=DJ("bondegaardsland/den-vilde-hoensejagt")),
 ("djurs-sommerland", "DrageKongen"): M(min=130, acc_min=120, acc_max=130, max=196, src=DJ("wild-asia/dragekongen")),
 ("djurs-sommerland", "Jungle Rally"): M(min=120, acc_min=90, acc_max=120, src=DJ("wild-asia/jungle-rally")),
 ("djurs-sommerland", "T-Rex Family Coaster"): M(min=130, acc_min=90, acc_max=130, src=DJ("dinosaurland/t-rex-family-coaster")),
 ("drayton-manor", "Jormungandr"): M(min=120, acc_min=105, acc_max=120, note="Riders 105 to 120 cm must be accompanied by an adult.", src=DM("jormungandr")),
 ("drayton-manor", "Troublesome Trucks Runaway Coaster"): M(min=120, acc_min=100, acc_max=120, note="Riders under 120 cm must be accompanied by an adult.", src=DM("troublesome-trucks-runaway-coaster")),
 ("drayton-manor", "Accelerator"): M(min=120, acc_min=100, acc_max=120, note="Riders under 120 cm must be accompanied by a responsible person aged 16 or over.", src=DM("accelerator")),
 ("drayton-manor", "Wave"): M(min=132, acc_min=120, acc_max=132, note="Riders under 132 cm must be accompanied by a responsible person aged 16 or over.", src=DM("the-wave")),
 ("drayton-manor", "Gold Rush"): M(min=100, max=196, src=DM("gold-rush")),
 ("tusenfryd", "Thundercoaster"): M(min=120, src=TF("thundercoaster")),
 ("tusenfryd", "Loopen"): M(min=110, src=TF("loopen")),
 ("tusenfryd", "SuperSplash"): M(min=120, src=TF("supersplash")),
 ("tusenfryd", "Speed Monster"): M(min=140, src=TF("speedmonster")),
 ("tusenfryd", "Western-Expressen"): M(min=110, acc_min=95, acc_max=110, src=TF("western-expressen")),
 ("tusenfryd", "HuriHuri"): M(min=110, acc_min=95, acc_max=110, src=TF("hurihuri")),
 ("tusenfryd", "Storm - The Dragon Legend"): M(min=130, src=TF("storm")),
 ("bobbejaanland", "Dreamcatcher"): M(min=130, acc_min=110, acc_max=130, src=BJ("dreamcatcher")),
 ("bobbejaanland", "Revolution"): M(min=140, acc_min=100, acc_max=140, src=BJ("revolution")),
 ("bobbejaanland", "Bob Express"): M(min=140, acc_min=120, acc_max=140, max=195, src=BJ("bob-express")),
 ("bobbejaanland", "Oki Doki"): M(min=140, acc_min=95, acc_max=140, src=BJ("oki-doki")),
 ("bobbejaanland", "Typhoon"): M(min=140, acc_min=125, acc_max=140, src=BJ("typhoon")),
 ("bobbejaanland", "Speedy Bob"): M(min=140, acc_min=110, acc_max=140, max=195, src=BJ("speedy-bob")),
 ("bobbejaanland", "Naga Bay"): M(min=140, acc_min=120, acc_max=140, max=195, src=BJ("naga-bay")),
 ("bobbejaanland", "Fury"): M(min=130, src=BJ("fury")),
 ("skyline-park", "Berg- und Tal Hetz"): M(min=130, acc_min=120, acc_max=130, note="The park lists the ride from age 6.", src=SKP("berg-tal-hetz")),
 ("skyline-park", "Flotter Otto"): M(min=120, acc_min=90, acc_max=120, note="The park lists the ride from age 2.", src=SKP("flotter-otto")),
 ("skyline-park", "Kids Spin"): M(min=120, acc_min=105, acc_max=120, note="The park lists the ride from age 4.", src=SKP("kids-spin")),
 ("skyline-park", "Sky Rider"): M(min=140, acc_min=120, acc_max=140, note="The park lists the ride from age 6; riders up to 10 years old must ride with an adult.", src=SKP("sky-rider")),
 ("skyline-park", "Sky Wheel"): M(min=150, max=200, note="The park lists the ride from age 12.", src=SKP("sky-wheel")),
}
HP_INTL.update(HP_B11b)
INTL_PARKS += [
 dict(slug="six-flags-qiddiya-city", name="Six Flags Qiddiya City", short="Six Flags Qiddiya", loc="Qiddiya, Riyadh, Saudi Arabia", state="Riyadh", country="SA", official="https://sixflagsqiddiyacity.com/en", group="Six Flags Qiddiya City"),
 dict(slug="legoland-windsor", name="Legoland Windsor", short="Legoland Windsor", loc="Windsor, England", state="Berkshire", country="GB", official="https://www.legoland.co.uk/", group="Merlin Entertainments"),
 dict(slug="legoland-deutschland", name="Legoland Deutschland", short="Legoland Deutschland", loc="Günzburg, Germany", state="Bavaria", country="DE", official="https://www.legoland.de/", group="Merlin Entertainments"),
 dict(slug="legoland-billund", name="Legoland Billund", short="Legoland Billund", loc="Billund, Denmark", state="Southern Denmark", country="DK", official="https://www.legoland.dk/en/", group="Merlin Entertainments"),
 dict(slug="mirabilandia", name="Mirabilandia", short="Mirabilandia", loc="Ravenna, Italy", state="Emilia-Romagna", country="IT", official="https://www.mirabilandia.it/en", group="Parques Reunidos"),
 dict(slug="tripsdrill", name="Erlebnispark Tripsdrill", short="Tripsdrill", loc="Cleebronn, Germany", state="Baden-Württemberg", country="DE", official="https://tripsdrill.de/en/", group="Tripsdrill"),
 dict(slug="djurs-sommerland", name="Djurs Sommerland", short="Djurs Sommerland", loc="Nimtofte, Denmark", state="Central Denmark", country="DK", official="https://www.djurssommerland.dk/en/", group="Djurs Sommerland"),
 dict(slug="drayton-manor", name="Drayton Manor", short="Drayton Manor", loc="Tamworth, England", state="Staffordshire", country="GB", official="https://www.draytonmanor.co.uk/", group="Drayton Manor"),
 dict(slug="tusenfryd", name="TusenFryd", short="TusenFryd", loc="Vinterbro, Norway", state="Akershus", country="NO", official="https://www.tusenfryd.no/en/", group="Parques Reunidos"),
 dict(slug="bobbejaanland", name="Bobbejaanland", short="Bobbejaanland", loc="Lichtaart, Belgium", state="Antwerp", country="BE", official="https://www.bobbejaanland.be/", group="Parques Reunidos"),
 dict(slug="skyline-park", name="Skyline Park", short="Skyline Park", loc="Bad Wörishofen, Germany", state="Bavaria", country="DE", official="https://www.skylinepark.de/", group="Skyline Park"),
]
DISPLAY_INTL.update({("legoland-windsor", "Dragon"): "The Dragon", ("legoland-billund", "Dragen"): "The Dragon", ("legoland-deutschland", "Das Große LEGO Rennen"): "Das Große LEGO Rennen (The Great LEGO Race)",
 ("legoland-deutschland", "Maximus - Der Flug des Wächters"): "Maximus: Der Flug des Wächters", ("drayton-manor", "Wave"): "The Wave", ("tusenfryd", "Storm - The Dragon Legend"): "Storm: The Dragon Legend",
 ("skyline-park", "Berg- und Tal Hetz"): "Berg & Tal Hetz"})

# ---- Batch 11c (10 Nov 2026): Nickelodeon Universe (Mall of America, American Dream), Bakken, Walibi Rhone-Alpes, Bellewaerde, Adventure Island, Sea World, IMG Worlds, Lightwater Valley ----
NUM = ("Nickelodeon Universe (Mall of America), official FAQ", "https://nickelodeonuniverse.com/faq/")
def NAD(s): return ("Nickelodeon Universe at American Dream, official attraction page", f"https://www.americandream.com/venue/nickelodeon-universe/attraction/{s}")
def BK(s): return ("Bakken, official ride page", f"https://www.bakken.dk/forlystelser/alle-forlystelser/{s}/")
def WRA(s): return ("Walibi Rhône-Alpes, official ride page", f"https://www.walibi.fr/en/explore-the-park/rides/{s}")
def BW(s): return ("Bellewaerde, official attraction page", f"https://www.bellewaerde.be/park/nl/het-park/attracties/{s}")
def AI(s): return ("Adventure Island, official ride page", f"https://adventureisland.co.uk/ride/{s}/")
def SWG(s): return ("Sea World Gold Coast, official attraction page", f"https://seaworld.com.au/attractions/{s}")
IMGR = ("IMG Worlds of Adventure, official rides page", "https://www.imgworlds.com/activities/rides")
LWV = ("Lightwater Valley, official rides page", "https://lightwatervalley.co.uk/rides")
AIN = "Riders 100 to 120 cm must be accompanied by a person aged 14 or over."
HP_B11c = {
 ("nickelodeon-universe-moa", "Pepsi Orange Streak"): dict(min=47, acc_min=42, acc_max=47, note="Riders 42 to 47 inches must ride with a chaperone.", src=NUM),
 ("nickelodeon-universe-moa", "Fairly Odd Coaster"): dict(min=47, acc_min=43, acc_max=47, note="Riders 43 to 47 inches must ride with a chaperone.", src=NUM),
 ("nickelodeon-universe-moa", "SpongeBob SquarePants Rock Bottom Plunge"): dict(min=48, src=NUM),
 ("nickelodeon-universe-moa", "Avatar Airbender"): dict(min=48, src=NUM),
 ("nickelodeon-universe-american-dream", "TMNT Shellraiser"): dict(min=48, src=NAD("tmnt-shellraiser")),
 ("nickelodeon-universe-american-dream", "Shredder"): dict(min=52, acc_min=44, acc_max=52, max=77, note="Riders 44 to 52 inches must ride with a companion.", src=NAD("the-shredder")),
 ("nickelodeon-universe-american-dream", "Sandy’s Blasting Bronco"): dict(min=52, max=77, src=NAD("sandys-blasting-bronco")),
 ("nickelodeon-universe-american-dream", "Nickelodeon Slime Streak"): dict(min=48, acc_min=42, acc_max=48, note="Riders 42 to 48 inches must ride with a companion.", src=NAD("nickelodeon-slime-streak")),
 ("nickelodeon-universe-american-dream", "Timmy's Half-Pipe Havoc"): dict(min=48, max=77, src=NAD("timmys-half-pipe-havoc")),
 ("bakken", "Vilde Mus"): M(min=120, acc_min=107, acc_max=120, note="Riders 107 to 120 cm must ride with an adult; the park also sets a minimum age of 8 to ride without an adult.", src=BK("de-vilde-mus")),
 ("bakken", "Rutschebanen"): M(min=120, acc_min=100, acc_max=120, note="Riders 100 to 120 cm must ride with an adult.", src=BK("rutschebanen")),
 ("bakken", "Tornado"): M(min=120, src=BK("tornado")),
 ("walibi-rhone-alpes", "Generator"): M(min=130, src=WRA("thrills/generator")),
 ("walibi-rhone-alpes", "Coccinelle"): M(min=120, acc_min=90, acc_max=120, note="Riders 90 to 120 cm must be accompanied by an adult.", src=WRA("famille/la-coccinelle")),
 ("walibi-rhone-alpes", "Woodstock Express"): M(min=120, src=WRA("thrills/woodstock-express")),
 ("walibi-rhone-alpes", "Timber"): M(min=120, acc_min=110, acc_max=120, note="Riders 110 to 120 cm must be accompanied by an adult.", src=WRA("thrills/timber")),
 ("walibi-rhone-alpes", "Mystic"): M(min=130, max=195, src=WRA("thrills/mystic")),
 ("walibi-rhone-alpes", "Mahuka"): M(min=120, max=195, src=WRA("thrills/mahuka")),
 ("bellewaerde", "Huracan"): M(min=120, acc_min=100, acc_max=120, note="Riders 100 to 120 cm must be accompanied by an adult.", src=BW("huracan")),
 ("bellewaerde", "Dawson Duel"): M(min=120, acc_min=100, acc_max=120, note="Riders 100 to 120 cm must be accompanied by an adult.", src=BW("dawson-duel")),
 ("bellewaerde", "Wakala"): M(min=120, acc_min=100, acc_max=120, note="Riders 100 to 120 cm must be accompanied by an adult.", src=BW("wakala")),
 ("bellewaerde", "Brazilian Buggies"): M(min=120, acc_min=90, acc_max=120, note="Riders 90 to 120 cm must be accompanied by an adult.", src=BW("brazilian-buggies")),
 ("bellewaerde", "Boomerang"): M(min=130, src=BW("boomerang")),
 ("adventure-island", "Green Scream"): M(min=120, acc_min=100, acc_max=120, note=AIN, src=AI("green-scream")),
 ("adventure-island", "Barnstormer"): M(min=120, acc_min=100, acc_max=120, note=AIN, src=AI("barnstormer")),
 ("adventure-island", "Mighty Mini Mega"): M(min=120, acc_min=100, acc_max=120, note=AIN, src=AI("mighty-mini-mega")),
 ("adventure-island", "Rage"): M(min=120, src=AI("rage")),
 ("sea-world-gold-coast", "Leviathan"): M(min=122, max=200, src=SWG("leviathan")),
 ("sea-world-gold-coast", "Storm Coaster"): M(min=130, acc_min=110, acc_max=130, max=200, note="Riders 110 to 130 cm must be accompanied by a responsible person.", src=SWG("storm-coaster")),
 ("sea-world-gold-coast", "SpongeBob's Boating School Blast"): M(min=105, acc_min=90, acc_max=105, note="Riders 90 to 105 cm must be accompanied by a responsible adult.", src=SWG("spongebobs-boating-school-blast")),
 ("img-worlds", "Velociraptor"): M(min=130, src=IMGR),
 ("img-worlds", "Predator"): M(min=125, src=IMGR),
 ("lightwater-valley", "Spinning Racer"): M(min=120, src=LWV),
 ("lightwater-valley", "Ladybird"): M(min=90, src=LWV),
}
HP_INTL.update(HP_B11c)
INTL_PARKS += [
 dict(slug="nickelodeon-universe-moa", name="Nickelodeon Universe (Mall of America)", short="Nickelodeon Universe MOA", loc="Bloomington, Minnesota", state="MN", country="US", official="https://nickelodeonuniverse.com/", group="Mall of America"),
 dict(slug="nickelodeon-universe-american-dream", name="Nickelodeon Universe at American Dream", short="Nickelodeon Universe NJ", loc="East Rutherford, New Jersey", state="NJ", country="US", official="https://www.americandream.com/venue/nickelodeon-universe", group="American Dream"),
 dict(slug="bakken", name="Bakken (Dyrehavsbakken)", short="Bakken", loc="Klampenborg, Denmark", state="Capital Region", country="DK", official="https://www.bakken.dk/", group="Bakken"),
 dict(slug="walibi-rhone-alpes", name="Walibi Rhône-Alpes", short="Walibi Rhône-Alpes", loc="Les Avenières, France", state="Auvergne-Rhône-Alpes", country="FR", official="https://www.walibi.fr/en", group="Compagnie des Alpes"),
 dict(slug="bellewaerde", name="Bellewaerde Park", short="Bellewaerde", loc="Ypres, Belgium", state="West Flanders", country="BE", official="https://www.bellewaerde.be/", group="Compagnie des Alpes"),
 dict(slug="adventure-island", name="Adventure Island", short="Adventure Island", loc="Southend-on-Sea, England", state="Essex", country="GB", official="https://adventureisland.co.uk/", group="Adventure Island"),
 dict(slug="sea-world-gold-coast", name="Sea World (Gold Coast)", short="Sea World Gold Coast", loc="Main Beach, Gold Coast, Australia", state="Queensland", country="AU", official="https://seaworld.com.au/", group="Village Roadshow Theme Parks"),
 dict(slug="img-worlds", name="IMG Worlds of Adventure", short="IMG Worlds", loc="Dubai, United Arab Emirates", state="Dubai", country="AE", official="https://www.imgworlds.com/", group="IMG Group"),
 dict(slug="lightwater-valley", name="Lightwater Valley", short="Lightwater Valley", loc="North Stainley, Ripon, England", state="North Yorkshire", country="GB", official="https://lightwatervalley.co.uk/", group="Lightwater Valley"),
]
DISPLAY_INTL.update({("nickelodeon-universe-american-dream", "Shredder"): "The Shredder", ("nickelodeon-universe-american-dream", "Sandy’s Blasting Bronco"): "Sandy's Blasting Bronco", ("bakken", "Vilde Mus"): "De Vilde Mus", ("walibi-rhone-alpes", "Coccinelle"): "La Coccinelle"})

# ---- Batch 11d (10 Nov 2026): Fort Fun, Kolmården, Bayern-Park, Beech Bend, Casino Pier, Parc Spirou, Duinrell, Belantis, Terra Mítica ----
def FF(s): return ("Fort Fun Abenteuerland, official attraction page", f"https://fortfun.de/attraktion/{s}")
KOL = ("Kolmården, official attractions page", "https://www.kolmarden.com/attraktioner")
def BYP(s): return ("Bayern-Park, official attraction page", f"https://www.bayern-park.com/de/attraktionen/{s}")
BBH = ("Beech Bend, official height and weight requirements page", "https://beechbend.com/amusement-park/rides-attractions/height-requirements/")
CPR = ("Casino Pier, official boardwalk rides page", "https://casinopiernj.com/boardwalk-rides/")
SPI = ("Parc Spirou, official attractions page", "https://www.parc-spirou.com/les-attractions/")
def DR(s): return ("Duinrell, official attraction page", f"https://www.duinrell.nl/attractiepark/attracties/{s}")
BEL = ("Belantis, official attractions page", "https://www.belantis.de/de/belantis-entdecken/attraktionen")
def TM(s): return ("Terra Mítica, official attraction page", f"https://www.terramiticabenidorm.com/atracciones/{s}/")
HP_B11d = {
 ("fort-fun", "Devil's Mine"): M(min=120, acc_min=100, acc_max=120, note="Riders 100 to 120 cm must ride with an adult.", src=FF("devils-mine")),
 ("fort-fun", "Marienkäferbahn"): M(min=120, acc_min=100, acc_max=120, note="Riders 100 to 120 cm must ride with an adult.", src=FF("marienkaeferbahn")),
 ("fort-fun", "SpeedSnake FREE"): M(min=140, acc_min=130, acc_max=140, note="Riders 130 to 140 cm must ride with an adult.", src=FF("speedsnake-free")),
 ("fort-fun", "Trapper Slider"): M(min=130, acc_min=100, acc_max=130, note="Riders 100 to 130 cm must ride with an adult.", src=FF("trapper-slider")),
 ("kolmarden", "Wildfire"): M(min=120, src=KOL),
 ("kolmarden", "Delfinexpressen"): M(min=120, acc_min=95, acc_max=120, note="The park also sets a minimum age: 8 to ride alone, 4 with an adult.", src=KOL),
 ("kolmarden", "Godiståget"): M(min=120, acc_min=100, acc_max=120, max=195, note="The park also sets a minimum age: 6 to ride alone, 4 with an adult.", src=KOL),
 ("bayern-park", "Freischütz"): M(min=140, max=210, note="The park lists the ride from age 8.", src=BYP("details/freischuetz-1/")),
 ("bayern-park", "FirleFranz"): M(min=90, max=210, note="The park lists the ride from age 3.", src=BYP("details/firlefranz-familienachterbahn/")),
 ("bayern-park", "Froschbahn"): M(min=95, note="The park lists the ride from age 3.", src=BYP("")),
 ("beech-bend", "Kentucky Rumbler"): dict(min=48, src=BBH),
 ("beech-bend", "Wild Mouse"): dict(min=48, acc_min=42, acc_max=48, note="Riders 42 to 48 inches must be accompanied by an adult.", src=BBH),
 ("beech-bend", "Spinning Out"): dict(min=47, acc_min=36, acc_max=47, note="Riders 36 to 47 inches must be accompanied by an adult.", src=BBH),
 ("casino-pier", "Hydrus"): dict(min=48, src=CPR),
 ("casino-pier", "Pirates Hideaway"): dict(min=48, acc_min=38, acc_max=48, note="Riders 38 to 48 inches must be accompanied by a paying adult (18+).", src=CPR),
 ("casino-pier", "Xolo Loca"): dict(min=47, acc_min=36, acc_max=47, note="47 inches is the minimum for the spinning car; the rollover car needs 55 inches (maximum 77). Riders 36 to 47 inches must be accompanied by a paying adult rider (18+).", src=CPR),
 ("parc-spirou", "Kyûbi Unchained"): M(min=130, acc_min=105, acc_max=130, note="Riders 105 to 130 cm must ride accompanied.", src=SPI),
 ("parc-spirou", "Spirou Racing"): M(min=130, acc_min=100, acc_max=130, max=195, note="Riders 100 to 130 cm must ride accompanied.", src=SPI),
 ("parc-spirou", "Wanted Dalton"): M(min=130, acc_min=90, acc_max=130, note="Riders 90 to 130 cm must ride accompanied.", src=SPI),
 ("duinrell", "Falcon"): M(min=120, src=DR("falcon")),
 ("duinrell", "Dragon Fly"): M(min=110, src=DR("dragonfly")),
 ("belantis", "Huracan"): M(min=130, max=195, src=BEL),
 ("belantis", "Drachenritt"): M(min=100, src=BEL),
 ("terra-mitica", "Titánide"): M(min=130, max=195, note="Recommended minimum age: 14.", src=TM("titanide")),
 ("terra-mitica", "Inferno"): M(min=140, max=195, note="Recommended minimum age: 14.", src=TM("inferno")),
 ("terra-mitica", "Alucinakis"): M(min=110, acc_min=92, acc_max=110, note="Riders 92 to 110 cm must ride accompanied; recommended minimum age 5.", src=TM("alucinakis")),
}
HP_INTL.update(HP_B11d)
INTL_PARKS += [
 dict(slug="fort-fun", name="Fort Fun Abenteuerland", short="Fort Fun", loc="Bestwig, Germany", state="North Rhine-Westphalia", country="DE", official="https://fortfun.de/", group="Fort Fun"),
 dict(slug="kolmarden", name="Kolmården Wildlife Park", short="Kolmården", loc="Kolmården, Sweden", state="Östergötland", country="SE", official="https://www.kolmarden.com/", group="Parks and Resorts Scandinavia"),
 dict(slug="bayern-park", name="Bayern-Park", short="Bayern-Park", loc="Reisbach, Germany", state="Bavaria", country="DE", official="https://www.bayern-park.com/de/", group="Bayern-Park"),
 dict(slug="beech-bend", name="Beech Bend Amusement Park", short="Beech Bend", loc="Bowling Green, Kentucky", state="KY", country="US", official="https://beechbend.com/", group="Beech Bend"),
 dict(slug="casino-pier", name="Casino Pier", short="Casino Pier", loc="Seaside Heights, New Jersey", state="NJ", country="US", official="https://casinopiernj.com/", group="Casino Pier"),
 dict(slug="parc-spirou", name="Parc Spirou Provence", short="Parc Spirou", loc="Monteux, France", state="Provence-Alpes-Côte d'Azur", country="FR", official="https://www.parc-spirou.com/", group="Parc Spirou"),
 dict(slug="duinrell", name="Duinrell", short="Duinrell", loc="Wassenaar, Netherlands", state="South Holland", country="NL", official="https://www.duinrell.nl/", group="Duinrell"),
 dict(slug="belantis", name="Belantis", short="Belantis", loc="Leipzig, Germany", state="Saxony", country="DE", official="https://www.belantis.de/", group="Parques Reunidos"),
 dict(slug="terra-mitica", name="Terra Mítica", short="Terra Mítica", loc="Benidorm, Spain", state="Valencian Community", country="ES", official="https://www.terramiticabenidorm.com/", group="Terra Mítica"),
]
DISPLAY_INTL.update({("bayern-park", "Achterbahn"): "Raupenachterbahn", ("duinrell", "Dragon Fly"): "Dragonfly", ("casino-pier", "Pirates Hideaway"): "Pirate's Hideaway"})

# ---- Batch 11e (10 Nov 2026): Nagashima Spa Land, Yomiuriland, Hirakata Park ----
NSL = ("Nagashima Spa Land, official attraction restrictions page", "https://www.nagashima-onsen.co.jp/spaland/attraction/limit.html")
def YL(s): return ("Yomiuriland, official attraction page", f"https://www.yomiuriland.com/attraction/{s}/")
def HKP(s): return ("Hirakata Park, official attraction page", f"https://www.hirakatapark.co.jp/attractions/{s}/")
HP_B11e = {
 ("nagashima-spa-land", "Steel Dragon 2000"): M(min=140, max=185, note="Minimum age 10.", src=NSL),
 ("nagashima-spa-land", "Hakugei"): M(min=130, src=NSL),
 ("nagashima-spa-land", "Arashi"): M(min=120, src=NSL),
 ("nagashima-spa-land", "Acrobat"): M(min=135, max=198, src=NSL),
 ("nagashima-spa-land", "Looping Star"): M(min=130, src=NSL),
 ("nagashima-spa-land", "Shuttle Loop"): M(min=120, src=NSL),
 ("nagashima-spa-land", "Wild Mouse"): M(min=120, note="Minimum age 9.", src=NSL),
 ("nagashima-spa-land", "Corkscrew"): M(min=110, src=NSL),
 ("yomiuriland", "Bandit"): M(min=120, note="The park also requires riders to be elementary-school age or older.", src=YL("bandit")),
 ("yomiuriland", "Lipovitan Rocket☆Luna"): M(min=130, acc_min=110, acc_max=130, note="Riders 110 to 130 cm must ride with a companion of junior-high age or older.", src=YL("lipovitan")),
 ("yomiuriland", "Spin Runway"): M(min=130, acc_min=110, acc_max=130, note="Riders 110 to 130 cm need a companion of junior-high age or older. Minimum age 4; under 6 must ride with a companion.", src=YL("spinrunway")),
 ("yomiuriland", "Wan Wan Coaster Wandit"): M(min=90, note="Minimum age 3; under 5 must ride with a companion of junior-high age or older.", src=YL("wandit")),
 ("yomiuriland", "DinoRunner"): M(min=110, acc_min=90, acc_max=110, note="These limits are for the dinosaur cars: riders 90 to 110 cm need a companion of junior-high age or older. The park lists no height limit for the trolley cars. Minimum age 2.", src=YL("dinorunner")),
 ("hirakata-park", "Crazy Mouse"): M(min=130, acc_min=110, acc_max=130, note="Riding alone needs both 130 cm and age 10. Riders 110 to 130 cm, or under 10, must ride with a companion aged 15 or older.", src=HKP("crazy-mouse")),
 ("hirakata-park", "Elf"): M(min=110, src=HKP("elf")),
 ("hirakata-park", "Red Falcon"): M(min=120, src=HKP("red-falcon")),
}
HP_INTL.update(HP_B11e)
INTL_PARKS += [
 dict(slug="nagashima-spa-land", name="Nagashima Spa Land", short="Nagashima Spa Land", loc="Kuwana, Mie, Japan", state="Mie", country="JP", official="https://www.nagashima-onsen.co.jp/spaland/", group="Nagashima Resort"),
 dict(slug="yomiuriland", name="Yomiuriland", short="Yomiuriland", loc="Inagi, Tokyo, Japan", state="Tokyo", country="JP", official="https://www.yomiuriland.com/", group="Yomiuriland"),
 dict(slug="hirakata-park", name="Hirakata Park", short="Hirakata Park", loc="Hirakata, Osaka, Japan", state="Osaka", country="JP", official="https://www.hirakatapark.co.jp/", group="Keihan"),
]
DISPLAY_INTL.update({("nagashima-spa-land", "Wild Mouse"): "Double Wild Mouse", ("yomiuriland", "Lipovitan Rocket☆Luna"): "Lipovitan Rocket Luna"})

# ---- Batch 11f (10 Nov 2026): Plopsaland De Panne, Plopsaland Deutschland ----
def PLB(s): return ("Plopsaland De Panne, official attraction page", f"https://www.plopsa.com/nl/plopsaland-belgium/attracties/{s}")
def PLD(s): return ("Plopsaland Deutschland, official attraction page", f"https://www.plopsa.com/de/plopsaland-deutschland/attraktionen/{s}")
def _acc(a, m): return f"Riders {a} to {m} cm must ride accompanied."
HP_B11f = {
 ("plopsaland-de-panne", "Ride to Happiness"): M(min=130, src=PLB("the-ride-to-happiness-by-tomorrowland")),
 ("plopsaland-de-panne", "Anubis: The Ride"): M(min=140, acc_min=125, acc_max=140, note=_acc(125, 140), src=PLB("anubis-the-ride")),
 ("plopsaland-de-panne", "Heidi The Ride"): M(min=140, acc_min=120, acc_max=140, note=_acc(120, 140), src=PLB("heidi-the-ride")),
 ("plopsaland-de-panne", "Draconis"): M(min=120, acc_min=96, acc_max=120, note=_acc(96, 120), src=PLB("draconis")),
 ("plopsaland-de-panne", "K3 Roller Skater"): M(min=120, acc_min=90, acc_max=120, note=_acc(90, 120), src=PLB("k3-roller-skater")),
 ("plopsaland-de-panne", "#LikeMe Coaster"): M(min=120, acc_min=90, acc_max=120, note=_acc(90, 120), src=PLB("likeme-coaster")),
 ("plopsaland-deutschland", "Expedition GeForce"): M(min=140, src=PLD("bigfm-expedition-geforce")),
 ("plopsaland-deutschland", "Sky Scream"): M(min=140, src=PLD("sky-scream")),
 ("plopsaland-deutschland", "100% Wolf"): M(min=130, acc_min=100, acc_max=130, note=_acc(100, 130), src=PLD("100-wolf-die-familienachterbahn")),
 ("plopsaland-deutschland", "Tabalugas Achterbahn"): M(min=120, acc_min=100, acc_max=120, note=_acc(100, 120), src=PLD("tabalugas-achterbahn")),
}
HP_INTL.update(HP_B11f)
INTL_PARKS += [
 dict(slug="plopsaland-de-panne", name="Plopsaland De Panne", short="Plopsaland De Panne", loc="Adinkerke-De Panne, Belgium", state="West Flanders", country="BE", official="https://www.plopsa.com/nl/plopsaland-belgium", group="Plopsa"),
 dict(slug="plopsaland-deutschland", name="Plopsaland Deutschland", short="Plopsaland Deutschland", loc="Haßloch, Germany", state="Rhineland-Palatinate", country="DE", official="https://www.plopsa.com/de/plopsaland-deutschland", group="Plopsa", former="Holiday Park", former_note="RCDB lists Holiday Park as a former name, and holidaypark.de redirects to the Plopsaland Deutschland page on plopsa.com"),
]
DISPLAY_INTL.update({("plopsaland-de-panne", "Ride to Happiness"): "The Ride to Happiness", ("plopsaland-deutschland", "Tabalugas Achterbahn"): "Tabaluga's Achterbahn"})

# ---- Batch 11g (10 Nov 2026): Avonturenpark Hellendoorn, Fraispertuis-City ----
def AVH(s): return ("Avonturenpark Hellendoorn, official attraction page", f"https://www.avonturenpark.nl/attraction-detail/{s}")
FRS = ("Fraispertuis-City, official attractions page", "https://www.fraispertuis-city.fr/le-parc/attractions/le-plein-de-sensations/")
FRF = ("Fraispertuis-City, official attractions page", "https://www.fraispertuis-city.fr/le-parc/attractions/pour-la-famille/")
HP_B11g = {
 ("hellendoorn", "Balagos"): M(min=120, src=AVH("balagos")),
 ("hellendoorn", "Rioolrat"): M(min=100, src=AVH("rioolrat")),
 ("hellendoorn", "Donderstenen"): M(min=120, acc_min=90, acc_max=120, note="Riders 90 to 120 cm must ride with an adult.", src=AVH("donderstenen")),
 ("hellendoorn", "RidderStrijd"): M(min=140, acc_min=120, acc_max=140, note="Riders 120 to 140 cm must ride with an adult.", src=AVH("ridderstrijd")),
 ("fraispertuis-city", "Timber Drop"): M(min=122, src=FRS),
 ("fraispertuis-city", "Grand Canyon"): M(min=95, src=FRS),
 ("fraispertuis-city", "Fireline Redwood"): M(min=95, src=FRF),
}
HP_INTL.update(HP_B11g)
INTL_PARKS += [
 dict(slug="hellendoorn", name="Avonturenpark Hellendoorn", short="Hellendoorn", loc="Hellendoorn, Netherlands", state="Overijssel", country="NL", official="https://www.avonturenpark.nl/", group="Avonturenpark Hellendoorn"),
 dict(slug="fraispertuis-city", name="Fraispertuis-City", short="Fraispertuis-City", loc="Jeanménil, France", state="Grand Est", country="FR", official="https://www.fraispertuis-city.fr/", group="Fraispertuis-City"),
]
DISPLAY_INTL.update({("fraispertuis-city", "Grand Canyon"): "Le Grand Canyon"})

# ---- Batch 11h (10 Nov 2026): Parque de Atracciones de Madrid ----
def PAM(s): return ("Parque de Atracciones de Madrid, official attraction page", f"https://www.parquedeatracciones.es/experiencias/atracciones/{s}")
HP_B11h = {
 ("parque-de-atracciones-madrid", "Abismo"): M(min=135, max=200, src=PAM("abismo")),
 ("parque-de-atracciones-madrid", "Tornado"): M(min=120, max=193, src=PAM("tornado")),
 ("parque-de-atracciones-madrid", "Tarántula"): M(min=120, max=195, src=PAM("tarantula")),
 ("parque-de-atracciones-madrid", "TNT Tren de la Mina"): M(min=120, acc_min=100, acc_max=120, max=195, note="Riders 100 to 120 cm must ride with an adult.", src=PAM("tnt-tren-de-la-mina")),
 ("parque-de-atracciones-madrid", "Paw Patrol: Patrulla Canina"): M(min=120, acc_min=90, acc_max=120, note="Riders 90 to 120 cm must ride with an adult.", src=PAM("patrulla-canina")),
 ("parque-de-atracciones-madrid", "Padrinos Voladores"): M(min=120, acc_min=90, acc_max=120, note="Riders 90 to 120 cm must ride with an adult.", src=PAM("padrinos-voladores")),
}
HP_INTL.update(HP_B11h)
INTL_PARKS += [
 dict(slug="parque-de-atracciones-madrid", name="Parque de Atracciones de Madrid", short="Parque de Atracciones", loc="Madrid, Spain", state="Community of Madrid", country="ES", official="https://www.parquedeatracciones.es/", group="Parques Reunidos"),
]
DISPLAY_INTL.update({("parque-de-atracciones-madrid", "Paw Patrol: Patrulla Canina"): "Patrulla Canina (PAW Patrol)"})

# ---- Batch 12a (11 Nov 2026): parks scraped earlier, official heights now read ----
MTO = ("Mt. Olympus Water & Theme Park, Outdoor Theme Park ride list", "https://www.mtolympuspark.com/parks/outdoor-theme-park/")
GWR = ("Gulliver's World Resort, official rides page", "https://www.gulliversworldresort.co.uk/explore/rides/")
def FUR(s): return ("Furuvik, official ride page", f"https://www.furuvik.se/{s}")
def BCW(s): return ("Beto Carrero World, official attraction page", f"https://www.betocarrero.com.br/atracoes/{s}")
HHR = ("Hopi Hari, official thrill attractions page", "https://www.hopihari.com.br/atracoesRadical")
HHA = ("Hopi Hari, official attractions page", "https://www.hopihari.com.br/atracoes")
LEO = ("Leolandia, official rides and attractions page (ride detail panels)", "https://www.leolandia.it/giostre-e-attrazioni-per-bambini-e-ragazzi.html")
def NIG(s): return ("Nigloland, official attraction page", f"https://www.nigloland.fr/attractions-et-spectacles/{s}")
def WGE(s): return ("Walygator Grand Est, official attraction page", f"https://www.walygatorparc.com/grandest/attractions/{s}/")
def HAN(s): return ("Hansa-Park, official attraction page (size and age limits)", f"https://www.hansapark.de/attraktion/{s}/?language=de")
def _adult(a, m): return f"Riders {a} to {m} cm must ride with an adult."
HP_B12a = {
 ("mt-olympus", "Hades 360"): dict(min=48, src=MTO),
 ("mt-olympus", "Cyclops"): dict(min=48, src=MTO),
 ("mt-olympus", "Zeus"): dict(min=48, src=MTO),
 ("mt-olympus", "Pegasus"): dict(min=42, src=MTO),
 ("mt-olympus", "Little Titans"): dict(min=40, max=56, note="Kids' coaster: minimum 40 inches, maximum 56 inches, no adults.", src=MTO),
 ("gullivers-warrington", "Antelope"): M(min=140, acc_min=110, acc_max=140, note=_adult(110, 140), src=GWR),
 ("gullivers-warrington", "Grand Prix Racers"): M(min=120, acc_min=100, acc_max=120, max=195, note="At Gulliver's World it sits in the Gulliver's Gears area; riders 100 to 120 cm must ride with an adult, and riders over 195 cm cannot ride.", src=GWR),
 ("gullivers-warrington", "Wriggler"): M(min=120, acc_min=90, acc_max=120, max=195, note=_adult(90, 120), src=GWR),
 ("furuvik", "Fireball"): M(min=120, acc_min=100, acc_max=120, max=205, note="Riders 100 to 120 cm (and at least 4 years old) must ride with an adult; riding alone needs 120 cm and age 8.", src=FUR("fireball")),
 ("furuvik", "Draken"): M(min=120, acc_min=100, acc_max=120, note="Riders 100 to 120 cm (and at least 4 years old) must ride with an adult.", src=FUR("tivoli/draken")),
 ("furuvik", "Lightning"): M(min=120, acc_min=100, acc_max=120, note="Riders 100 to 120 cm (and at least 4 years old) must ride with an adult; riding alone needs 120 cm and age 6.", src=FUR("tivoli/lightning")),
 ("beto-carrero", "Firewhip"): M(min=130, src=BCW("firewhip")),
 ("beto-carrero", "Tigor Mountain"): M(min=95, src=BCW("tigor-mountain")),
 ("beto-carrero", "Jacaré Dum-Dum"): M(min=80, src=BCW("dum-dum")),
 ("hopi-hari", "Montezum"): M(min=140, src=HHR),
 ("hopi-hari", "Vurang"): M(min=140, src=HHR),
 ("hopi-hari", "Katapul"): M(min=140, src=HHR),
 ("hopi-hari", "Speedi '64"): M(min=120, acc_min=100, acc_max=120, note="Children 100 to 120 cm must ride with a responsible adult.", src=HHA),
 ("leolandia", "Reversum"): M(min=130, acc_min=105, acc_max=130, note=_adult(105, 130), src=LEO),
 ("leolandia", "Twister Mountain"): M(min=120, acc_min=105, acc_max=120, note=_adult(105, 120), src=LEO),
 ("leolandia", "Vroom"): M(min=120, acc_min=90, acc_max=120, note=_adult(90, 120), src=LEO),
 ("leolandia", "Mine Train"): M(min=105, acc_min=90, acc_max=105, note=_adult(90, 105), src=LEO),
 ("nigloland", "Alpina Blitz"): M(min=130, src=NIG("sensations-fortes/alpina-blitz")),
 ("nigloland", "Krampus Expédition"): M(min=110, src=NIG("sensations-fortes/krampus-expedition")),
 ("nigloland", "Spatiale Expérience"): M(min=140, acc_min=120, acc_max=140, note="Riders under 140 cm must be accompanied (minimum 120 cm).", src=NIG("sensations-fortes/spatiale-experience")),
 ("nigloland", "Gold Mine Train"): M(min=120, acc_min=100, acc_max=120, note="Riders under 120 cm must be accompanied (minimum 100 cm).", src=NIG("sensations-fortes/le-train-de-la-mine")),
 ("nigloland", "Descente en Schlitt'"): M(min=120, acc_min=100, acc_max=120, note="Riders under 120 cm must be accompanied (minimum 100 cm).", src=NIG("sensations-fortes/le-schlitt-express")),
 ("nigloland", "Noisette Express"): M(min=120, acc_min=90, acc_max=120, note="Riders under 120 cm must be accompanied (minimum 90 cm).", src=NIG("pour-la-famille/noisette-express")),
 ("walygator-grand-est", "Anaconda"): M(min=120, src=WGE("anaconda")),
 ("walygator-grand-est", "Monster"): M(min=140, src=WGE("the-monster")),
 ("walygator-grand-est", "Comet"): M(min=120, max=190, src=WGE("comet")),
 ("walygator-grand-est", "Family Coaster"): M(min=120, acc_min=80, acc_max=120, note="Riders 80 to 120 cm must be accompanied.", src=WGE("family-coaster")),
 ("hansa-park", "Schwur des Kärnan"): M(min=130, src=HAN("13/details/der-schwur-des-kaernan")),
 ("hansa-park", "Flucht von Novgorod"): M(min=125, src=HAN("28/details/flucht-von-novgorod")),
 ("hansa-park", "Kleine Zar"): M(min=120, acc_min=90, acc_max=120, note="Riders 90 to 120 cm may only ride in the child seat next to an accompanying adult.", src=HAN("12/details/der-kleine-zar")),
 ("hansa-park", "Schlange von Midgard"): M(min=90, note="Children aged 5 and under must ride next to an adult.", src=HAN("15/details/die-schlange-von-midgard")),
 ("hansa-park", "Cornwall Coaster"): M(min=90, note="Children aged 7 and under must ride next to an adult.", src=HAN("274/details/cornwall-coaster")),
}
HP_INTL.update(HP_B12a)
INTL_PARKS += [
 dict(slug="mt-olympus", name="Mt. Olympus Water & Theme Park", short="Mt. Olympus", loc="Wisconsin Dells, Wisconsin", state="WI", country="US", official="https://www.mtolympuspark.com/", group="Mt. Olympus", checked="11 Nov 2026"),
 dict(slug="gullivers-warrington", name="Gulliver's World Warrington", short="Gulliver's World", loc="Warrington, England", state="Cheshire", country="GB", official="https://www.gulliversworldresort.co.uk/", group="Gulliver's", checked="11 Nov 2026"),
 dict(slug="furuvik", name="Furuvik", short="Furuvik", loc="Furuvik, Sweden", state="Gävleborg", country="SE", official="https://www.furuvik.se/", group="Parks and Resorts Scandinavia", checked="11 Nov 2026"),
 dict(slug="beto-carrero", name="Beto Carrero World", short="Beto Carrero", loc="Penha, Santa Catarina, Brazil", state="Santa Catarina", country="BR", official="https://www.betocarrero.com.br/", group="Beto Carrero World", checked="11 Nov 2026"),
 dict(slug="hopi-hari", name="Hopi Hari", short="Hopi Hari", loc="Vinhedo, São Paulo, Brazil", state="São Paulo", country="BR", official="https://www.hopihari.com.br/", group="Hopi Hari", checked="11 Nov 2026"),
 dict(slug="leolandia", name="Leolandia", short="Leolandia", loc="Capriate San Gervasio, Italy", state="Lombardy", country="IT", official="https://www.leolandia.it/", group="Leolandia", checked="11 Nov 2026"),
 dict(slug="nigloland", name="Nigloland", short="Nigloland", loc="Dolancourt, France", state="Grand Est", country="FR", official="https://www.nigloland.fr/", group="Nigloland", checked="11 Nov 2026"),
 dict(slug="walygator-grand-est", name="Walygator Grand Est", short="Walygator", loc="Maizières-lès-Metz, France", state="Grand Est", country="FR", official="https://www.walygatorparc.com/grandest/", group="Walygator", checked="11 Nov 2026"),
 dict(slug="hansa-park", name="Hansa-Park", short="Hansa-Park", loc="Sierksdorf, Germany", state="Schleswig-Holstein", country="DE", official="https://www.hansapark.de/", group="Hansa-Park", checked="11 Nov 2026"),
]
DISPLAY_INTL.update({("gullivers-warrington", "Antelope"): "The Antelope", ("gullivers-warrington", "Wriggler"): "The Wriggler", ("walygator-grand-est", "Monster"): "The Monster",
 ("hansa-park", "Schwur des Kärnan"): "Der Schwur des Kärnan", ("hansa-park", "Kleine Zar"): "Der kleine Zar", ("hansa-park", "Schlange von Midgard"): "Die Schlange von Midgard",
 ("beto-carrero", "Firewhip"): "FireWhip"})

# ---- Batch 12b (11 Nov 2026): Fårup, PowerPark, MagicLand, Geiselwind, UK seaside parks, Fantasilandia, Chimelong, Gyeongju World ----
FAR = ("Fårup Sommerland, official height and age guide", "https://www.faarupsommerland.dk/planlaeg/praktisk-information/hoejde-og-alderskrav/")
PPK = ("PowerPark, official safety limits table (Turvarajat)", "https://www.powerpark.fi/huvilaitteet/turvarajat/")
def MGL(s): return ("MagicLand, official attraction page", f"https://magicland.it/it/attrazioni/{s}")
def FLG(s): return ("Freizeit-Land Geiselwind, official attraction page", f"https://freizeit-land.de/{s}/")
def PWH(s): return ("Pleasurewood Hills, official ride page", f"https://pleasurewoodhills.com/ride/{s}/")
GLR = ("Gulliver's Land Resort, official rides page", "https://www.gulliverslandresort.co.uk/explore/rides/")
def FIS(s): return ("Fantasy Island, official ride page", f"https://www.fantasyislandresort.co.uk/rides-and-attractions/{s}/")
def FTL(s): return ("Fantasilandia, official attraction page", f"https://www.fantasilandia.cl/explora-el-parque/atracciones/{s}.html")
def CLO(i): return ("Chimelong Ocean Kingdom, official attraction page (safety rules)", f"https://www.chimelong.com/zh/oceankingdom/exhibition/{i}.html")
def CLP(i): return ("Chimelong Paradise, official attraction page (height limits)", f"https://www.chimelong.com/gz/chimelongparadise/exhibition/{i}.html")
def GJW(n): return ("Gyeongju World, official attraction page", f"https://www.gjw.co.kr/Contents/eng_contents.php?cmsNo=ENGN100%2Fview%2F{n}")
HP_B12b = {
 ("farup-sommerland", "Fønix"): M(min=140, acc_min=120, acc_max=140, note=_adult(120, 140), src=FAR),
 ("farup-sommerland", "Lynet"): M(min=120, src=FAR),
 ("farup-sommerland", "Falken"): M(min=130, acc_min=110, acc_max=130, note=_adult(110, 130), src=FAR),
 ("farup-sommerland", "Flagermusen"): M(min=150, acc_min=115, acc_max=150, note=_adult(115, 150), src=FAR),
 ("farup-sommerland", "Saven"): M(min=120, acc_min=95, acc_max=120, note=_adult(95, 120), src=FAR),
 ("farup-sommerland", "Orkanen"): M(min=105, max=205, src=FAR),
 ("farup-sommerland", "Mine Expressen"): M(min=105, acc_min=90, acc_max=105, note=_adult(90, 105), src=FAR),
 ("farup-sommerland", "Pindsvinet"): M(min=105, acc_min=90, acc_max=105, note=_adult(90, 105), src=FAR),
 ("powerpark", "Thunderbird"): M(min=130, src=PPK),
 ("powerpark", "Cobra"): M(min=130, max=195, src=PPK),
 ("powerpark", "Junker"): M(min=130, max=195, note="Riders aged 8 to 10 (over 130 cm) must ride with a guardian.", src=PPK),
 ("powerpark", "Pitts Special"): M(min=130, max=195, note="Riders aged 8 to 10 (over 130 cm) must ride with a guardian.", src=PPK),
 ("powerpark", "Neo's Twister"): M(min=130, acc_min=120, acc_max=130, note="Riders 120 to 130 cm must ride with a guardian (15 or older).", src=PPK),
 ("powerpark", "Joyride"): M(min=120, src=PPK),
 ("powerpark", "Mine Train"): M(min=110, note="The park lists 110 cm as the safety limit and says riders under 110 cm may ride only with a guardian (15 or older); no lower limit is stated.", src=PPK),
 ("magicland", "Shock"): M(min=130, max=200, note="Minimum age 8.", src=MGL("shock")),
 ("magicland", "Cagliostro"): M(min=120, max=195, src=MGL("cagliostro")),
 ("magicland", "Olandese Volante"): M(min=130, acc_min=110, acc_max=130, note="Riders under 130 cm must be accompanied (minimum 110 cm, minimum age 4).", src=MGL("olandese-volante")),
 ("magicland", "Dune"): M(min=122, acc_min=95, acc_max=122, max=200, note="Riders under 122 cm must be accompanied (minimum 95 cm, minimum age 4).", src=MGL("dune")),
 ("magicland", "Esplorabruco"): M(min=120, acc_min=95, acc_max=120, note="Riders under 120 cm must be accompanied (minimum 95 cm).", src=MGL("esplorabruco")),
 ("freizeit-land-geiselwind", "Fluch des Kraken"): M(min=130, max=190, note="Minimum age 10.", src=FLG("fluch-des-kraken")),
 ("freizeit-land-geiselwind", "Cobra"): M(min=130, max=195, note="Children under 12 must ride with a companion.", src=FLG("cobra-coaster")),
 ("freizeit-land-geiselwind", "Wilde Hilde"): M(min=130, acc_min=120, acc_max=130, note="Riders 120 to 130 cm must ride with a companion; minimum age 6.", src=FLG("wildehilde")),
 ("freizeit-land-geiselwind", "Taka Waka"): M(min=120, note="Ages 6 and 7 ride with a companion; from age 8 alone.", src=FLG("taka-waka")),
 ("freizeit-land-geiselwind", "Drachen Höhle"): M(min=120, note="Children aged 6 to 12 ride with a companion.", src=FLG("drachenhoehle")),
 ("freizeit-land-geiselwind", "Doggy Dog"): M(min=105, note="Children aged 3 to 6 ride with a companion.", src=FLG("doggy-dog")),
 ("pleasurewood-hills", "Wipeout"): M(min=130, src=PWH("wipeout")),
 ("pleasurewood-hills", "Marble Madness"): M(min=125, src=PWH("marble-madness-roller-coaster")),
 ("pleasurewood-hills", "Egg-Spress"): M(min=125, acc_min=90, acc_max=125, note="Guests between 0.9 m and 1.25 m must be accompanied by an adult.", src=PWH("egg-spress-roller-coaster")),
 ("gullivers-land", "Runaway Train"): M(min=120, acc_min=90, acc_max=120, note=_adult(90, 120), src=GLR),
 ("gullivers-land", "Grand Prix Racers"): M(min=120, acc_min=100, acc_max=120, note="At Gulliver's Land it sits in the Adventure Land area, where the park pitches it as a race to the finish to nail the perfect lap. Riders 100 to 120 cm must ride with an adult, under 100 cm cannot ride, and no maximum height is listed there.", src=GLR),
 ("gullivers-land", "Wriggler"): M(min=120, acc_min=90, acc_max=120, max=195, note=_adult(90, 120), src=GLR),
 ("fantasy-island", "Millennium"): M(min=140, acc_min=120, acc_max=140, note="Riders under 1.4 m must be accompanied by an adult (minimum 1.2 m).", src=FIS("millennium")),
 ("fantasy-island", "Odyssey"): M(min=140, acc_min=130, acc_max=140, note="Riders under 1.4 m must be accompanied by an adult (minimum 1.3 m).", src=FIS("odyssey")),
 ("fantasy-island", "Rhombus Express"): M(min=120, acc_min=100, acc_max=120, note="Riders under 1.2 m must be accompanied by an adult (minimum 1.0 m).", src=FIS("the-rhombus-express")),
 ("fantasy-island", "Jellikins Coaster"): M(min=100, max=160, src=FIS("jellikins")),
 ("fantasilandia", "Raptor"): M(min=140, src=FTL("adrenalina/raptor")),
 ("fantasilandia", "Boomerang"): M(min=120, src=FTL("adrenalina/boomerang")),
 ("fantasilandia", "Wild Mouse"): M(min=120, src=FTL("familiares/wild-mouse")),
 ("fantasilandia", "Tren Minero"): M(min=140, acc_min=90, acc_max=140, note="Riders 0.90 to 1.40 m must ride with an adult.", src=FTL("adrenalina/tren-minero")),
 ("fantasilandia", "Car City"): M(min=120, acc_min=90, acc_max=120, max=195, note="Riders 0.90 to 1.20 m must ride with an adult.", src=FTL("familiares/car-city")),
 ("fantasilandia", "Montaña Dragón"): M(min=90, src=FTL("zona-kids/monta%C3%B1a-dragon")),
 ("chimelong-ocean-kingdom", "Parrot Coaster"): M(min=132, max=195, src=CLO(2330)),
 ("chimelong-ocean-kingdom", "Polar Explorer"): M(min=150, acc_min=120, acc_max=150, note="Children 1.2 m to 1.5 m (inclusive) must ride with an adult.", src=CLO(2336)),
 ("chimelong-ocean-kingdom", "Walrus Splash"): M(min=132, acc_min=120, acc_max=132, note="Children 1.2 m to 1.32 m (inclusive) must ride with a guardian.", src=CLO(2325)),
 ("chimelong-ocean-kingdom", "Jungle Coaster"): M(min=120, acc_min=100, acc_max=120, note="Children 1 m to 1.2 m (inclusive) must ride with an adult; not for children under 4.", src=CLO(2328)),
 ("chimelong-ocean-kingdom", "Penguin Coaster"): M(min=120, acc_min=100, acc_max=120, note="Children 1 m to 1.2 m (inclusive) must ride with an adult; not for children under 4.", src=CLO(2312)),
 ("chimelong-paradise", "Circus Roller Coaster"): M(min=140, max=195, note="Children under 12 must ride with a parent.", src=CLP(7897)),
 ("chimelong-paradise", "Sky Rocket"): M(min=140, max=195, src=CLP(2358)),
 ("chimelong-paradise", "Launch Coaster"): M(min=130, max=195, note="Children under 10 must ride with a parent.", src=CLP(7607)),
 ("chimelong-paradise", "Young Star Coaster"): M(min=130, acc_min=100, acc_max=130, note="Children 1 m to 1.3 m must ride with a parent.", src=CLP(2356)),
 ("gyeongju-world", "Phaethon"): M(min=145, src=GJW(8)),
 ("gyeongju-world", "Draken"): M(min=135, src=GJW(14)),
 ("gyeongju-world", "Sköll & Hati"): M(min=125, src=GJW(56)),
 ("gyeongju-world", "Valkyrie"): M(min=120, src=GJW(50)),
 ("gyeongju-world", "Wizard Race"): M(min=105, src=GJW(54)),
}
HP_INTL.update(HP_B12b)
_C = "11 Nov 2026"
INTL_PARKS += [
 dict(slug="farup-sommerland", name="Fårup Sommerland", short="Fårup", loc="Blokhus, Denmark", state="North Jutland", country="DK", official="https://www.faarupsommerland.dk/", group="Parks and Resorts Scandinavia", checked=_C),
 dict(slug="powerpark", name="PowerPark", short="PowerPark", loc="Härmä, Kauhava, Finland", state="South Ostrobothnia", country="FI", official="https://www.powerpark.fi/", group="PowerPark", checked=_C),
 dict(slug="magicland", name="MagicLand", short="MagicLand", loc="Valmontone, Italy", state="Lazio", country="IT", official="https://magicland.it/", group="MagicLand", checked=_C),
 dict(slug="freizeit-land-geiselwind", name="Freizeit-Land Geiselwind", short="Geiselwind", loc="Geiselwind, Germany", state="Bavaria", country="DE", official="https://freizeit-land.de/", group="Freizeit-Land Geiselwind", checked=_C),
 dict(slug="pleasurewood-hills", name="Pleasurewood Hills", short="Pleasurewood Hills", loc="Lowestoft, England", state="Suffolk", country="GB", official="https://pleasurewoodhills.com/", group="Pleasurewood Hills", checked=_C),
 dict(slug="gullivers-land", name="Gulliver's Land", short="Gulliver's Land", loc="Milton Keynes, England", state="Buckinghamshire", country="GB", official="https://www.gulliverslandresort.co.uk/", group="Gulliver's", checked=_C),
 dict(slug="fantasy-island", name="Fantasy Island", short="Fantasy Island", loc="Ingoldmells, England", state="Lincolnshire", country="GB", official="https://www.fantasyislandresort.co.uk/", group="Fantasy Island", checked=_C),
 dict(slug="fantasilandia", name="Fantasilandia", short="Fantasilandia", loc="Santiago, Chile", state="Santiago Metropolitan Region", country="CL", official="https://www.fantasilandia.cl/", group="Fantasilandia", checked=_C),
 dict(slug="chimelong-ocean-kingdom", name="Chimelong Ocean Kingdom", short="Ocean Kingdom", loc="Hengqin, Zhuhai, China", state="Guangdong", country="CN", official="https://www.chimelong.com/zh/oceankingdom/", group="Chimelong", checked=_C),
 dict(slug="chimelong-paradise", name="Chimelong Paradise", short="Chimelong Paradise", loc="Panyu, Guangzhou, China", state="Guangdong", country="CN", official="https://www.chimelong.com/gz/chimelongparadise/", group="Chimelong", checked=_C),
 dict(slug="gyeongju-world", name="Gyeongju World", short="Gyeongju World", loc="Gyeongju, South Korea", state="North Gyeongsang", country="KR", official="https://www.gjw.co.kr/", group="Gyeongju World", checked=_C),
]
DISPLAY_INTL.update({("farup-sommerland", "Mine Expressen"): "Mine-Expressen", ("fantasy-island", "Rhombus Express"): "The Rhombus Express",
 ("freizeit-land-geiselwind", "Drachen Höhle"): "Drachenhöhle"})

# ---- Batch 12c (11 Nov 2026): Emerald Park, Potts Park, BonBon-Land, Tivoli Friheden, Drievliet, US family parks, Rusutsu, Parque España ----
def EMP(s): return ("Emerald Park, official attraction page", f"https://www.emeraldpark.ie/attraction/{s}/")
POT = ("Potts Park, official access restrictions (Zugangsbeschränkungen, PDF)", "https://www.pottspark-minden.de/wp-content/uploads/2025/09/Zugangsbeschraenkungen-2025.pdf")
BBL = ("BonBon-Land, official height requirements (Højdekrav, PDF)", "https://www.bonbonland.dk/content/dam/bbl/files/Hoejdekrav.pdf")
def TFR(s): return ("Tivoli Friheden, official ride page", f"https://www.friheden.dk/oplev-friheden/forlystelser/{s}")
def DRV(s): return ("Drievliet, official attraction page", f"https://www.drievliet.nl/attraction-detail/{s}")
def GWC(s): return ("Glenwood Caverns Adventure Park, official ride page", f"https://www.glenwoodcaverns.com/thrill-rides/{s}/")
def PCC(s): return ("Playland's Castaway Cove, official ride page", f"https://oceancityfun.com/Rides/{s}/")
def DWW(s): return ("Deno's Wonder Wheel Amusement Park, official rides page", f"https://www.denoswonderwheel.com/{s}")
CLF = ("Cliff's Amusement Park, official attraction height requirements (PDF)", "https://www.cliffsamusementpark.com/wp-content/uploads/2025/03/2025-Attraction-Height-Requirements-and-Accessibility.pdf")
RUS = ("Rusutsu Resort Amusement Park, official attractions page", "https://rusutsu.com/amusement-park/attractions/")
PQE = ("Shima Spain Village Parque España, official attraction rules page", "https://www.parque-net.com/attraction/information.html")
_BB = lambda a, m: f"Riders {a} to {m} cm must ride with a companion aged 15 or older."
_DR = lambda a, m: f"Riders {a} to {m} cm must ride with an adult."
_P65 = "Not for guests aged 65 or older."
HP_B12c = {
 ("emerald-park", "Cú Chulainn Coaster"): M(min=120, src=EMP("the-cu-chulainn-coaster")),
 ("emerald-park", "Fianna Force"): M(min=120, max=205, src=EMP("na-fianna-force")),
 ("emerald-park", "Quest"): M(min=120, acc_min=95, acc_max=120, note=_adult(95, 120), src=EMP("the-quest")),
 ("emerald-park", "Dino Dash"): M(min=120, acc_min=95, acc_max=120, note=_adult(95, 120), src=EMP("dino-dash")),
 ("potts-park", "Braus & Saus"): M(min=120, acc_min=90, acc_max=120, note="Riding alone needs 120 cm and age 6; from 90 cm and age 3 riders must be accompanied.", src=POT),
 ("potts-park", "Säbelsaurus"): M(min=125, acc_min=105, acc_max=125, note="Riding alone needs 125 cm and age 7; from 105 cm and age 4 riders must be accompanied.", src=POT),
 ("potts-park", "Turbo-Drachen"): M(min=130, acc_min=105, acc_max=130, note="Riding alone needs 130 cm and age 8; from 105 cm and age 3 riders must be accompanied.", src=POT),
 ("potts-park", "Kiddy-Racer"): M(min=90, note="Minimum age 3, ridden under supervision; maximum weight 40 kg.", src=POT),
 ("bonbon-land", "Vild-Svinet"): M(min=140, acc_min=125, acc_max=140, note=_BB(125, 140), src=BBL),
 ("bonbon-land", "Han-Katten"): M(min=130, acc_min=110, acc_max=130, note=_BB(110, 130), src=BBL),
 ("bonbon-land", "Hundeprutten"): M(min=115, acc_min=95, acc_max=115, note=_BB(95, 115), src=BBL),
 ("bonbon-land", "Viktor Vandorm"): M(min=120, acc_min=90, acc_max=120, note=_BB(90, 120), src=BBL),
 ("tivoli-friheden", "Tyfonen"): M(min=120, src=TFR("tyfonen")),
 ("tivoli-friheden", "Vindfald"): M(min=125, max=195, src=TFR("vindfald")),
 ("tivoli-friheden", "Bisværmen"): M(min=120, acc_min=90, acc_max=120, max=195, note="Riders from 90 cm may ride with an adult; 120 cm to ride alone.", src=TFR("bisvaermen")),
 ("drievliet", "Kopermijn"): M(min=130, acc_min=100, acc_max=130, note=_DR(100, 130), src=DRV("kopermijn")),
 ("drievliet", "Twistrix"): M(min=120, acc_min=100, acc_max=120, note=_DR(100, 120), src=DRV("twistrix")),
 ("drievliet", "Dynamite Express"): M(min=120, acc_min=100, acc_max=120, note=_DR(100, 120), src=DRV("dynamite-express")),
 ("drievliet", "Formule X"): M(min=130, src=DRV("formule-x")),
 ("glenwood-caverns", "Defiance"): dict(min=56, acc_min=48, acc_max=56, note="Riders 48 to 56 inches must ride with a Supervising Companion (16 or older).", src=GWC("defiance-coaster")),
 ("glenwood-caverns", "Cliffhanger"): dict(min=56, acc_min=48, acc_max=56, note="Riders 48 to 56 inches must ride with a Supervising Companion (16 or older).", src=GWC("cliffhanger-roller-coaster")),
 ("glenwood-caverns", "Wild West Express"): dict(min=48, acc_min=36, acc_max=48, note="Riders 36 to 48 inches must ride with a Supervising Companion.", src=GWC("wild-west-express")),
 ("glenwood-caverns", "Alpine Coaster"): dict(min=54, acc_min=38, acc_max=54, note="54 inches to ride alone; from 38 inches (and at least 3 years old) as the front rider with a taller driver; maximum combined weight 330 lb.", src=GWC("alpine-coaster")),
 ("playlands-castaway-cove", "GaleForce"): dict(min=48, src=PCC("galeforce-roller-coaster-ocean-city-new-jersey")),
 ("playlands-castaway-cove", "Wild Waves"): dict(min=48, acc_min=42, acc_max=48, note="42 inches to ride; 48 inches to ride alone.", src=PCC("wild-waves-coaster")),
 ("playlands-castaway-cove", "Whirlwind"): dict(min=48, acc_min=36, acc_max=48, note="36 inches to ride; 48 inches to ride alone.", src=PCC("whirlwind-coaster")),
 ("playlands-castaway-cove", "Pirates Gold Rush"): dict(min=36, acc_min=33, acc_max=36, note="33 inches to ride; 36 inches to ride alone.", src=PCC("pirates-gold-rush-2")),
 ("denos-wonder-wheel", "Phoenix"): dict(min=48, acc_min=39, acc_max=48, note="48 inches to ride alone; 39 inches with a responsible person.", src=DWW("adultpark")),
 ("denos-wonder-wheel", "Sea Serpent"): dict(min=38, acc_min=36, acc_max=38, note="38 inches alone or 36 inches accompanied by a responsible attending person.", src=DWW("kiddie-park")),
 ("denos-wonder-wheel", "Skyflyer"): dict(min=36, src=DWW("kiddie-park")),
 ("cliffs-amusement-park", "New Mexico Rattler"): dict(min=48, src=CLF),
 ("cliffs-amusement-park", "Galaxi"): dict(min=48, acc_min=36, acc_max=48, note="No one under 36 inches; riders under 48 inches need a Supervising Companion at least 54 inches tall.", src=CLF),
 ("cliffs-amusement-park", "Spin-O-Rama"): dict(min=48, acc_min=36, acc_max=48, note="No one under 36 inches; riders under 48 inches need a Supervising Companion at least 54 inches tall.", src=CLF),
 ("rusutsu", "Hurricane"): M(min=130, max=200, note="Minimum age 10.", src=RUS),
 ("rusutsu", "Ultra Twister"): M(min=120, src=RUS),
 ("rusutsu", "Standing Coaster"): M(min=130, src=RUS),
 ("rusutsu", "Corkscrew"): M(min=125, src=RUS),
 ("rusutsu", "Loop the Loop"): M(min=110, src=RUS),
 ("rusutsu", "Mountain Jet Coaster"): M(min=110, src=RUS),
 ("rusutsu", "Go Go Sneaker"): M(min=110, acc_min=105, acc_max=110, note="Minimum age 4; riders 105 to 110 cm (age 4 or older) may ride with an adult.", src=RUS),
 ("parque-espana", "Pyrenees"): M(min=130, note="Not for children under 10. " + _P65, src=PQE),
 ("parque-espana", "Steampunk Coaster Iron Bull"): M(min=110, note=_P65, src=PQE),
 ("parque-espana", "Gran Montserrat"): M(min=110, note=_P65, src=PQE),
 ("parque-espana", "Kiddy Montserrat"): M(min=90, note="Children below school age must ride with a guardian.", src=PQE),
}
HP_INTL.update(HP_B12c)
INTL_PARKS += [
 dict(slug="emerald-park", name="Emerald Park", short="Emerald Park", loc="Ashbourne, County Meath, Ireland", state="County Meath", country="IE", official="https://www.emeraldpark.ie/", group="Emerald Park", checked=_C),
 dict(slug="potts-park", name="Potts Park", short="Potts Park", loc="Minden, Germany", state="North Rhine-Westphalia", country="DE", official="https://www.pottspark-minden.de/", group="Potts Park", checked=_C),
 dict(slug="bonbon-land", name="BonBon-Land", short="BonBon-Land", loc="Holme-Olstrup, Denmark", state="Zealand", country="DK", official="https://www.bonbonland.dk/", group="Parques Reunidos", checked=_C),
 dict(slug="tivoli-friheden", name="Tivoli Friheden", short="Friheden", loc="Aarhus, Denmark", state="Central Jutland", country="DK", official="https://www.friheden.dk/", group="Tivoli Friheden", checked=_C),
 dict(slug="drievliet", name="Drievliet", short="Drievliet", loc="The Hague, Netherlands", state="South Holland", country="NL", official="https://www.drievliet.nl/", group="Drievliet", checked=_C),
 dict(slug="glenwood-caverns", name="Glenwood Caverns Adventure Park", short="Glenwood Caverns", loc="Glenwood Springs, Colorado", state="CO", country="US", official="https://www.glenwoodcaverns.com/", group="Glenwood Caverns", checked=_C),
 dict(slug="playlands-castaway-cove", name="Playland's Castaway Cove", short="Castaway Cove", loc="Ocean City, New Jersey", state="NJ", country="US", official="https://oceancityfun.com/", group="Playland's Castaway Cove", checked=_C),
 dict(slug="denos-wonder-wheel", name="Deno's Wonder Wheel Amusement Park", short="Deno's", loc="Coney Island, Brooklyn, New York", state="NY", country="US", official="https://www.denoswonderwheel.com/", group="Deno's Wonder Wheel", checked=_C),
 dict(slug="cliffs-amusement-park", name="Cliff's Amusement Park", short="Cliff's", loc="Albuquerque, New Mexico", state="NM", country="US", official="https://www.cliffsamusementpark.com/", group="Cliff's", checked=_C),
 dict(slug="rusutsu", name="Rusutsu Resort Amusement Park", short="Rusutsu", loc="Rusutsu, Hokkaido, Japan", state="Hokkaido", country="JP", official="https://rusutsu.com/amusement-park/", group="Rusutsu Resort", checked=_C),
 dict(slug="parque-espana", name="Shima Spain Village Parque España", short="Parque España", loc="Shima, Mie, Japan", state="Mie", country="JP", official="https://www.parque-net.com/", group="Kintetsu", checked=_C),
]
DISPLAY_INTL.update({("emerald-park", "Quest"): "The Quest", ("emerald-park", "Cú Chulainn Coaster"): "The Cú Chulainn Coaster", ("emerald-park", "Fianna Force"): "Na Fianna Force",
 ("bonbon-land", "Vild-Svinet"): "Vildsvinet", ("bonbon-land", "Han-Katten"): "Hankatten"})

# ---- Batch 12d (11 Nov 2026): Kijima Kogen, Suzuka Circuit, Washuzan Highland, Lagunasia, Seoul Land, Leofoo Village ----
def KJK(s): return ("Kijima Kogen Park, official attraction page", f"https://www.kijimakogen-park.jp/ride/{s}/")
SZK = ("Suzuka Circuit Park, official attraction usage conditions", "https://www.suzukacircuit.jp/park/limit/")
WSH = ("Brazilian Park Washuzan Highland, official attractions page", "https://www.w-highland.co.jp/attraction/")
LGN = ("Lagunasia, official guide map with attraction limits (PDF)", "https://www.lagunatenbosch.co.jp/lagunasia/l_img/guidemap/p_guidemap2025_07.pdf")
SEL = ("Seoul Land, official attractions page", "https://seoulland.co.kr/?p=42")
LFV = ("Leofoo Village Theme Park, official park rules (ride height limits)", "https://www.leofoovillage.com.tw/Infos/Considerations/")
_K65 = "Not for guests aged 65 or older."
HP_B12d = {
 ("kijima-kogen", "Jupiter"): M(min=120, note=_K65, src=KJK("jupiter")),
 ("kijima-kogen", "Super LS Coaster"): M(min=120, note=_K65, src=KJK("lscoaster")),
 ("kijima-kogen", "Gold Rush"): M(min=120, note=_K65, src=KJK("goldrush")),
 ("kijima-kogen", "Dragon"): M(min=120, acc_min=105, acc_max=120, note="Riding alone needs 120 cm and age 7; riders 105 to 120 cm, and children aged 4 to 6, must ride with a guardian.", src=KJK("dragoncoaster")),
 ("kijima-kogen", "Roller Skater"): M(min=110, acc_min=105, acc_max=110, note="Minimum age 4; riders 105 to 110 cm must ride with a guardian.", src=KJK("rollerskate")),
 ("suzuka-circuit", "Rocky Coaster"): M(min=120, src=SZK),
 ("suzuka-circuit", "GP Racers"): M(min=120, src=SZK),
 ("suzuka-circuit", "Adventure Drive"): M(min=100, note="Pre-school children (ages 0 to 6) must be accompanied by someone of junior-high age or older.", src=SZK),
 ("washuzan-highland", "Ultra Twister"): M(min=120, src=WSH),
 ("washuzan-highland", "Pink Typhoon Standing Coaster"): M(min=140, note="The park lists it as the Standing Coaster.", src=WSH),
 ("washuzan-highland", "Chupy Coaster"): M(min=110, src=WSH),
 ("lagunasia", "Pirates' Blast"): M(min=130, note="No accompanied option is listed.", src=LGN),
 ("lagunasia", "Aqua Wind"): M(min=130, acc_min=110, acc_max=130, note="Riders from 110 cm may ride with a guardian; it runs forwards and backwards.", src=LGN),
 ("lagunasia", "Gummy Coaster"): M(min=110, acc_min=90, acc_max=110, note="Riders from 90 cm may ride with a guardian. The park map lists it under its former name, Stella Coaster.", src=LGN),
 ("seoul-land", "Columbia Double Loop Coaster"): M(min=120, note="The park lists it as 은하열차888 (Galaxy Train 888).", src=SEL),
 ("seoul-land", "Black Hole 2000"): M(min=120, src=SEL),
 ("seoul-land", "Crazy Mouse"): M(min=120, note="The park lists it as 달나라열차 (Moon Train).", src=SEL),
 ("seoul-land", "Tikitoc Train"): M(min=100, note="The park lists it as 티키톡열차.", src=SEL),
 ("seoul-land", "Tobot Train"): M(min=80, note="The park lists it as 또봇트레인.", src=SEL),
 ("leofoo-village", "Screaming Condor"): M(min=140, max=190, note="Chinese name 笑傲飛鷹.", src=LFV),
 ("leofoo-village", "Sahara Twist"): M(min=90, max=185, note="Chinese name 沙漠風暴.", src=LFV),
 ("leofoo-village", "Little Rattler"): M(min=90, note="Chinese name 西部瘋狂列車.", src=LFV),
}
HP_INTL.update(HP_B12d)
INTL_PARKS += [
 dict(slug="kijima-kogen", name="Kijima Kogen Park", short="Kijima Kogen", loc="Beppu, Oita, Japan", state="Oita", country="JP", official="https://www.kijimakogen-park.jp/", group="Kijima Kogen", checked=_C),
 dict(slug="suzuka-circuit", name="Suzuka Circuit Park", short="Suzuka Circuit", loc="Suzuka, Mie, Japan", state="Mie", country="JP", official="https://www.suzukacircuit.jp/park/", group="Mobilityland", checked=_C),
 dict(slug="washuzan-highland", name="Brazilian Park Washuzan Highland", short="Washuzan Highland", loc="Kurashiki, Okayama, Japan", state="Okayama", country="JP", official="https://www.w-highland.co.jp/", group="Washuzan Highland", checked=_C),
 dict(slug="lagunasia", name="Lagunasia", short="Lagunasia", loc="Gamagori, Aichi, Japan", state="Aichi", country="JP", official="https://www.lagunatenbosch.co.jp/lagunasia/", group="Laguna Ten Bosch", checked=_C),
 dict(slug="seoul-land", name="Seoul Land", short="Seoul Land", loc="Gwacheon, Gyeonggi, South Korea", state="Gyeonggi", country="KR", official="https://seoulland.co.kr/", group="Seoul Land", checked=_C),
 dict(slug="leofoo-village", name="Leofoo Village Theme Park", short="Leofoo Village", loc="Guanxi, Hsinchu County, Taiwan", state="Hsinchu County", country="TW", official="https://www.leofoovillage.com.tw/", group="Leofoo", checked=_C),
]
