#this is what the tutorial is telling me that i should do

import os
import discord
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')

client = commands.Bot(command_prefix="r ")

@client.event
async def on_ready():
    print ("Bot is ready")


@client.command()
async def hello(ctx):
    await ctx.send("Hi, My name is Reggie!")

client.run(TOKEN)