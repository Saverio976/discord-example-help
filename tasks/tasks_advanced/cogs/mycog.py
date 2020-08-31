import discord
from discord.ext import commands, tasks

bot = commands.Bot(command_prefix = '!')

class MyCog(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
        # and we start th some_task task
        self.some_task.start()

    @tasks.loop(minutes = 2.0)
    async def some_task(self): # we are in a loop, dont forgot self
        print("task in cog !!!")


def setup(bot):
    bot.add_cog(MyCog(bot))
