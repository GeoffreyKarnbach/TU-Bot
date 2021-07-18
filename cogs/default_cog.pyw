import discord
from discord.ext import commands
import sqlite3
from .Modules.paginator import*

class CogName(commands.Cog):
    def __init__(self, client):
        self.client = client
        self.db = sqlite3.connect("Data/database.db")

    # First Command 
    
def setup(client):
    client.add_cog(CogName(client))
