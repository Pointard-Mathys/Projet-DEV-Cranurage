
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


from dis import disco
import os
# from socket import send_fds
from unittest import result
from urllib import response
from click import launch
import discord
import random
import typing
import interactions
import numpy as np
import math
from discord import Embed
from discord.ext import commands
from discord.ext.tasks import loop
from discord import app_commands
from dotenv import load_dotenv
from pulp import *
from Request_SQL import name_from, element_from, critical_from, materials_from
# from scipy.optimize import linprog
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

# COMMANDES MOGAPÉDIA

@tree.command(name="mhfzzhelp", description="Aide pour l'utilisation des commandes liées à Monster Hunter Frontier Z Zenith.")
async def self(interation: discord.Interaction):
    await interation.response.send_message("En cours de construction !")

@tree.command(name="mhfzzinstall", description="Guide d'installation de Monster Hunter Frontier Z Zenith.")
async def self(interation: discord.Interaction):
    await interation.response.send_message("Lien de téléchargement des fichiers : https://drive.google.com/file/d/14WJcwhDAlr_8l_eZkarR6oKRHpQdi-Wy/view\n")

@tree.command(name="mhfzzweapon", description="Obtenir des informations sur une arme.")
async def self(interation: discord.Interaction):
    result = name_from('tonfa', 'Enrapture Tonfa "Solo"')
    embed=discord.Embed(title="weapon_type", description="Armes disponibles pour les paramètres sélectionnés :", color=0xff0000)
    embed.set_author(name="HeroFactory#0311", url="https://discord.gg/f77VwBX5w7", icon_url="https://cdn.discordapp.com/attachments/662904063058509836/1097454406015914045/Elder_Fatalis_armor_.png")
    embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/662904063058509836/1097474419795968010/Mini_Poogie_trop_cute.png")
    embed.add_field(name="Nom de l'arme :", value=result[0][0], inline=True)
    embed.add_field(name="Attaque :", value=result[0][2], inline=True)
    embed.add_field(name="Élement :", value="weapon_element", inline=True)
    embed.add_field(name="Affinité :", value="weapon_affinity", inline=True)
    # embed.add_field(name="​", value="​", inline=False)
    # embed.add_field(name="Nom de l'arme :", value="weapon_name", inline=True)
    # embed.add_field(name="Attaque :", value="weapon_attack", inline=True)
    # embed.add_field(name="Élement :", value="weapon_element", inline=True)
    # embed.add_field(name="Affinité :", value="weapon_affinity", inline=True)
    # embed.add_field(name="​", value="​", inline=False)
    # embed.add_field(name="Nom de l'arme :", value="weapon_name", inline=True)
    # embed.add_field(name="Attaque :", value="weapon_attack", inline=True)
    # embed.add_field(name="Élement :", value="weapon_element", inline=True)
    # embed.add_field(name="Affinité :", value="weapon_affinity", inline=True)
    # embed.add_field(name="​", value="​", inline=False)
    # embed.add_field(name="Nom de l'arme :", value="weapon_name", inline=True)
    # embed.add_field(name="Attaque :", value="weapon_attack", inline=True)
    # embed.add_field(name="Élement :", value="weapon_element", inline=True)
    # embed.add_field(name="Affinité :", value="weapon_affinity", inline=True)
    # embed.add_field(name="​", value="​​", inline=False)
    # embed.add_field(name="Nom de l'arme :", value="weapon_name", inline=True)
    # embed.add_field(name="Attaque :", value="weapon_attack", inline=True)
    # embed.add_field(name="Élement :", value="weapon_element", inline=True)
    # embed.add_field(name="Affinité :", value="weapon_affinity", inline=True)

    
    # second_embed=discord.Embed(title="weapon_type", description="Armes disponibles pour les paramètres sélectionnés :", color=0xff0000)
    # second_embed.set_author(name="HeroFactory#0311", url="https://discord.gg/f77VwBX5w7", icon_url="https://cdn.discordapp.com/attachments/662904063058509836/1097454406015914045/Elder_Fatalis_armor_.png")
    # second_embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/662904063058509836/1097454114671186001/Mini_Poogie_trop_cute.ico")
    # second_embed.add_field(name="Nom de l'arme :", value="weapon_name", inline=True)
    # second_embed.add_field(name="Attaque :", value="weapon_attack", inline=True)
    # second_embed.add_field(name="Élement :", value="weapon_element", inline=True)
    # second_embed.add_field(name="Affinité :", value="weapon_affinity", inline=True)
    # second_embed.add_field(name="​", value="​", inline=False)
    # second_embed.add_field(name="Nom de l'arme :", value="weapon_name", inline=True)
    # second_embed.add_field(name="Attaque :", value="weapon_attack", inline=True)
    # second_embed.add_field(name="Élement :", value="weapon_element", inline=True)
    # second_embed.add_field(name="Affinité :", value="weapon_affinity", inline=True)
    # second_embed.add_field(name="​", value="​", inline=False)
    # second_embed.add_field(name="Nom de l'arme :", value="weapon_name", inline=True)
    # second_embed.add_field(name="Attaque :", value="weapon_attack", inline=True)
    # second_embed.add_field(name="Élement :", value="weapon_element", inline=True)
    # second_embed.add_field(name="Affinité :", value="weapon_affinity", inline=True)
    # second_embed.add_field(name="​", value="​", inline=False)
    # second_embed.add_field(name="Nom de l'arme :", value="weapon_name", inline=True)
    # second_embed.add_field(name="Attaque :", value="weapon_attack", inline=True)
    # second_embed.add_field(name="Élement :", value="weapon_element", inline=True)
    # second_embed.add_field(name="Affinité :", value="weapon_affinity", inline=True)
    # second_embed.add_field(name="​", value="​​", inline=False)
    # second_embed.add_field(name="Nom de l'arme :", value="weapon_name", inline=True)
    # second_embed.add_field(name="Attaque :", value="weapon_attack", inline=True)
    # second_embed.add_field(name="Élement :", value="weapon_element", inline=True)
    # second_embed.add_field(name="Affinité :", value="weapon_affinity", inline=True)
    if len(result) > 10:
        await interation.response.send_message("Il y a trop d'armes qui remplissent les critères de recherche. Rendez-vous sur "+
        "https://xl3lackout.github.io/MHFZ-Ferias-English-Project/buki/bukiF.htm et lancez une recherche sur la page de l'arme de votre choix (Ctrl + F).")
    else:
        await interation.response.send_message(embed=embed)

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
        "> <:pfs:1087197250595344445> Points forge x127\n> <:pieces:1087197281482199080> Pièces x2 300\n> <:marchandises:1087197265065689089> Marchandises x2 300\n"+
        "\nRessources de l'Âge du Bronze :\n> <:marbre:1087197550030901327> Marbre x2\n> <:bois:1087197572436852796> Bois x2")
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
    if age == "COLO":
        await interation.response.send_message("Total des ressources nécessaires pour terminer toutes les technologies de l'Âge Colonial :\n\nRessources générales :\n" +
        "> <:pfs:1087197250595344445> Points forge x1 000\n> <:pieces:1087197281482199080> Pièces x115 337\n> <:marchandises:1087197265065689089> Marchandises x421 870"+
        "\n\nRessources du Haut Moyen-Âge :\n> <:cuivre:1087197301866504202> Cuivre x160\n> <:or:1087197355910115389> Or x170\n" + 
        "> <:granite:1087197333189566576> Granite x150\n> <:miel:1087197315846127726> Miel x160\n> <:albatre:1087197371034771496> Albâtre x120" +
        "\n\nRessources du Moyen-Âge Classique :\n> <:brique:1087310864434085898> Brique x100\n> <:verre:1087310822772056114> Verre x130\n" +
        "> <:herbessechees:1087310842934079489> Herbes séchées x110\n> <:corde:1087310783337218118> Corde x110\n> <:sel:1087310801926373437> Sel x100\n\n" +
        "Ressources de la Renaissance :\n> <:basalte:1087311977686241371> Basalte x160\n> <:laiton:1087311943280361503> Laiton x140\n> <:poudrecanon:1087311883909988422>" +
        " Poudre à canon x150\n> <:soie:1087311860744855582> Soie x150\n> <:poudretalquer:1087311792952320011> Poudre à talquer x140\n\nRessources de l'âge Colonial :\n" +
        "> <:cafe:1087332129546977361> Café x40\n> <:papier:1087332160895189103> Papier x80\n> <:porcelaine:1087332179509514320> Porcelaine x60\n> " +
        "<:goudron:1087332196647456768> Goudron x40\n> <:fil:1087332103328378910> Fil x80")
    if age == "INDUS":
        await interation.response.send_message("Total des ressources nécessaires pour terminer toutes les technologies de l'Âge Industriel :\n\nRessources générales :\n" +
        "> <:pfs:1087197250595344445> Points forge x1 010\n> <:pieces:1087197281482199080> Pièces x303 000\n> <:marchandises:1087197265065689089> Marchandises x1 798 000"+
        "\n\nRessources du Moyen-Âge Classique :\n> <:brique:1087310864434085898> Brique x220\n> <:verre:1087310822772056114> Verre x160\n" +
        "> <:herbessechees:1087310842934079489> Herbes séchées x190\n> <:corde:1087310783337218118> Corde x190\n> <:sel:1087310801926373437> Sel x210\n\n" +
        "Ressources de la Renaissance :\n> <:basalte:1087311977686241371> Basalte x170\n> <:laiton:1087311943280361503> Laiton x260\n> <:poudrecanon:1087311883909988422>" +
        " Poudre à canon x210\n> <:soie:1087311860744855582> Soie x230\n> <:poudretalquer:1087311792952320011> Poudre à talquer x130\n\nRessources de l'âge Colonial :\n" +
        "> <:cafe:1087332129546977361> Café x170\n> <:papier:1087332160895189103> Papier x120\n> <:porcelaine:1087332179509514320> Porcelaine x160\n" +
        "> <:goudron:1087332196647456768> Goudron x150\n> <:fil:1087332103328378910> Fil x160\n\nRessources de l'Âge Industriel :\n> <:coke:1087332304436867122> Coke x105\n" +
        "> <:engrais:1087332224199835688> Engrais x95\n> <:caoutchouc:1087332264880377946> Caoutchouc x160\n> <:textile:1087332336733016154> Textile x100\n" +
        "> <:huildedebaleine:1087332356307812402> Huile de baleine x110")
    if age == "PROG":
        await interation.response.send_message("Total des ressources nécessaires pour terminer toutes les technologies de l'Ère Progressiste :\n\nRessources générales :\n" +
        "> <:pfs:1087197250595344445> Points forge x1 430\n> <:pieces:1087197281482199080> Pièces x514 111\n> <:marchandises:1087197265065689089> Marchandises x2 026 111"+
        "\n\nRessources de la Renaissance :\n> <:basalte:1087311977686241371> Basalte x180\n> <:laiton:1087311943280361503> Laiton x210\n> <:poudrecanon:1087311883909988422>" +
        " Poudre à canon x160\n> <:soie:1087311860744855582> Soie x150\n> <:poudretalquer:1087311792952320011> Poudre à talquer x240\n\nRessources de l'âge Colonial :\n" +
        "> <:cafe:1087332129546977361> Café x320\n> <:papier:1087332160895189103> Papier x220\n> <:porcelaine:1087332179509514320> Porcelaine x380\n" +
        "> <:goudron:1087332196647456768> Goudron x320\n> <:fil:1087332103328378910> Fil x250\n\nRessources de l'Âge Industriel :\n> <:coke:1087332304436867122> Coke x180\n" +
        "> <:engrais:1087332224199835688> Engrais x275\n> <:caoutchouc:1087332264880377946> Caoutchouc x260\n> <:textile:1087332336733016154> Textile x230\n" +
        "> <:huildedebaleine:1087332356307812402> Huile de baleine x220\n\nRessources de l'Ère Progressiste :\n> <:amiante:1087332385667952751> Amiante x330\n" +
        "> <:explosif:1087332458460086322> Explosif x300\n> <:piecedetachee:1087332427950719057> Pièce détachée x330\n> <:essence:1087332408627560549> Essence x300\n" +
        "> <:ferblanc:1087332495252521010> Fer blanc x350")

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

# @tree.command(name="grepodefensecalculator", description="Retourne la meilleure défense possible pour un montant de population donné.")
# async def self(interation: discord.Interaction, population: int):
#     if population < 5000:
#         # Units' statistics
#         hoplite_stats = [18, 12, 7]
#         swordsman_stats = [14, 8, 30]
#         bowman_stats = [7, 25, 13]

#         # Define the problem as a minimization problem
#         prob = LpProblem("Most Balanced Defense", LpMinimize)

#         # Define the decision variables
#         x1 = LpVariable("x1", 0, None, LpInteger)
#         x2 = LpVariable("x2", 0, None, LpInteger)
#         x3 = LpVariable("x3", 0, None, LpInteger)

#         # Define the objective function
#         prob += lpSum([hoplite_stats[i]*x1 + swordsman_stats[i]*x2 + bowman_stats[i]*x3 for i in range(3)])

#         # Define the constraints
#         prob += x1 + x2 + x3 == population
#         prob += hoplite_stats[0]*x1 + swordsman_stats[0]*x2 + bowman_stats[0]*x3 >= 0.33*lpSum([hoplite_stats[i]*x1 + swordsman_stats[i]*x2 + bowman_stats[i]*x3 for i in range(3)])
#         prob += hoplite_stats[1]*x1 + swordsman_stats[1]*x2 + bowman_stats[1]*x3 >= 0.33*lpSum([hoplite_stats[i]*x1 + swordsman_stats[i]*x2 + bowman_stats[i]*x3 for i in range(3)])
#         prob += hoplite_stats[2]*x1 + swordsman_stats[2]*x2 + bowman_stats[2]*x3 >= 0.33*lpSum([hoplite_stats[i]*x1 + swordsman_stats[i]*x2 + bowman_stats[i]*x3 for i in range(3)])

#         # Solve the problem
#         prob.solve()

#         # Check if the problem has an optimal solution
#         if LpStatus[prob.status] != "Optimal":
#             await interation.response.send_message("Il y a trop peu de population pour pouvoir faire un véritable équilibrage.")
#             return

#         # Convert the decision variables to integers and return their values
#         x1_value = int(x1.value())
#         x2_value = int(x2.value())
#         x3_value = int(x3.value())

#         await interation.response.send_message(f"La composition défensive la plus optimisée avec {population} habitants est la suivante :\n\n"+
#         f"{x1_value} Hoplites\n{x2_value} CE\n{x3_value} Archers\n\nPour le total défensif suivant :\n" +
#         f"{hoplite_stats[0] * x1_value + swordsman_stats[0] * x2_value + bowman_stats[0] * x3_value}\n" +
#         f"{hoplite_stats[1] * x1_value + swordsman_stats[1] * x2_value + bowman_stats[1] * x3_value}\n" +
#         f"{hoplite_stats[2] * x1_value + swordsman_stats[2] * x2_value + bowman_stats[2] * x3_value}\n")

#     else:
#         await interation.response.send_message(f"Une ville ne peut pas avoir {population} habitants !")


@tree.command(name="grepooffcalculator", description="Retourne le nombre de troupes faisables pour un montant de BFx, de Catas et de population donné.")
async def self(interation: discord.Interaction, population_totale: int, nombre_de_catapultes: int, nombre_de_bfx: int):
    start_pop = population_totale
    if population_totale < 5000:

        pop_cata = nombre_de_catapultes * 15
        population_totale -= 10 * nombre_de_bfx
        population_totale -= pop_cata
        pop_btr = population_totale -5
        pop_bt = population_totale -7
        pop_same_island = population_totale

        if population_totale <= 0:
            await interation.response.send_message("Il y a trop de catapultes ou de BFx par rapport à la population donnée !")
            return

        btr_count = 1
        bt_count = 1

        btr_unit_count = 0
        bt_unit_count = 0
        unit_count = 0

        btr_capacity = 16
        bt_capacity = 32

        btr_message = ""
        bt_message = ""

        btr_count += math.ceil(pop_cata / 16)
        if btr_count * 5 > population_totale:
            btr_message += f"Il y a trop de catapultes pour transporter ce montant de population en BTR avec {nombre_de_bfx} BFx."
        else:
            btr_capacity += 16 - pop_cata % 16
            btr_unit_count += pop_cata
        print("BTR capacity : ", btr_capacity)
        print("BTR unity count : ", btr_unit_count)
        print("Première pop BTR  :", pop_btr)

        bt_count += math.ceil(pop_cata / 32)
        if bt_count * 7 > population_totale:
            bt_message += f"Il y a trop de catapultes pour transporter ce montant de population en BT avec {nombre_de_bfx} BFx."
        else:
            bt_capacity += 32 - pop_cata % 32
            bt_unit_count += pop_cata

        while pop_btr > 0:
            if btr_capacity > 0:
                pop_btr -= 1
                btr_capacity -= 1
                btr_unit_count += 1
            if btr_capacity == 0 and pop_btr >= 5:
                pop_btr -= 5
                btr_count += 1
                btr_capacity = 16
            elif btr_capacity == 0:
                pop_btr = 0
            if pop_btr <= 5:
                pop_btr = 0
            print("Pop BTR :", pop_btr)
            print("BTR units count :", btr_unit_count)
            print("BTR count :", btr_count)
            print("Total pop : ", btr_unit_count + btr_count * 5)

        while pop_bt > 0:
            if bt_capacity > 0:
                pop_bt -= 1
                bt_capacity -= 1
                bt_unit_count += 1
            if bt_capacity == 0 and pop_bt >= 7:
                pop_bt -= 7
                bt_count += 1
                bt_capacity = 32
            elif bt_capacity == 0:
                pop_bt = 0
            if pop_bt <= 7:
                pop_bt = 0
            print("Pop BT :", pop_bt)
            print("BT units count :", bt_unit_count)

        # while pop_btr > 0:
        #     pop_btr -= 1
        #     btr_unit_count += 1
        #     if pop_btr - 5 < 0:
        #         pop_btr = 0
        #     elif btr_unit_count % 16 == 0 and pop_btr - 5 >= 0:
        #         pop_btr -= 5
        #         btr_count += 1
        #         btr_capacity = btr_count * 16

        # while pop_bt > 0:
        #     pop_bt -= 1
        #     bt_unit_count += 1
        #     if pop_bt - 7 < 0:
        #         pop_bt = 0
        #     elif bt_unit_count % 32 == 0 and pop_bt - 7 >= 0:
        #         pop_bt -= 7
        #         bt_count += 1
        #         bt_capacity = bt_count * 32

        btr_unit_count -= pop_cata
        bt_unit_count -= pop_cata
        print("Last BTR unit count :", btr_unit_count)

        while pop_same_island > 0:
            pop_same_island -= 1
            unit_count += 1

        # if btr_capacity < btr_unit_count:
        #     return

        # if bt_capacity < bt_unit_count:
        #     return

        # if btr_unit_count < 0:
        #     btr_message += f"Il y a trop de catapultes pour transporter ce montant de population en BTR avec {nombre_de_bfx} BFx."
        if pop_btr == 0:
            btr_message = f"- En BTR :\n{btr_unit_count} Fr / Hop ou {math.floor(btr_unit_count / 3)} Cavas, transportés par {btr_count} BTR avec {nombre_de_bfx} BFx."+ \
            f"\nAvec les Fr / Hop, il restera {start_pop - (btr_unit_count + 5 * btr_count + 15 * nombre_de_catapultes + 10 * nombre_de_bfx)} habitants dans la ville."+\
                f"\nAvec les Cavas, il restera {start_pop - (btr_unit_count - btr_unit_count % 3 + 5 * btr_count + 15 * nombre_de_catapultes + 10 * nombre_de_bfx)} habitants dans la ville."

        # if bt_unit_count < 0:
        #     bt_message += f"Il y a trop de catapultes pour transporter ce montant de population en BT avec {nombre_de_bfx} BFx."
        if pop_bt == 0:
            bt_message = f"- En BT :\n{bt_unit_count} Fr / Hop ou {math.floor(bt_unit_count / 3)} Cavas, transportés par {bt_count} BT avec {nombre_de_bfx} BFx."+ \
            f"\nAvec les Fr / Hop, il restera {start_pop - (bt_unit_count + 7 * bt_count + 15 * nombre_de_catapultes + 10 * nombre_de_bfx)} habitants dans la ville." +\
                f"\nAvec les Cavas, il restera {start_pop - (bt_unit_count - bt_unit_count % 3 + 7 * bt_count + 15 * nombre_de_catapultes + 10 * nombre_de_bfx)} habitants dans la ville."

        await interation.response.send_message(f"Avec {start_pop} habitants, {nombre_de_bfx} BFx et {nombre_de_catapultes} Catas, une OT sera composée de :\n\n"+
        f"- Sur la même île :\n{unit_count} Fr / Hop ou {math.floor(unit_count / 3)} Cavas (dans ce cas, il restera {unit_count % 3} habitants dans la ville)." +
        f"\n\n{btr_message}\n\n{bt_message}")
        return
    else:
        await interation.response.send_message(f"Une ville ne peut pas avoir {population_totale} habitants !")



#----------------------------------------------------------------------------------------------------------------

@bot.event
async def on_message(message):
    user_message = message.content
    print(user_message)

    if  "poogie" in user_message.lower():
        hasPoogie = False
        for emoji in message.guild.emojis:
            if emoji.name.lower() == "poogiedancing":
                await message.add_reaction(emoji)
            elif emoji.name.lower() == "poogie":
                hasPoogie = True
                await message.add_reaction(emoji)
        if hasPoogie == False:
            await message.add_reaction("<:poogie:964488145041256508>")

    if "gimme emoji" in user_message.lower():
        for emoji in message.guild.emojis:
            print(emoji.name)
            print(emoji.id)


#----------------------------------------------------------------------------------------------------------------

def launch():
    bot.run(token)