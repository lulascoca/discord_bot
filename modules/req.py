#!/usr/bin/python3

import requests
import sys
import configparser
import json

#cofnig = configparser.ConfigParser()

r = requests.get("http://api.openweathermap.org/data/2.5/forecast?id=524901&APPID=0c0f9be83b03974dc0e892436eaa9a13")

with open("city.list.json", "r") as file:
	data = json.load(file)

for f in data:
     a = f["name"]
     if a == "Viseu":
             print(a)





"""
with open("city.list.json") as json_file:
    #text = json_file.read()
    json_data = json.loads(json_file)
    print(json_data)
"""

#json_data = json.loads("city.list.json")

#sample
#r = requests.get("https://samples.openweathermap.org/data/2.5/forecast?id=524901&appid=b1b15e88fa797225412429c1c50c122a1")

print(r.status_code)

for key in r.headers:
	print(key + ": ")
	print(r.headers[key] + "\n")
