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
