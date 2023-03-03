
from sys import prefix
import discord
import os
import random
from dotenv import load_dotenv
from discord.ext import commands
# from discord import app_commands

load_dotenv()

intent = discord.Intents.default()
intent.members = True
intent.message_content = True

client = discord.Bot(intents = intent)
token = os.getenv('TOKEN')
tree = discord.app_commands.CommandTree(client)

poogie = "poogie"
poogie_emoji = "<:poogie:964488145041256508>"


@client.event
async def on_message(message):
    username = str(message.author).split("#")[0]
    channel = str(message.channel.name)
    channel_id = message.channel.id
    user_message = message.content

    print(f'Message : \"{user_message}\" envoyé par {username} dans {channel}')

    if message.author == client.user:
        return

    if  poogie in user_message.lower():
        await message.add_reaction(poogie_emoji)
        return

    if channel_id == 903375076731285504:
        if user_message.lower() == "poogie" or user_message.lower() == "poogie !" or user_message.lower() == "poogie!":
            print("Poogie was sent")
            await message.channel.send(f'N\'oublie pas de prier Poogie quotidiennement {username} !')
            return
        elif user_message.lower() == "bye":
            await message.channel.send(f'Bye {username}')
        elif user_message.lower() == "tell me a joke":
            jokes = [" Can someone please shed more\
            light on how my lamp got stolen?",
                    "Why is she called llene? She\
                    stands on equal legs.",
                    "What do you call a gazelle in a \
                    lions territory? Denzel."]
            await message.channel.send(random.choice(jokes))

# client = commands.Bot(command_prefix="c!*")

# @client.command()
# async def ping(ctx):
#     await ctx.send('Pong')

client.run(token)