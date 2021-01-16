import discord
from discord.ext import commands


#  make a text file with token.txt as name and put your bot token in there
#  and put that file in your .gitignore file, otherwise you will get issues with the bot
#   also we can both run the scripts for different bots then
token = open("token.txt", "r").read()

prefix = "-"

client = commands.Bot(command_prefix=prefix)

@client.event #this gets called when the bot is ready
async def on_ready():
    print("bot is ready!")

@client.command()
async def ping(ctx):
    await ctx.send("pong")

client.run(token) 