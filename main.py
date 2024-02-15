import discord
from discord.ext import commands
from discord import Intents
import json
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

@client.command()
async def getcar(ctx):
    # Lade Daten aus allmodels.json
    with open("allmodels.json", "r") as file:
        all_models = json.load(file)

    # Wähle ein zufälliges Modell aus einem zufälligen Eintrag aus
    selected_entry = random.choice(all_models)
    selected_models = selected_entry["Models"]["Results"]
    selected_model = random.choice(selected_models)

    # Entferne das ausgewählte Modell aus dem "Models" Array
    selected_models.remove(selected_model)

    # Speichere die aktualisierten Daten in allmodels.json
    with open("allmodels.json", "w") as file:
        json.dump(all_models, file, indent=4)

    # Lade bisherige Modelle aus takenModels.json, wenn die Datei vorhanden ist
    taken_models = []
    try:
        with open("takenModels.json", "r") as taken_file:
            taken_models = json.load(taken_file)
    except FileNotFoundError:
        pass

    # Füge das ausgewählte Modell zur Liste der genommenen Modelle hinzu
    taken_models.append(selected_model)

    # Speichere die Liste der genommenen Modelle in takenModels.json
    with open("takenModels.json", "w") as taken_file:
        json.dump(taken_models, taken_file, indent=4)

    await ctx.send(
        f"Modell: {selected_model['Model_Name']} \n" +
        f"Firma: {selected_entry['Make_Name']}"
        )

#---RUN------------------------------------------------------------------------------------
with open("../keys/dct.txt", "r") as file:
    token = file.read().strip()
    print(token)

client.run(token)
