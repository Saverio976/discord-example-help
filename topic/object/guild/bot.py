import discord
from discord.ext import commands

bot = commands.Bot(command_prefix = '!')

@bot.event()
async def on_message(message):
    # we can have a guild object
    # mesage.guild
    guild = message.guild

    # show the name of this guild
    print("guild name :", guild.name)

    # you can have all channel oject that exist in this guild
    list_channel = guild.channels
    for channel in list_channel:
        print("guild channels :", channel.name)

    # you can have all categories object
    lis_categories = guild.categories
    for category in list_categories:
        print("guild categories :", category.name)

    # if you want more, go to the doc and search "discord.Guild"




bot.run("your tokken here")
