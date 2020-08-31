import discord
from discord.ext import commands

bot = commands.Bot(command_prefix = '!')

class Fun(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def ping(self, ctx):
        await ctx.send('Pong')

    @commands.command()
    async def say(self, ctx, arg1, arg2):
        await ctx.send(f"arg1 : {arg1}\narg2 : {arg2}")

def setup(bot):
    bot.add_cog(Fun(bot))
