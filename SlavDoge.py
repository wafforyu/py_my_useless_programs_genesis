#WARNING! THIS BOT HAS NSFW FEATURES

import random
import discord
from discord.ext import commands
import os
import requests
import json
import praw
#import asyncpraw
from keep_alive import keep_alive

client = discord.Client()
client = commands.Bot(command_prefix='#')



reddit = praw.Reddit(client_id="KRC_38kNGCM5MQ",
                     client_secret=os.getenv("reddit_secret"),
                     username=os.getenv('reddit_username'),
                     password=os.getenv("reddit_password"),
                     user_agent="dik")

#asyncReddit = asyncpraw.Reddit(client_id="KRC_38kNGCM5MQ",
#                               client_secret=os.getenv("reddit_secret"),
#                               username=os.getenv('reddit_username'),
#                               password=os.getenv("reddit_password"),
#                               user_agent="dik")
#

#==================================================================================
warning = ["cyka!", "cyka blyat!!", "blyat"]

sad_words = [
    "i am sad", "depressed", "unhappy", "miserable", "i feel terrible",
    "depressing", 'unhappy', 'angry', 'feel bad', 'i wanna kms'
]

homophobic = ["gay", "gae", "gei"]

bad_words = [
    "fuck", "shit", 'bitch', 'pussy', 'cunt', 'idiot', 'asshole', 'dumbass',
    'cyka', 'dumass', 'cock', 'bobo', 'tanga', 'inutil', 'puta', 'tangina',
    'taena', 'tang ina', 'sex', 'hentai', 'cum', 'cumming', 'gago', 'gagi',
    'kupal', 'damn', 'deym', 'fucks sake', 'jesus sake', 'stfkp', 'nude',
    'tits', 'titties', 'tiddies', 'fuk', 'dfq', 'dafuq', 'pota', 'poota',
    'puta', 'put tank in a moo', 'put tank in a mall', 'put your pp inside me',
    'pp inside', 'put it inside me', 'peepee', 'pppe', 'fck', "dick", 'dicc',
    'you hoe', 'hoe', 'coom', 'bdsm', 'tite', 'etits', 'titi', 'plok'
]

starter_encouragements = ["Cheer up.", "Hang in there.", "You can do it!"]

uwus = ["uwu", "owo", "oWo", "UWU", "uWu"]

racist_words = [
    "nigger", "chingchong", "nigga", "nibba", "knee grr", 'niggur',
    'ching chong'
]

sleep = ["sleep", "tulog"]

sleep_gifs = [
		"https://media.tenor.com/images/a4d2ca9f7b7049e7e8207fba6bacd0bf/tenor.gif",
		"https://media.tenor.com/images/0a159a15040b1e0524575166914b6f91/tenor.gif",
		"https://media.tenor.com/images/64d7609dd788b7d1d875982310d9a150/tenor.gif",
		"https://media.tenor.com/images/a395e107c84e7fb3db9a9376f3c57377/tenor.gif",
		"https://media.tenor.com/images/c6e0e367edd2ae8006c4dd85f584ce0b/tenor.gif",
		"https://media.tenor.com/images/aef583e12530fa1c290e0a8aa980c5ea/tenor.gif",
		"https://media.tenor.com/images/9683bd4b5e4485cd54d0f8856c58c9c1/tenor.gif",
		"https://media.tenor.com/images/118333ca646504eb25f522fe955bc452/tenor.gif",
		"https://media.tenor.com/images/b4d07af4dacb2b8b43dd9fee7436b7c6/tenor.gif",
		"https://media.tenor.com/images/4480e91ba352333d7b5486d866c30c7a/tenor.gif",
		"https://media.tenor.com/images/bbf488c0eb1240638b24c4f50ff1b50b/tenor.gif",
		"https://media.tenor.com/images/945d5292243ffbfa4095d4df59e44636/tenor.gif",
		"https://media.tenor.com/images/fb587a556ce3c05a0eee3eed463a3aaa/tenor.gif",
		"https://media1.tenor.com/images/b39b6b3ff46bffff747bf7b450addce9/tenor.gif?itemid=9225001",
    "https://media1.tenor.com/images/ebb2533fc574395a36c18c2795516d6b/tenor.gif?itemid=6046035",
    "https://media1.tenor.com/images/f89c189082d675ca5d27eb5028969beb/tenor.gif?itemid=10555880",
    "https://media1.tenor.com/images/d52cc0b8e8d885effa73e5c26b31e298/tenor.gif?itemid=14865519",
    "https://media1.tenor.com/images/f287f3c67acbeb3850d781fd14215149/tenor.gif?itemid=16980796",
    "https://media.tenor.com/images/478f0cdde7d929c44405c3543a8d142c/tenor.gif",
    "https://media.tenor.com/images/4e5e4cabdb06cffd906186ef6313c00b/tenor.gif",
    "https://media.tenor.com/images/a5fa7d6967e07a9c2bae1aeede18ac02/tenor.gif",
    "https://media.tenor.com/images/c34605e9a57102f57f731c93312cb801/tenor.gif"
]

inspire = "inspire me"


def get_quote():
    response = requests.get("https://zenquotes.io/api/random")
    json_data = json.loads(response.text)
    quote = json_data[0]['q'] + " -" + json_data[0]['a']

    return (quote)


@client.event
async def on_ready():
    print("We have logged in as {0.user}".format(client))
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="your family."))
 
#---------------------------------------------


@client.event
async def on_message(message):

    msg = message.content

    if message.author == client.user:
        return

    if message.content == ">purge":
        await message.channel.purge(limit=10)

    if message.content == ">purge2":
        await message.channel.purge(limit=2)


    if message.content.lower() == "send meme" or message.content.lower(
    ) == "send memes":
        if msg == "SEND MEMES":
            await message.channel.purge(limit=1)

        all_subs = []
        subreddit = reddit.subreddit("dankmemes")
        top = subreddit.hot(limit=100)

        for sub in top:
            all_subs.append(sub)

        random_sub = random.choice(all_subs)
        name = random_sub.title
        url = random_sub.url
        em = discord.Embed(title=name)
        em.set_image(url=url)

        await message.channel.send(embed=em)

    if message.content.lower() == "send loods" or message.content.lower(
    ) == "send lewds" or message.content.lower() == "send lewd":

        if msg == "SEND LOODS":
            await message.channel.purge(limit=1)

        all_subs = []
        subreddit = reddit.subreddit("hentai")
        top = subreddit.hot(limit=100)

        for sub in top:
            all_subs.append(sub)

        random_sub = random.choice(all_subs)
        name = random_sub.title
        url = random_sub.url
        em = discord.Embed(title=name)
        em.set_image(url=url)

        await message.channel.send(embed=em)  
    if message.content == "nword":
      await client.edit(nick="0221")

#=============BETA_++++++++++++++++++++++++++++++++++++++++++++++++++
#    if msg == "beta":
#      subreddit = await asyncReddit.subreddit("learnpython")
#      async for submission in subreddit.hot(limit=10):
#        await message.channel.send(submission.title)
#
    if message.content.lower() == 'hi':
        await message.channel.send("Hello there!")

    if message.content.lower() == 'hello':
        await message.channel.send("Hello there!")

    if message.content.lower() == 'help':
        await message.channel.send("Sorry, Can't help ya.")

    if message.content.lower() == inspire:
        quote = get_quote()
        await message.channel.send(quote)

    if any(word in msg.lower() for word in sleep):
        await message.channel.send(random.choice(sleep_gifs))

    #if any(word in msg.lower() for word in bad_words):
    #    await message.channel.send(random.choice(warning))

    #if any(word in msg.lower() for word in uwus):
    #    await message.channel.send(random.choice(uwus))

    if any(word in msg.lower() for word in racist_words):
        await message.channel.send("Stop being racist.")

    if message.content.lower() == "gay" or message.content.lower() == "gae":
        await message.channel.send("Gender neutrality please.")

    if message.content.lower() == 'loli':
        await message.channel.send("THIS IS THE FBI, OPEN UP!!")

keep_alive()

client.run(os.getenv('token'))
