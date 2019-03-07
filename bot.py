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

print("Discord version: %s" % discord.__version__)

def read_token():
	with open("files/token.txt", "r") as f:
		lines = f.readlines()
		return lines[0].strip()

TOKEN = read_token()

bot = commands.Bot(command_prefix = "!")

class Main_commands():
	def __init__(self, bot):
		self.bot = bot

def get_channel(channels, channel_name):
    for channel in bot.get_all_channels():
        print(channel)
        if channel.name == channel_name:
            return channel
    return None

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

@bot.command(pass_context = True)
async def pepe(ctx):
	await bot.send_file(ctx.message.channel, open("images/dank_pepe_or_nah_by_sheepjesus-d9khyt8.png", "rb"))

@bot.command(pass_context = True)
async def gif(ctx):
        await bot.send_file(ctx.message.channel, open("images/a.gif", "rb"))

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

bot.run(TOKEN)
