from webs import keep_alive #webserver
import os #used to access .env file 
#DISCORD IMPORTS
###########################
import discord

import discord.ext
from discord.ext import commands
###############################


intents = discord.Intents.default()
intents.members = True
bot = commands.Bot(command_prefix='!',intents=intents)
#--------------------EVENTS--------------------------
@bot.event
async def on_ready():
  #Statements that execute when  the bot boots.
  print("") # do nothing but enough not to cause an error

@bot.event
async def on_message(message):
  #Statements that execute when a message is sent in a server(guild), the bot is in
  print(message.content)
@bot.event
async def on_member_join(member):
  #Statements that execute when someone joins a server the bot is in
  print(str(member))


#--------------------COMMANDS--------------------------  
@bot.command()
async def ping(ctx):
    await ctx.send((str((bot.latency*1000))) + "ms")







#----------------------RUN BOT CODE-------------------------



#keep the bot online         
keep_alive()
#get the token from .env 
TOKEN=os.environ.get("DISCORD_BOT_SECRET")
bot.run(TOKEN)
