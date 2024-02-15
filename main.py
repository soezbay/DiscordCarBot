import discord
from discord.ext import commands
from discord import Intents
import json
import requests
import random

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

###
@client.command()
async def getcar(ctx):
    # Lade Daten aus allmodels.json
    with open("allmodels.json", "r") as file:
        all_models = json.load(file)

    # Wähle ein zufälliges Modell aus
    selected_model = random.choice(all_models)

    # Entferne das ausgewählte Modell aus allmodels.json
    all_models.remove(selected_model)

    # Speichere das ausgewählte Modell in takenModels.json
    with open("takenModels.json", "a") as taken_file:
        json.dump(selected_model, taken_file, indent=4)

    # Aktualisiere allmodels.json
    with open("allmodels.json", "w") as file:
        json.dump(all_models, file, indent=4)

    await ctx.send(f"Das ausgewählte Modell ist: {selected_model['Models']['Results'][0]['Model_Name']}")

#---RUN------------------------------------------------------------------------------------
with open("../keys/dct.txt", "r") as file:
    token = file.read().strip()
    print(token)

client.run(token)


