import discord
from discord.ext import commands
from discord import Intents

intents = Intents.default()
intents.messages = True
intents.message_content = True
client = commands.Bot(command_prefix='!', intents=intents)

@client.event
async def on_ready():
    print("The bot is ready to use!")
    print("=========================")

@client.command()
async def hello(ctx):
    await ctx.send("Hello back!")

with open("../dct/dct.txt", "r") as file:
    token = file.read().strip()
    print(token)

client.run(token)