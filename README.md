# ReggieBot

This is ReggieBot.
All commands must be prefixed with "r "
this bot comes in 2 variants, one with NSFW commands available, and one without.
___

## LATEST ADDED FEATURES (Last Three Changes)

### 2020-10-30
EVENT SETTER
Allows reggiebot to set events on any day at any hour and notify the server at that date and hour.
(still no alerts, soon)
Fixed Bot using multiple fonts.
Added help command

### 2020-10-27
added "r ithink"

### 2020-10-25:  
added "r reggiepic"  
changed "r threaten" to "r insult"  
readme improvements

___
## CHANGES TO IMPLEMENT
1. INSTALL INSTRUCTIONS
2. Fix viewevents formatting
2. full rewrite of all music commands
2b. allow searching for music with a spotify link (@Jfbob1#9886)   
2c. improvements to "r qlist"  
2d. switch from music downloading to realtime music streaming with youtube_dl  
___
___

## GENERAL SPEECH COMMANDS
##### These are basic commands that simply return strings of text to the user.  

### r help
Gets help

### r welcomespeech
Gives the bot's basic welcome speech.

### r hello
Returns "Hi, My name is Reggie!" to the user.

### r flipcoin
Flips a coin, returning "Heads!" or "Tails!" to the user.

### r insult "user to insult's @"
sends the specified user a randomised threatening message.

### r pogchamp
returns a random gif of a character doing the fortnite default dance.

### r askreggie "user's question"
returns a randomised answer to the user's question.

### r msgfromreggie "target user's @" "message to send"
sends a direct message to the specified user with the specified contents.

### r lovecalc "person's @" "another person's @" "manual override value (optional)"
calculates the love percentage between the two specified users.

### r owo
just prints "OwO"

### r uwu
just prints "UwU"

### r rate "anything"
the bot will give a randomised 1 through ten rating of whatever is sent. this could be people, images, etc.

### r ithink "what reggie thinks"
the bot will respond saying "It is my personal belief that (thing you entered)."  

___
___

## GENERAL SPEECH COMMANDS (NSFW VERSION ONLY)
##### Same category as the above general speech commands, but only available in the NSFW version.

### r sex
sexes the user.

### r reggiepic
returns a random image of our lord and savior.

### r ppsize "user's @ (optional)"
returns an ascii image of the user's pp and rates it based on it's randomised length  

### r rategay
rates ur gayness
___
___

## Moderation Commands
This is for any command that can even slightly be considered related to server moderation.

### r setevent "yyyy-mm-dd hh"
adds an event to the event list

### r viewevents
shows the user a list of all upcming events

### r delevent "yyyy-mm-dd hh"
deletes the specified event from the event list

### r r "subreddit"
picks a random post from the top 50 hot on the chosen subreddit.  
(yes, it works for NSFW subreddits and posts.)

### r pingspam "specified user's @"
spams the requested user with 5 pings

### r clear "amount of messages to clear"
clears the specified number of messages from the channel
(WARNING, no minimum permissions limit, anyone can use this unless modified.)

### r ping
returns the bot's latency to the discord server

### r ytsearch "search query"
returns the first youtube result for whatever is searched.

___
___

## MUSIC (REMOVED FOR NOW)
##### this is for any command to play and control music playback


### join
makes the bot join the call the user is currently in

### leave 
removes the bot from it's current call.

### r q "song name or youtube link"
queues the specified song, autoplaying it if it's the first added to the queue.

### r qplay
plays the first song in the queue. (kinda never need to use this.)

### r pause
pauses music playback

### r resume
resumes music playback

### r qlist
returns a list of all songs in the queue.

### r stop
stops the current song.

### r skip
skips the current song and starts playing the next song in queue.

### r remove "number of song in qlist"
removes the specified item from the queue.

___
___

# INSTALLATION GUIDE
if you want to add this bot to your own server, use the following steps.  

(INSTALLATION GUIDE COMING SOON)