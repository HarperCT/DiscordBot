import os
import discord
from dotenv import load_dotenv

client = discord.Client()
load_dotenv()


@client.event
async def on_ready():
    print("Logged in as {0.user}".format(client))


@client.event
async def on_message(message):
    # if message from bot do nothing
    if message.author == client.user:
        return
    if message.content.startswith('$hello'):
        await message.channel.send('Hello!')


client.run(os.getenv("TOKEN"))
