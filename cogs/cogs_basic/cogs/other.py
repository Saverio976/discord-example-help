# see fun.py to read full description
# we just prove that we are some cogs
# and it works fine

import discord
from discord.ext import commands

bot = commands.Bot(command_prefix = '!')

class Other(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def test(self): # dont forgot the self parameter in a class function
        await ctx.send("test")

def setup(bot):
    bot.add_cog(Other(bot))
