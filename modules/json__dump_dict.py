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
		"50d": ":fog:️"
		}

with open("../files/icons.json", "w") as file:
	json.dump(icons, file)