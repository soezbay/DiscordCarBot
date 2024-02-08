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

client.run('MTE5NjQ4Mjk0ODU5NDE1OTcwNg.GNbuk2.PvNAw4V3o1s-QZy_dKrGZUk_rXnqnEcOBuS9sU')