import discord
from discord.ext import tasks

bot = commands.Bot(command_prefix = '!')

@bot.event()
async def on_message(message):
    # we can have an channel object
    # mesage.channel
    channel = message.channel

    # show the name of this channel
    print("channel name :", channel.name)


    # a channel is in a guild so we can have the guild object
    # see object/guild
    print("channel guild", channel.guild.name)

    # we can delete an amount of message
    '''
    await channel.purge(limit = 100)
    '''

    # if you want more, go to the doc and search "discord.TextChannel"




bot.run("your tokken here")
