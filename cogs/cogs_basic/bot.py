import discord
from discord.ext import commands

bot = commands.Bot(command_prefix = '!')

bot.load_extension('cogs.fun')
# we add the file ./cogs/fun.py
# (N.B. : we dont write the python
# extension '.py')
bot.load_extension('cogs.other')
# same with ./cogs/other.py

bot.run("your tokken here")
