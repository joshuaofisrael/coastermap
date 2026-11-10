# Coaster Map (coastermap.com)

Roller coasters at the big theme parks, mapped and explained: height requirements (official park pages), stats (RCDB), intensity, who it suits, seat guidance, park maps (Leaflet + OSM), a ride height checker and a coaster quiz.

- Repo: https://github.com/joshuaofisrael/coastermap  · Hosting: GitHub Pages, branch `main`, folder `/`, custom domain coastermap.com (CNAME file).
- Build: `python3 _build/build.py` then `python3 _build/check.py` (JSON-LD, beacon, legal line, broken links, duplicate titles). Commit the built HTML.
- Data (all in `_build/`):
  - `rcdb.json`: RCDB scrape (10 Nov 2026) for every park: operating coasters, stats, coordinates, former names. Scraper: `scrape_new.py` (park slug to RCDB id map in `NEW`; run `python3 scrape_new.py slug...`, caches raw pages in /workspace/coastermap-data/raw/).
  - `sf_heights.json`: sixflags.com heights for the original Cedar Point and Magic Mountain, keyed by ride name.
  - `sf_heights_new.json`: heights scraped by `sf_heights_new.py` from sixflags.com ride pages and Enchanted Parks ride pages (Worlds of Fun, Valleyfair, Michigan's Adventure, Mid America Adventure), keyed `park-slug|RCDB name`; `sf_extra_slugs.json` holds slug overrides. After a run, clear acc_min when it equals min.
  - `data.py`: `PARKS` (slug, names, location, official URL, group, optional `former` park name), `ORIGINAL` (launch parks, which use `sf_heights.json` and `H`), `DISPLAY` / `DISPLAY_PARK` name overrides, `H` (launch-park heights) and `HP2` (expansion-park heights keyed (park slug, RCDB name)), each with its official source tuple. Lookup order: sf_heights_new (non-original parks), then HP2, then H.
  - Height model: `min` = ride alone, `acc_min`/`acc_max` = companion range, `max` = maximum, `thrill` = park's 1 to 5 rating, optional `unit="cm"` when the park's official rule is metric (stored in cm, shown as cm with inches; the height checker compares in the rule's own unit).
  - Never add an unsourced number; if a rule cannot be verified on an official page, leave it out (the page then says "check park").
- Expansion log (parks/coasters added after launch, with commits): expansion-log.md
- Config in `_build/build.py`: BASE_URL, INDEXNOW_KEY (fe204aafdcd4bf6d890c7776842749c0), CF_BEACON_TOKEN (shared JI Ventures Analytics 2 token eac63f2b..., requestHost match; both CF accounts at Web Analytics site limit), GSC_TOKEN, SIGNUP_ENDPOINT (Worker coastermap-signups on Cloudflare account eb5337..., shared signups D1 71ea4103..., site=coastermap; collect only), FORM_ENDPOINT (FormSubmit hashed endpoint, same as siblings).
- IndexNow: `./indexnow.sh` (all sitemap URLs) or `./indexnow.sh URL...`.
- Not yet covered: Universal Orlando ride pages (blocked to our fetcher; heights via Visit Orlando). Omitted height rules and skipped parks are listed in expansion-log.md.
