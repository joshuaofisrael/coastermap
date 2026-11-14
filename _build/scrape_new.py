"""Scrape additional parks from RCDB and merge into rcdb.json (same fields as scrape_rcdb.py + former.py)."""
import re, json, time, sys, os, urllib.request, html as H
UA={'User-Agent':'Mozilla/5.0 (CoasterMap research; contact via coastermap.com)'}
def get(u):
    for i in range(3):
        try: return urllib.request.urlopen(urllib.request.Request(u,headers=UA),timeout=30).read().decode('utf-8','replace')
        except Exception as e: err=e; time.sleep(3)
    raise err
def tx(s): return H.unescape(re.sub('<[^>]+>','',s)).strip()
NEW={'epcot':15503,'hollywood-studios':4735,'animal-kingdom':5109,'seaworld-orlando':4746,'kings-island':4540,'busch-gardens-williamsburg':4548,'hersheypark':4545,'knotts-berry-farm':4546,'dollywood':4593,'six-flags-great-adventure':4534,
 'six-flags-great-america':4530,'carowinds':4542,'canadas-wonderland':4539,'six-flags-over-texas':4531,'six-flags-over-georgia':4535,'kings-dominion':4544,'disneyland':4571,'disney-california-adventure':4783,'silver-dollar-city':4579,
 'six-flags-fiesta-texas':4538,'six-flags-new-england':4565,'six-flags-discovery-kingdom':4711,'californias-great-america':4541,'worlds-of-fun':4533,'valleyfair':4552,'dorney-park':4588,'michigans-adventure':4578,'seaworld-san-diego':5320,'seaworld-san-antonio':4601,'kennywood':4553,'holiday-world':4554,'universal-studios-hollywood':5265,
 'six-flags-darien-lake':4581,'la-ronde':4567,'frontier-city':4559,'mid-america-adventure':4536,'lake-compounce':4683,'knoebels':4557,'lagoon':4570,'silverwood':4564,
 'europa-park':4870,'phantasialand':4872,'alton-towers':4796,'thorpe-park':4814,'blackpool-pleasure-beach':4795,'portaventura-park':4792,'ferrari-land':12016,'efteling':4839,'liseberg':4909,'fuji-q-highland':4961,'universal-studios-japan':5492,'tokyo-disneyland':4959,'tokyo-disneysea':5073,'disneyland-paris':4864,'disney-adventure-world':5054,'hong-kong-disneyland':5279,'shanghai-disneyland':6556}
NEW.update({'legoland-florida':5589,'legoland-california':4733,'legoland-new-york':14429,'great-escape':4596,'kentucky-kingdom':4563,'elitch-gardens':4574,'gardaland':4866,'energylandia':12068,'heide-park':4874,'movie-park-germany':4869,'walibi-holland':4794,'walibi-belgium':4847,'parc-asterix':4790,'everland':5017,'lotte-world':5016,'ferrari-world':6302,'warner-bros-movie-world':4934,'dreamworld':4938,'universal-studios-singapore':4859,'universal-beijing-resort':17287})
NEW.update({'indiana-beach':4599,'adventureland-iowa':4576,'wild-adventures':4703,'waldameer':4646,'six-flags-mexico':4629,'canobie-lake-park':4602,'fun-spot-orlando':10346,'fun-spot-kissimmee':6373,'toverland':4900,'chessington':4798,'grona-lund':4910,'tivoli-gardens':4905,'linnanmaki':4917,'flamingo-land':4804,'moreys-piers':4560,'parque-warner-madrid':5028,'sarkanniemi':4919,'seabreeze':4583,'santa-cruz-beach-boardwalk':4573,'luna-park-coney-island':9250,'dutch-wonderland':4591,'idlewild':4600})
NEW.update({'six-flags-qiddiya-city':21275,'legoland-windsor':4813,'legoland-deutschland':5059,'legoland-billund':4903,'mirabilandia':4793,'tripsdrill':4886,'djurs-sommerland':5012,'drayton-manor':4803,'tusenfryd':4901,'bobbejaanland':4846,'skyline-park':4885})
NEW.update({'nickelodeon-universe-moa':4547,'nickelodeon-universe-american-dream':15593,'bakken':4907,'walibi-rhone-alpes':4857,'bellewaerde':4848,'adventure-island':4836,'sea-world-gold-coast':4942,'img-worlds':6645,'lightwater-valley':4797})
NEW.update({'nigloland':4854,'mt-olympus':4561,'kolmarden':6334,'nagashima-spa-land':4958,'parc-spirou':12676,'bayern-park':5068,'leolandia':5117,'belantis':5112,'fort-fun':4881,'casino-pier':4624,'lakeside':4575,'beech-bend':4717,'duinrell':4858,'furuvik':4911,'terra-mitica':4921,'beto-carrero':4948,'hopi-hari':4947,'yomiuriland':4968,'hirakata-park':5004,'gullivers-warrington':4823})
NEW.update({'hansa-park':4873,'plopsaland-de-panne':4850,'plopsaland-deutschland':4871})
NEW.update({'hellendoorn':4841,'walygator-grand-est':4855,'fraispertuis-city':5216})
NEW.update({'parque-de-atracciones-madrid':4928})
NEW.update({'chimelong-ocean-kingdom':8991,'chimelong-paradise':5904,'farup-sommerland':4908,'magicland':5627,'motiongate':13813,'legoland-malaysia':9575,'freizeit-land-geiselwind':4876,'pleasurewood-hills':4818,'gullivers-land':4825,'gyeongju-world':5040,'powerpark':5532,'fantasy-island':4812,'schloss-thurn':4894,'fantasilandia':4949,'julianatoren':4853})
NEW.update({'emerald-park':12363,'potts-park':4879,'drievliet':4840,'bonbon-land':5015,'tivoli-friheden':4726,'glenwood-caverns':6423,'playlands-castaway-cove':4675,'denos-wonder-wheel':4772,'cliffs-amusement-park':4661,'rusutsu':4985,'kijima-kogen':4983,'parque-espana':4970,'tobu-zoo':4978,'seoul-land':5019,'salitre-magico':5085,'parque-diversiones':5473,'land-of-legends':13838,'imagicaa':11296,'lagunasia':5228,'suzuka-circuit':4969,'washuzan-highland':5051,'e-world':5041,'leofoo-village':5045,'dunia-fantasi':5036,'vialand':10829,'schwaben-park':4877,'eifelpark':4884,'ok-corral':4861,'parque-del-cafe':5034,'enchanted-kingdom':4971,'fiabilandia':5198,'oriental-heritage':11603})
NEW.update({'magic-springs':4682,'lost-island':17529,'cotaland':18828,'family-kingdom':4619,'jolly-roger':4749,'quassy':4647,'camden-park':4607,'galaxyland':4568,'calaway-park':4608,'santas-village-dundee':4721,'little-amerricka':4598,'wonderland-amarillo':4594,'alabama-adventure':4702,'palace-playland':4655})
NEW.update({'freizeitpark-plohn':4925,'karls-elstal':15489,'tierpark-thule':5070,'rasti-land':4896,'le-pal':4865,'parc-saint-paul':5024,'bagatelle':4860,'parc-du-bocasse':5658,'futuroscope':5991,'familypark':5302,'conny-land':5951,'sommerland-sjaelland':5063,'brean':4862,'great-yarmouth-pleasure-beach':4802,'bottons':4806,'de-waarbeek':5227,'tosselilla':5636,'walygator-sud-ouest':4856,'mer-de-sable':5217,'papea':5403,'dennlys':5240,'cavallino-matto':5162,'new-jesolandia':6359,'fasanolandia':4930,'dreamland-margate':4826})
NEW.update({'greenland':4967,'nasu-highland':4986,'himeji-central-park':4966,'new-reoma':5667,'japan-monkey-park':4996,'hokkaido-greenland':5176,'yokohama-cosmoworld':4999,'benyland':5182,'wonderland-eurasia':12017,'ocean-park-hk':4974,'gold-reef-city':4957,'parque-de-la-costa':5010,'rainbows-end':4940,'gumbuya':15442,'kataplum':15712,'wonderla-bangalore':6066,'wonderla-kochi':5100,'wonderla-hyderabad':13854,'lotte-world-busan':17315,'e-da':8655,'janfusun':5044,'happy-valley-beijing':5689,'happy-valley-shanghai':6259,'happy-valley-shenzhen':5166,'sun-world-ba-na-hills':14134,'star-city':5527,'dream-world-thailand':5053,'viaport':7326,'mundo-petapa':5528,'xetulul':5148})
d=json.load(open('rcdb.json'))
NEW.update({'jardin-d-acclimatation':5113,'mandoria':17863,'winnoland':11420,'vinwonders-nha-trang':6218,'vinwonders-phu-quoc':7070,'vinwonders-nam-hoi-an':16441})
NEW.update({'adventureland-ny': 4676, 'playland-vancouver': 4609, 'luna-park-sydney': 4944, 'genting-skyworlds': 4977, 'lake-winnepesaukah': 4626, 'real-madrid-world': 18310, 'quest-doha': 12041, 'wicksteed-park': 4808, 'crealy': 4822, 'west-midlands-safari-park': 4809, 'gullivers-valley': 16181, 'serengeti-park': 4890, 'legoland-japan': 13644, 'warner-bros-world-abu-dhabi': 13899, 'adventure-park-usa': 5968, 'tropic-falls': 14398, 'parc-du-petit-prince': 14416, 'festyland': 5196, 'feeryland': 6276, 'ange-michel': 6241, 'karls-doebeln': 18135, 'karls-oberhausen': 5099, 'karls-roevershagen': 16269, 'jaderpark': 5069, 'lochmuehle': 5067, 'taunus-wunderland': 4895, 'tolk-schau': 4892, 'funny-world': 5856, 'churpfalzpark': 4887, 'trampolino': 6317, 'edelwies': 13367, 'sky-ranch-tagaytay': 6714, 'enakyo-wonderland': 5276, 'adventure-world-shirahama': 5002, 'robotland': 15327, 'ecoland': 21899, 'luna-park-tel-aviv': 5107, 'boudewijn-seapark': 4851, 'camel-creek': 9035, 'milky-way-adventure-park': 5072, 'twinlakes': 5731, 'barry-island': 4835, 'global-village': 6358, 'kingoland': 11524, 'fabrikus-world': 5584, 'jacquou-parc': 4936, 'didiland': 5401, 'parc-des-combes': 5449, 'magic-park-land': 5624, 'kid-parc': 6116, 'antibes-land': 6145, 'loos-parc': 16522, 'le-fleury': 13482, 'parc-de-la-vallee': 6324, 'la-recre-des-3-cures': 5402, 'lunapark-frejus': 6148, 'erlebniswelt-thale': 5289, 'hossoland': 20757, 'legendia': 5637, 'canpol-wonderland': 20674, 'fantasiland-pomezia': 10008, 'europark-idroscalo': 5957, 'serena-aventura': 19893, 'aztlan': 4628, 'cidade-da-crianca': 5008, 'animalia-park': 18057, 'dam-sen': 6071, 'suoi-tien': 6068, 'dai-nam': 8633, 'trans-studio-cibubur': 16828, 'jawa-timur-park-1': 5686, 'atlantis-land': 17083, 'kiftzuba': 12253, 'western-playland': 5993, 'ocean-beach-pleasure-park': 5387, 'fun-land-towyn': 5825, 'gateway-resort': 19659, 'yesterland-farm': 9263, 'cj-barrymores': 13371, 'festival-land-ajman': 16018, 'adventureland-sharjah': 5360})
NEW.update({'skara-sommarland': 5060, 'dalmaland': 14322, 'yerevan-park': 17231})
NEW.update({'divo-ostrov': 5489, 'dream-island': 14505, 'skazka-moscow': 15216, 'sochi-park': 10836})
for slug in sys.argv[1:] or NEW:
    pid=NEW[slug]
    h=get(f'https://rcdb.com/{pid}.htm'); time.sleep(1)
    name=tx(re.search(r'<h1>(.*?)</h1>',h).group(1))
    i=h.find('Operating Roller Coasters'); j=h.find('</table>',i)
    rows=re.findall(r'<a href=/(\d+)\.htm>([^<]+)</a>',h[i:j])
    park={'rcdb_id':pid,'name':name,'rcdb_url':f'https://rcdb.com/{pid}.htm','coasters':[]}
    for cid,cname in rows:
        fn=f'raw/{cid}.html'
        if os.path.exists(fn): c=open(fn).read()
        else: c=get(f'https://rcdb.com/{cid}.htm'); open(fn,'w').write(c); time.sleep(1)
        dd={'rcdb_id':int(cid),'name':H.unescape(cname),'rcdb_url':f'https://rcdb.com/{cid}.htm'}
        m=re.search(r'Operating</a> since <time datetime="([^"]+)"',c); dd['opened']=m.group(1) if m else None
        dd['tags']=[tx(x) for x in re.findall(r'<li><a href="/g.htm\?id=\d+">([^<]+)</a>',c.split('<div class=scroll>')[0])]
        m=re.search(r'Make: <a href=/\d+\.htm>([^<]+)</a>',c); dd['make']=H.unescape(m.group(1)) if m else None
        m=re.search(r'Model: (.*?)</p>',c); dd['model']=tx(m.group(1)) if m else None
        sec=c[c.find('<h3>Tracks</h3>'):]; sec=sec[:sec.find('</section>')]
        stats={}
        for k,v in re.findall(r'<tr><th>([^<]+)<td>(.*?)(?=<tr>|</tbody>|</table>)',sec):
            if k=='Elements': continue
            stats.setdefault(k,[]).append(tx(v))
        dd['stats']=stats
        m=re.search(r'Arrangement<td>(.*?)<',c); dd['trains']=tx(m.group(1)) if m else None
        m=re.search(r'place/(-?[\d.]+),(-?[\d.]+)/',c); dd['lat'],dd['lon']=(float(m.group(1)),float(m.group(2))) if m else (None,None)
        m=re.search(r'<th>Former names?<td>(.*?)</tr>|<th>Former names?<td>(.*?)<tr',c)
        seg=(m.group(1) or m.group(2)) if m else None
        dd['former']=re.sub(r'\s+',' ',H.unescape(re.sub('<[^>]+>',' ',seg))).strip() if seg else None
        st={}
        for k,v in re.findall(r'<tr><th>([^<]+)<td>(.*?)(?=<tr>|</tbody>|</table>)',sec):
            if k=='Elements': continue
            vals=re.findall(r'<span class=float>([\d.]+)</span>\s*([a-z°]+)?',v)
            if vals: st[k]=vals[0][0]+((' '+vals[0][1]) if vals[0][1] else '')
            else: st[k]=re.split(r'(?<=\d)(?=\d:)|(?<=\S)(?=\S*$)', H.unescape(re.sub('<[^>]+>','|',v)).strip('|'))[0].split('|')[0]
        dd['st']=st
        park['coasters'].append(dd); print(slug,'|',dd['name'],dd['opened'],dd['make'],st.get('Height'),st.get('Speed'),st.get('Inversions'),dd['lat'],dd['former'])
    d[slug]=park
    json.dump(d,open('rcdb.json','w'),indent=1,ensure_ascii=False)
