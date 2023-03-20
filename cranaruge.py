
# from code import interact
# from sys import prefix
# import discord
# import os
# import random
# from dotenv import load_dotenv
# from discord.ext import *
# # import typing
# # from discord import Embed
# from discord import *
# # from discord_slash import SlashCommand

# load_dotenv()
# token = os.getenv('TOKEN')

# bot = discord.interactions.Client(token)

# intent = discord.Intents.default()
# intent.members = True
# intent.message_content = True

# # tree = discord.app_commands.CommandTree(client)

# poogie = "poogie"
# poogie_emoji = "<:poogie:964488145041256508>"
# #--------------------------------------------------------------
# class abot(discord.Client):
#     def __init__(self):
#         super().__init__(intents=discord.Intents.default())
#         self.synced = False

#     async def on_ready(self):
#         await tree.sync(guild=discord.Object(id=903362470482165832))
#         self.synced = True
#         print("Bot is online")

# bot = abot()
# tree = app_commands.CommandTree(bot)
# bot.run()
# #--------------------------------------------------------------
# @client.event
# async def on_message(message):
#     username = str(message.author).split("#")[0]
#     channel = str(message.channel.name)
#     channel_id = message.channel.id
#     user_message = message.content

#     print(f'Message : \"{user_message}\" envoyé par {username} dans {channel}')

#     if message.author == client.user:
#         return

#     if  poogie in user_message.lower():
#         await message.add_reaction(poogie_emoji)
#         return

#     if channel_id == 903375076731285504:
#         if user_message.lower() == "poogie" or user_message.lower() == "poogie !" or user_message.lower() == "poogie!":
#             print("Poogie was sent")
#             await message.channel.send(f'N\'oublie pas de prier Poogie quotidiennement {username} !')
#             return
#         elif user_message.lower() == "bye":
#             await message.channel.send(f'Bye {username}')
#         elif user_message.lower() == "tell me a joke":
#             jokes = [" Can someone please shed more\
#             light on how my lamp got stolen?",
#                     "Why is she called llene? She\
#                     stands on equal legs.",
#                     "What do you call a gazelle in a \
#                     lions territory? Denzel."]
#             await message.channel.send(random.choice(jokes))

# # client = commands.Bot(command_prefix="c!*")

# # @client.command()
# # async def ping(ctx):
# #     await ctx.send('Pong')

# client.run(token)
# # def Launch():
# #     bot.run(token)



############################################################################################


import os
from click import launch
import discord
import random
import typing
import interactions
from discord import Embed
from discord.ext import commands
from discord import app_commands
from dotenv import load_dotenv
load_dotenv()
token = os.getenv('TOKEN')
# TOKEN = "OTcyMTgwMDU1MDAwMjUyNDY2.GJAhkG.CLFEAkPCUPSkQIDyLLQMKAHhk0CcPAbSot9XQg"
bot = interactions.Client(token)

Aleksis007 = '6bocMayFv0MB1UlCRmAYbybEybkkD_-z6pN07btgxMLrVo8'
GuildList = [903362470482165832, 662904062215323662]
#----------------------------------------------------------------------------------------------------------------

class abot(discord.Client):
    def __init__(self):
        super().__init__(intents=discord.Intents.all())
        self.synced = False

    async def on_ready(self):
        await tree.sync()
        self.synced = True
        print("Bot is online")

bot = abot()
tree = app_commands.CommandTree(bot)
#----------------------------------------------------------------------------------------------------------------
@tree.command(name="opgg", description="get basic rank infos")
async def self(interation: discord.Interaction,name:str , region: typing.Literal["EUW","EUNE","NA","BR","JP","KR","LA","LAS","OC","TR","RU"], queue: typing.Literal["SoloQ","FelxQ"]):
    await interation.response.send_message("str à la con")

# COMMANDES GLOBALES

@tree.command(name="pang", description="Yes, Cranaruge is here.")
async def self(interation: discord.Interaction):
    await interation.response.send_message("Poogie pongs you.")

# COMMANDES FOE

@tree.command(name="foewiki", description="Lance une recherche sur le Wiki français officiel de FOE.")
async def self(interation: discord.Interaction, terme_recherché: str):
    tmp = ""
    for i in range(0, len(terme_recherché)):
        if terme_recherché[i] == " ":
            tmp += "_"
        else:
            tmp += terme_recherché[i]
    await interation.response.send_message("https://fr.wiki.forgeofempires.com/index.php?title=" + tmp)

@tree.command(name="foeressourcesage", description="Sélectionnez un âge, et voyez les denrées nécessaires pour le terminer !")
async def self(interation: discord.Interaction, age: typing.Literal["ADB", "ADF", "HMA", "MAC", "REN", "COLO", "INDUS", "PROG", "MOD", "POST", "CTP", "DEM", "FUT", "FA", "FO", "FV", "ESM", "ESCA", "ESV", "ESLJ"]):
    if age == "ADB":
        await interation.response.send_message("Total des ressources nécessaires pour terminer toutes les technologies de l'Âge du Bronze :\n\n" +
        "<:pfs:1087197250595344445> Points forge x127\n<:pieces:1087197281482199080> Pièces x2 300\n<:marchandises:1087197265065689089> Marchandises x2 300\n"+
        "<:marbre:1087197550030901327> Marbre x2\n<:bois:1087197572436852796> Bois x2")

# COMMANDES GREPOLIS

@tree.command(name="grepowiki", description="Lance une recherche sur le Wiki français officiel de Grepolis.")
async def self(interation: discord.Interaction, terme_recherché: str):
    tmp = ""
    for i in range(0, len(terme_recherché)):
        if terme_recherché[i] == " ":
            tmp += "_"
        else:
            tmp += terme_recherché[i]
    await interation.response.send_message("https://wiki.fr.grepolis.com/wiki/" + tmp)


#----------------------------------------------------------------------------------------------------------------

@bot.event
async def on_message(message):
    user_message = message.content
    print(user_message)

    if  "poogie" in user_message.lower():
        for emoji in message.guild.emojis:
            if emoji.name.lower() == "poogiedancing":
                await message.add_reaction(emoji)
            elif emoji.name.lower() == "poogie":
                await message.add_reaction(emoji)
    

    if "kut-ku" in user_message.lower():
        await message.add_reaction("<:gimmeyoursoul:903363514683515000>")

    if "gimme emoji" in user_message.lower():
        for emoji in message.guild.emojis:
            print(emoji.name)
            print(emoji.id)


def launch():
    bot.run(token)