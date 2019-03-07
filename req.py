#!/usr/bin/python3

import requests
import sys
import configparser

cofnig = configparser.ConfigParser()

#actual request with my api (just an example tho remembver to get json)
#r = requests.get("http://api.openweathermap.org/data/2.5/forecast?id=524901&APPID=0c0f9be83b03974dc0e892436eaa9a13")

#sample
r = requests.get("https://samples.openweathermap.org/data/2.5/forecast?id=524901&appid=b1b15e88fa797225412429c1c50c122a1")

print(r.status_code)

for key in r.headers:
	print(key + ": ")
	print(r.headers[key] + "\n")
