# Coaster Map (coastermap.com)

Roller coasters at the big theme parks, mapped and explained: height requirements (official park pages), stats (RCDB), intensity, who it suits, seat guidance, park maps (Leaflet + OSM), a ride height checker and a coaster quiz.

- Repo: https://github.com/joshuaofisrael/coastermap  · Hosting: GitHub Pages, branch `main`, folder `/`, custom domain coastermap.com (CNAME file).
- Build: `python3 _build/build.py` then `python3 _build/check.py` (JSON-LD, beacon, legal line, broken links, duplicate titles). Commit the built HTML.
- Data: `_build/rcdb.json` (scraped from RCDB 10 Nov 2026), `_build/sf_heights.json` (sixflags.com ride pages for the original Cedar Point and Magic Mountain, keyed by ride name), `_build/sf_heights_new.json` (sixflags.com ride pages for Kings Island, Knott's, Great Adventure, keyed `park-slug|RCDB name`), heights for other original parks in `_build/data.py` H dict and for expansion parks in the HP2 dict keyed (park slug, RCDB name), each with source. Never add an unsourced number. Scrapers: /workspace/coastermap-data/scrape_new.py (RCDB, park ids in NEW) and sf_heights_new.py.
- Expansion log (parks/coasters added after launch, with commits): expansion-log.md
- Config in `_build/build.py`: BASE_URL, INDEXNOW_KEY (fe204aafdcd4bf6d890c7776842749c0), CF_BEACON_TOKEN (shared JI Ventures Analytics 2 token eac63f2b..., requestHost match; both CF accounts at Web Analytics site limit), GSC_TOKEN, SIGNUP_ENDPOINT (Worker coastermap-signups on Cloudflare account eb5337..., shared signups D1 71ea4103..., site=coastermap; collect only), FORM_ENDPOINT (FormSubmit hashed endpoint, same as siblings).
- IndexNow: `./indexnow.sh` (all sitemap URLs) or `./indexnow.sh URL...`.
- Not yet covered: Universal ride pages (blocked to our fetcher; heights via Visit Orlando), Pteranodon Flyers / Great American Revolution / Canyon Cruiser height rules unverified.
