from dis import disco
from email import message
from email.policy import default
from http import client
import os
from pydoc import describe
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
from Request_SQL import name_from, global_search
import grepolis
from num2words import num2words
import usefullfunctions
from itertools import product
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

# COMMANDES GLOBALES

@tree.command(name="pang", description="Yes, Cranaruge is here.")
async def self(interation: discord.Interaction):
    await interation.response.send_message("Poogie pongs you.")

@tree.command(name="poll", description="Make a simple Discord poll. Separate each option with a semicolon \";\".")
@app_commands.describe(
    options="The options you want to set in your poll. Separate each one with a semicolon \";\".",
    title="Title of your poll.",
    description="An explicative text to explain users what is your poll about.",
    channel="Channel name where Cranaruge will send the poll. NOT FUNCTIONAL"
)
async def self(interation: discord.Interaction, options: str, title: typing.Optional[str] = "Poll", description: typing.Optional[str] = "This is a sample description", channel: typing.Optional[str] = ""):
    if options.count(";") >= 1:
        poll = usefullfunctions.createPoll(title, options, description)
        await interation.response.send_message("Poll created.", ephemeral=True)
        msg = await interation.channel.send(embed=poll)
        for idx, _ in enumerate(options.split(";", 10)):
            await msg.add_reaction(f'{idx}\N{COMBINING ENCLOSING KEYCAP}')
        return
    await interation.response.send_message("This poll has less than two options!")
    return

# COMMANDES MOGAPÉDIA

@tree.command(name="mhfzzhelp", description="Aide pour l'utilisation des commandes liées à Monster Hunter Frontier Z Zenith.")
async def self(interation: discord.Interaction, commande: typing.Literal["help", "install", "hr5guide", "weapon", "weaponname"]):
    response = f"# Guide d'utilisation de la commande ``mhfzz{commande}``\n\n"

    match commande:
        case "help":
            response += f"La commande ``/mhfzz{commande}`` permet d'obtenir un guide d'utilisation de toutes les commandes liées à Monster Hunter Frontier Z Zenith.\n"\
                "### Liste des commandes disponibles :\n- ``/mhfzzhelp``\n- ``/mhfzzinstall``\n- ``/mhfzzhr5guide``\n- ``/mhfzzweapon``\n- ``/mhfzzweaponname``"
        case "install":
            response += f"Tapez ``/mhfzz{commande}`` pour obtenir un lien permettant d'installer Monster Hunter Frontier Z Zenith gratuitement !"
        case "hr5guide":
            response += f"Tapez ``/mhfzz{commande} pour obtenir un lien vers un guide des nouveautés du RC5 dans Frontier."
        case "weapon":
            response += f"Tapez ``/mhfzz{commande}`` pour rechercher une arme dans la base de données de Frontier. L'affichage des données des armes artilleur est en cours de construction.\n" \
                "### Critères de recherche :\n- type_d_arme (**obligatoire**) : le type d'arme que vous recherchez. À choisir parmi une liste d'options.\n"\
                    "- element (optionnel) : l'élément de l'arme que vous recherchez. Inclut aussi les éléments combinés et les statuts. À choisir parmi une liste d'options.\n"\
                        "- affinite (optionnel) : la valeur de l'affinité que l'arme doit avoir. Attention : il s'agit d'une valeur exacte d'affinité, la recherche n'incluera pas de résultat ayant une affinité différente de la valeur saisie.\n"\
                            "- materiaux (optionnel) : précisez un ou plusieurs matériaux de création / amélioration. Il est recommandé de se baser sur les noms des matéraiux dans le jeu, ne faites pas de traduction.\n"\
                                "- rarete (optionnel) : la rareté de l'arme que vous recherchez. Attention : n'inclut que la rareté exacte sélectionnée, ignore toutes les autres. Cette option permet notamment d'affiner la recherche en fonction de votre RC."
        case "weaponname":
            response += f"Tapez ``/mhfzz{commande} pour rechercher une arme en utilisant son nom, ou une partie de son nom. L'affichage des données des armes artilleur est en cours de construction.\n"\
                "### Critères de recherche :\n- type_d_arme (**obligatoire**) : le type d'arme que vous recherchez.\n"\
                    "- nom (**obligatoire**) : le nom ou une partie du nom de l'arme que vous recherchez."
        case _:
            response += "Cette commande n'existe pas !"

    await interation.response.send_message(response)

@tree.command(name="mhfzzinstall", description="Guide d'installation de Monster Hunter Frontier Z Zenith.")
async def self(interation: discord.Interaction):
    await interation.response.send_message("Cliquez [ici](https://drive.google.com/drive/folders/1Kqc755YcnirjaHB3uhCugcLvYugArHGS) pour télécharger les fichiers MHFZZ !")

@tree.command(name="mhfzzhr5guide", description="Guide pour chasseurs arrivés au RC5.")
async def self(interation: discord.Interaction):
    await interation.response.send_message("[Ce document](https://docs.google.com/document/d/1HF-Y5eNk3Zbzk6PY7G8KiPJhMYQHSbgw) explique les nouveautés qui arrivent à partir du RC5, et comment passer outre le pic de difficulté imposé par le jeu.\n"\
        "### Guide épéiste uniquement.")

# @tree.command(name="mhfzzsetup", description="Guide pour les joueurs ayant déjà installé le jeu sans passer par la Mogapédia.")
# async def self(interation: discord.Interaction):
#     await interation.response.send_message("Si vous avez déjà installé Monster Hunter Frontier Z Zenith sans passer par la Mogapédia, suivez les instructions suivantes :\n\n")

@tree.command(name="mhfzzweapon", description="Obtenir des informations sur une arme.")
@app_commands.describe(
    type_d_arme="Le type d'arme à rechercher.",
    element="L'attribut que l'arme doit avoir. Inclut aussi les statuts et éléments combinés. Optionnel.",
    affinite="L'affinité de l'arme. Optionnel.",
    materiaux="Un ou plusieurs matériaux nécessaire à la réalisation de l'arme. Référez-vous aux noms dans le jeu. Optionnel.",
    rarete="La rareté de l'arme recherchée. Optionnel."
)
async def self(interation: discord.Interaction, type_d_arme: typing.Literal["Grande épée", "Épée longue", "Épée & Bouclier", "Lames doubles", "Marteau", "Lance", "Lancecanon", "Corne de chasse", "Morpho-hache", "Tonfas", "Magnet Spike", "Fusarbalète léger", "Fusarbalète lourd", "Arc"],
element: typing.Optional[typing.Literal["Feu", "Eau", "Foudre", "Glace", "Dragon", "Brasier", "Lumière", "Foudre magnétique", "Tenshou", "Séraphim Glacé", "Sou", "Flamme noire", "Ténèbre", "Démon rougeoyant", "Empereur céleste", "Burning Zero", "Vent", "Bruit", "Poison", "Paralysie", "Sommeil", "Explosion"]] = "",
affinite: typing.Optional[int] = 0, materiaux: typing.Optional[str] = "", rarete: typing.Optional[typing.Literal[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]] = 0):
    weapon_type = ""
    match type_d_arme:
        case "Grande épée":
            weapon_type = "great_sword"
        case "Épée longue":
            weapon_type = "long_sword"
        case "Épée & Bouclier":
            weapon_type = "sword_and_shield"
        case "Lames doubles":
            weapon_type = "dual_swords"
        case "Marteau":
            weapon_type = "hammer"
        case "Lance":
            weapon_type = "lance"
        case "Lancecanon":
            weapon_type = "gunlance"
        case "Corne de chasse":
            weapon_type = "hunting_horn"
        case "Morpho-hache":
            weapon_type = "switch_axe"
        case "Tonfas":
            weapon_type = "tonfa"
        case "Magnet Spike":
            weapon_type = "magnet_spike"
        case "Fusarbalète léger":
            weapon_type = "light_bowgun"
        case "Fusarbalète lourd":
            weapon_type = "heavy_bowgun"
        case "Arc":
            weapon_type = "bows"

    match element:
        case "Feu":
            element = "fire"
        case "Eau":
            element = "water"
        case "Foudre":
            element = "thunder"
        case "Glace":
            element = "ice"
        case  "Dragon":
            element = "dragon"
        case "Brasier":
            element = "blaze"
        case "Lumière":
            element = "light"
        case "Foudre magnétique":
            element = "thunder pole"
        case "Flamme noire":
            element = "black flame"
        case "Ténèbre":
            element = "darkness"
        case "Démon rougeoyant":
            element = "crimson demon"
        case "Burning Zero":
            element = "burning zero"
        case "Vent":
            element = "wind"
        case "Bruit":
            element = "sound"
        case "Empereur céleste":
            element = "emperor's roar"
        case "Poison":
            element = "poison"
        case "Paralysie":
            element = "para"
        case "Sommeil":
            element = "sleep"


    results = global_search(table=weapon_type, element=element, affinity=affinite, materials=materiaux.lower(), rarity=rarete)
    print(results)
    if len(results) == 0:
        await interation.response.send_message("Aucune arme ne correspond aux critères sélectionnés.")
        return
    embed=discord.Embed(title=type_d_arme, description="Armes disponibles pour les paramètres sélectionnés :", color=0xff0000)
    embed.set_author(name="HeroFactory#0311", url="https://discord.gg/f77VwBX5w7", icon_url="https://cdn.discordapp.com/attachments/662904063058509836/1097454406015914045/Elder_Fatalis_armor_.png")
    embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/662904063058509836/1097474419795968010/Mini_Poogie_trop_cute.png")
    if len(results) > 4:
        tmp_res = results[0:4]
        for weapon in tmp_res:
            weapon_name = weapon[0]
            weapon_attack = weapon[4]
            weapon_attributes = weapon[5]
            weapon_affinity = weapon[6]
            embed.add_field(name="__Nom__ :", value=weapon_name, inline=True)
            embed.add_field(name="Attaque :", value=weapon_attack, inline=True)
            embed.add_field(name="Élement :", value=weapon_attributes, inline=True)
            embed.add_field(name="Affinité :", value=weapon_affinity, inline=True)
            embed.add_field(name="", value="", inline=True)
            embed.add_field(name="", value="", inline=True)
        await interation.response.send_message(f"Pas le bon résultat ? Réessayez en précisant davantage de critères, ou rendez-vous directement sur le site de [Ferias](https://xl3lackout.github.io/MHFZ-Ferias-English-Project/buki/bukiF.htm)\n\n" +
        f"4 résultats affichés sur {len(results)}", embed=embed)
        return
    else:
        for weapon in results:
            weapon_name = weapon[0]
            weapon_attack = weapon[4]
            weapon_attributes = weapon[5]
            weapon_affinity = weapon[6]
            embed.add_field(name="Nom :", value=weapon_name, inline=True)
            embed.add_field(name="Attaque :", value=weapon_attack, inline=True)
            embed.add_field(name="Élement :", value=weapon_attributes, inline=True)
            embed.add_field(name="Affinité :", value=weapon_affinity, inline=True)
            embed.add_field(name="", value="", inline=True)
            embed.add_field(name="", value="", inline=True)
        await interation.response.send_message(f"Pas le bon résultat ? Réessayez avec d'autres critères !", embed=embed)
        return

@tree.command(name="mhfzzweaponname", description="Rechercher une arme en utilisant son nom")
async def self(interation: discord.Interaction, type_d_arme: typing.Literal["Grande épée", "Épée longue", "Épée & Bouclier", "Lames doubles", "Marteau", "Lance", "Lancecanon", "Corne de chasse", "Morpho-hache", "Tonfas", "Magnet Spike", "Fusarbalète léger", "Fusarbalète lourd", "Arc"],
nom: str):
    weapon_type = ""
    match type_d_arme:
        case "Grande épée":
            weapon_type = "great_sword"
        case "Épée longue":
            weapon_type = "long_sword"
        case "Épée & Bouclier":
            weapon_type = "sword_and_shield"
        case "Lames doubles":
            weapon_type = "dual_swords"
        case "Marteau":
            weapon_type = "hammer"
        case "Lance":
            weapon_type = "lance"
        case "Lancecanon":
            weapon_type = "gunlance"
        case "Corne de chasse":
            weapon_type = "hunting_horn"
        case "Morpho-hache":
            weapon_type = "switch_axe"
        case "Tonfas":
            weapon_type = "tonfa"
        case "Magnet Spike":
            weapon_type = "magnet_spike"
        case "Fusarbalète léger":
            weapon_type = "light_bowgun"
        case "Fusarbalète lourd":
            weapon_type = "heavy_bowgun"
        case "Arc":
            weapon_type = "bows"

    results = name_from(weapon_type, nom.lower())

    embed=discord.Embed(title=type_d_arme, description="Armes disponibles pour les paramètres sélectionnés :", color=0xff0000)
    embed.set_author(name="HeroFactory#0311", url="https://discord.gg/f77VwBX5w7", icon_url="https://cdn.discordapp.com/attachments/662904063058509836/1097454406015914045/Elder_Fatalis_armor_.png")
    embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/662904063058509836/1097474419795968010/Mini_Poogie_trop_cute.png")
    if len(results) == 0:
        await interation.response.send_message("Aucune arme ne correspond aux critères sélectionnés.")
        return
    embed=discord.Embed(title=type_d_arme, description="Armes disponibles pour les paramètres sélectionnés :", color=0xff0000)
    embed.set_author(name="HeroFactory#0311", url="https://discord.gg/f77VwBX5w7", icon_url="https://cdn.discordapp.com/attachments/662904063058509836/1097454406015914045/Elder_Fatalis_armor_.png")
    embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/662904063058509836/1097474419795968010/Mini_Poogie_trop_cute.png")
    if len(results) > 4:
        tmp_res = results[0:4]
        for weapon in tmp_res:
            weapon_name = weapon[0]
            weapon_rarity = weapon[3]
            weapon_attack = weapon[4]
            weapon_attributes = weapon[5]
            weapon_affinity = weapon[6]
            weapon_slots = weapon[8]
            weapon_rank = weapon[9]
            embed.add_field(name="__Nom__ :", value=weapon_name, inline=True)
            embed.add_field(name="Attaque :", value=weapon_attack, inline=True)
            embed.add_field(name="Élement :", value=weapon_attributes, inline=True)
            embed.add_field(name="Affinité :", value=weapon_affinity, inline=True)
            embed.add_field(name="", value="", inline=True)
            embed.add_field(name="", value="", inline=True)
        await interation.response.send_message(f"Pas le bon résultat ? Réessayez en précisant davantage de critères, ou rendez-vous directement sur le site de [Ferias](https://xl3lackout.github.io/MHFZ-Ferias-English-Project/buki/bukiF.htm)\n\n" +
        f"4 résultats affichés sur {len(results)}", embed=embed)
        return
    elif len(results) > 1:
        for weapon in results:
            weapon_name = weapon[0]
            weapon_rarity = weapon[3]
            weapon_attack = weapon[4]
            weapon_attributes = weapon[5]
            weapon_affinity = weapon[6]
            weapon_slots = weapon[8]
            weapon_rank = weapon[9]
            embed.add_field(name="__Nom__ :", value=weapon_name, inline=True)
            embed.add_field(name="Attaque :", value=weapon_attack, inline=True)
            embed.add_field(name="Élement :", value=weapon_attributes, inline=True)
            embed.add_field(name="Affinité :", value=weapon_affinity, inline=True)
            embed.add_field(name="", value="", inline=True)
            embed.add_field(name="", value="", inline=True)
        await interation.response.send_message(f"Pas le bon résultat ? Réessayez avec d'autres critères !", embed=embed)
        return
    else:
        for weapon in results:
            weapon_name = weapon[0]
            previous_level = weapon[1]
            next_level = weapon[2]
            weapon_rarity = weapon[3]
            weapon_attack = weapon[4]
            weapon_attributes = weapon[5]
            weapon_affinity = weapon[6]
            weapon_slots = weapon[8]
            weapon_rank = weapon[9]
            weapon_crea_mats = weapon[11]
            weapon_up_mats = weapon[12]
            embed.add_field(name="__Nom de l'arme__ :", value=weapon_name, inline=True)
            embed.add_field(name="Amélioration précédente :", value=previous_level, inline=True)
            embed.add_field(name="Amélioration suivante :", value=next_level, inline=True)
            embed.add_field(name="Attaque :", value=weapon_attack, inline=True)
            embed.add_field(name="Élement :", value=weapon_attributes, inline=True)
            embed.add_field(name="Affinité :", value=weapon_affinity, inline=True)
            embed.add_field(name="Emplacements :", value=weapon_slots, inline=True)
            embed.add_field(name="Rareté :", value=weapon_rarity, inline=True)
            embed.add_field(name="Rang :", value=weapon_rank, inline=True)
            embed.add_field(name="Matériaux de création", value=weapon_crea_mats, inline=True)
            embed.add_field(name="Matériaux d'amélioration", value=weapon_up_mats, inline=True)
        await interation.response.send_message(embed=embed)
        return

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
    link = "https://wiki.fr.grepolis.com/wiki/" + tmp
    await interation.response.send_message(f"Page du wiki pour [{terme_recherché}]({link}).")

@tree.command(name="grepodefensecalculator", description="Retourne la meilleure défense possible pour un montant de population donné.")
async def self(interation: discord.Interaction, population: int):
    if population < 4500:

        response_str = f"Avec {population} habitants, une DT équilibrée s'organise comme suit :\n\n"

        btr_pop = 5
        btr_capacity = 16
        btr_count = 0
        btr_transportable_pop = 0

        if grepolis.can_fit_in_bt(population, btr_pop, btr_capacity, 0):
            btr_count += grepolis.bt_count_calculator(population, btr_pop, btr_capacity, 0)[0]
            remaining_pop = grepolis.bt_count_calculator(population, btr_pop, btr_capacity, 0)[1]
            print("btr count :", btr_count)
            print("btr pop :", btr_pop)
            print("btr remaining pop :", remaining_pop)
            print("population :", population)
            btr_transportable_pop += population - btr_count * btr_pop - remaining_pop
            print("btr trans pop :", btr_transportable_pop)
            response_str += f"{math.floor(btr_transportable_pop / 2)} Hoplites, {math.floor(btr_transportable_pop / 4)} Archers et {math.floor(btr_transportable_pop / 4)} CE transportés par {btr_count} BTR.\n" + \
            f"Les valeurs défensives sont :\n{math.floor(btr_transportable_pop / 2) * 18 + math.floor(btr_transportable_pop / 4) * 7 + math.floor(btr_transportable_pop / 4) * 14}\n" + \
                f"{math.floor(btr_transportable_pop / 2) * 12 + math.floor(btr_transportable_pop / 4) * 25 + math.floor(btr_transportable_pop / 4) * 8}\n" + \
                    f"{math.floor(btr_transportable_pop / 2) * 7 + math.floor(btr_transportable_pop / 4) * 13 + math.floor(btr_transportable_pop / 4) * 30}\n\n"

        bt_pop = 7
        bt_capacity = 32
        bt_count = 0
        bt_transportable_pop = 0

        if grepolis.can_fit_in_bt(population, bt_pop, bt_capacity, 0):
            bt_count += grepolis.bt_count_calculator(population, bt_pop, bt_capacity, 0)[0]
            remaining_pop = grepolis.bt_count_calculator(population, bt_pop, bt_capacity, 0)[1]
            bt_transportable_pop += population - bt_count * bt_pop - remaining_pop
            response_str += f"{math.floor(bt_transportable_pop / 2)} Hoplites, {math.floor(bt_transportable_pop / 4)} Archers et {math.floor(bt_transportable_pop / 4)} CE transportés par {bt_count} BT.\n" + \
            f"Les valeurs défensives sont :\n{math.floor(bt_transportable_pop / 2) * 18 + math.floor(bt_transportable_pop / 4) * 7 + math.floor(bt_transportable_pop / 4) * 14}\n" + \
                f"{math.floor(bt_transportable_pop / 2) * 12 + math.floor(bt_transportable_pop / 4) * 25 + math.floor(bt_transportable_pop / 4) * 8}\n" + \
                    f"{math.floor(bt_transportable_pop / 2) * 7 + math.floor(bt_transportable_pop / 4) * 13 + math.floor(bt_transportable_pop / 4) * 30}\n\n"

        await interation.response.send_message(response_str)

    else:
        await interation.response.send_message(f"Une ville ne peut pas avoir {population} habitants !")


@tree.command(name="grepooffcalculator", description="Retourne le nombre de troupes faisables pour des montants de BFx, de Catas et de population donnés.")
async def self(interation: discord.Interaction, population_totale: int, nombre_de_bfx: typing.Optional[int] = 0, nombre_de_catas: typing.Optional[int] = 0, nombre_de_sirenes: typing.Optional[int] = 0):
    if population_totale > 4500:
        await interation.response.send_message(f"Une ville ne peut pas contenir {population_totale} habitants !")
        return

    pop_cata = nombre_de_catas * 15
    pop_bfx = nombre_de_bfx * 10
    pop_sirenes = nombre_de_sirenes * 16

    if population_totale - pop_bfx - pop_cata - pop_sirenes < 0:
        await interation.response.send_message("Il y a trop de catapultes, de BFx ou de sirènes pour la population sélectionnée.")
        return

    response_str = f"Avec {population_totale} habitants, {nombre_de_catas} catapultes, {nombre_de_bfx} BFx et {nombre_de_sirenes} sirènes, une OT sera composée de :\n\n"
    available_pop = population_totale - pop_bfx - pop_sirenes

    btr_pop = 5
    btr_capacity = 16
    btr_count = 0
    btr_transportable_pop = 0


    if grepolis.can_fit_in_bt(available_pop, btr_pop, btr_capacity, pop_cata):
        btr_count += grepolis.bt_count_calculator(available_pop, btr_pop, btr_capacity, pop_cata)[0]
        remaining_pop = grepolis.bt_count_calculator(available_pop, btr_pop, btr_capacity, pop_cata)[1]
        btr_transportable_pop += available_pop - pop_cata - btr_count * btr_pop - remaining_pop
        response_str += f"{btr_transportable_pop} Frondeurs / {math.floor(btr_transportable_pop / 3)} Cavas, {nombre_de_catas} catapultes transportés par {btr_count} BTR et accompagnés par {nombre_de_bfx} BFx et {nombre_de_sirenes} sirènes.\n\n"

    bt_pop = 7
    bt_capacity = 32
    bt_count = 0
    bt_transportable_pop = 0

    if grepolis.can_fit_in_bt(available_pop, bt_pop, bt_capacity, pop_cata):
        bt_count += grepolis.bt_count_calculator(available_pop, bt_pop, bt_capacity, pop_cata)[0]
        remaining_pop = grepolis.bt_count_calculator(available_pop, bt_pop, bt_capacity, pop_cata)[1]
        bt_transportable_pop += available_pop - pop_cata - bt_count * bt_pop - remaining_pop
        response_str += f"{bt_transportable_pop} Frondeurs / {math.floor(bt_transportable_pop / 3)} Cavas, {nombre_de_catas} catapultes transportés par {bt_count} BT et accompagnés par {nombre_de_bfx} BFx et {nombre_de_sirenes} sirènes.\n\n"

    if nombre_de_bfx == 0 and nombre_de_sirenes == 0:
        pop_off = population_totale - pop_cata
        response_str += f"{pop_off} Frondeurs / {math.floor(pop_off / 3)} Cavas et {nombre_de_catas} catapultes sur la même île."

    await interation.response.send_message(response_str)

@tree.command(name="grepocounttroupes", description="Obtenir un récapitulatif du nombre de troupes de l'ally.")
async def self(interation: discord.Interaction, troupes: typing.Literal["BFx", "BB", "DT"]):
    units_channel = ""
    count = 0

    channels = interation.guild.channels

    for channel in channels:
        if channel.name == f"compte-{troupes.lower()}":
            units_channel = channel
            break

    if units_channel != "":
        async for message in units_channel.history(limit=200):
            count += grepolis.getIntFromStr(message.content)
        await interation.response.send_message(f"L'ally dispose actuellement de {count} {troupes} !")
        return

    await interation.response.send_message(f"Il n'y a pas de salon appelé ``compte-{troupes.lower()}`` sur ce serveur !")



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