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
