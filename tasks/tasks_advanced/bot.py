import discord
from discord.ext import tasks

bot = commands.Bot(command_prefix = '!')

# a task that run every 2 seconds
# but repeat itself 10 time and stop after
@tasks.loop(seconds = 2.0, count = 10)
async def some_name():
    print("hi")

# a task that run every 2 minutes
# but we add a "before" function
@tasks.loop(minutes = 2.0)
async def random_name():
    print("ok.")
# the before function
@random.before_loop()
async def before_random_name():
    # we ensure that the bot is ready and have
    # all ok to continue and pass to the loop
    await bot.wait_until_ready()
    print("the bot is ready, go random_name task")

# a task tha run every 2 hours
# but when the task ends, it do wome stuf
@tasks.loop(hours = 2.0)
async def func_name():
    print("spam every 2 hours")
# the after function
@func_name.after_loop()
async def after_func_name():
    print("the func_name task ends, i print this msg")

# a task that run every 2 hours 2 minutes and 2 seconds
@tasks.loop(hours = 2.0, minutes = 2.0, seconds = 2.0)
async def anoher_task():
    print("OWO")


# we start all the tasks
some_name.start()
random_name.start()
func_name.start()
another_task.start()


# we can also create tasks in cog
# so we add the cog like cogs
bot.load_extension('cogs.my_cog')

bot.run("your tokken here")
