import discord
from discord.ext import commands


token = "[TOKEN HERE]"
prefix = "-"

client = commands.Bot(command_prefix=prefix)

@client.event #this gets called when the bot is ready
async def on_ready():
    print("bot is ready!")

client.run(token) #this line has to be at the end of the code