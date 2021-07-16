from discord.ext import commands, tasks
import discord
import os
import sqlite3
from cogs.Modules.sql_utils import*
from cogs.Modules.json import*
import asyncio
from datetime import datetime
import json

###################################################################### COG UNLOAD + LOAD    ################################################
def load_all():
    for file in os.listdir("cogs"):
        if file.endswith(".py"):
            print(f"===== {file[:-3]} loaded =====")
            client.load_extension("cogs."+file[:-3])

def unload_all():
    for file in os.listdir("cogs"):
        if file.endswith(".py"):
            print(f"===== {file[:-3]} unloaded =====")
            client.unload_extension("cogs."+file[:-3])


###################################################################### DATABASE MANAGING    ################################################
database = sqlite3.connect("Data/database.db")
create_table(database, "paginator", "(page integer, pageNB integer, messageId integer, embeds blob)")
reset_table(database, "paginator")
######################################################################     DISCORD BOT    ################################################

async def get_pre(bot, message):
    with open('Configuration/server_setting.json') as json_file:
        data = json.load(json_file)
        prefix = data["prefix"]
    return prefix

client = commands.Bot(command_prefix = get_pre)

@client.command(brief='Command to reload all cogs (For Hotfixes).')
async def reload_cogs(ctx):
    unload_all()
    load_all()
    await ctx.send("All cogs have been reloaded.")

    
# Load all cogs
load_all()

######################################################################   RUN BOT WITH TOKEN    ################################################
with open("token.txt","r") as file:
    client.run(file.readline())

