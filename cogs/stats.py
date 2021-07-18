import discord
from discord.ext import commands
import sqlite3
from .Modules.paginator import*

class Stats(commands.Cog):
    def __init__(self, client):
        self.client = client
        self.db = sqlite3.connect("Data/database.db")
    
    @commands.command(brief='Command to verify if server is setup properly to display stats.')
    async def verify_server(self, ctx):
        category_found = False
        for category in ctx.message.guild.categories:
            if category.name == "STATS":
                category_found = True
                new_category = category
        
        if not category_found:
            new_category = await ctx.guild.create_category("STATS")
            await ctx.send("Created category ***STATS***.")
        else:
            await ctx.send("Category ***STATS***  already existing.")
        
        channel_found = False
        for channel in ctx.message.guild.channels:
            if channel.name == "current-member":
                channel_found = True
                
        if not channel_found:
            channel = await ctx.guild.create_text_channel('current-member', category=new_category)
            await ctx.send("Created channel ***current-member***.")
        else:
            await ctx.send("Channel ***current-member***  already existing.")
        
def setup(client):
    client.add_cog(Stats(client))
