#!/usr/bin/env python3.8
import os
import random
from time import time
import discord
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = 897945940273549343

client = discord.Client()


@client.event
async def on_ready():
    for guild in client.guilds:
        if guild.name == GUILD:
            break

    print(
        f'{client.user} is connected to the following guild:\n'
        f'{guild.name}(id: {guild.id})\n'
    )



@client.event
async def on_message(message):
    decider = random.randint(0,5)

    if decider == 20:
        if message.channel == 898004365716115467:
            await message.channel.send("https://cdn.discordapp.com/attachments/898004365716115467/1035701847102591048/Screenshot_20221028-174833_Discord.jpg")
            decider = random.randint(0,5)
    elif '&ping' in message.content.lower():
        await message.channel.send("pong")



client.run(TOKEN)
