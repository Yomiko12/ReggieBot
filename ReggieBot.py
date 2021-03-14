#ReggieBot.py
#Lucas McFarlane, Last Updated 2020-12-13
#A bot that i made for my personal Discord server named after the infamous mouse/rat, Reggie.

###TO DO###
#brand new event setter with multi server support
#make bot more easily customisable for users. (allow changing reggies played games, message when event, etc)
#rewrite the README
#improve bot message interfaces
#add more administrative features (ban, kick, silence, etc for admins only)
#restrictions to clear command for admins only
#easier bot update system


#IMPORTS#
import os      #A requirement of "dotenv."
import time      #used for timers and timed events.
import praw        #allows retrieval of posts and images from reddit.
import rule34        #API for grabbing posts from the rule34 website.
import random          #Used for randomisation and random number generation
import asyncio           #i dont remember what this is but its here
import discord             #Discord's bot API
import requests              #dont know what this is for either
import datetime                #Adds retrieval of dates and times for setting events
from random import choice        #for r34 code, idk what it does or how it works. (Thanks RKCoding)
import urllib.request as u         #also for r34 code, idk what it does
from dotenv import load_dotenv       #Allows for storing the bot token and other sensitive info in a seperate file which is not uploaded to github. For obvious reasons, you do not want your token posted on github publicly.
import xml.etree.ElementTree as et     #also also for r34 code, still dont know what it does.
from discord.ext import commands,tasks   #"commands" allows for the bot to recieve commands from server users, "tasks" allows the bot to run scheduled background tasks, such as changing the bot status on a timer.
from youtube_search import YoutubeSearch   #Allows for the bot to search YouTube for videos (originally for music playback, but kept the feature implemented.)
from discord.ext import commands as command  #also also also for r34
#TESTING ENDS

#GLOBAL VARIABLES#
eventlist = [] #temporary event storing variable
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
    if (i == 1): await ctx.send("**Heads!**")
    else: await ctx.send("**Tails!**")

###SEX###
##NSFW?##
#reggie will sex the user
@client.command(help = "Reggie sexes you")
async def sex(ctx):
    await ctx.send("**We are sexing now.\nKinda poggers.**")

###INSULT###
#Allows the user to put in a user's name and recieve a randomised message from reggie insulting them.
@client.command(help = "Reggie insults you")
async def insult(ctx,*,user):
    j= [
        "**You're gonna die or something maybe",
        "**You're dumb and stuff",
        "**You're an idiot head",
        "**Nobody asked",
        "**Not gonna lie, You kinda suck"
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
        "**wWhat kind of question is this?? There must be something seriously wrong with you.**",
        "**Bruh...**",
        "**I'm Reggie!**",
        "**NO!!**",
        "**Bruh, there is no way..**",
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
    await ctx.send("**OwO**")

###UWU###
#literally just prints "UwU"
@client.command(help = "UwU")
async def uwu(ctx):
    await ctx.send("**UwU**")

###PPSIZE###
##NSFW?##
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
##NSFW?##
#rates ur gayness
@client.command(help = "Rates your gayness")
async def rategay(ctx):
    i=random.randint(1, 100)
    await ctx.send(f"**Your gayness level is {i}%!**")

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
        "https://cdn.discordapp.com/attachments/505177959686995978/770072831182241802/ElHl5HTU0AEPAme.png",
        "https://cdn.discordapp.com/attachments/505177959686995978/770072904682831874/Ek8OMOXVgAIXl39.png",
        "https://cdn.discordapp.com/attachments/505177959686995978/770073506385362944/EiDm2fhU8AEccTY.png",
        "https://cdn.discordapp.com/attachments/505177959686995978/805494433318436864/861b550f0ac0d8b800dd3d58cd9ed67c.png",
        "https://cdn.discordapp.com/attachments/505177959686995978/805494782984978462/ce5269d0b908c50662aeb3f7818f3559.png",
        "https://cdn.discordapp.com/attachments/505177959686995978/770073830184976384/EdLZa3HWAAElkq0.png",
        "https://cdn.discordapp.com/attachments/505177959686995978/770073907616808970/EgMLgjCUcAAhRtj.png",
        "https://cdn.discordapp.com/attachments/505177959686995978/770073958979993660/EdIrkfgUMAAnXtF.png",
        "https://cdn.discordapp.com/attachments/505177959686995978/805495107947069460/welcome-intrusion-005.png",
        "https://cdn.discordapp.com/attachments/505177959686995978/805495475176210462/EsHlZdAVQAEUAYA.png",
        "https://cdn.discordapp.com/attachments/505177959686995978/805495548340863016/Er8yS7LU0AAo6Im.png",
        "https://cdn.discordapp.com/attachments/505177959686995978/805495574366781440/EsBtZJWW8AARDWq.png",
        "https://twitter.com/i/status/1314658830765047809",
        "https://twitter.com/i/status/1308214223080570880",
        "https://twitter.com/i/status/1281640986297290753",
        "https://twitter.com/i/status/1274037700698374144",
        "https://twitter.com/i/status/1247290642956341248",
        "https://twitter.com/i/status/1247293619536461826",
        "https://twitter.com/i/status/1243711781794504704",
        "https://twitter.com/i/status/1243711092846559232",
        "https://cdn.discordapp.com/attachments/505177959686995978/770074185208299630/unknown.png",
        "https://cdn.discordapp.com/attachments/505177959686995978/770074410689364048/unknown.png",
        "https://cdn.discordapp.com/attachments/505177959686995978/770074684582002748/unknown.png",
        "https://cdn.discordapp.com/attachments/505177959686995978/770074933518270485/EZHsOBdVAAExOkY.png",
        "https://cdn.discordapp.com/attachments/505177959686995978/770074992833462323/EYTvZOfXgAMqUwX.png",
        "https://cdn.discordapp.com/attachments/505177959686995978/770075316965998622/EX54hU7X0AcAIXV.png",
        "https://cdn.discordapp.com/attachments/505177959686995978/770075393687814174/EW8mhbkVcAAbeS5.png",
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
        "**I just bombed an innocent Syrian village!!**",
        "**I just conducted a biological experiment on prisoners of war!!**",
        "**I just took a civilian hostage!!**",
        "**I led a direct attack against innocents!!**"
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
	answer = ''
	arg = str(arg)
	arg = arg.replace(',','')
	arg = arg.replace('(','')
	arg = arg.replace(')','')
	arg = arg.replace("'",'')
	waitone = await ctx.send("**Searching...**")
	newint = pidfix(arg)
	if newint > 2000:
		newint = 2000
		answer = rdl(arg,random.randint(1,newint))

	if newint > 1:
		answer = rdl(arg,random.randint(1,newint))

	elif newint < 1:
		if newint == 0:
			answer = rdl(arg,0)

		elif newint != 0:
			answer = rdl(arg,1)
   
	if 'webm' in answer:
		waitone.delete
		await ctx.send(answer)

	elif 'webm' not in answer:
		embed = discord.Embed(title=f'Rule34: {arg}',color=ctx.author.color)
		embed.set_author(name=f'{ctx.author.display_name}',icon_url=f'{ctx.author.avatar_url}')
		embed.set_thumbnail(url='https://rule34.paheal.net/themes/rule34v2/rule34_logo_top.png')
		embed.set_image(url=f'{answer}')
		embed.set_footer(text="Now That's Epic!",icon_url='https://cdn.discordapp.com/avatars/268211297332625428/e5e43e26d4749c96b48a9465ff564ed2.png?size=128')
		waitone.delete
		await ctx.send(embed = embed)

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


###################
###LOOPING TASKS###
###################
#this is where all loping tasks are placed.

##STATUS##
#Changes the bot's status once an hour.
status = ["Doki Doki Literature Club","Huniepop","Minecraft", "Roblox", "Amorous"]
@tasks.loop(seconds=1200)
async def change_status():
    await client.change_presence(activity=discord.Game(choice(status)))


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