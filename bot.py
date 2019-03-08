#!/usr/bin/env python3

import discord
from discord.ext import commands
from discord.ext.commands import Bot
import time
import sys
import random
import requests
import json
import io
import modules.req as r

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

@bot.command(pass_context = True)
async def weather(ctx, name="", id=0):
	a = r.search_city(name, id)
	print(str(a))
	if a == None:
		await bot.say("Couldn't find that place sry m8 :heart:")
	else:
		weath = r.get_weather(a)
		print(weath)
		ls = weath["list"]
		m = ls[0]
		main = m["main"]
		temp = main["temp"]
		await bot.say("The current temperature in " + name + " is currently " + str(temp))

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

"""
@bot.command()
async def porn():
	await bot.say("fuk me daddy")
	with open("dank_pepe_or_nah_by_sheepjesus-d9khyt8.png", "rb") as pic:
		await bot.send_file(get_channel(bot.get_all_channels(),channel_name="general", pic)
"""

# actual bot running :)
bot.run(TOKEN)

