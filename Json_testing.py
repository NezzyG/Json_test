steam ={
    "103890994440728576": {
        "steamid": "76561197979389131",
        "userid": 103890994440728576,
        "rank": 20,
        "mmr": 0,
        "matches": 92,
        "wins": 0,
        "wins_recent30": 6,
        "top3_recent30": 12,
        "average_rank": 3.0,
        "last_updated": "2019-06-11T17:31:31+00:00"
    },
    "560501841255727115": {
        "steamid": "76561198042153811",
        "userid": 560501841255727115,
        "rank": 18,
        "mmr": 0,
        "matches": 119,
        "wins": 0,
        "wins_recent30": 9,
        "top3_recent30": 12,
        "average_rank": 2.8,
        "last_updated": "2019-06-11T17:31:45+00:00"
    },
    "489828419308224512": {
        "steamid": "76561198050329211",
        "userid": 489828419308224512,
        "rank": 13,
        "mmr": 0,
        "matches": 76,
        "wins": 0,
        "wins_recent30": 0,
        "top3_recent30": 10,
        "average_rank": 4.6,
        "last_updated": "2019-06-11T17:31:58+00:00"
    }
}
import json
from pprint import pprint

with open("users.json","w",encoding="utf-8") as f:
    data = json.dumps(steam, indent=4)
    f.write(data)
with open("users.json","r",encoding="utf-8") as f:
    data=json.load(f)
    pprint(data)
with open("users.json","w", encoding="utf-8") as f:
    data=json.dumps(data, indent=4)
    f.write(data)