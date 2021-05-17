# ReggieBot

![alt text](https://i.kym-cdn.com/entries/icons/original/000/027/368/Screen_Shot_2018-10-12_at_10.03.28_AM.png "Logo Title Text 1")

## This is ReggieBot, a bot made for my personal Discord server
## (Currently active in 11+ servers)
___

## ADD TO YOUR SERVER  
[CLICK HERE](https://discord.com/oauth2/authorize?client_id=766730222665728061&permissions=8&scope=bot)  
___

## WARNING
this bot requires administrator priveleges to function. this enables the bot to have access to large amounts of personal data and control over your Discord server. ReggieBot will NEVER share your personal data with ANYONE, but like any Discord bot, it technically could, so BE WARNED!

### Data ReggieBot may store
Server name and ID  
Server member count  
text chat ID's  
User set events (newevent command)  
___

## Report Issues/Possible Improvements
If you discover any issues or have suggestions, please open a New Issue [HERE](https://github.com/Yomiko12/ReggieBot/issues)
___

## Latest Release (Update 3)  
### Major Changes  
NEW - GetMembers system allows you to referce server members easier.  
You can now reference users by a unique string of letters or numbers in their username or nickname.  
You can also use 'ME' or your own name to reference yourself.  
Supported Commands:  
- r insult
- r msgfromreggie
- r lovecalc 
- r ppsize
- r mute
- r deafen
- r disconnect
- r ban
- r kick
- r pingspam  

NEW - Status now shows user and server count.  
NEW - Added kick, ban, mute, deafen, disconnect, github, help commands.  
NEW - Added required permissions for specific moderation commands. 
NEW - NSFW commands are now limited to NSFW channels.  
NEW - When using r reddit command, NSFW subreddits can only be viewed in NSFW channels.  
NEW - Most commands now respond with new embed style messages.  
NEW - Added shortened command prefixes to certain commands.  
NEW - Pingspam now supports multiple words or people.  

REMOVED - r ithink (it was dumb)  
REMOVED - r rategay (also dumb)  
___

## Latest Changes  

### 2021-05-05 (Update 3 B3)  

REGGIEBOT UPDATE 3 RELEASED  
fixed the getmembers implementation in pingspam command  
replaced help command with github link  
fixed r pogchamp gifs  
added the ME alias to all commands using the new getmembers system  
getmembers function can also make searches based off of the users nickname  

### 2021-04-17  (Update 3 B2)
added the getmembers system  
All bot commands that take a name can now use the new getmembers system  
bug fixes  

### 2021-04-26  
more shorthand command aliases  
updated README  

### 2021-04-24  (Update 3 B1)
minor performance improvements  
Removed r34 command (didn't work great, stolen code, rarely used, etc.)  
Added r github command  
Status now shows user and server count  
fixed permissions for locked commands  
reaction responses to administrative commands  
NSFW commands are now limited to NSFW channels  
new message styles with embeds  
removed r rategay because its stupid  
added shortened prefix options to some commands (deafen works with df, mute mt, etc)  
you can now pingspam more than one word or person at once  
added kick and ban  

### 2021-04-20
Added Mute, Deafen, and Disconnect commands.  
Removed i'm responses (too annoying after about an hour)  
added sendmsg command to send messages to any chat by ID that Reggie has access to  
Removed R ithink

### 2021-03-14
Added new event setter, now with support for multiple servers.

### 2021-03-13
Major rewrite and performance improvements
___

## UPCOMING Update 4 CHANGES
1. set up notification system for servers to notify of updates, downtime, set  default notification chat, etc  
2. randomised responses will not respond to the same question twice so that responses are more realistic  
3. improved event setter (maybe)
4. async support
5. self updating README  
6. server owners can remove commands they dont want members to have access to  
7. add more games that Reggie can play, or replace playing screen with a normal status  
8. mute and deafen commands toggle mute or deafen status  
___

## UPCOMING Update 5 CHANGES
1. MINIGAMES!  
___

## COMMANDS
### Bot prefix is "r " or "R "
## GENERAL COMMANDS
### commands that have no real effect on anything, just general chat commands and fun stuff
___

### R welcomespeech  
Formatting: "r welcomespeech", "r welcome", "r speech"   
Gives the bot's welcome speech. Reggie introduces himself and shares the link to the GitGub repo.  

### R hello  
Formatting: "r hello", "r hi"  
Simply returns "Hi, My name is Reggie!"

### R Github  
Formatting: "r github", "r git"  
Sends the link to the GitHub repository.  


### R flipcoin  
Formatting: "r flipcoin", "r flip"  
Flips a coin, randomly returning heads or tails.

### R sex
NSFW  
Formatting: "r sex"  
Reggie has sex with the user.

### R insult  
Formatting: "r insult 'optionally, pick a user to insult' "  
Reggie will insult the user or chosen server member.

### R Pogchamp  
Formatting: "r pogchamp", "r pog"  
Reggie sends a GIF of a random character doing the Fortnite default dance.  

### R Askreggie
Formatting: "r askreggie 'your question'", "r ask '' "  
Ask reggie a question and get a randomised response.  

### R Msgfromreggie
Formatting: "r msgfromreggie 'user' 'message' ", "r message '' '' ", "r msg '' '' "  
Sends a direct message to the chosen user.  

### R lovecalc
Formatting: "r lovecalc 'user 1' 'user 2'", "r love '' '' "  
Calcualates the love between two server members.  

### R owo
Formatting: "r owo"  
Literally just returns "OwO"  

### R uwu
Formatting: "r uwu"  
Literally just returns "UwU"  

### R ppsize
NSFW  
Formatting: "r ppsize 'optional user'", "r pp '' "  
Shows the users pp size.  

### R rate
Formatting: "r rate 'anything here'"  
Reggie will rate whatever you want him to.

### R Reggiepic
NSFW
Formatting: "r reggiepic", "r rpic"  
Sends an image or video of Reggie the Rat in a less than family friendly scenario.

### R poll
Formatting: "r poll 'poll topic'"  
Creates a yes or no poll about anything you want.  

### R Warcrime
Formatting: "r warcrime"  
Reggie commits a warcrime.  
___

## MODERATION COMMANDS
### Server moderation type commands, as well as commands to retrieve images/data
___

### R mute
Formatting: "r mute 'user'", "r mt '' "  
Mutes the chosen server member (if you have administrator priveleges.)

### R deafen
Formatting: "r deafen 'user'", "r df '' "  
Deafens the chosen server member (if you have administrator priveleges)

### R disconnect
Formatting: "r disconnect 'user'" , "r dc '' "  
Disconnects the chosen server member (if you have administrator priveleges.)  

### R ban  
Formatting: "r ban 'user' 'reason' "  
Ban the chosen user  

### R kick   
Formatting: "r kick 'user' 'reason' "  
Kick the chosen user

### R clear
Formatting: "r clear 'number of messages'"  
Clears the specified amount of messages from the current channel (if you have administrator priveleges.)  

### R sendmsg
Formatting: "r sendmsg 'channel ID' 'message'"  
Reggie will send your message to any server channel as long as it has access to it.  

### R pingspam
Formatting: "r pingspam 'user to ping'", "r spam '' "  
pings the chosen user 5 times

### R ping
Formatting: "r ping"  
Returns the bots latency to the server.

### R reddit
NSFW  
Formatting: "r reddit 'subreddit'", "r r '' "  
Returns a random post from top 50 hot on the specified subreddit.

### R newevent
Formatting: "r newevent 'yyyy-mm-dd-hh' 'event name'" (time must be 24h format)  
Create a new event that reggie will remind you of when the set time comes.  

### R viewevents
Formatting: "r viewevents"  
View your servers set events.  

### R delevent
Formatting: "r delevent 'event# (from viewevents)'"  
Deletes the selected event.
