import discord
from discord.ext import tasks

bot = commands.Bot(command_prefix = '!')

@bot.event()
async def on_message(message):
    # we can have an user/ member object
    # mesage.author
    # this user/member object have name attribut
    # see object/user or object/member
    print("message author name :", message.author.name)

    # we can have acces to the content of this message
    # message.content
    print("message content :", message.content)

    # we have the channel object where the message is
    # see object/channel
    print("message channel name", message.channel.name)

    # or the guild object (guild = server in our language)
    # see object/guild
    print("message guild name :", message.guild.name)

    # but if i continue to list all object, i will do like the documentation
    # to see all information about message object, go to the doc and in the search bar type discord.Message


bot.run("your tokken here")
