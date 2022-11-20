#!/usr/bin/env python3.8
import os
import random
from time import time
import discord
from dotenv import load_dotenv

print("starting...")
load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

print("This security sucks ass")
print(TOKEN)

client = discord.Client()


#@client.event
async def on_ready():
    print("Ready")
    print("Logged in as a bot {0.user}".format(client))



@client.event
async def on_message(message):
    items = ["in the fab lab",
             "in Wes\' car",
             "in Erik\'s basement",
             "in Kistler\'s meth lab",
             "in the software dungeon",
             "in the intestines of the goat",
             "",
             "on McMaster-Carr"
             ]
    decider = random.randint(0,40)
    print(decider)
    print("message recived")

    username = str(message.author).split("#")[0]
    channel = str(message.channel.name)
    user_message = str(message.content)

    print(f'Message {user_message} by {username} on {channel}')

    if message.author == client.user:
        print("")

    if message.author == 272519236927225858 or message.author == 324286034382815254:
        if decider == 2:
            await message.channel.send("I use linux")


    elif decider == 0:
        formatted_message = "Hey look what I found " + \
            random.choice(items) + "\n" + \
            "https://cdn.discordapp.com/attachments/898004365716115467/1035701847102591048/Screenshot_20221028-174833_Discord.jpg"

        print(formatted_message)
        await message.channel.send(formatted_message)
        print("Operation complete. Target neutralized.")

    elif "minors" in message.content.lower():
        if decider == 3:
            await message.channel.send("Ahem, " + random.choice(["Flip", "Croix"]))

    elif "python" in message.content.lower():
        if decider == 4:
            await message.channel.send("await message.channel.send(\"Python sucks\") ")

    elif "money" in message.content.lower():
        await message.channel.send("Ben will pay for it")

    elif "linux" in message.content.lower() and message.author != client.user:
        await message.channel.send("Windows is better")

    elif "windows" in message.content.lower() and message.author != client.user:
        await message.channel.send("Linux is better")

    elif decider == 6:
        await message.channel.send("https://media.discordapp.net/attachments/678825700978851860/818188972584468490/image0-18.gif")

    elif "loctite" in message.content.lower():
        await message.channel.send("yummy")

    elif "glue" in message.content.lower():
        await message.channel.send("yummy")

    elif '&ping' in message.content.lower():
        await message.channel.send("pong")


print("here")
client.run(TOKEN)
