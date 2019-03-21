#!usr/bin/python3

import requests
import json
import sys

id = "494717"
url = ("https://api.twitch.tv/helix/streams")

a = requests.get(url, data={"game_id": id}, headers={"Client-ID": "hsubli4s6848rcl50n36yc6rt1c83u"})
b = a.json()
streamer_list = []

def get_streamers():
    str_list=[]
    for i in b["data"]:
        print(i["user_name"])
        user_name = i["user_name"]
        str_list.append(user_name)
    return str_list

with open("a.json", "r") as f:
    c = json.load(f)

data = c["data"]
for i in data:
    print(i["id"])

with open("a.json", "w") as f:
    json.dump(b, f)

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
