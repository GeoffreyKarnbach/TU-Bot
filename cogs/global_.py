import discord
from discord.ext import commands
import sqlite3
from .Modules.paginator import*

class Global(commands.Cog):

    def __init__(self, client):
        self.client = client
        self.db = sqlite3.connect("Data/database.db")

    @commands.Cog.listener()
    async def on_ready(self):
        print("Bot is ready")

    @commands.Cog.listener()
    async def on_member_join(self, member):
        pass

    @commands.command(brief='Command to get latency of bot.')
    async def ping(self,ctx):
        await ctx.send("Pong!")
        
    @commands.command(brief='Command to set prefix of bot.')
    async def prefix(self, ctx, *, prefix = "."):
        with open('Configuration/server_setting.json', "r") as json_file:
            data = json.load(json_file)
            data["prefix"] = prefix
        
        with open('Configuration/server_setting.json', "w") as json_file:
            json_file.write(json.dumps(data))

        await ctx.send(f"New prefix will be {prefix}")
        

    @commands.command(aliases=['s'], brief='Command to shutdown the bot.')
    async def shutdown(self,ctx):
        if ctx.message.author.id == 450259740153479189:
            await ctx.send("Bot shuting down.")
            exit(-1)
        else:
            await ctx.send("Missing permissions.")
    
    @commands.Cog.listener()
    async def on_raw_reaction_add(self, event):
        await paginator_edit(event, self.client)

    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
        await ctx.send("An error occured when using this command.")
        await ctx.send("```"+str(error)+"```")


            
def setup(client):
    client.add_cog(Global(client))




    
    

