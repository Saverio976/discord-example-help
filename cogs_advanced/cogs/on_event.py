import discord
from discord.ext import commands

bot = commands.Bot(command_prefix = '!')

class OnEvent(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener
    async def on_ready(self): # dont forgot the self parameter in a class function
        print("not ready !")

    '''
    you can use all on_event but with the
    @commands.Cog.listener
    decorator
    '''


def setup(bot):
    bot.add_cog(OnEvent(bot))
