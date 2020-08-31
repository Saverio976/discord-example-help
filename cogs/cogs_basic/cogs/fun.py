# import discord
import discord
from discord.ext import commands
# initialise the bot object
bot = commands.Bot(command_prefix = '!')

# create the class wher we will
#write the commands
class Fun(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    # our first command in a cog, enjoy :)
    @commands.command()
    async def ping(self):
        # dont forgot the self parameter
        # in a class function
        await ctx.send('Pong')

    # our second command
    @commands.command()
    async def say(self, arg1, arg2):
        # dont forgot the self parameter
        # in a class function
        await ctx.send(f"arg1 : {arg1}\narg2 : {arg2}")

    # and we can write infinite of
    # commands (not so much)

# and we just create the def function tha add the cog to the bot
# this fonction is always call "setup" with the bot object
def setup(bot):
    bot.add_cog(Fun(bot))
