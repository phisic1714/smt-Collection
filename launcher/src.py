import sys
import urllib.parse
import subprocess
import json
import datetime

# with open("launcher.log", "a", encoding="utf-8") as f:
#     f.write(f"{datetime.datetime.now()} argv={sys.argv}\n")

url = sys.argv[1]

parsed = urllib.parse.urlparse(url)

query = urllib.parse.parse_qs(parsed.query)

game_id = query.get("id", [""])[0]

with open(
    "C:/Users/pee/Documents/GitHub/smt-Collection/src/app/util/gameslist.json",
    "r",
    encoding="utf-8",
) as f:
    games = json.load(f)

game = next((g for g in games if g.get("run") == game_id), None)

if game:
    subprocess.Popen([game["emulator"], game["rom"]])
