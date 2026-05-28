import sys
import urllib.parse
import subprocess
import json

print("f")
url = sys.argv[1]

parsed = urllib.parse.urlparse(url)

query = urllib.parse.parse_qs(parsed.query)

game_id = query.get("id", [""])[0]

with open("src/app/util/gameslist.json", "r", encoding="utf-8") as f:
    games = json.load(f)

game = games.get(game_id)

if game:
    subprocess.Popen([game["emulator"], game["rom"]])
