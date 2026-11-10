import glob,re,json,os,sys,html
ROOT=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
LEGAL={'terms','privacy','disclaimer','copyright','ad-disclosure'}
bad=0;titles={}
files=[f for f in glob.glob(ROOT+'/**/*.html',recursive=True) if '/_build/' not in f]
for f in files:
    h=open(f).read(); rel=os.path.relpath(f,ROOT)
    for m in re.findall(r'<script type="application/ld\+json">(.*?)</script>',h):
        try: json.loads(m)
        except Exception as e: print('JSONLD',rel,e); bad+=1
    top=rel.split('/')[0]
    if top not in LEGAL|{'credits'} and re.search(r'Joshua|Israel Ventures|©(?! <a href="https://www.openstreetmap)',re.sub(r'<script.*?</script>','',h,flags=re.S)): print('LLC/©',rel); bad+=1
    if top in LEGAL and 'is a trade name of Joshua Israel Ventures LLC' not in h: print('nolegalline',rel); bad+=1
    if 'static.cloudflareinsights.com/beacon.min.js' not in h: print('nobeacon',rel); bad+=1
    if 'noindex' in h and rel!='404.html': print('noindex',rel); bad+=1
    if '—' in h or '–' in h: print('dash',rel)
    t=re.search(r'<title>(.*?)</title>',h).group(1); titles.setdefault(t,[]).append(rel)
    for l in re.findall(r'href="(/[^"#?]*)',h):
        p=os.path.join(ROOT,l.lstrip('/')); 
        if not (os.path.isfile(p) or os.path.isfile(os.path.join(p,'index.html'))): print('broken',rel,l); bad+=1
for t,fs in titles.items():
    if len(fs)>1: print('duptitle',t,fs); bad+=1
    if len(html.unescape(t))>70: print('longtitle',len(t),t)
print('files',len(files),'issues',bad)
