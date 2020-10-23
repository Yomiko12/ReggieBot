#ReggieBot.py
#This is my bot for my personal server named after the infamous mouse/rat, Reggie.
#credit to RKCoding (I modified his code): https://github.com/RK-Coding/Videos/blob/master/rkcodingmusic.py

#imports
import os #for dotenv support among other things.
import random #for randomisation and random number generation.
import discord #imports the discord bot library? (is library the correct term?) it's the discord stuff idk.
from discord.ext import commands, tasks #adds the ability for the discord bot to respond to commands I believe.
from dotenv import load_dotenv #adds dotenv so that I can store important variables that may have to be updated often in another file.
placeholder = "YOU FORGOT SOMETHING DUMBDUMB"#using this as placeholder for when a function isn't finished but needs something in it so it doesn't complain.
import asyncio #the music bot config was whining about not having this import even though it doesn't need it, that's the only reason it's here.


#music bot stuff


from discord.voice_client import VoiceClient
import youtube_dl

from random import choice

from youtube_search import YoutubeSearch

queue = []

#assigns the discord bot token and Guild name from the .env file to variables TOKEN and GUILD. (all variables from dotenv use uppercase)
#not sure why i need a GUILD variable, I don't remember why I put this here. Maybe to check it against the server name and make sure it's connected to the correct one?
load_dotenv()
envTOKEN = os.getenv('DISCORD_TOKEN')
envGUILD = os.getenv('DISCORD_GUILD')

#sets the bot's command prefix, this is what has to be put first in the text for the bot to know it has to respond to it.
#also does some voodoo magic that i found in a youtube comment to allow the bot to see when users join and leave or something idk.
#intents = discord.Intents(messages = True, guilds = True, reactions = True, members = True, presences = True)
#client = commands.Bot(command_prefix="r ", intents = intents)
client = commands.Bot(command_prefix="r ")


###MSG_FROM_REGGIE###
#This command sends a direct message to the user specified.
@client.command()
async def msgfromreggie(ctx, member : discord.Member,*, msg_content= "Hi, My name is Reggie!"):
    await member.send(f'{msg_content}')
    await ctx.send("Message delivered!")

###ANON_MSG_FROM_REGGIE###
#you get the idea.



####UNTESTED####
###KICK###
#Kicks the user specified if the user of the bot has permissions to do so.
#it also sends a direct message to the person kicked.
@client.command()
@commands.has_permissions(kick_members=True)
async def kick(ctx, member : discord.Member,*, reason= "No reason given"):
    await member.send("You have been kicked from a server! Reason: " + reason)
    await ctx.send(member + " has been kicked from the server! Reason: " + reason)
    await member.kick(reason=reason)

####UNTESTED####
###BAN###
#Bans the user specified if the user of the bot has permissions to do so.
#it also sends a direct message to the person banned.
@client.command()
@commands.has_permissions(ban_members=True)
async def ban(ctx, member : discord.Member,*, reason= "No reason given"):
    await member.send(f'You have been banned from a server! Reason: {reason}')
    await ctx.send(f'{str(member)} has been banned from the server! Reason: {reason}')
    await member.ban(reason=reason)
##############
###Statuses###
##############
#I want to write a sytem to change the status of the bot every hour or so, and that will go here.
#put bot statuses in here




##########
#MUSIC BOT PASTE
##########

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



@client.event
async def on_ready():
    change_status.start()
    print('Bot is online!')

@client.event
async def on_member_join(member):
    channel = discord.utils.get(member.guild.channels, name='general')
    await channel.send(f'Welcome {member.mention}!  Ready to jam out? See `?help` command for details!')


###MUSIC SHIT###

@client.command(name='join', help='This command makes the bot join the voice channel')
async def join(ctx):
    if not ctx.message.author.voice:
        await ctx.send("You are not connected to a voice channel")
        return
    
    else:
        channel = ctx.message.author.voice.channel

    await channel.connect()



@client.command()
async def q(ctx,*, url):
    global queue
    server = ctx.message.guild
    queuestartlen=len(queue)

    if "https://www.youtube." in url:
        queue.append(url)
        await ctx.send(f'`{url}` added to queue!')

    else:
        await ctx.send("searching YouTube...")
        results = YoutubeSearch(url, max_results=1).to_dict()
        for item in results:
            video_url= ("https://www.youtube.com"+item['url_suffix'])
        for item in results:
            video_title=(item['title'])

        queue.append(video_url)
        await ctx.send(f'{video_url}: ({video_title}) added to queue!')

    queueendlen=len(queue)

    if (queuestartlen<queueendlen):
        await ctx.send("**Starting download...**")
        async with ctx.typing():
            player = await YTDLSource.from_url(queue[int(len(queue))-1], loop=client.loop)
            print(player)
            await ctx.send("**ready**")

        if (len(queue) == 1): #this still throws errors because the queue is shortened the moment something starts playing,
            # so the queue will once again be len 1, but it works so leave it alone lol
            server = ctx.message.guild
            voice_channel = server.voice_client

            async with ctx.typing():
                player = await YTDLSource.from_url(queue[0], loop=client.loop)
                voice_channel.play(player, after=lambda e: print('Player error: %s' % e) if e else None)

            await ctx.send('**Now playing:** {}'.format(player.title))
            del(queue[0]) 

    else:
        ctx.send("No video found, download not started.")



@client.command(name='remove', help='This command removes an item from the list')
async def remove(ctx, number):
    global queue

    try:
        del(queue[int(number+1)])
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

@client.command()
async def qlist(ctx):
    i=0
    await ctx.send("**QUEUE:**")
    for item in queue:
        i+=1
        if 'youtube.com/' in queue[i-1]:
            await ctx.send(f'{i}: <{item}>')




@client.command(name='leave', help='This command stops makes the bot leave the voice channel')
async def leave(ctx):
    voice_client = ctx.message.guild.voice_client
    await voice_client.disconnect()

@client.command(name='stop', help='This command stops the song!')
async def stop(ctx):
    server = ctx.message.guild
    voice_channel = server.voice_client
    voice_channel.stop()


status = ["teststatus1","teststatus2","teststatus3"]
@tasks.loop(seconds=1200)
async def change_status():
    await client.change_presence(activity=discord.Game(choice(status)))


@client.command()
async def ytsearch(ctx,*,search):
    await ctx.send("Searching...")
    results = YoutubeSearch(search, max_results=1).to_dict()
    for item in results:
        video_url= ("https://www.youtube.com"+item['url_suffix'])
        await ctx.send(video_url)


#skip works equivalently to running stop and then play again, so that is what i am doing.
@client.command()
async def skip(ctx):
    #copy of stop command
    server = ctx.message.guild
    voice_channel = server.voice_client
    voice_channel.stop()

    #copy of play command
    global queue
    server = ctx.message.guild
    voice_channel = server.voice_client
    async with ctx.typing():
        player = await YTDLSource.from_url(queue[0], loop=client.loop)
        voice_channel.play(player, after=lambda e: print('Player error: %s' % e) if e else None)

    await ctx.send('**Now playing:** {}'.format(player.title))
    del(queue[0])


###########
client.run(envTOKEN)


#ideas for additions and things that need changed

#LOW PRIORITY
#bot leaves call after set time of inactivity
#automatic erasing of downloaded webm files after a period of time or at a certain time of day, idk figure it out at some point.
#message command dm's the requested user with the message requested
#fix the contexts in which the "bot is typing" thing is activated.

#HIGH PRIORITY
#bot must autoplay next song

#once the above and any other possible features are completed, merge with ReggieBot.py
