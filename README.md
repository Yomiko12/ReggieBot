# ReggieBot

This is ReggieBot.
All commands must be prefixed with "r "
this bot comes in 2 variants, one with NSFW commands available, and one without.
___

## LATEST ADDED FEATURES

### 2020-10-25:  
added "r reggiepic"  
changed "r threaten" to "r insult"  
readme improvements

___
## CHANGES TO IMPLEMENT
allow searching for music with a spotify link (@Jfbob1#9886)   
improvements to "r qlist"  
switch from music downloading to realtime music streaming with youtube_dl  
fix music file download errors  
schedule command to set alerts on specific dates and/or times. (@wa_ge#5304)
___
___

## GENERAL SPEECH COMMANDS
##### These are basic commands that simply return strings of text to the user.  



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
___
___

## GENERAL SPEECH COMMANDS (NSFW VERSION ONLY)
##### Same category as the above general speech commands, but only available in the NSFW version.


### r sex
sexes the user.

### r reggiepic
returns a random image of our lord and savior.

### r ppsize "user's @ (optional)"
returns an ascii image of the user's pp and rates it based on it's randomised length.

## Moderation Commands
This is for any command that can even slightly be considered related to server moderation.


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

## MUSIC
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

## REDDIT
##### retrieve posts from reddit

### r r "subreddit"
picks a random post from the top 50 hot on the chosen subreddit.  
(yes, it works for NSFW subreddits and posts.)