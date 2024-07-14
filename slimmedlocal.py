import discord
import discord.ext
from discord.ext import commands

intents = discord.Intents.all()
intents.members = True
bot = commands.Bot(command_prefix='!',intents=intents)

@bot.event
async def on_message(message):
  #Statements that execute when a message is sent in a server(guild), the bot is in
  await bot.process_commands(message)



#yes I know this is bad coding 
TOKEN=""
bot.run(TOKEN)
