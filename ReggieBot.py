#ReggieBot.py
#This is my bot for my personal server named after the infamous mouse/rat, Reggie.

#imports
import os #for dotenv support among other things.
import random #for randomisation and random number generation.
import discord #imports the discord bot library? (is library the correct term?) it's the discord stuff idk.
from discord.ext import commands #adds the ability for the discord bot to respond to commands I believe.
from dotenv import load_dotenv #adds dotenv so that I can store important variables that may have to be updated often in another file.
placeholder = "YOU FORGOT SOMETHING DUMBDUMB"#using this as placeholder var for useless print statements
#i believe there is also security benefits to using this for the bot token and such things but that's just what the tutorial said.

#assigns the discord bot token and Guild name from the .env file to variables TOKEN and GUILD. (all variables from dotenv use uppercase)
#not sure why i need a GUILD variable, I don't remember why I put this here. Maybe to check it against the server name and make sure it's connected to the correct one?
load_dotenv()
envTOKEN = os.getenv('DISCORD_TOKEN')
envGUILD = os.getenv('DISCORD_GUILD')

#sets the bot's command prefix, this is what has to be put first in the text for the bot to know it has to respond to it.
#also does some voodoo magic that i found in a youtube comment to allow the bot to see when users join and leave or something idk.
intents = discord.Intents(messages = True, guilds = True, reactions = True, members = True, presences = True)
client = commands.Bot(command_prefix="r ", intents = intents)

#an event that runs when the bot has finished getting ready.
@client.event
async def on_ready():
    print ("Bot is ready")



#############################
###General Speech Commands###
#############################

###HELLO###
#prints "Hi, My name is Reggie!" when the user sends "r hello"
@client.command()
async def hello(ctx):
    await ctx.send("Hi, My name is Reggie!")

###FLIPCOIN###
#prints "Heads" or "Tails" randomly when asked "r flipcoin"
@client.command()
async def flipcoin(ctx):
    i = random.randint(1,2) #picks one or two randomly
    if (i == 1):#prints heads if 1 and vise versa
        await ctx.send("Heads!")
    else:
        await ctx.send("Tails!")

###SEX###
#reggie will sex the user
@client.command()
async def sex(ctx):
    await ctx.send("We are sexing now.\nKinda poggers.")

###WIP (needs to do stuff)###
#THREATEN
#allows the user to put in a user's name and recieve a customised message from reggie threatening them
@client.command()
async def threaten(ctx):
    print(placeholder)

###POGCHAMP###
#selects a random gif of a character doing the fortite default dance
@client.command()
async def pogchamp(ctx):
    i = random.randint(0,6)
    j=[
        "https://tenor.com/view/shrek-dance-fortnite-fortnite-default-dance-shrek-dance-gif-15809394",
        "https://tenor.com/view/default-dance-epic-win-victory-royale-dank-gif-14897370",
        "https://tenor.com/view/goose-default-dance-dancing-dance-moves-feeling-good-gif-16364185",
        "https://tenor.com/view/mario-cool-dance-yahoo-super-mario-gif-12778263",
        "https://tenor.com/view/baldi-fortnite-fortnite-dance-gif-12747343",
        "https://tenor.com/view/shaggy-default-dance-victory-gif-14972422",
        "https://tenor.com/view/minecraft-fortnite-default-dance-funny-steve-gif-13329851"
    ]
    await ctx.send(env[i])

###ASKREGGIE###
#ask reggie a question and get a randomised response
@client.command()
async def askreggie(ctx):
    i = random.randint(0,12)
    j = [
        "YES!!",
        "OF COURSE!!",
        "Yea, probably..",
        "idk..",
        "Maybe..",
        "It's possible..",
        "What kind of question is this?? There must be something seriously wrong with you.",
        "Bruh...",
        "I'm Reggie!",
        "NO!!",
        "Bruh, there is no way..",
        "Nahhh..",
        "FEMBOYS!!"
    ]
    await ctx.send(j[i])



#########################
###MODERATION COMMANDS###
#########################

###PINGSPAM###
#does what is says it does
@client.command()
async def pingspam(ctx, user):
    for i in range(5):
        await ctx.send(user + "\n")

#WIP (Needs restrictions for users with low permissions)
###CLEAR###
#this command will clear the specifid amount of posts that the user requests
@client.command()
async def clear(ctx, amount=2):
    await ctx.channel.purge(limit=amount)

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
client.run(envTOKEN)