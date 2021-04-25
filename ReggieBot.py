#ReggieBot.py
#Lucas McFarlane, Last Updated 2021-04-21
#A bot that I originally made for my personal Discord server named after the infamous mouse/rat, Reggie.

import os            #A requirement of "dotenv" 
import praw            #Allows retrieval of posts and images from reddit
import random                #Used for randomisation and random number generation
import discord                 #Discord's bot API
import datetime                  #Adds retrieval of dates and times for setting events
from random import choice          #For r34 code, idk what it does or how it works (Thanks RKCoding)
from datetime import datetime          #Used to get the current time, used for the event setter
from dotenv import load_dotenv           #Allows for storing passwords and private information outside of the GitHub repository
from discord.ext import commands,tasks       #"commands" allows for the bot to recieve commands from server users, "tasks" allows the bot to run scheduled background tasks
from discord.ext.commands import has_guild_permissions #For commands requiring special permissions

#assigns variables based on the .env file to keep passwords and sensitive info out of GitHub.
load_dotenv()
envTOKEN = os.getenv('DISCORD_TOKEN')
envPRAWPASSWORD = os.getenv('REDDIT_PASSWORD')
envPRAWSECRET = os.getenv('REDDIT_SECRET')
envPRAWID = os.getenv("PRAW_ID")

#sets bot command prefix.
client = commands.Bot(command_prefix=("r ", "R "))

#setup for praw to access reddit
reddit = praw.Reddit(client_id= envPRAWID, client_secret= envPRAWSECRET, username= "Yomiko_ReggieBot", password=envPRAWPASSWORD, user_agent ="reggiebot")

#runs once on startup, starts looping tasks and notifies when bot ready
@client.event
async def on_ready():
	change_status.start()
	check_events.start()

	print ("Bot is ready\nConnected Servers:")
	for guild in client.guilds:
		print(f'{guild.name} ({guild.id})')
	print("___________________")


######################
###General Commands###
######################
#commands that have no real effect on anything, just general chat commands and fun stuff

###WELCOMESPEECH###
#Gives the bot's welcome speech. and sends the Github page link
@client.command(help = "Reggie introduces himself and sends the GitHub link")
async def welcomespeech(ctx):
	embed = discord.Embed(
		title = "Hi! My name is Reggie!",
		description = "I am your server's new Discord bot, created by yours truly, Yomiko12#1137",
		colour = discord.Colour.magenta()
	)
	embed.set_image(url = "https://i.kym-cdn.com/entries/icons/original/000/027/368/Screen_Shot_2018-10-12_at_10.03.28_AM.png")
	embed.add_field(name = "GitHub (Read the README if you haven't already)", value="https://github.com/Yomiko12/ReggieBot", inline=False)
	embed.add_field(name = "Problems or Suggestions?", value="Add an issue on GitHub OR contact me (Yomiko12#1137)", inline=False)
	await ctx.send(embed=embed)


###HELLO###
#Simple command that returns "Hi, My name is Reggie!" to the channel.
@client.command(help = "Say hello to Reggie")
async def hello(ctx):
	embed = discord.Embed(
		title = f"Hi, {ctx.author}, My name is Reggie!",
		colour = discord.Colour.magenta()
	)
	embed.set_image(url = "https://i.pinimg.com/originals/aa/01/90/aa019023148ed37537f9d22fcbe53041.gif")
	await ctx.send(embed=embed)


###GITHUB###
#send the link to the github
@client.command(help = "sends the link to the ReggieBot GitHub repository")
async def github(ctx):
	await ctx.send("https://github.com/Yomiko12/ReggieBot")


###FLIPCOIN###
#Randomly chooses heads or tails and returns the output to the channel.
@client.command(help = "Flips a coin, randomly picking heads or tails")
async def flipcoin(ctx):
	i = random.randint(1,2)
	if i==1: headsTails = "Heads!"
	else: headsTails = "Tails!"
	embed = discord.Embed(
		title = headsTails,
		colour = discord.Colour.magenta()
		)
	embed.set_image(url="https://media.giphy.com/media/gVROkjyShPnos/giphy.gif")
	await ctx.send(embed = embed)


###SEX#NSFW###
#reggie will sex the user
@client.command(help = "Reggie sexes you")
@commands.is_nsfw()
async def sex(ctx):
	embed = discord.Embed(
		title="We are having sex now!",
		description = "poggers!",
		colour = discord.Colour.magenta()
	)
	embed.set_image(url = "https://i.kym-cdn.com/photos/images/masonry/001/760/741/d09.gif")
	await ctx.send(embed=embed)

@sex.error
async def sex_error(ctx, error):
	await ctx.send("You must be in a NSFW channel!")


###INSULT###
#Allows the user to put in a user's name and recieve a randomised message from reggie insulting them.
@client.command(help = "Reggie insults you")
async def insult(ctx,*,user=''):
	if user == '': user=ctx.message.author
	j= [
      "You're gonna die or something maybe",
      "You're dumb and stuff",
      "You're an idiot head",
      "Nobody asked",
      "Not gonna lie, You kinda suck"
  ]
	i = random.randint(0, len(j) -1)

	embed=discord.Embed(
		title=f"{j[i]}, {user}!",
		colour = discord.Colour.magenta()
	)
	embed.set_image(url = "https://media.tenor.com/images/3f606b31ef45d720da40abd35d9085ac/tenor.gif")
	await ctx.send(embed=embed)


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
	embed = discord.Embed(
		title="POGGERS!!",
		colour = discord.Colour.magenta()
	)
	embed.set_image(url = j[i])
	await ctx.send(embed=embed)

###ASKREGGIE###
#Ask reggie a question and get a randomised response.
@client.command(help = "Allows you to ask Reggie a Question")
async def askreggie(ctx, *, question):
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
	embed=discord.Embed(
		title = f"'{question}?'",
		colour = discord.Colour.magenta()
	)
	embed.set_author(name=f"{ctx.message.author}asks:")
	embed.add_field(name = "Reggie Says: ", value = j[i])
	await ctx.send(embed=embed)


###MSGFROMREGGIE###
#This command sends a direct message to the user specified.
@client.command(help = "Sends a direct message to the specified user")
async def msgfromreggie(ctx, member : discord.Member,*, msg_content= "Hi, My name is Reggie!"):
	await member.send(f'{msg_content}')
	embed=discord.Embed(
		title = f"Message Sent! to {member}!",
		description = f"'{msg_content}'",
		colour = discord.Colour.magenta()
	)
	await ctx.send(embed=embed)

###LOVECALC###
#Returns a percentage value of love compatibility
@client.command(help = "Calculates love between two people")
async def lovecalc(ctx, user1, user2):
	i = random.randint(1,100)
	embed = discord.Embed(
		title = f"{user1} and {user2} : ",
		description = f"Your compatibility is {i}%!!!",
		colour = discord.Colour.magenta()
	)
	embed.set_image(url = "https://i.kym-cdn.com/photos/images/original/001/461/337/f96.gif")
	await ctx.send(embed=embed)

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


###PPSIZE#NSFW###
#returns the user's pp size
@client.command(help = "Shows the users pp size")
@commands.is_nsfw()
async def ppsize(ctx):
	i="8"
	j=random.randint(1,15)
	if ctx.message.author.id == 413096914972835840: j=25
	for k in range(j):
		i+="="
	i+="D"

	if (j > 10):
		i+=" **NICE!**"
	elif (j>5 and j<=10):
		i+=" **Not too bad!**"
	else:
		i+=" **That's pretty rough...**"

	embed = discord.Embed(
		Title = f"{ctx.message.author}'s pp size: ",
		description=i
	)
	embed.set_image(url = "https://i.ytimg.com/vi/_zBaBlKgjWI/maxresdefault.jpg")
	await ctx.send(embed=embed)

@ppsize.error
async def ppsize_error(ctx, error):
	await ctx.send("You must be in a NSFW channel!")


###RATE###
#rates whatever is sent to the bot randomly
@client.command(help = "Reggie will rate whatever you show him")
async def rate(ctx):
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
    i=random.randint(0,len(j) -1)
    await ctx.send(j[i])

###REGGEPIC#NSFW###
#randomly returns one of sixteen images of reggie.
##NSFW##
@client.command(help = "Sends a picture of Reggie (NSFW)")
@commands.is_nsfw()
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
	embed = discord.Embed(
		title="Here's Your Reggie pic!",
	)
	if (j[i].startswith("https://twitter.com")):
		embed.add_field(name="UwU", value=j[i])
	else:
		embed.set_image(url=j[i])
	await ctx.send(embed=embed)

@reggiepic.error
async def reggiepic_error(ctx, error):
	await ctx.send("You must be in a NSFW channel!")


###POLL###
#Creates a poll for the requested topic
@client.command(help = "Creates a poll")
async def poll(ctx,*,poll):
   message = await ctx.send(f"**{poll}?** *30 seconds to vote*")
   await message.add_reaction("👍")
   await message.add_reaction("👎")
   user = client.get_user(766730222665728061)


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
	embed = discord.Embed(
		title=crimes[i]
	)
	embed.set_image(url="https://img.ifunny.co/images/54e619252b0af7c944109eafdcdb1ee2fdeec8bae58d051654ad1612097cd5f1_1.gif")
	await ctx.send(embed=embed)

#########################
###MODERATION COMMANDS###
#########################
#server moderation type commands, as well as the reddit and r34 commands

###MUTE###
#requires perms
#mute the selected member if you have the permissions to do so
@client.command(help="'mute, mt' : mutes the chosen user", pass_context = True , aliases=['mt'])
@has_guild_permissions(mute_members=True)
async def mute(ctx, member: discord.Member):
	await member.edit(mute = True)
	await ctx.message.add_reaction("👍")

@mute.error
async def mute_error(ctx, error):
	await ctx.send("**You are missing permissions or did something wrong**")


###DEAFEN###
#requires perms
#deafen the selected member if you have the permissions to do so
@client.command(help="'deafen, df' : deafens the chosen user" , pass_context = True , aliases=['df'])
@has_guild_permissions(deafen_members=True)
async def deafen(ctx, member: discord.Member):
	await member.edit(deafen = True)
	await ctx.message.add_reaction("👍")

@deafen.error
async def deafen_error(ctx, error):
	await ctx.send("**You are missing permissions or did something wrong**")


###DISCONNECT###
#requires perms
#disconnects the chosen user if you have the permissions to do so
@client.command(help="'disconnect, dc' : Disconnects the chosen user", pass_context = True , aliases=['dc'])
@has_guild_permissions(move_members=True)
async def disconnect(ctx, member: discord.Member):
	await member.edit(voice_channel=None)
	await ctx.message.add_reaction("👍")

@disconnect.error
async def disconnect_error(ctx, error):
	await ctx.send("**You are missing permissions or did something wrong**")


###BAN###
#requires perms
#bans the chosen user
@client.command(help="ban a user")
@has_guild_permissions(ban_members=True)
async def ban(ctx, user: discord.Member, *, reason):
	await ctx.guild.ban(user, reason=reason)
	await ctx.message.add_reaction("👍")

@ban.error
async def ban_error(ctx, error):
	await ctx.send("**You are missing permissions or did something wrong**")


###KICK###
#requires perms
#kicks the chosen user
@client.command(help="kick a user")
@has_guild_permissions(kick_members=True)
async def kick(ctx, user: discord.Member, *, reason):
	await ctx.guild.kick(user, reason=reason)
	await ctx.message.add_reaction("👍")

@kick.error
async def kick_error(ctx, error):
	await ctx.send("**You are missing permissions or did something wrong**")


###CLEAR###
#requires perms
#clears the set amount of messages with the limit being 300
@client.command(help = "'clear, clr' : Clears the specified amount of messages", pass_context = True , aliases=['clr'])
@has_guild_permissions(manage_messages=True)
async def clear(ctx, amount=2):
    if (amount > 300): amount = 300
    await ctx.channel.purge(limit=amount)

@clear.error
async def clear_error(ctx, error):
	await ctx.send("**You are missing permissions or did something wrong**")


###SENDMSG###
#Send a message to any channel reggie can access by channel ID
@client.command(help="Send a message to any channel reggie can access by channel ID")
async def sendmsg(ctx, arg, *, message):
	channel = client.get_channel(int(arg))
	await channel.send(message)
	await ctx.message.add_reaction("👍")


###PINGSPAM###
#Spams the chosen user with 5 pings.
@client.command(help = "Spams a user with 5 pings")
async def pingspam(ctx, *, user):
	for i in range(5):
		await ctx.send(user)


###PING###
#Reports the bot's ping to the user.
@client.command(help = "Returns Reggie's ping to the server")
async def ping(ctx): ##Does "round()" round a number to the nearest integer value? because if so, that's pretty damn useful.
	await ctx.send(f'my ping is {round(client.latency * 1000)} ms')


###REDDIT#NSFW###
#gets a random post from the hot top 100 from the chosen subreddit.
@client.command(help = "Returns one of the top 50 hot posts on the chosen subreddit")
@commands.is_nsfw()
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

@r.error
async def r_error(ctx, error):
	await ctx.send("You must be in a NSFW channel!")


###NEWEVENT###
#allow users to create new events and have reggie notify them when they occur (only down to the hour right now)
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

##STATUS##
#Changes the bot's status once an hour.
status = ["Doki Doki Literature Club","Huniepop","Minecraft", "Roblox", "Amorous"]
@tasks.loop(seconds=1200)
async def change_status():

	serverCount = 0
	userCount = 0
	for guild in client.guilds:
		serverCount += 1
		userCount += guild.member_count

	message = choice(status)
	message = message + f" (used by {userCount} people in {serverCount} servers!)"
	await client.change_presence(activity=discord.Game(message))


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

client.run(envTOKEN)