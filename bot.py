#!/usr/bin/env python3

import discord
from discord.ext import commands
from discord.ext.commands import Bot
import time
import signal
import sys
import os
import random
import requests
import json
import io
import modules.req as r
import modules.twitch_get

# prints the discord version
print("Discord version: %s" % discord.__version__)

# this function takes a file named token.txt and reads the contents then passing it to the bot when called (returning)
def read_token():
	with open("files/token.txt", "r") as f:
		lines = f.readlines()
		return lines[0].strip()

# using the above function to pass the token into the variable TOKEN
TOKEN = read_token()

# create bot/client "object" with command prefix !
bot = commands.Bot(command_prefix = "!")

# dunno what this is I was gonna do smthg but forgot what XD
class Main_commands():
	def __init__(self, bot):
		self.bot = bot

# just in case I need to get a channel :)
def get_channel(channels, channel_name):
    for channel in bot.get_all_channels():
        print(channel)
        if channel.name == channel_name:
            return channel
    return None

# print when the bot is ready
@bot.event
async def on_ready():
	print("ready\n")
"""
@bot.event
async def on_message(message):
    print(message.author.id)
"""
# send currnet weather and temperature to the current channel user is in
@bot.command(pass_context = True)
async def weather(ctx, name="", units="metric"):
	a = r.search_city(name)
	print(str(a))
	if a == None:
		await bot.say("Couldn't find that place sry m8 :heart:")
	else:
		#print(weath)
		emoji_dict = r.get_emoji("files/icons.json")
		if units == "metric":
			weath = r.get_weather(a, units)
			ls = weath["list"]
			m = ls[0]
			main = m["main"]
			temp = main["temp"]
			cond = m["weather"]
			cond1 = cond[0]
			cond2 = cond1["main"]
			cond_icon = cond1["icon"]
			await bot.say("The condition in " + weath["city"]["name"] + " is currently: \n" + cond2 + " " + emoji_dict[cond_icon] + "\nRn the temperature is " + str(temp) + "ºC")
		elif units == "imperial":
			weath = r.get_weather(a, units)
			ls = weath["list"]
			m = ls[0]
			main = m["main"]
			temp = main["temp"]
			cond = m["weather"]
			cond1 = cond[0]
			cond2 = cond1["main"]
			cond_icon = cond1["icon"]
			await bot.say("The condition in " + weath["city"]["name"] + " is currently: \n" + cond2 + " " + emoji_dict[cond_icon] + "\nRn the temperature is " + str(temp) + "ºF")
		else:
			await bot.say("You entered an invalid unit type, choose either 'metric' or 'imperial'")

# basic ping command
@bot.command()
async def ping():
	""" Pong! """
	before = time.monotonic()
	message = await bot.say("Pong!")
	ping = (time.monotonic() - before) * 1000
	await bot.say("This took " + str(ping) + " ms")

# basic image test command might use this as a base to future better commands
@bot.command(pass_context = True)
async def pepe(ctx):
	await bot.send_file(ctx.message.channel, open("images/dank_pepe_or_nah_by_sheepjesus-d9khyt8.png", "rb"))

# basic gif sending command
@bot.command(pass_context = True)
async def gif(ctx):
        await bot.send_file(ctx.message.channel, open("images/a.gif", "rb"))

# basic echo command that repeats user input
@bot.command()
async def echo(*message):
	output = ""
	for word in message:
		output += word
		output += " "
	await bot.say(output)

@bot.command()
async def streams():
	twitch_get.

# catches keyboardinterrupt and closes cursor safely before closing bot
def keyboardInterruptHandler(signal, frame):
    print("KeyboardInterrupt (ID: {}) has been caught. Cleaning up...".format(signal))
    #print("Closed cursor")
    exit(0)

signal.signal(signal.SIGINT, keyboardInterruptHandler)

# actual bot running :)
bot.run(TOKEN)
