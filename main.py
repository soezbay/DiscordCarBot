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
    selected_entry = random.choice(all_models)

    # Entnimm das "Models" Array des ausgewählten Eintrags
    selected_models = selected_entry["Models"]["Results"]

    # Entferne das ausgewählte Modell aus allmodels.json
    all_models.remove(selected_entry)

    # Speichere das aktualisierte allmodels.json
    with open("allmodels.json", "w") as file:
        json.dump(all_models, file, indent=4)

    # Speichere das ausgewählte Modell in takenModels.json
    with open("takenModels.json", "a") as taken_file:
        json.dump(selected_entry, taken_file, indent=4)

    await ctx.send(f"Die ausgewählten Modelle sind: {', '.join([model['Model_Name'] for model in selected_models])}")

#---RUN------------------------------------------------------------------------------------
with open("../keys/dct.txt", "r") as file:
    token = file.read().strip()
    print(token)

client.run(token)


