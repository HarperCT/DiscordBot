import discord

client = discord.Client()


@client.event
async def on_ready():
    print("Logged in as {0.user}").format(client)


@client.event
async def on_message(message):
    # if message from bot do nothing
    if message.author == client.user:
        return
