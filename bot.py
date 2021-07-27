from keep_alive import keep_alive
import discord
import os
from dotenv import load_dotenv
from discord.ext import tasks
import feedparser

keep_alive()
load_dotenv()
DISCORD_TOKEN = os.getenv("TOKEN")
feed = []

@bot.event
async def on_ready():
    clear.start()
    check.start()

@tasks.loop(seconds = 604800)
async def clear():
    global feed
    d = feedparser.parse('https://www.thesun.co.uk/tech/rss')
    feed.clear()
    feed.append(d.entries[0]['link'])

@tasks.loop(seconds = 11)
async def check():
    global feed
    channel = bot.get_channel(590870954243129344)
    d = feedparser.parse('https://www.thesun.co.uk/tech/rss')
    if (d.entries[0]['link'] not in feed):
        feed.append(d.entries[0]['link'])
        await channel.send(d.entries[0]['link'])
    else:
        pass
