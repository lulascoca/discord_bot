#!/usr/bin/python3

import requests
import sys
import configparser
import json
import urllib.request

#cofnig = configparser.ConfigParser()

#r = requests.get("http://api.openweathermap.org/data/2.5/forecast?id=524901&APPID=0c0f9be83b03974dc0e892436eaa9a13")


def search_city(name="", id=0):
	with open("files/city.list.json", "r") as file:
		data = json.load(file)
	try:
		for f in data:
			cit_name = f["name"]
			cit_id = f["id"]
			if cit_name.lower() == name.lower() and not cit_name == "":
				for key in f:
					print(key + " - " + str(f[key]))
				print("\n")
				return cit_id
			elif cit_id == id:
				for key in f:
					print(key + " - " + str(f[key]))
				print("\n")
				return cit_id
	except Exception as e:
		print("unable to locate city/place")

def get_weather(a):
	url = ("http://api.openweathermap.org/data/2.5/forecast?id=" + str(a) + "&APPID=0c0f9be83b03974dc0e892436eaa9a13" + "&units=metric")
	print(url)
	with urllib.request.urlopen(url) as url_:
		data = json.loads(url_.read().decode())
		return data

"""
print(r.status_code)

for key in r.headers:
	print(key + ": ")
	print(r.headers[key] + "\n")
"""
