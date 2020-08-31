import discord
from discord.ext import tasks

bot = commands.Bot(command_prefix = '!')

# a task that run every 2 seconds
@tasks.loop(seconds = 2.0)
async def some_name():
    print("hi")

# a task that run every 2 minutes
@tasks.loop(minutes = 2.0)
async def random_name():
    print("ok.")

# a task tha run every 2 hours
@tasks.loop(hours = 2.0)
async def func_name():
    print("spam every 2 hours")

# a task that run every 2 hours 2 minutes and 2 seconds
@tasks.loop(hours = 2.0, minutes = 2.0, seconds = 2.0)
async def anoher_task():
    print("OWO")


# we start all the tasks
some_name.start()
random_name.start()
func_name.start()
another_task.start()


bot.run("your tokken here")
