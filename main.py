import discord
from discord.ext import commands
from discord import Intents
import json
import requests

intents = Intents.default()
intents.messages = True
intents.message_content = True
intents.members = True
client = commands.Bot(command_prefix='!', intents=intents)


@client.event
async def on_ready():
    print("The bot is ready to use!")
    print("=========================")


@client.event
async def on_member_join(member):
    channel = client.get_channel(976637572807786569)
    await member.send("Hi Mr. ")


@client.event
async def on_member_remove(member):
    channel = client.get_channel(976637572807786569)
    await member.send("Bye Mr. ")


@client.command()
async def hello(ctx):
    await ctx.send("Hello back!")


@client.command()
async def bye(ctx):
    await ctx.send("Bye Bye!")


@client.command()
async def getCar(ctx):
    url = "https://dealerkit.p.rapidapi.com/api/get-vin/"

    querystring = {"vin": "4F2YU09161KM33122", "format": "json"}

    headers = {
        "X-RapidAPI-Key": "SIGN-UP-FOR-KEY",
        "X-RapidAPI-Host": "dealerkit.p.rapidapi.com"
    }

    response = requests.get(url, headers=headers, params=querystring)

    print(response.json())

    await ctx.send(response.json())

with open("../dct/dct.txt", "r") as file:
    token = file.read().strip()
    print(token)

client.run(token)
