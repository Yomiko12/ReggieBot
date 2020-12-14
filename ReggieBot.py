#ReggieBot.py
#Lucas McFarlane, Last Updated 2020-12-13
#A bot that i made for my personal Discord server named after the infamous mouse/rat, Reggie.

#IMPORTS#
import os   #A requirement of "dotenv."
import time    #used for timers and timed events.
import praw       #allows retrieval of posts and images from reddit.
import random        #Used for randomisation and random number generation
import discord          #Discord bot API.
import datetime               #Adds retrieval of dates and times for setting events
from random import choice           #Not sure what this does but something I copied from the internet is using it. (Thanks RKCoding!)
from dotenv import load_dotenv         #Allows for storing the bot token and other sensitive info in a seperate file which is not uploaded to github. For obvious reasons, you do not want your token posted on github publicly.
from discord.ext import commands,tasks    #"commands" allows for the bot to recieve commands from server users, "tasks" allows the bot to run scheduled background tasks, such as changing the bot status on a timer.
from youtube_search import YoutubeSearch     #Allows for the bot to search YouTube for videos (originally for music playback, but kept the feature implemented.)

#global variable for storing events temporarily 
eventlist = []

#global variable to determine if I'm responses are enabled
doIm=True

#Assigns variables based on the .env file to keep passwords and sensitive info out of github.
load_dotenv()
envTOKEN = os.getenv('DISCORD_TOKEN')
envPRAWPASSWORD = os.getenv('REDDIT_PASSWORD')
envPRAWSECRET = os.getenv('REDDIT_SECRET')

#sets the bots command prefix. This is what the user must put in front of whatever command they issue to the bot.
client = commands.Bot(command_prefix="r ")

#setup for praw to access reddit
reddit = praw.Reddit(client_id ="tY1SNZGWr-x6GA" , client_secret =envPRAWSECRET , username = "Yomiko_ReggieBot", password=envPRAWPASSWORD, user_agent ="reggiebot" )

#event that runs once on startup, printing to the terminal and initialising looping background tasks.
@client.event
async def on_ready():
    change_status.start()
    event_checker.start()
    print ("Bot is ready")


#############################
###General Speech Commands###
#############################
#basic commands that simply return strings of text or basic information to the user.


###WELCOMESPEECH###
#Gives the bot's welcome speech. and sends the Github page link
@client.command(help = "Reggie introduces himself and sends the GitHub link")
async def welcomespeech(ctx):
    await ctx.send("**Hi, My name is Reggie! I am your server's new bot created by yours truly, Yomiko12!!**")
    await ctx.send("**You can find more information about me at:**\n https://github.com/Yomiko12/ReggieBot")


###HELLO###
#Simple command that returns "Hi, My name is Reggie!" to the channel.
@client.command(help = "Say hello to Reggie")
async def hello(ctx):
    await ctx.send("**Hi, My name is Reggie!**")


###FLIPCOIN###
#Randomly chooses heads or tails and returns the output to the channel.
@client.command(help = "Flips a coin, randomly picking heads or tails")
async def flipcoin(ctx):
    i = random.randint(1,2)
    if (i == 1):
        await ctx.send("**Heads!**")
    else:
        await ctx.send("**Tails!**")


###SEX###
#reggie will sex the user
@client.command(help = "Reggie sexes you")
async def sex(ctx):
    await ctx.send("**We are sexing now.\nKinda poggers.**")


###INSULT###
#Allows the user to put in a user's name and recieve a randomised message from reggie insulting them.
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
@client.command(help = "Sends a direct message to the specified user")
async def msgfromreggie(ctx, member : discord.Member,*, msg_content= "Hi, My name is Reggie!"):
    await member.send(f'{msg_content}')
    await ctx.send("**Message delivered!**")


###LOVECALC###
#Returns a percentage value of love compatibility
#This command has a manual override option because i can
@client.command(help = "Calculates love between two people")
async def lovecalc(ctx, user1, user2):
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


###PPSIZE###
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
    print(k)#i dont know why i need this but its here

###RATEGAY###
#rates ur gayness
@client.command(help = "Rates your gayness")
async def rategay(ctx):
    i=random.randint(1, 100)
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
@client.command(help = "Sends a picture of Reggie (NSFW)")
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


###POLL###
#Creates a poll for the requested topic
@client.command(help = "Creates a poll")
async def poll(ctx,*,poll):
   message = await ctx.send(f"**{poll}?** *30 seconds to vote* @here")
   await message.add_reaction("👍")
   await message.add_reaction("👎")
   user = client.get_user(766730222665728061)
   time.sleep(30)
   await message.remove_reaction("👍",user)
   await message.remove_reaction("👎",user)
   await ctx.send("**The Results are in!**")

#########################
###MODERATION COMMANDS###
#########################
#this is for any command that can even slightly be related to server moderation.


###SETEVENT###
#Tool used to set a new event
#This is messily written and could use some work.
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



###ENABLEIM###
#Enables "I'm" responses
@client.command(help = "Enable 'I'm' responses")
async def enableim(ctx):
    global doIm
    doIm = True
    await ctx.send("**'I'm' responses enabled!**")


###DISABLEIM###
#Disables "I'm" responses
@client.command(help = "Disable 'I'm' responses")
async def disableim(ctx):
    global doIm
    doIm = False
    await ctx.send("**'I'm' responses disabled!**")


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
        await ctx.send(f'**{postlist[j*3]}\nPost by: u/{postlist[(j*3)+1]}**')
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


##IM CHECKER##
#Constantly checks if a user uses im or i'm in a message and responds to it
#Known bug where work with "im" letter sequence is detected as im, dont know how to fix it right now, also the code is messy.
@client.event
async def on_message(message):
    global doIm
    if doIm == True:
        if client.user.id != message.author.id:
            messageSend = False
            if 'im ' in message.content:
                botMessage = str(message.content)
                imMessage = botMessage[botMessage.find('im'):]
                imMessage = imMessage[3:]
                messageSend=True

            if "I'm " in message.content:
                botMessage = str(message.content)
                imMessage = botMessage[botMessage.find("I'm"):]
                imMessage = imMessage[4:]
                messageSend=True

            if "i'm " in message.content:
                botMessage = str(message.content)
                imMessage = botMessage[botMessage.find("i'm"):]
                imMessage = imMessage[4:]
                messageSend=True

            if "I'M " in message.content:
                botMessage = str(message.content)
                imMessage = botMessage[botMessage.find("I'M"):]
                imMessage = imMessage[4:]
                messageSend=True

            if "i'M " in message.content:
                botMessage = str(message.content)
                imMessage = botMessage[botMessage.find("i'M"):]
                imMessage = imMessage[4:]
                messageSend=True

            if "IM " in message.content:
                botMessage = str(message.content)
                imMessage = botMessage[botMessage.find("IM"):]
                imMessage = imMessage[3:]
                messageSend=True

            if "Im " in message.content:
                botMessage = str(message.content)
                imMessage = botMessage[botMessage.find("Im"):]
                imMessage = imMessage[3:]
                messageSend=True

            if "I AM " in message.content:
                botMessage = str(message.content)
                imMessage = botMessage[botMessage.find("I AM"):]
                imMessage = imMessage[5:]
                messageSend=True
                
            if "I am " in message.content:
                botMessage = str(message.content)
                imMessage = botMessage[botMessage.find("I am"):]
                imMessage = imMessage[5:]
                messageSend=True

            if "i am " in message.content:
                botMessage = str(message.content)
                imMessage = botMessage[botMessage.find("i am"):]
                imMessage = imMessage[5:]
                messageSend=True

            if messageSend == True and (imMessage.startswith('Reggie') or imMessage.startswith('reggie')):
                await message.channel.send ("**No, I'm Reggie!**")
                messageSend = False

            if messageSend == True:
                await message.channel.send(f"**Hello, {imMessage}!**")
        await client.process_commands(message)
    else:
        print("I'm off")

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
        #This looks like it will most definitely break on someone elses server.
        #either find a fix or give simple instruction to fix.
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

#THE END
client.run(envTOKEN)
