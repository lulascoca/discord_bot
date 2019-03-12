#!/usr/bin/python3

import json

icons = {
		"01d": ":sunny:️", 
		"02d": ":partly_sunny:", 
		"03d": ":cloud:️",
		"04d": ":cloud::cloud:",
		"09d": ":cloud_rain:️",
		"10d": ":white_sun_rain_cloud:️",
		"11d": ":cloud_lightning:️",
		"13d": ":cloud_snow:️",
		"50d": ":fog:️",
		"01n": ":sunny:️", 
		"02n": ":partly_sunny:", 
		"03n": ":cloud:️",
		"04n": ":cloud::cloud:",
		"09n": ":cloud_rain:️",
		"10n": ":white_sun_rain_cloud:️",
		"11n": ":cloud_lightning:️",
		"13n": ":cloud_snow:️",
		"50n": ":fog:️"
		}

with open("../files/icons.json", "w") as file:
	json.dump(icons, file)