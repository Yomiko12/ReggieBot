#ReggieBot.py
#Lucas McFarlane
#This is my bot for my personal server named after the infamous rat, Reggie.

#IMPORTS#
import os   #A requirement of "dotenv."
import time    #don't know if i am using this anywhere right now, but it will be useful, so it's here.
import praw       #allows me to get images from reddit.
import random        #Allows for random number generation.
import discord          #Imports the Discord bot API.
import asyncio             #A requirement for the youtube_dl config section. works without, but throws an error.
import datetime               #allows to check the current date for setting events and checking events.
import youtube_dl                #Allows for downloading of YouTube videos to play them back as music.
from random import choice           #Not sure what this does but something I copied from the internet is using it. (Thanks RKCoding!)
from dotenv import load_dotenv         #Allows for storing the bot token in a seperate file which is not uploaded to github. For obvious reasons, you do not want your token posted on github publicly.
from discord.ext import commands,tasks    #"commands" allows for the bot to recieve commands from server users, "tasks" allows the bot to run scheduled tasks, such as changing the bot status on a timer.
from youtube_search import YoutubeSearch     #Allows for the bot to search YouTube for videos, meaning the bot does not require direct links to play music.
from discord.voice_client import VoiceClient    #Allows the bot to enter voice calls and broadcast audio.

#global variable(s)
eventlist = []

#Assigns variables based on the .env file to keep passwords and sensitive info out of the github.
load_dotenv()
envTOKEN = os.getenv('DISCORD_TOKEN')
envPRAWPASSWORD = os.getenv('REDDIT_PASSWORD')
envPRAWSECRET = os.getenv('REDDIT_SECRET')

#sets the bots command prefix. This is what the user must put in front of whatever command they issue to the bot.
client = commands.Bot(command_prefix="r ")

#setup for the reddit bot.
reddit = praw.Reddit(client_id ="tY1SNZGWr-x6GA" , client_secret =envPRAWSECRET , username = "Yomiko_ReggieBot", password=envPRAWPASSWORD, user_agent ="reggiebot" )

#Event that will run once the bot is fully ready, printing a line to the terminal.
#This can also be used to start looping tasks that always run.
@client.event
async def on_ready():
    change_status.start()
    event_checker.start()
    print ("Bot is ready")


#############################
###General Speech Commands###
#############################
#basic commands that simply return strings of text to the user.
#These are here just for fun, and will likely be used once and then never again.

###WELCOME SPEECH###
#Gives the bot's welcome speech. and sends the Github page link
@client.command(help = "Reggie introduces himself and sends the github link")
async def welcomespeech(ctx):
    await ctx.send("**Hi, My name is Reggie! I am your server's new bot!**")
    await ctx.send("**You can find more information about me at:**\n https://github.com/Yomiko12/ReggieBot")


###HELLO###
#Simple command that returns "Hi, My name is Reggie!" to the channel.
@client.command(help = "Reggie introduces himself")
async def hello(ctx):
    await ctx.send("**Hi, My name is Reggie!**")


###FLIPCOIN###
#Randomly chooses heads or tails and returns the output to the channel.
@client.command(help = "Flips a coin")
async def flipcoin(ctx):
    i = random.randint(1,2)
    if (i == 1):
        await ctx.send("**Heads!**")
    else:
        await ctx.send("**Tails!**")


###SEX### (NSFW ONLY)
#reggie will sex the user
@client.command(help = "Reggie sexes you")
async def sex(ctx):
    await ctx.send("**We are sexing now.\nKinda poggers.**")


###INSULT###
#Allows the user to put in a user's name and recieve a customised message from reggie insulting them.
@client.command(help = "Reggie insults you")
async def insult(ctx,*,user):
    i = random.randint(0,4)
    j= [
        "**You're gonna die or something maybe",
        "**You're dumb and stuff",
        "**You're an idiot head",
        "**Nobody asked",
        "**Not gonna lie, You kinda suck"
    ]
    await ctx.send(f'{j[i]}, {user}!**')


###POGCHAMP###
#Selects a random gif of a character doing the fortite default dance and sends it to the channel.
@client.command(help = "Sends a random gif of someone pogging")
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
@client.command(help = "Allows you to ask Reggie a Question")
async def askreggie(ctx):
    i = random.randint(0,12)
    j = [
        "**YES!!**",
        "**OF COURSE!!**",
        "**Yea, probably..**",
        "**idk..**",
        "**Maybe..**",
        "**It's possible..**",
        "**wWhat kind of question is this?? There must be something seriously wrong with you.**",
        "**Bruh...**",
        "**I'm Reggie!**",
        "**NO!!**",
        "**Bruh, there is no way..**",
        "**Nahhh..**",
        "**FEMBOYS!!**"
    ]
    await ctx.send(j[i])


###MSGFROMREGGIE###
#This command sends a direct message to the user specified.
@client.command(help = "Sends a direct message to a user")
async def msgfromreggie(ctx, member : discord.Member,*, msg_content= "Hi, My name is Reggie!"):
    await member.send(f'{msg_content}')
    await ctx.send("**Message delivered!**")


###LOVECALC###
#Returns a percentage value of love compatibility
@client.command(help = "Calculates love between two people")
async def lovecalc(ctx, user1, user2, *,forcepercent=-2):
    try:
        forcepercent = int(forcepercent)
    except:
        await ctx.send("**You broke something!**")
        return

    if (forcepercent>-1):
        i=forcepercent
        await ctx.send(f'**Your love compatibility is {i}%! (what a surprise!)**')
    else:
        i = random.randint(1,100)
        await ctx.send(f'**Your love compatibility is {i}%!**')


###OWO###
#literally just prints "OwO"
@client.command(help = "OwO")
async def owo(ctx):
    await ctx.send("**OwO**")

###UWU###
#literally just prints "UwU"
@client.command(help = "UwU")
async def uwu(ctx):
    await ctx.send("**UwU**")


###PPSIZE### (NSFW ONLY)
#returns the user's pp size
@client.command(help = "Shows the users pp size")
async def ppsize(ctx):
    i="8"
    j=random.randint(1,15)
    for k in range(j):
        i+="="
        
    i+="D"
    await ctx.send(i)

    if (j > 10):
        await ctx.send("**NICE!**")
    elif (j>5 and j<=10):
        await ctx.send("**Not too bad!**")
    else:
        await ctx.send("**That's pretty rough...**")
    print(k)#don't ask

###GAYRATE###
#rates ur gayness
@client.command()
async def rategay(ctx, override = -1):
    i=random.randint(1, 100)
    if override>0:
        i=override
    await ctx.send(f"**Your gayness level is {i}%!**")

###RATE###
#rates whatever is sent to the bot randomly
@client.command(help = "Reggie will rate whatever you show him")
async def rate(ctx):
    i=random.randint(0,9)
    j = [
        "**1-10, ew.**",
        "**2-10, icky.**",
        "**3-10, meh.**",
        "**4-10, eh, alright i guess..**",
        "**5-10, Not horrible...**",
        "**6-10, It's alright**",
        "**7-10, Pretty good**",
        "**8-10, Very good**",
        "**9-10, Hella good**",
        "**10-10, UNBELIEVABLY POGGERS**",
    ]
    await ctx.send(j[i])



###REGGEPIC### (NSFW ONLY)
#randomly returns one of sixteen images of reggie.
@client.command(help = "Sends a picture of Reggie")
async def reggiepic(ctx):
    i=random.randint(0,15)
    j=[
        "https://cdn.discordapp.com/attachments/505177959686995978/770072831182241802/ElHl5HTU0AEPAme.png",
        "https://cdn.discordapp.com/attachments/505177959686995978/770072904682831874/Ek8OMOXVgAIXl39.png",
        "https://cdn.discordapp.com/attachments/505177959686995978/770073506385362944/EiDm2fhU8AEccTY.png",
        "https://cdn.discordapp.com/attachments/505177959686995978/770073521987911710/EgUVqa9WkAAFnQh.png",
        "https://cdn.discordapp.com/attachments/505177959686995978/770073786283851776/EfptiLtU4AA-t1r.png",
        "https://cdn.discordapp.com/attachments/505177959686995978/770073830184976384/EdLZa3HWAAElkq0.png",
        "https://cdn.discordapp.com/attachments/505177959686995978/770073907616808970/EgMLgjCUcAAhRtj.png",
        "https://cdn.discordapp.com/attachments/505177959686995978/770073958979993660/EdIrkfgUMAAnXtF.png",
        "https://cdn.discordapp.com/attachments/505177959686995978/770074156409815040/Ec0m5bFUwAAWDHA.png",
        "https://cdn.discordapp.com/attachments/505177959686995978/770074185208299630/unknown.png",
        "https://cdn.discordapp.com/attachments/505177959686995978/770074410689364048/unknown.png",
        "https://cdn.discordapp.com/attachments/505177959686995978/770074684582002748/unknown.png",
        "https://cdn.discordapp.com/attachments/505177959686995978/770074933518270485/EZHsOBdVAAExOkY.png",
        "https://cdn.discordapp.com/attachments/505177959686995978/770074992833462323/EYTvZOfXgAMqUwX.png",
        "https://cdn.discordapp.com/attachments/505177959686995978/770075316965998622/EX54hU7X0AcAIXV.png",
        "https://cdn.discordapp.com/attachments/505177959686995978/770075393687814174/EW8mhbkVcAAbeS5.png",
    ]
    await ctx.send(j[i])

###ITHINK###
#This is a very simple command that returns Reggie's personal belief
@client.command(help = "Reggie tells you his personal belief")
async def ithink(ctx,*,belief):
    await ctx.send(f"**It is my personal belief that {belief}.**")

###SETEVENT###
#Tool used to set a new event
@client.command(help = "Set a new event")
async def setevent(ctx, date, hour):
    global eventlist
    year = date[0:4]#parsing the strings to get year month and day variables, exclusing the "-"'s
    month = date[5:7]
    day = date[8:10]
    now = datetime.datetime.now()

    #Check all possible failiure states
    lengthchecker = (f"{year}{month}{day}{hour}")
    if len(lengthchecker)!=10:
        await ctx.send("**Make sure you entered that date and time value corrently!**")
    elif int(year)< int(now.year):
        await ctx.send("**Make sure that you entered a valid year!**")
    elif int(year) == int(now.year) and int(month) < int(now.month):
        await ctx.send("**Make sure that the date and time you entered is later than the current date and time!**")
    elif int(year) == int(now.year) and int(month) == int(now.month) and int(day)< int(now.day):
        await ctx.send("**Make sure that the date and time you entered is later than the current date and time!**")
    elif (int(hour) <0 or int(hour) >23):
        await ctx.send("**Make sure you entered a valid hour!**")

    else: #if all failiure checks pass...
        await ctx.send("**Updating events list...**")
        
        currentdir = os.path.dirname(os.path.abspath(__file__))#Code I stole from the internet because relative file path is broken or something idk
        eventstxt = os.path.join(currentdir, 'events.txt')
        events = open(eventstxt, "r+")

        #write all current events to list variable and clear the txt file
        eventlist = []
        eventlist = [line.strip() for line in events]
        events.close()
        open(eventstxt, 'w').close()
        
        # add the new event to the event list and sort the list
        eventlist.append(f"{year}{month}{day}{hour}")
        eventlist.sort()
        
        #print all currently scheduled events
        await ctx.send("**Currently scheduled events,**")
        for item in eventlist:
            year = item[0:4]#parsing the strings to get year month and day variables, exclusing the "-"'s
            month = item[4:6]
            day = item[6:8]
            hour = item[8:10]
            await ctx.send(f"{year}-{month}-{day} {hour}")#Can this be done better?

        #update the eventlist txt
        events = open(eventstxt, "r+")
        for item in eventlist:
            events.write("%s\n" % item)

        events.close()#close the event list
            



###VIEWEVENTS###
#some copied code from the above command that just prints all of the currently scheduled commands.
@client.command(help = "View Events")
async def viewevents(ctx):
    global eventlist
    #make sure that eventlist is up to date with the txt document if for some reason it isnt already.
    eventlist = []
    currentdir = os.path.dirname(os.path.abspath(__file__))#Code I stole from the internet because relative file path is broken or something idk
    eventstxt = os.path.join(currentdir, 'events.txt')
    events = open(eventstxt, "r+")
    #write all current events to list variable
    eventlist = []
    eventlist = [line.strip() for line in events]
    events.close()
    
    #print current events.
    await ctx.send("**Currently scheduled events,**")
    for item in eventlist:
            year = item[0:4]#parsing the strings to get year month and day variables, exclusing the "-"'s
            month = item[4:6]
            day = item[6:8]
            hour = item[8:10]
            await ctx.send(f"{year}-{month}-{day} {hour}")#Can this be done better?


###DELEVENT###
#deletes an event.
@client.command(help = "Delete an event")
async def delevent (ctx, date, hour):
    year = date[0:4]#parsing the strings to get year month and day variables, exclusing the "-"'s
    month = date[5:7]
    day = date[8:10]

    #check that date was formatted correctly
    lengthchecker = (f"{year}{month}{day}{hour}")
    if len(lengthchecker)!= 10:
        await ctx.send("**Make sure you entered that date and time value corrently!**")

    else:
        #make sure that eventlist is up to date with the txt document if for some reason it isnt already.
        eventlist = []
        currentdir = os.path.dirname(os.path.abspath(__file__))#Code I stole from the internet because relative file path is broken or something idk
        eventstxt = os.path.join(currentdir, 'events.txt')
        events = open(eventstxt, "r+")
        #write all current events to list variable
        eventlist = [line.strip() for line in events]
        events.close()

        userinput = (f"{year}{month}{day}{hour}")
        for item in eventlist:
            if item == userinput:
                while item in eventlist: eventlist.remove(item)

        eventlist.sort()
        #print all currently scheduled events
        await ctx.send("**Currently scheduled events,**")
        for item in eventlist:
            await ctx.send(item)#Can this be done better?

        #update the eventlist txt
        open(eventstxt, 'w').close()
        events = open(eventstxt, "r+")
        for item in eventlist:
            events.write("%s\n" % item)

        events.close()#close the event list


#########################
###MODERATION COMMANDS###
#########################
#this is for any command that can even slightly be related to server moderation.


###PINGSPAM###
#Spams the chosen user with 5 pings.
@client.command(help = "Spams a user with 5 pings")
async def pingspam(ctx, user):
    for i in range(5):
        await ctx.send(user + "\n")
        print(i) #only here to stop the warning i don't know how to fix rn


###CLEAR###
#this command will clear the specifid amount of posts that the user requests
@client.command(help = "Clears the specified amount of messages")
async def clear(ctx, amount=2):
    await ctx.channel.purge(limit=amount)
###WARNING###
#The above command is not complete.
#There are no restrictions as to who can run this command, it should only be for users with the permission to manage messages.


###PING###
#Reports the bot's ping to the user.
@client.command(help = "Returns Reggie's ping to the server")
async def ping(ctx):            ##Does "round()" round a number to the nearest integer value? because if so, that's pretty damn useful.
    await ctx.send(f'my ping is {round(client.latency * 1000)} ms')


##On_Member_Join##
#sends a message to the chat channel whenever a new user joins the server.
@client.event
async def on_member_join(member):
    channel = discord.utils.get(member.guild.channels, name='chat')
    await channel.send("**Howdy Partner!**")



##On_Member_Remove##
#prints to the terminal whenever a user leaves the server
@client.event
async def on_member_remove(member):
    channel = discord.utils.get(member.guild.channels, name='chat')
    await channel.send("**Why you leave? not poggers.**")
###WARNING###
#Requires modification based on the code above, this only sends a message to terminal and not the server itself.


###YTSEARCH###
#searches youtube and returns the first result to the channel.
#only implemented because i needed to figure out how it worked so that i could use it in the queue command for music.
@client.command(help = "Returns results of a youtube search")
async def ytsearch(ctx,*,search):
    await ctx.send("**Searching...**")
    results = YoutubeSearch(search, max_results=1).to_dict()
    for item in results:
        video_url= ("https://www.youtube.com"+item['url_suffix'])
        await ctx.send(video_url)



###########################
###REDDIT POST RETRIEVAL###
###########################
#this is for anything that requires getting information from reddit.
#only one command in here right now, because it covers all reddit post retrieval needs.

###REDDIT###
#gets a random post from the hot top 100 from the chosen subreddit.
@client.command(help = "Returns one of the top 50 hot posts on the chosen subreddit")
async def r(ctx, sub):
    await ctx.send("**Searching...**")
    try:
        postlist = []
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
        await ctx.send("**Something went wrong, maybe check your spelling?**")



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

##EVENTCHECKER##
#checks if an event in eventlist should be celebrated and does if it is
@tasks.loop(seconds = 300)
async def event_checker():
    currentdir = os.path.dirname(os.path.abspath(__file__))#Code I stole from the internet because relative file path is broken or something idk
    eventstxt = os.path.join(currentdir, 'events.txt')
    events = open(eventstxt, "r+")
    global eventlist
    #write all current events to list variable and clear the txt file
    eventlist = []
    eventlist = [line.strip() for line in events]
    events.close()

    #check if event is actve right now
    now = datetime.datetime.now()
    for item in eventlist:
        year = item[0:4]
        month = item[4:6]
        day = item[6:8]
        hour = item[8:10]
        channel = client.get_channel(538943056955834379)

    if len(eventlist)>0:
        if int(year) == int(now.year) and int(month) == int(now.month) and int(day) == int(now.day) and int(hour) == int(now.hour):
            await channel.send(f"**IT IS {year}-{month}-{day} {hour}!!! THE TIME HAS COME!!!**")
            
            #copy from delevent command to remove the event from the list after it has been celebrated
            userinput = (f"{year}{month}{day}{hour}")
            for item in eventlist:
                if item == userinput:
                    while item in eventlist: eventlist.remove(item)

            eventlist.sort()
            #update the eventlist txt
            open(eventstxt, 'w').close()
            events = open(eventstxt, "r+")
            for item in eventlist:
                events.write("%s\n" % item)

            events.close()#close the event list



#End (yeehaw)
client.run(envTOKEN)
