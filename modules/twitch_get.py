#!/usr/bin/python3

import requests
import json
import sys

"""game = requests.get("https://api.twitch.tv/helix/games", params={"name": "fortnite"}, headers={"Client-ID": "hsubli4s6848rcl50n36yc6rt1c83u"})
game_data=game.json()
print(game_data)"""

def get_game_id(name):
    print(name)
    req = requests.get("https://api.twitch.tv/helix/games", params={"name": name}, headers={"Client-ID": "hsubli4s6848rcl50n36yc6rt1c83u"})
    req_json = req.json()
    print(req_json)
    return req_json["data"][0]["id"]

id=get_game_id("fortnite")
url = ("https://api.twitch.tv/helix/streams/")

a = requests.get(url, params={"game_id": id}, headers={"Client-ID": "hsubli4s6848rcl50n36yc6rt1c83u"})
print(a.json())
b = a.json()
#print(b)
streamer_list = []

def get_streamers():
    str_list=[]
    for i in b["data"]:
        print(i["user_name"])
        user_name = i["user_name"]
        str_list.append(user_name)
    return str_list

get_streamers()

"""
with open("a.json", "r") as f:
    c = json.load(f)

data = c["data"]
for i in data:
    print(i["id"])

with open("a.json", "w") as f:
    json.dump(b, f)
"""
"""
streamer_list=get_streamers()
streamer_list_check=get_streamers()

if streamer_list == streamer_list_check:
    print("nothing to see here")
else:
    print("as")

print(streamer_list)
"""
#print(b)
