
import os #used to access .env file 
#DISCORD IMPORTS
###########################
import discord

import discord.ext
from discord.ext import commands
###############################


intents = discord.Intents.all()
intents.members = True
bot = commands.Bot(command_prefix='!',intents=intents)
#--------------------EVENTS--------------------------
@bot.event
async def on_ready():
 pass #do nothing for now (add any code you want to run when the bot boots here)

@bot.event
async def on_message(message):
  #Statements that execute when a message is sent in a server(guild), the bot is in
  await bot.process_commands(message)
@bot.event
async def on_member_join(member):
  #Statements that execute when someone joins a server the bot is in
  pass

#Get the bot latency(ping)
@bot.command()
async def ping(ctx):
    await ctx.send((str((bot.latency*1000))) + "ms")









#RUN BOT



#get the token from .env 
TOKEN=os.environ.get("DISCORD_BOT_SECRET")
bot.run(TOKEN)
