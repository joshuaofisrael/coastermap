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
NEW.update({'indiana-beach':4599,'adventureland-iowa':4576,'wild-adventures':4703,'waldameer':4646,'six-flags-mexico':4629,'canobie-lake-park':4602,'fun-spot-orlando':10346,'fun-spot-kissimmee':6373,'toverland':4900,'chessington':4798,'grona-lund':4910,'tivoli-gardens':4905,'linnanmaki':4917,'flamingo-land':4804,'moreys-piers':4560,'parque-warner-madrid':5028,'sarkanniemi':4919,'seabreeze':4583,'santa-cruz-beach-boardwalk':4573,'luna-park-coney-island':9250})
d=json.load(open('rcdb.json'))
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
