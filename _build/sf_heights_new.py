import json,re,html,subprocess,time,unicodedata,sys
UA='Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 Chrome/124 Safari/537.36'
d=json.load(open('rcdb.json'))
def slugify(s):
    s=unicodedata.normalize('NFKD',s).encode('ascii','ignore').decode().lower().replace("'","").replace('’','').replace('!','')
    return re.sub(r'[^a-z0-9]+','-',s).strip('-')
extra=json.load(open('sf_extra_slugs.json'))
try: res=json.load(open('sf_heights_new.json'))
except: res={}
PARKS=[('kings-island','kingsisland'),('knotts-berry-farm','knotts'),('six-flags-great-adventure','greatadventure'),('six-flags-great-america','greatamerica'),('carowinds','carowinds'),('canadas-wonderland','canadaswonderland'),('six-flags-over-texas','overtexas'),('six-flags-over-georgia','overgeorgia'),('kings-dominion','kingsdominion'),('six-flags-fiesta-texas','fiestatexas'),('six-flags-new-england','newengland'),('six-flags-discovery-kingdom','discoverykingdom'),('californias-great-america','cagreatamerica'),('dorney-park','dorneypark'),
 ('worlds-of-fun','https://worldsoffun.enchantedparks.com/rides-and-experiences/attractions/'),('valleyfair','https://valleyfair.enchantedparks.com/rides-and-experiences/attractions/'),('michigans-adventure','https://miadventure.enchantedparks.com/rides-and-experiences/attractions/')]
only=sys.argv[1:]
for park,pk in PARKS:
    if only and park not in only: continue
    for c in d[park]['coasters']:
        n=c['name']; key=f'{park}|{n}'
        if res.get(key): continue
        found=None
        for s in extra.get(key,[])+[slugify(n),'the-'+slugify(n)]:
            u=(pk+s+'/') if pk.startswith('http') else f'https://www.sixflags.com/{pk}/attractions/{s}'
            h=subprocess.run(['curl','-sL','-A',UA,'--max-time','25',u],capture_output=True,text=True).stdout
            t=re.sub(r'\s+',' ',html.unescape(re.sub(r'<script.*?</script>|<style.*?</style>|<[^>]+>',' ',h,flags=re.S)))
            t=t.replace('"','”')
            m=re.search(r'Min Height (\d+)” (?:Min Height Accompanied (\d+)” )?(?:Max Height Accompanied \d+” )?(?:Max Height (\d+)” )?(?:Thrill Level (\d))?',t)
            if m:
                intro=re.search(r'Introduced (\d{4})',t)
                acc=re.search(r'Min Height Accompanied (\d+)”',t)
                found={'url':u,'min':m.group(1),'acc_min':m.group(2),'acc_max':m.group(1) if m.group(2) else None,'max':m.group(3),'thrill':m.group(4),'introduced':intro.group(1) if intro else None,'ctx':t[m.start():m.start()+200]}; break
            time.sleep(0.4)
        res[key]=found; print(key, found and {k:found[k] for k in ['url','min','acc_min','max','thrill','introduced']})
json.dump(res,open('sf_heights_new.json','w'),indent=1,ensure_ascii=False)
