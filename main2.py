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


# @client.command()
# async def getCar1(ctx):
#     # Öffnen der Textdatei und Lesen des API-Schlüssels
#     with open("../keys/rapidApiKey.txt", "r") as key_file:
#         api_key = key_file.read().strip()
        
#     url = "https://dealerkit.p.rapidapi.com/api/get-vin/"

#     querystring = {"vin": "4F2YU09161KM33122", "format": "json"}

#     headers = {
#         "X-RapidAPI-Key": api_key,
#         "X-RapidAPI-Host": "dealerkit.p.rapidapi.com"
#     }

#     response = requests.get(url, headers=headers, params=querystring)

#     print(response.json())

#     await ctx.send(response.json())

####
# @client.command()
# async def getcar(ctx):
        
#     # url = "http://vpic.nhtsa.dot.gov/api/vehicles/GetVehicleTypesForMakeId/412?format=json"
#     url = "http://vpic.nhtsa.dot.gov/api/vehicles/getallmakes?format=json"

#     response = requests.get(url)

#     data = response.json()

#     # Überprüfen, ob die Antwort erfolgreich war
#     if 'Results' in data:
#         # Liste der IDs aus den Ergebnissen extrahieren
#         ids = [result['Make_ID'] for result in data['Results']]

#         # IDs aufsteigend sortieren
#         sorted_ids = sorted(ids)
#         print(f"Alle IDs aufsteigend: {sorted_ids}")
#         print(f"Größe des Arrays: {len(sorted_ids)}")
#     else:
#         print("Fehler bei der Abfrage der Daten")

####
# @client.command()
# async def getcarminid(ctx):

#     url = "http://vpic.nhtsa.dot.gov/api/vehicles/GetVehicleTypesForMakeId/412?format=json"

#     response = requests.get(url)

#     data = response.json()

#     # Überprüfen, ob die Antwort erfolgreich war
#     if 'Results' in data:
#         # Liste der IDs aus den Ergebnissen extrahieren
#         ids = [result['Make_ID'] for result in data['Results']]

#         # Die kleinste ID finden
#         min_id = min(ids)

#         print(f"Die kleinste ID ist: {min_id}")
#     else:
#         print("Fehler bei der Abfrage der Daten")

###
@client.command()
async def getcar(ctx):
        
    with open("all_responses.json", "r") as file:
        token = file.read().strip()

    print(token)

    # # Überprüfen, ob die Antwort erfolgreich war
    # if 'Results' in data:
    #     # Liste der IDs aus den Ergebnissen extrahieren
    #     ids = [result['Make_ID'] for result in data['Results']]

    #     # IDs aufsteigend sortieren
    #     sorted_ids = sorted(ids)
    #     print(f"Alle IDs aufsteigend: {sorted_ids}")
    #     print(f"Größe des Arrays: {len(sorted_ids)}")
    # else:
    #     print("Fehler bei der Abfrage der Daten")
        
# @client.event
# async def on_message(message):
    
#     print(message)        


#---RUN------------------------------------------------------------------------------------
with open("../keys/dct.txt", "r") as file:
    token = file.read().strip()
    print(token)

client.run(token)


