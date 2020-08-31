import discord
from discord.ext import commands

bot = commands.Bot(command_prefix = '!')

class Other(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def test(self, ctx):
        await ctx.send("test")

def setup(bot):
    bot.add_cog(Other(bot))
