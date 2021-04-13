#ReggieBot.py
#Lucas McFarlane, Last Updated 2020-12-13
#A bot that i made for my personal Discord server named after the infamous mouse/rat, Reggie.

#IMPORTS#
import os    #A requirement of "dotenv." 
import praw    #allows retrieval of posts and images from reddit.
import time      #a requirement of r34
import rule34      #API for grabbing posts from the rule34 website.
import random        #Used for randomisation and random number generation
import asyncio         #i dont remember what this is but its here
import discord           #Discord's bot API
import requests            #dont know what this is for either
import datetime              #Adds retrieval of dates and times for setting events
from random import choice      #for r34 code, idk what it does or how it works. (Thanks RKCoding)
import urllib.request as u       #also for r34 code, idk what it does
from datetime import datetime      #used to get the current time, used for the event setter
from dotenv import load_dotenv       #allows for storing passwords and private information outside of the GitHub repository.
import xml.etree.ElementTree as et     #also also for r34 code, still dont know what it does.
from discord.ext import commands,tasks   #"commands" allows for the bot to recieve commands from server users, "tasks" allows the bot to run scheduled background tasks, such as changing the bot status on a timer.
from youtube_search import YoutubeSearch   #Allows for the bot to search YouTube for videos (originally for music playback, but kept the feature implemented.)
from discord.ext import commands as command  #also also also for r34

#GLOBAL VARIABLE(S)#
doIm=True #determines if messages containing "I'm" should be responded to 

#Assigns variables based on the .env file to keep passwords and sensitive info out of github.
load_dotenv()
envTOKEN = os.getenv('DISCORD_TOKEN')
envPRAWPASSWORD = os.getenv('REDDIT_PASSWORD')
envPRAWSECRET = os.getenv('REDDIT_SECRET')
envPRAWID = os.getenv("PRAW_ID")

#sets the bots command prefix. (Can this be made case-unsensitive?)
client = commands.Bot(command_prefix=("r ", "R "))

#setup for praw to access reddit
reddit = praw.Reddit(client_id= envPRAWID, client_secret= envPRAWSECRET, username= "Yomiko_ReggieBot", password=envPRAWPASSWORD, user_agent ="reggiebot")

#runs once on startup, starts looping tasks and notifies when bot ready
@client.event
async def on_ready():
	change_status.start()
	check_events.start()
	print ("Bot is ready")

#Code for R34 bot copied from RKCoding
ltime = time.asctime(time.localtime())
Client = discord.Client()
rr = rule34.Rule34
def xmlparse(str):
	root = et.parse(u.urlopen(str))
	for i in root.iter('post'):
		fileurl = i.attrib['file_url']
		return fileurl
def xmlcount(str):
	root = et.parse(u.urlopen(str))
	for i in root.iter('posts'):
		count = i.attrib['count']
		return count
def pidfix(str):
	ye = int(xmlcount(rr.urlGen(tags=str,limit=1)))
	ye = ye - 1
	return ye
def rdl(str,int):
	print(f'[INFO {ltime}]: integer provided: {int}')

	if int > 2000:
		int = 2000
	if int == 0:
		int == 0
		print(f'[INFO {ltime}]: Integer is 0, accommodating for offset overflow bug. ')	
	elif int != 0:	
		int = random.randint(1,int)
	print(f'[INFO {ltime}]: integer after randomizing: {int}')
	xurl = rr.urlGen(tags=str,limit=1,PID=int)
	print(xurl)
	wr = xmlparse(xurl)
	
	if 'webm' in wr:
		if 'sound' not in str:
			if 'webm' not in str:
				print(f'[INFO {ltime}]: We got a .webm, user didnt specify sound. Recursing. user tags: {str}')
				wr = rdl(str,pidfix(str))
		else:
			pass
	elif 'webm' not in wr:
		print(f'[INFO {ltime}]: Not a webm, dont recurse.')
	return wr
#Stolen code ends

######################
###General Commands###
######################

###WELCOMESPEECH###
#Gives the bot's welcome speech. and sends the Github page link
@client.command(help = "Reggie introduces himself and sends the GitHub link")
async def welcomespeech(ctx):
    await ctx.send("**Hi, My name is Reggie, prior CEO of Nintendo!!**")
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
    if (i == 1): await ctx.send("**Heads!**")
    else: await ctx.send("**Tails!**")

###SEX###
##NSFW?##
#reggie will sex the user
@client.command(help = "Reggie sexes you")
async def sex(ctx):
    await ctx.send("**I am far too wholesome to be doing this, I refuse to sex you.**")

###INSULT###
#Allows the user to put in a user's name and recieve a randomised message from reggie insulting them.
@client.command(help = "Reggie insults you")
async def insult(ctx,*,user):
    j= [
        "**I would never insult you, you are perfect**"
    ]
    i = random.randint(0, len(j) -1)
    await ctx.send(f'{j[i]}, {user}!**')

###POGCHAMP###
#Selects a random gif of a character doing the fortite default dance and sends it to the channel.
@client.command(help = "Sends a random gif of someone pogging")
async def pogchamp(ctx):
    j=[
        "https://tenor.com/view/shrek-dance-fortnite-fortnite-default-dance-shrek-dance-gif-15809394",
        "https://tenor.com/view/default-dance-epic-win-victory-royale-dank-gif-14897370",
        "https://tenor.com/view/goose-default-dance-dancing-dance-moves-feeling-good-gif-16364185",
        "https://tenor.com/view/mario-cool-dance-yahoo-super-mario-gif-12778263",
        "https://tenor.com/view/baldi-fortnite-fortnite-dance-gif-12747343",
        "https://tenor.com/view/shaggy-default-dance-victory-gif-14972422",
        "https://tenor.com/view/minecraft-fortnite-default-dance-funny-steve-gif-13329851"
    ]
    i = random.randint(0,len(j) -1)
    await ctx.send(j[i])

###ASKREGGIE###
#Ask reggie a question and get a randomised response.
@client.command(help = "Allows you to ask Reggie a Question")
async def askreggie(ctx):
    j = [
        "**YES!!**",
        "**OF COURSE!!**",
        "**Yea, probably..**",
        "**idk..**",
        "**Maybe..**",
        "**It's possible..**",
        "**I'm Reggie!**",
        "**NO!!**",
        "**Nahhh..**"
    ]
    i = random.randint(0,len(j) -1)
    await ctx.send(j[i])

###MSGFROMREGGIE###
#This command sends a direct message to the user specified.
@client.command(help = "Sends a direct message to the specified user")
async def msgfromreggie(ctx, member : discord.Member,*, msg_content= "Hi, My name is Reggie!"):
    await member.send(f'{msg_content}')
    await ctx.send("**Message delivered!**")

###LOVECALC###
#Returns a percentage value of love compatibility
@client.command(help = "Calculates love between two people")
async def lovecalc(ctx, user1, user2):
    i = random.randint(1,100)
    await ctx.send(f'**Your love compatibility is {i}%!**')

###OWO###
#literally just prints "OwO"
@client.command(help = "OwO")
async def owo(ctx):
  await ctx.send("**Do you really think that I, Reggie, would do such a thing?**")

###UWU###
#literally just prints "UwU"
@client.command(help = "UwU")
async def uwu(ctx):
  await ctx.send("**Do you really think that I, Reggie, would do such a thing?**")

###PPSIZE###
##NSFW?##
#returns the user's pp size
@client.command(help = "Shows the users pp size")
async def ppsize(ctx):
  await ctx.send("**Do you really think that I, Reggie, would do such a thing?**")

###RATEGAY###
##NSFW?##
#rates ur gayness
@client.command(help = "Rates your gayness")
async def rategay(ctx):
  await ctx.send("**Do you really think that I, Reggie, would do such a thing?**")

###RATE###
#rates whatever is sent to the bot randomly
@client.command(help = "Reggie will rate whatever you show him")
async def rate(ctx):
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
    i=random.randint(0,len(j) -1)
    await ctx.send(j[i])

###REGGEPIC###
#randomly returns one of sixteen images of reggie.
##NSFW##
@client.command(help = "Sends a picture of Reggie (NSFW)")
async def reggiepic(ctx):
    j=[
			"https://cdn.discordapp.com/attachments/505177959686995978/826915388251308134/1399460-20080724_i_4442.jpg",
			"https://cdn.discordapp.com/attachments/505177959686995978/826915396795891782/631610908.0.jpg",
			"https://cdn.discordapp.com/attachments/505177959686995978/826915411013533757/Culture_Replay_Reggie-Fils-Aime-107926697.jpg",
			"https://cdn.discordapp.com/attachments/505177959686995978/826915416060330085/exQq9KZS.png",
			"https://cdn.discordapp.com/attachments/505177959686995978/826915421499293757/reggie_fils_aime_5568.jpg",
			"https://cdn.discordapp.com/attachments/505177959686995978/826915435479957555/Reggie_Fils-Aime_-_Game_Developers_Conference_2011_-_Day_2_1.jpg",
			"https://cdn.discordapp.com/attachments/505177959686995978/826915445764259890/Reggie-Fils-Aime_2017.jpg",
			"https://cdn.discordapp.com/attachments/505177959686995978/826915455675400252/reggie-gamestop-fils-aime-nintendo-president-board-of-directors.jpg"
    ]
    i=random.randint(0,len(j) -1)
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

###WARCRIME###
#Reggie commits a warcrime
@client.command(help = "Reggie commits a warcrime")
async def warcrime (ctx):
    crimes = [
        "**I, Reggie, would never do such a thing.**"
            ]
    i=random.randint(0,len(crimes) -1)
    await ctx.send (crimes[i])

#########################
###MODERATION COMMANDS###
#########################
#this is for any command that can even slightly be related to server moderation.
#this also includes the event setter and various other commands that grab images.

###R34###
##NSFW##
#grabs a random r34 image from chosen category
#(This code is stolen.)
@client.command(help = "Pulls a random post from the chosen r34 category")
async def r34(ctx,*arg):
	await ctx.send("Nope")


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

###CLEAR###
###WARNING###
#This command does not have any proveleges so anyone can use it to any extent
#this command will clear the specifid amount of posts that the user requests (limit 300)
@client.command(help = "Clears the specified amount of messages")
async def clear(ctx, amount=2):
    if (amount > 300): amount = 300
    await ctx.channel.purge(limit=amount)

###PING###
#Reports the bot's ping to the user.
@client.command(help = "Returns Reggie's ping to the server")
async def ping(ctx): ##Does "round()" round a number to the nearest integer value? because if so, that's pretty damn useful.
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

###NEWEVENT###
#allow users to create new events and have reggie notify them when they occur (only down to the hour right now)
#possibly, a web interface could be added to the website to manage events as well
@client.command(help = "set an event ( format: yyyy-mm-dd-(00-23) 'name of event (no quotes)' )")
async def newevent(ctx, setTime, *,eventName):

	#get the current date and time and format it
	currentTime = str(datetime.now())
	currentTime = currentTime.replace(" ", "").replace("-", "")
	currentTime = currentTime[:10]

	#format the date given by the user
	setTime = setTime.replace("-", "")

	#check that the inputted date length is the same as the current to ensure valid input
	if ( len(setTime) != len(currentTime) ):
		await ctx.send("Invalid date, try again")
		return

	#get clannel id so notification can be sent there
	channel = str(ctx.channel.id)
	#get server id for check events command
	server = str(ctx.guild.id)

	#assign information from currentTime to seperate variables to compare against user input
	currentYear = currentTime[:4]
	currentMonth = currentTime[4:6]
	currentDate = currentTime[6:8]
	currentHour = currentTime[8:]
	#assign information given by user to seperate variables to compare against current date
	setYear = setTime[:4]
	setMonth = setTime[4:6]
	setDate = setTime[6:8]
	setHour = setTime[8:]

	#a sketchy attempt at keeping invalid dates out of the database (a txt file)
	if (setYear < currentYear):
		await ctx.send("**Invalid Year, Try Again**")
		return
	if (setYear == currentYear and setMonth < currentMonth):
		await ctx.send("**invalid Month, Try Again**")
		return
	if (setYear == currentYear and setMonth == currentMonth and setDate < currentDate):
		await ctx.send("**invalid Date, Try Again**")
		return
	if (setYear == currentYear and setMonth == currentMonth and setDate == currentDate and setHour < currentHour):
		await ctx.send("**invalid Hour, Try Again**")
		return
    
	#after data has been verified, write the information to the events.txt document.
	f = open("events.txt", "a")
	f.write(f"{setTime}-{eventName}--{server}-{channel}\n")
	f.close()
	await ctx.send(f"**Event '{eventName}' added successfully!!**")

###VIEW EVENTS###
#see all currently set events for your server
@client.command(help = "see all currently set events")
async def viewevents(ctx):

	#open the file
	f = open("events.txt", "r")

	#clean up the items in the file
	eventList = []
	newEvents = []

	for line in f:
		eventList.append(line)
	for item in eventList:
		newEvents.append(item.replace("\n",""))

	eventList = newEvents

	#get the events that apply to the server of where the command was called
	currentServer = str(ctx.guild.id)
	
	#get a new list of events that belong to the correct server
	validEvents = []
	for item in eventList:
		if item.find(currentServer) > 1:
			validEvents.append(item)

	printEvents = []

	for item in validEvents:
		output = ""
		cutoff = item.find("--")
		output += f"{item[:4]}-{item[4:6]}-{item[6:8]}-{item[8:10]}: {item [11:cutoff] }"
		printEvents.append(output)
	
	output = ""
	counter = 1
	for item in printEvents:
		output += f"{counter}: {item}\n"
		counter+=1
	
	f.close()

	if len(printEvents) == 0:
		await ctx.send("**NO EVENTS!!**")
		return

	await ctx.send(output)

###DELEVENT###
#delete an event based on its numerical position in in the txt document
@client.command(help = "remove an event based on its numerical value in viewevents")
async def delevent(ctx, number):

	number = int(number)
	f = open("events.txt", "r+")

	#clean up the items in the file
	eventList = []

	for line in f:
		eventList.append(line)
	
	currentServer = str(ctx.guild.id)
	validEvents = []

	for item in eventList:
		if item.find(currentServer) > 1:
			validEvents.append(item)
	
	print(len(validEvents))
	
	if number > len(validEvents):
		await ctx.send("**Invalid Input, Try Again**")
		return

	itemToRemove = validEvents[number-1]
	f.seek(0)

	lines = f.readlines()
	f.seek(0)

	for line in lines:
		if line != itemToRemove:
			f.write(line)
	f.truncate()

	await ctx.send(f"**Event #{number} has been removed!**")

	f.close()

###################
###LOOPING TASKS###
###################
#this is where all loping tasks are placed.

##STATUS##
#Changes the bot's status once an hour.
status = ["The Legend of Zelda: Breath of the Wild", "Super Smash Bros Ultimate", "Super Mario Odyssey", "Animal Crossing", "Mario Kart 8"]
@tasks.loop(seconds=1200)
async def change_status():
    await client.change_presence(activity=discord.Game(choice(status)))

@tasks.loop(seconds=30)
async def check_events():

  #get the current date and time and format it
	currentTime = str(datetime.now())
	currentTime = currentTime.replace(" ", "").replace("-", "")
	currentTime = currentTime[:10]

	f = open("events.txt", "r+")

	eventList = []
	for line in f:
		eventList.append(line)

	for item in eventList:
		eventTime = item[:10]

		if eventTime == currentTime:
			
			#get the event name from the item
			cutoff = item.find("-")
			secondCutoff = item.find("--")
			eventName = item[(cutoff + 1):secondCutoff]
			print(eventName)

			#trim down item to server and chat
			cutoff = item.find("--")
			eventInfo = item[cutoff + 2:]

			#get event server from the event info
			cutoff = eventInfo.find("-")
			eventServer = eventInfo[:cutoff]

			#get the event chat from the event info
			eventChat = eventInfo[(cutoff + 1):]

			channel = client.get_channel(int(eventChat))
			await channel.send(f"@here **EVENT '{eventName}' IS HAPPENING RIGHT NOW!!**")

			f.seek(0)
			lines = f.readlines()
			f.seek(0)

			for line in lines:
				if line != item:
					f.write(line)
			f.truncate()

	f.close()

##IM CHECKER##
#Constantly checks if a user uses im or i'm in a message and responds to it
@client.event
async def on_message(message):
    global doIm
    msgContent = str(message.content).lower()
    checks = ["im", "i'm", "i am"]
    sendMsg = False
    Message = ""

    if client.user.id != message.author.id:
        for item in checks:
            if ( (" " + item + " ") in msgContent or msgContent.startswith(item + " ") ):
                sendMsg = True
                Message = msgContent[msgContent.find(item):]
                Message = Message[len(item):]
        
        if sendMsg == True and doIm == True:
            await message.channel.send(f"**Hello, {Message}!!**")
    await client.process_commands(message)     

client.run(envTOKEN)