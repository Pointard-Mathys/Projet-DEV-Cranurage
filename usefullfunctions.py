from unicodedata import name
import discord
from discord import Embed
from num2words import num2words

def createPoll(title, options, description):
    options_list = options.split(";", 10)
    embed = discord.Embed(title=title, description=description, color=0xff0000)
    embed.set_author(name="HeroFactory#0311", url="https://discord.gg/f77VwBX5w7", icon_url="https://cdn.discordapp.com/attachments/662904063058509836/1097454406015914045/Elder_Fatalis_armor_.png")
    embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/662904063058509836/1097474419795968010/Mini_Poogie_trop_cute.png")
    for idx, option in enumerate(options_list):
        embed.add_field(name=f":{num2words(idx)}: " + option, value="", inline=False)
    return embed