#ReggieBot.py
#This is my bot for my personal server named after the infamous mouse/rat, Reggie.

#imports
import os #for dotenv support among other things.
import random #for randomisation and random number generation.
import discord #imports the discord bot library? (is library the correct term?) it's the discord stuff idk.
from discord.ext import commands #adds the ability for the discord bot to respond to commands I believe.
from dotenv import load_dotenv #adds dotenv so that I can store important variables that may have to be updated often in another file.
placeholder = "YOU FORGOT SOMETHING DUMBDUMB"#using this as placeholder var for useless print statements

#music bot stuff
from discord.ext import tasks
import youtube_dl
from random import choice
from discord.voice_client import VoiceClient

################################
#####YOUTUBEDL CONFIG STUFF#####
################################
#I don't have any idea what this is doing, but a guy on the
youtube_dl.utils.bug_reports_message = lambda: ''

ytdl_format_options = {
    'format': 'bestaudio/best',
    'outtmpl': '%(extractor)s-%(id)s-%(title)s.%(ext)s',
    'restrictfilenames': True,
    'noplaylist': True,
    'nocheckcertificate': True,
    'ignoreerrors': False,
    'logtostderr': False,
    'quiet': True,
    'no_warnings': True,
    'default_search': 'auto',
    'source_address': '0.0.0.0' # bind to ipv4 since ipv6 addresses cause issues sometimes
}

ffmpeg_options = {
    'options': '-vn'
}

ytdl = youtube_dl.YoutubeDL(ytdl_format_options)

class YTDLSource(discord.PCMVolumeTransformer):
    def __init__(self, source, *, data, volume=0.5):
        super().__init__(source, volume)

        self.data = data

        self.title = data.get('title')
        self.url = data.get('url')

    @classmethod
    async def from_url(cls, url, *, loop=None, stream=False):
        loop = loop or asyncio.get_event_loop()
        data = await loop.run_in_executor(None, lambda: ytdl.extract_info(url, download=not stream))

        if 'entries' in data:
            # take first item from a playlist
            data = data['entries'][0]

        filename = data['url'] if stream else ytdl.prepare_filename(data)
        return cls(discord.FFmpegPCMAudio(filename, **ffmpeg_options), data=data)
####YOUTUBEDL CONFIG ENDS####






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
    print ("Bot is online")



###MODERATION COMMANDS###

####UNTESTED####
###KICK###
#Kicks the user specified if the user of the bot has permissions to do so.
#it also sends a direct message to the person kicked.
@client.command()
@commands.has_permissions(kick_members=True)
async def kick(ctx, member : discord.Member,*, reason= "No reason given"):
    await member.send("You have been kicked from a server! Reason: " + reason)
    await ctx.send(member + " has been kicked from the server! Reason: " + reason)

####UNTESTED####
###BAN###
#Bans the user specified if the user of the bot has permissions to do so.
#it also sends a direct message to the person banned.
@client.command()
@commands.has_permissions(ban_members=True)
async def ban(ctx, member : discord.Member,*, reason= "No reason given"):
    await member.send("You have been banned from a server! Reason: " + reason)
    await ctx.send(member + " has been banned from the server! Reason: " + reason)

##############
###Statuses###
##############
#I want to write a sytem to change the status of the bot every hour or so, and that will go here.
#put bot statuses in here
status = ["teststatus1","teststatus2","teststatus3"]




#music stuff
queue = []

@client.command(name='join', help='This command makes the bot join the voice channel')
async def join(ctx):
    if not ctx.message.author.voice:
        await ctx.send("You are not connected to a voice channel")
        return
    
    else:
        channel = ctx.message.author.voice.channel

    await channel.connect()

@client.command(name='queue', help='This command adds a song to the queue')
async def queue_(ctx, url):
    global queue

    queue.append(url)
    await ctx.send(f'`{url}` added to queue!')

@client.command(name='remove', help='This command removes an item from the list')
async def remove(ctx, number):
    global queue

    try:
        del(queue[int(number)])
        await ctx.send(f'Your queue is now `{queue}!`')
    
    except:
        await ctx.send('Your queue is either **empty** or the index is **out of range**')
        
@client.command(name='play', help='This command plays songs')
async def play(ctx):
    global queue

    server = ctx.message.guild
    voice_channel = server.voice_client

    async with ctx.typing():
        player = await YTDLSource.from_url(queue[0], loop=client.loop)
        voice_channel.play(player, after=lambda e: print('Player error: %s' % e) if e else None)

    await ctx.send('**Now playing:** {}'.format(player.title))
    del(queue[0])

@client.command(name='pause', help='This command pauses the song')
async def pause(ctx):
    server = ctx.message.guild
    voice_channel = server.voice_client

    voice_channel.pause()

@client.command(name='resume', help='This command resumes the song!')
async def resume(ctx):
    server = ctx.message.guild
    voice_channel = server.voice_client

    voice_channel.resume()

@client.command(name='view', help='This command shows the queue')
async def view(ctx):
    await ctx.send(f'Your queue is now `{queue}!`')

@client.command(name='leave', help='This command stops makes the bot leave the voice channel')
async def leave(ctx):
    voice_client = ctx.message.guild.voice_client
    await voice_client.disconnect()

@client.command(name='stop', help='This command stops the song!')
async def stop(ctx):
    server = ctx.message.guild
    voice_channel = server.voice_client

    voice_channel.stop()





client.run(envTOKEN)