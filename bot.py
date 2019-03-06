#!/usr/bin/env python3

import discord
from discord.ext import commands
from discord.ext.commands import Bot
from discord.voice_client import VoiceClient
import time
import sys
import random
import selenium

print("Discord version: %s" % discord.__version__)

def read_token():
	with open("token.txt", "r") as f:
		lines = f.readlines()
		return lines[0].strip()

TOKEN = read_token()
bot = commands.Bot(command_prefix = "!")

class Main_commands():
	def __init__(self, bot):
		self.bot = bot

@bot.event
async def on_ready():
	print("ready\n")

@bot.command()
async def ping():
	""" Pong! """
	before = time.monotonic()
	message = await bot.say("Pong!")
	ping = (time.monotonic() - before) * 1000
	await bot.say("This took " + str(ping) + " ms")

@bot.command()
async def play(song):
	pass

@bot.command()
async def echo(*message):
	output = ""
	for word in message:
		output += word
		output += " "
	await bot.say(output)


"""
try:
	bot.load_extension("Music")
except Exception as e:
	print("lol")


async def on_message(message):
	if message.content.upper().startswith("!PING"):
		userID = message.author.id
		await bot.send_message(message.channel, "<@%s> Pong!" % (userID))
	elif message.content.startswith("cookie"):
		await bot.send_message(message.channel, ":cookie:")
"""
bot.run(TOKEN)

