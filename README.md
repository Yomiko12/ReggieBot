# ReggieBot

This is ReggieBot, a bot made for my personal Discord server.
All commands must be prefixed with "r "
___

## LATEST CHANGES

### 2021-03-14
Added back event setter, now with support for multiple servers.

### 2021-03-13
Major rewrite and performance improvements

### 2021-01-12  
Added r34 command

### 2020-12-20
Added r die  
Added r warcrime  

### 2020-12-13
Added ability to enable and disable "I'm" Responses
minor performance improvements and improved code readability
common theming across all bot responses

___
## UPCOMING CHANGES
1. Make bot available to anyone to add to their server
2. improve the readme and create a website with better documentation
3. more moderation commands (ban, kick, silence, mute, deafen, etc.)
4. improved bot message formatting
5. restriced commands tha require administrator or hightened priveledges.
6. automated bot updates, (drastically improve bot uptime)
7. notifications for possible bot outages
8. general improvements to code efficiency and readability
___

## GENERAL SPEECH COMMANDS
##### These are basic commands that simply return strings or basic info to the user.  

### r help
Gets help

### r welcomespeech
Gives the bot's basic welcome speech.

### r hello
Returns "Hi, My name is Reggie!" to the user.

### r flipcoin
Flips a coin, returning "Heads!" or "Tails!" to the user.

### r sex
Reggie will sex you (NSFW)

### r insult "user to insult's @"
sends the specified user a randomised insulting message.

### r pogchamp
returns a gif of someone pogging

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

### r ppsize
Returns an ascii image of the users pp (NSFW)

### r rategay
Rates your gayness level (NSFW)

### r rate "anything"
the bot will give a randomised 1 through ten rating of whatever is sent. this could be people, images, etc.

### r reggiepic
Returns a random image of reggie, (NSFW)

### r ithink "what reggie thinks"
the bot will respond saying "It is my personal belief that (thing you entered)."  

### r poll "poll topic"
creates a 30 second poll for the topic you give

### r warcrime
Reggie commits a warcrime
___
___

## Moderation Commands
This is for any command that can even slightly be considered related to server moderation.

### r r34 "search term"  
returns a randomised image from r34 of the specified search term  
(NSFW)

### r enableim
enables "I'm" responses

### r disableim
disables "i'm" responses

### r pingspam "specified user's @"
spams the requested user with 5 pings

### r clear "amount of messages to clear"
clears the specified number of messages from the channel
(WARNING, no minimum permissions limit, anyone can use this unless modified.)

### r ping
returns the bot's latency to the discord server

### r r "subreddit"
picks a random post from the top 50 hot on the chosen subreddit.  
(yes, it works for NSFW subreddits and posts.)

### newevent "yyyy-mm-dd-(0-23) name of event" 
create a new event that reggie will remind you of at the set time

### viewevents 
list the upcoming events taking place on your server

### delevent "event# (from listevents)" 
delete the specified event

___
___
## ADD TO YOUR SERVER
https://discord.com/oauth2/authorize?client_id=766730222665728061&permissions=8&scope=bot 