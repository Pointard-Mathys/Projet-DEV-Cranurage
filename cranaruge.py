
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
bot = interactions.Client(token)

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
        await interation.response.send_message("Total des ressources nécessaires pour terminer toutes les technologies de l'Âge du Bronze :\n\nRessources générales :\n" +
        "<:pfs:1087197250595344445> Points forge x127\n<:pieces:1087197281482199080> Pièces x2 300\n<:marchandises:1087197265065689089> Marchandises x2 300\n"+
        "\nRessources de l'Âge du Bronze :\n<:marbre:1087197550030901327> Marbre x2\n<:bois:1087197572436852796> Bois x2")
    if age == "ADF":
        await interation.response.send_message("Total des ressources nécessaires pour terminer toutes les technologies de l'Âge du Fer :\n\nRessources générales :\n" +
        "> <:pfs:1087197250595344445> Points forge x256\n> <:pieces:1087197281482199080> Pièces x8 050\n> <:marchandises:1087197265065689089> Marchandises x13 100\n"+
        "\nRessources de l'Âge du Bronze :\n> <:marbre:1087197550030901327> Marbre x37\n> <:bois:1087197572436852796> Bois x60\n> <:teinture:1087197593567772762> Teinture x27\n" +
        "> <:pierre:1087197532133806171> Pierre x25\n> <:vin:1087197513217474572> Vin x58\n\nRessources de l'Âge du Fer :\n> <:tissu:1087197391779807322> Tissu x11\n" + 
        "> <:boisdebene:1087197468917235815> Bois d'ébène x4\n> <:bijoux:1087197426407985173> Bijoux x16\n> <:fer:1087197445492047995> Fer x13\n" + 
        "> <:calcaire:1087197408372465674> Calcaire x3\n")
    if age == "HMA":
        await interation.response.send_message("Total des ressources nécessaires pour terminer toutes les technologies du Haut Moyen-Âge :\n\nRessources générales :\n" +
        "> <:pfs:1087197250595344445> Points forge x505\n> <:pieces:1087197281482199080> Pièces x34 000\n> <:marchandises:1087197265065689089> Marchandises x65 250\n"+
        "\nRessources de l'Âge du Bronze :\n> <:marbre:1087197550030901327> Marbre x22\n> <:bois:1087197572436852796> Bois x34\n> <:teinture:1087197593567772762> Teinture x46\n" +
        "> <:pierre:1087197532133806171> Pierre x61\n> <:vin:1087197513217474572> Vin x35\n\nRessources de l'Âge du Fer :\n> <:tissu:1087197391779807322> Tissu x77\n" + 
        "> <:boisdebene:1087197468917235815> Bois d'ébène x63\n> <:bijoux:1087197426407985173> Bijoux x90\n> <:fer:1087197445492047995> Fer x82\n" + 
        "> <:calcaire:1087197408372465674> Calcaire x70\n\nRessources du Haut Moyen-Âge :\n> <:cuivre:1087197301866504202> Cuivre x23\n> <:or:1087197355910115389> Or x30\n" + 
        "> <:granite:1087197333189566576> Granite x4\n> <:miel:1087197315846127726> Miel x20\n> <:albatre:1087197371034771496> Albâtre x14")
    if age == "MAC":
        await interation.response.send_message("Total des ressources nécessaires pour terminer toutes les technologies du Moyen-Âge Classique :\n\nRessources générales :\n" +
        "> <:pfs:1087197250595344445> Points forge x733\n> <:pieces:1087197281482199080> Pièces x53 500\n> <:marchandises:1087197265065689089> Marchandises x194 000\n"+
        "\nRessources de l'Âge du Bronze :\n> <:marbre:1087197550030901327> Marbre x94\n> <:bois:1087197572436852796> Bois x79\n> <:teinture:1087197593567772762> Teinture x90\n" +
        "> <:pierre:1087197532133806171> Pierre x66\n> <:vin:1087197513217474572> Vin x71\n\nRessources de l'Âge du Fer :\n> <:tissu:1087197391779807322> Tissu x30\n" + 
        "> <:boisdebene:1087197468917235815> Bois d'ébène x42\n> <:bijoux:1087197426407985173> Bijoux x10\n> <:fer:1087197445492047995> Fer x47\n" + 
        "> <:calcaire:1087197408372465674> Calcaire x28\n\nRessources du Haut Moyen-Âge :\n> <:cuivre:1087197301866504202> Cuivre x20\n> <:or:1087197355910115389> Or x41\n" + 
        "> <:granite:1087197333189566576> Granite x60\n> <:miel:1087197315846127726> Miel x30\n> <:albatre:1087197371034771496> Albâtre x20" +
        "\n\nRessources du Moyen-Âge Classique :\n> <:brique:1087310864434085898> Brique x40\n> <:verre:1087310822772056114> Verre x50\n" +
        "> <:herbessechees:1087310842934079489> Herbes séchées x34\n> <:corde:1087310783337218118> Corde x4\n> <:sel:1087310801926373437> Sel x11")
    if age == "REN":
        await interation.response.send_message("Total des ressources nécessaires pour terminer toutes les technologies de la Renaissance :\n\nRessources générales :\n" +
        "> <:pfs:1087197250595344445> Points forge x1 072\n> <:pieces:1087197281482199080> Pièces x155 000\n> <:marchandises:1087197265065689089> Marchandises x427 500"+
        "\n\nRessources de l'Âge du Fer :\n> <:tissu:1087197391779807322> Tissu x130\n> <:boisdebene:1087197468917235815> Bois d'ébène x140\n" +
        "> <:bijoux:1087197426407985173> Bijoux x140\n> <:fer:1087197445492047995> Fer x100\n> <:calcaire:1087197408372465674> Calcaire x150\n\n" +
        "Ressources du Haut Moyen-Âge :\n> <:cuivre:1087197301866504202> Cuivre x150\n> <:or:1087197355910115389> Or x110\n" + 
        "> <:granite:1087197333189566576> Granite x140\n> <:miel:1087197315846127726> Miel x140\n> <:albatre:1087197371034771496> Albâtre x200" +
        "\n\nRessources du Moyen-Âge Classique :\n> <:brique:1087310864434085898> Brique x60\n> <:verre:1087310822772056114> Verre x80\n" +
        "> <:herbessechees:1087310842934079489> Herbes séchées x80\n> <:corde:1087310783337218118> Corde x120\n> <:sel:1087310801926373437> Sel x100\n\n" +
        "Ressources de la Renaissance :\n> <:basalte:1087311977686241371> Basalte x80\n> <:laiton:1087311943280361503> Laiton x50\n> <:poudrecanon:1087311883909988422>" +
        " Poudre à canon x50\n> <:soie:1087311860744855582> Soie x40\n> <:poudretalquer:1087311792952320011> Poudre à talquer x70")
    if age == "COLO": # Terminé Ress générales, reste ress des âges à faire
        await interation.response.send_message("Total des ressources nécessaires pour terminer toutes les technologies de l'Âge Colonial :\n\nRessources générales :\n" +
        "> <:pfs:1087197250595344445> Points forge x1 000\n> <:pieces:1087197281482199080> Pièces x115 337\n> <:marchandises:1087197265065689089> Marchandises x421 870"+
        "\n\nRessources du Haut Moyen-Âge :\n> <:cuivre:1087197301866504202> Cuivre x150\n> <:or:1087197355910115389> Or x110\n" + 
        "> <:granite:1087197333189566576> Granite x140\n> <:miel:1087197315846127726> Miel x140\n> <:albatre:1087197371034771496> Albâtre x200" +
        "\n\nRessources du Moyen-Âge Classique :\n> <:brique:1087310864434085898> Brique x60\n> <:verre:1087310822772056114> Verre x80\n" +
        "> <:herbessechees:1087310842934079489> Herbes séchées x80\n> <:corde:1087310783337218118> Corde x120\n> <:sel:1087310801926373437> Sel x100\n\n" +
        "Ressources de la Renaissance :\n> <:basalte:1087311977686241371> Basalte x80\n> <:laiton:1087311943280361503> Laiton x50\n> <:poudrecanon:1087311883909988422>" +
        " Poudre à canon x50\n> <:soie:1087311860744855582> Soie x40\n> <:poudretalquer:1087311792952320011> Poudre à talquer x70\n\nRessources de l'âge Colonial :\n" +
        "> <:cafe:1087332129546977361> Café x\n> <:papier:1087332160895189103> Papier x\n> <:porcelaine:1087332179509514320> Porcelaine x\n> <:goudron:1087332196647456768> Goudron x\n" +
        "> <:fil:1087332103328378910> Fil x")
    if age == "INDUS": # Template vide, données non encore remplies
        await interation.response.send_message("Total des ressources nécessaires pour terminer toutes les technologies de l'Âge Industriel :\n\nRessources générales :\n" +
        "> <:pfs:1087197250595344445> Points forge x1 000\n> <:pieces:1087197281482199080> Pièces x115 337\n> <:marchandises:1087197265065689089> Marchandises x421 870"+
        "\n\nRessources du Haut Moyen-Âge :\n> <:cuivre:1087197301866504202> Cuivre x150\n> <:or:1087197355910115389> Or x110\n" + 
        "> <:granite:1087197333189566576> Granite x140\n> <:miel:1087197315846127726> Miel x140\n> <:albatre:1087197371034771496> Albâtre x200" +
        "\n\nRessources du Moyen-Âge Classique :\n> <:brique:1087310864434085898> Brique x60\n> <:verre:1087310822772056114> Verre x80\n" +
        "> <:herbessechees:1087310842934079489> Herbes séchées x80\n> <:corde:1087310783337218118> Corde x120\n> <:sel:1087310801926373437> Sel x100\n\n" +
        "Ressources de la Renaissance :\n> <:basalte:1087311977686241371> Basalte x80\n> <:laiton:1087311943280361503> Laiton x50\n> <:poudrecanon:1087311883909988422>" +
        " Poudre à canon x50\n> <:soie:1087311860744855582> Soie x40\n> <:poudretalquer:1087311792952320011> Poudre à talquer x70\n\nRessources de l'âge Colonial :\n" +
        "> <:cafe:1087332129546977361> Café x\n> <:papier:1087332160895189103> Papier x\n> <:porcelaine:1087332179509514320> Porcelaine x\n> <:goudron:1087332196647456768> Goudron x\n" +
        "> <:fil:1087332103328378910> Fil x\n\nRessources de l'Âge Industriel :\n> <:coke:1087332304436867122> Coke x\n" +
        "> <:engrais:1087332224199835688> Engrais x\n> <:caoutchouc:1087332264880377946> Caoutchouc x\n> <:textile:1087332336733016154> Textile x\n" +
        "> <:huildedebaleine:1087332356307812402> Huile de baleine x")
    if age == "PROG": # Template vide, données non encore remplies
        await interation.response.send_message("Total des ressources nécessaires pour terminer toutes les technologies de l'Ère Progressiste :\n\nRessources générales :\n" +
        "> <:pfs:1087197250595344445> Points forge x1 000\n> <:pieces:1087197281482199080> Pièces x115 337\n> <:marchandises:1087197265065689089> Marchandises x421 870"+
        "\n\nRessources du Haut Moyen-Âge :\n> <:cuivre:1087197301866504202> Cuivre x150\n> <:or:1087197355910115389> Or x110\n" + 
        "> <:granite:1087197333189566576> Granite x140\n> <:miel:1087197315846127726> Miel x140\n> <:albatre:1087197371034771496> Albâtre x200" +
        "\n\nRessources du Moyen-Âge Classique :\n> <:brique:1087310864434085898> Brique x60\n> <:verre:1087310822772056114> Verre x80\n" +
        "> <:herbessechees:1087310842934079489> Herbes séchées x80\n> <:corde:1087310783337218118> Corde x120\n> <:sel:1087310801926373437> Sel x100\n\n" +
        "Ressources de la Renaissance :\n> <:basalte:1087311977686241371> Basalte x80\n> <:laiton:1087311943280361503> Laiton x50\n> <:poudrecanon:1087311883909988422>" +
        " Poudre à canon x50\n> <:soie:1087311860744855582> Soie x40\n> <:poudretalquer:1087311792952320011> Poudre à talquer x70\n\nRessources de l'âge Colonial :\n" +
        "> <:cafe:1087332129546977361> Café x\n> <:papier:1087332160895189103> Papier x\n> <:porcelaine:1087332179509514320> Porcelaine x\n> <:goudron:1087332196647456768> Goudron x\n" +
        "> <:fil:1087332103328378910> Fil x\n\nRessources de l'Âge Industriel :\n> <:coke:1087332304436867122> Coke x\n" +
        "> <:engrais:1087332224199835688> Engrais x\n> <:caoutchouc:1087332264880377946> Caoutchouc x\n> <:textile:1087332336733016154> Textile x\n" +
        "> <:huildedebaleine:1087332356307812402> Huile de baleine x\n\nRessources de l'Ère Progressiste :\n> <:amiante:1087332385667952751> Amiante x\n" +
        "> <:explosif:1087332458460086322> Explosif x\n> <:piecedetachee:1087332427950719057> Pièce détachée x\n> <:essence:1087332408627560549> Essence x\n" +
        "> <:ferblanc:1087332495252521010> Fer blanc x")

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
            else:
                await message.add_reaction("<:poogie:964488145041256508>")

    if "gimme emoji" in user_message.lower():
        for emoji in message.guild.emojis:
            print(emoji.name)
            print(emoji.id)


def launch():
    bot.run(token)