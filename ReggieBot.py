#ReggieBot.py
#Lucas McFarlane
#This is my bot for my personal server named after the infamous mouse/rat, Reggie.

#IMPORTS#
import os   #A requirement of "dotenv."
import time    #don't know if i am using this anywhere right now, but it will be useful, so it's here.
import praw       #allows me to get images from reddit.
import random        #Allows for random number generation.
import discord          #Imports the Discord bot API.
import asyncio             #A requirement for the youtube_dl config section. works without, but throws an error.
import youtube_dl             #Allows for downloading of YouTube videos to play them back as music.
from random import choice        #Not sure what this does but something I copied from the internet is using it. (Thanks RKCoding!)
from dotenv import load_dotenv      #Allows for storing the bot token in a seperate file which is not uploaded to github. For obvious reasons, you do not want your token posted on github publicly.
from discord.ext import commands,tasks #"commands" allows for the bot to recieve commands from server users, "tasks" allows the bot to run scheduled tasks, such as changing the bot status on a timer.
from youtube_search import YoutubeSearch  #Allows for the bot to search YouTube for videos, meaning the bot does not require direct links to play music.
from discord.voice_client import VoiceClient #Allows the bot to enter voice calls and broadcast audio.

placeholder=("PLACEHOLDER VALUE") #it's a placeholder value.
queue = [] #A global variable to store the music queue.
globalserver = None
aplayrunning = False

#Assigns the discord bot token and guild name from the .env file to variables envTOKEN and envGUILD respectively.
#I'm not sure why i need the envGUILD variable, but i'm just not going to touch it for now.
load_dotenv()
envTOKEN = os.getenv('DISCORD_TOKEN')
envGUILD = os.getenv('DISCORD_GUILD')
envPRAWPASSWORD = os.getenv('REDDIT_PASSWORD')

#Sets the bot's command prefix, this is what the discord user has to put before the command they wish to run
#Example, "r hello" will have the bot return "Hi, My name is Reggie!"
client = commands.Bot(command_prefix="r ")

reddit = praw.Reddit(client_id ="tY1SNZGWr-x6GA" , client_secret ="FFQKlHaU0gJyFbvtCuPRQucQaaQ" , username = "Yomiko_ReggieBot", password=envPRAWPASSWORD, user_agent ="reggiebot" )

#This is some code that i saw in a YouTube video that allowed for kick and ban commands to function properly.
#The issue is that using is causes issues with the code for music playback. I will have to sort it out later, but for now there are limited moderation commands.
##intents = discord.Intents(messages = True, guilds = True, reactions = True, members = True, presences = True)
##client = commands.Bot(command_prefix="r ", intents = intests.)

#Event that will run once the bot is fully ready, printing a line to the terminal.
#Also starts looping tasks
@client.event
async def on_ready():
    change_status.start()
    print ("Bot is ready")


#############################
###General Speech Commands###
#############################
#basic commands that simply return strings of text to the user.
#These are here just for fun, and will likely be used once and then never again.


###WELCOME SPEECH###
#Gives the bot's welcome speech.
@client.command()
async def welcomespeech(ctx):
    await ctx.send("**Hi, My name is Reggie! I am your server's new bot!**")
    await ctx.send("**You can find more information about me at:**\n https://github.com/Yomiko12/ReggieBot")


###HELLO###
#Simple command that returns "Hi, My name is Reggie!" to the channel.
@client.command()
async def hello(ctx):
    await ctx.send("Hi, My name is Reggie!")


###FLIPCOIN###
#Randomly chooses heads or tails and returns the output to the channel.
@client.command()
async def flipcoin(ctx):
    i = random.randint(1,2)
    if (i == 1):
        await ctx.send("Heads!")
    else:
        await ctx.send("Tails!")


###SEX### (NSFW ONLY)
#reggie will sex the user
@client.command()
async def sex(ctx):
    await ctx.send("We are sexing now.\nKinda poggers.")


###THREATEN###
#Allows the user to put in a user's name and recieve a customised message from reggie threatening them.
@client.command()
async def threaten(ctx,*,user):
    i = random.randint(0,4)
    j= [
        "You're gonna die or something maybe",
        "You're dumb and stuff",
        "You're an idiot head",
        "Nobody asked",
        "Not gonna lie, You kinda suck"
    ]
    await ctx.send(f'{j[i]}, {user}!')


###POGCHAMP###
#Selects a random gif of a character doing the fortite default dance and sends it to the channel.
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
    await ctx.send(j[i])

###ASKREGGIE###
#Ask reggie a question and get a randomised response.
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


###MSGFROMREGGIE###
#This command sends a direct message to the user specified.
@client.command()
async def msgfromreggie(ctx, member : discord.Member,*, msg_content= "Hi, My name is Reggie!"):
    await member.send(f'{msg_content}')
    await ctx.send("Message delivered!")


###LOVECALC###
#Returns a percentage value of love compatibility
@client.command()
async def lovecalc(ctx, user1, user2, *,forcepercent=-2):
    try:
        forcepercent = int(forcepercent)
    except:
        await ctx.send("You broke something!")
        return

    if (forcepercent>-1):
        i=forcepercent
        await ctx.send(f'Your love compatibility is {i}%! (what a surprise!)')
    else:
        i = random.randint(1,100)
        await ctx.send(f'Your love compatibility is {i}%!')


###OWO###
#literally just prints "OwO"
@client.command()
async def owo(ctx):
    await ctx.send("OwO")

###UWU###
#literally just prints "UwU"
@client.command()
async def uwu(ctx):
    await ctx.send("UwU")


###PPSIZE### (NSFW ONLY)
#returns the user's pp size
@client.command()
async def ppsize(ctx):
    i="8"
    j=random.randint(1,15)
    for k in range(j):
        i+="="
        
    i+="D"
    await ctx.send(i)

    if (j > 10):
        await ctx.send("NICE!")
    elif (j>5 and j<=10):
        await ctx.send("Not too bad!")
    else:
        await ctx.send("That's pretty rough...")
    print(k)#don't ask


###RATE###
#rates whatever is sent to the bot randomly
@client.command()
async def rate(ctx):
    i=random.randint(0,9)
    j = [
        "1-10, ew.",
        "2-10, icky.",
        "3-10, meh.",
        "4-10, eh, alright i guess..",
        "5-10, Not horrible...",
        "6-10, It's alright",
        "7-10, Pretty good",
        "8-10, Very good",
        "9-10, Hella good",
        "10-10, UNBELIEVABLY POGGERS",
    ]
    await ctx.send(j[i])

#########################
###MODERATION COMMANDS###
#########################
#this is for any command that can even slightly be related to server moderation.


###PINGSPAM###
#Spams the chosen user with 5 pings.
@client.command()
async def pingspam(ctx, user):
    for i in range(5):
        await ctx.send(user + "\n")
        print(i) #only here to stop the warning i don't know how to fix rn


###CLEAR###
#this command will clear the specifid amount of posts that the user requests
@client.command()
async def clear(ctx, amount=2):
    await ctx.channel.purge(limit=amount)
###WARNING###
#The above command is not complete.
#There are no restrictions as to who can run this command, it should only be for users with the permission to manage messages.


###PING###
#Reports the bot's ping to the user.
@client.command()
async def ping(ctx):            ##Does "round()" round a number to the nearest integer value? because if so, that's pretty damn useful.
    await ctx.send(f'my ping is {round(client.latency * 1000)} ms')


##On_Member_Join##
#sends a message to the chat channel whenever a new user joins the server.
@client.event
async def on_member_join(member):
    channel = discord.utils.get(member.guild.channels, name='chat')
    await channel.send(f'Howdy partner!')



##On_Member_Remove##
#prints to the terminal whenever a user leaves the server
@client.event
async def on_member_remove(member):
    print(f'{member} has left the server, Not poggers.')
###WARNING###
#Requires modification based on the code above, this only sends a message to terminal and not the server itself.


###YTSEARCH###
#searches youtube and returns the first result to the channel.
#only implemented because i needed to figure out how it worked so that i could use it in the queue command for music.
@client.command()
async def ytsearch(ctx,*,search):
    await ctx.send("Searching...")
    results = YoutubeSearch(search, max_results=1).to_dict()
    for item in results:
        video_url= ("https://www.youtube.com"+item['url_suffix'])
        await ctx.send(video_url)



###########
###MUSIC###
###########
#This is all of the code that the bot requires to play music in the server.
#it is currently in an unfinished state, and requires the following changes:

#REQUIRED IMPLEMENTATIONS
#bot must leave after a certain amount of inactivity
#bot must auto erase old webm files. (low priority rn as it can be done manually.)
#must fix the "bot is typing" issues. They appear in an incorrect context most times, and do not appear when it would be useful for it to happen.
#all of the music commands were messily thrown together, and they could all use much work at some point. (especially the aplay system)
##########################


###MUSIC BOT PASTE###
#The following is a direct copy paste from an RKCoding YouTube tutorial where he says he doesn't know what it does but i need it. Idk where he got it from.

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
###MUSIC BOT PASTE ENDS


###JOIN###
#makes the bot join the voice channel of the user.
@client.command()
async def join(ctx):

    if not ctx.message.author.voice:
        await ctx.send("You are not connected to a voice channel")
        return
    else:
        channel = ctx.message.author.voice.channel
        await channel.connect()


###Q (QUEUE)###
#This command is a big ol' mess.
#if the command is being run with nothing currently playing, it will start the first song. otherwise, it will just add it to queue.
#it also handles searching youtube for the song if a link is not sent.
@client.command()
async def q(ctx,*, url):
    global queue
    global globalserver
    global aplayrunning
    server = ctx.message.guild
    globalserver = ctx.message.guild
    queuestartlen=len(queue)
    if (aplayrunning==False):
        aplay.start()
        aplayrunning = True

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
###WARNING###
#This command is a big ol' mess and it totally throws errors all of the time
#it does work though, but maybe fix it sometime.


###REMOVE###
#removes the song that the user specifies from the queue.
@client.command()
async def remove(ctx, number):
    global queue
    try:
        del(queue[int(number+1)])
        await ctx.send("**Song removed!**")
    except:
        await ctx.send('**Your queue is either** ***empty*** **or the index is** ***out of range***')
   
###QPLAY###
#plays the first song in the queue, downloading it if not already done, and deletes it from queue.
@client.command()
async def qplay(ctx):
    global queue
    server = ctx.message.guild
    voice_channel = server.voice_client

    async with ctx.typing(): #fix these damn typing sections sometime!!!
        player = await YTDLSource.from_url(queue[0], loop=client.loop)
        voice_channel.play(player, after=lambda e: print('Player error: %s' % e) if e else None)

    await ctx.send('**Now playing:** {}'.format(player.title))
    del(queue[0])


###PAUSE###
#pauses the current song
@client.command()
async def pause(ctx):
    server = ctx.message.guild
    voice_channel = server.voice_client
    voice_channel.pause()


###RESUME###
#resumes the current song
@client.command()
async def resume(ctx):
    server = ctx.message.guild
    voice_channel = server.voice_client
    voice_channel.resume()


###QLIST###
#returns a list of all items currently in the queue.
@client.command()
async def qlist(ctx):
    i=0
    await ctx.send("**QUEUE:**")
    for item in queue:
        i+=1
        if 'youtube.com/' in queue[i-1]:
            await ctx.send(f'{i}: <{item}>')


###LEAVE###
#makes the bot leave whatever voice channel it is in.
@client.command()
async def leave(ctx):
    global aplayrunning
    await ctx.send("**Leaving...**")
    if (aplayrunning == True):
        aplay.stop()
        time.sleep(5)
        aplayrunning == False

    voice_client = ctx.message.guild.voice_client
    await voice_client.disconnect()


###STOP###
#stops the bot from playing whatever it's playing.
@client.command()
async def stop(ctx):
    server = ctx.message.guild
    voice_channel = server.voice_client
    voice_channel.stop()

###SKIP###
#literally just runs the stop command followed by the play command.
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

@client.command()
async def killaplay(ctx):
    aplay.stop()

###########################
###REDDIT POST RETRIEVAL###
###########################
#this is for anything that requires getting information from reddit.
#only one command in here right now, because it covers all reddit post retrieval needs.


###REDDIT###
#gets a random post from the hot top 100 from the chosen subreddit.
@client.command()
async def r(ctx, sub):
    await ctx.send("**Searching...**")
    postlist = []
    try:
        subreddit = reddit.subreddit(f'{sub}')
        hot = subreddit.hot(limit=50)
        for submission in hot:
            if not submission.stickied:
                postlist.append(submission.title)
                postlist.append(submission.author)
                postlist.append(submission.url)

        i=len(postlist)
        j = random.randint(0, (i/3)-1)
        await ctx.send(f'**{postlist[j*3]}**')
        await ctx.send(f'**Post by: u/{postlist[(j*3)+1]}**')
        await ctx.send(f'{postlist[(j*3)+2]}')
    except:
        await ctx.send("**Something went wrong, check the subreddit name?**")
        

###################
###LOOPING TASKS###
###################
#this is where all loping tasks are placed.

##STATUS##
#Changes the bot's status once an hour.
status = ["Doki Doki Literature Club","Huniepop","Minecraft", "Roblox"]
@tasks.loop(seconds=1200)
async def change_status():
    await client.change_presence(activity=discord.Game(choice(status)))


##APLAY##
#The autoplayer loop for the music commands. It really should not be done this way, but too bad.
@tasks.loop(seconds=5)
async def aplay():
    global queue
    server = globalserver
    voice_channel = server.voice_client

    try:
        player = await YTDLSource.from_url(queue[0], loop=client.loop)
        voice_channel.play(player, after=lambda e: print('Player error: %s' % e) if e else None)
        del(queue[0])
    except:
        print("aplay_running")


#End (yeehaw)
client.run(envTOKEN)