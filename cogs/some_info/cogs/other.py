# see fun.py to read full description
# we just prove that we are some cogs
# and it works fine

import discord
from discord.ext import commands

# we import the random lib
import random

bot = commands.Bot(command_prefix = '!')

class Other(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def test(self, ctx): # dont forgot the self parameter in a class function
        await ctx.send("test")

    @commands.command()
    async def random_number(self, ctx):
        # pick a random number between 0 and 10
        nb_random = random.randint(0, 10)
        await ctx.send(f"{nb_random}")

def setup(bot):
    bot.add_cog(Other(bot))
