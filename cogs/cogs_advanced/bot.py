import discord
from discord.ext import commands

import os

bot = commands.Bot(command_prefix = '!')

# instead of use this
'''
bot.load_extension('cogs.fun')
bot.load_extension('cogs.other')
'''
# i use this one
for x in os.listdir('./cogs'): # we list all file in the cogs folder
    if x.endswith('.py'): # if the file ends with the python extension
        client.load_extension(f'cogs.{x[:-3]}') # bot add this extension (N.B. : we remove the '.py' with str[:-3])

bot.run("your tokken here")
