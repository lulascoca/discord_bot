#!/usr/bin/env python3

import discord
from discord.ext import commands
from discord.ext.commands import Bot
import asyncio
import time
import sys

print("Discord version: %s" % discord.__version__)

def read_token():
	with open("token.txt", "r") as f:
		lines = f.readlines()
		return lines[0].strip()

TOKEN = read_token()
bot = commands.Bot(command_prefix = "!")


@bot.command()
async def ping():
	await bot.say("Pong")

@bot.command()
async def echo(*message):
	output = ""
	for word in message:
		output += word
		output += " "
	await bot.say(output)


"""
async def on_message(message):
	if message.content.upper().startswith("!PING"):
		userID = message.author.id
		await bot.send_message(message.channel, "<@%s> Pong!" % (userID))
	elif message.content.startswith("cookie"):
		await bot.send_message(message.channel, ":cookie:")
"""
bot.run(TOKEN)

