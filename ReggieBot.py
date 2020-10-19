#ReggieBot.py
#This is my bot for my personal server, named after the infamous mouse, Reggie.

#imports
import os #for dotenv support
import discord #imports the discord bot library? (is library the correct term?)
from discord.ext import commands #adds the ability for the discord bot to respond to commands i believe.
from dotenv import load_dotenv #adds dotenv so that I can store important variables that may have to be updated often in another file.
#i believe there is also security benefits to using this for the bot token and such things but that's just what the tutorial said.

#assigns the discord bot token and Guild name from the .env file to variables TOKEN and GUILD. (all variables from dotenv use uppercase)
#not sure why i need a GUILD variable, I don't remember why I put this here. Maybe to check it against the server name and make sure it's connected to the correct one?
load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')

#sets the bot's command prefix, this is what has to be put first in the text for the bot to know it has to respond to it.
#also does some voodoo magic that i found in a youtube comment to allow the bot to see when users join and leave or something idk.
intents = discord.Intents(messages = True, guilds = True, reactions = True, members = True, presences = True)
client = commands.Bot(command_prefix="r ", intents = intents)

#an event that runs when the bot has finished getting ready.
@client.event
async def on_ready():
    print ("Bot is ready")


#hello command. The bot will respond with "Hi, My name is Reggie!" when someone says "r hello."
@client.command()
async def hello(ctx):
    await ctx.send("Hi, My name is Reggie!")

#"r ping" will report the ping of the bot in milliseconds.
@client.command()
async def ping(ctx):
    await ctx.send(f'my ping is {round(client.latency * 1000)} ms')

#prints to the terminal whenever a user enters the server, don't really know why I have this here.
@client.event
async def on_member_join(member):
    print(f'{member} Has joined the server, That\'s poggers!')

#prints to the terminal whenever a user leaves the server, also don't know why i would need this, but it is here.
@client.event
async def on_member_remove(member):
    print(f'{member} has left the server, Not poggers.')

#starts the bot running i think, this likely needs to stay at the bottom.
client.run(TOKEN)