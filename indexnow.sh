#!/usr/bin/env bash
# Ping IndexNow for Coaster Map. Usage: ./indexnow.sh URL [URL...]   (no args = every URL in the live sitemap)
KEY=fe204aafdcd4bf6d890c7776842749c0
HOST=coastermap.com
BASE=https://coastermap.com/
if [ $# -eq 0 ]; then set -- $(curl -s ${BASE}sitemap.xml | grep -o '<loc>[^<]*' | sed 's/<loc>//'); fi
LIST=$(printf '%s\n' "$@" | python3 -c 'import sys,json;print(json.dumps([l.strip() for l in sys.stdin if l.strip()]))')
curl -s -o /dev/null -w "IndexNow HTTP %{http_code} ($# URLs)\n" -X POST https://api.indexnow.org/indexnow \
  -H 'Content-Type: application/json; charset=utf-8' \
  -d "{\"host\":\"$HOST\",\"key\":\"$KEY\",\"keyLocation\":\"${BASE}$KEY.txt\",\"urlList\":$LIST}"
