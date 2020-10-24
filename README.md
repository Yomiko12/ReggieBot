# ReggieBot

This is ReggieBot.
All commands must be prefixed with "r "
this bot comes in 2 variants, one with NSFW commands available, and one without.


## General Speech Commands
These are basic commands that simply return strings of text to the user.



### r welcomespeech
Gives the bot's basic welcome speech.

### r hello
Returns "Hi, My name is Reggie!" to the user.

### r flipcoin
Flips a coin, returning "Heads!" or "Tails!" to the user.

### r threaten "user to threaten's @"
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

### r rate "anything"
the bot will give a randomised 1 through ten rating of whatever is sent. this could be people, images, etc.


## General Speech Commands (NSFW VERSION ONLY)
Same category as the above general speech commands, but only available in the NSFW version.



### r sex
sexes the user.

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


## Music
this is for any command to play and control music playback



### join
makes the bot join the call the user is currently in

### leave 
removes the bot from it's current call.

### r q "song name or youtube link"
queues the specified song, autoplaying it if it's the first added to the queue.

### r play
plays the first song in the queue.

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