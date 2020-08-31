import discord
from discord.ext import tasks

bot = commands.Bot(command_prefix = '!')

@bot.event()
async def on_message(message):
    # we can have an user/ member object
    # mesage.author
    member = message.author

    # show the name of this member
    print("member name :", member.name)
    # but the member can have a nickname
    print("member nickname :", member.nick)

    # a member is an user in a guild, so we can prnt the guild where the user is in
    # see object/guild
    print("member guild", member.guild.name)

    # we can see all the roles that the member have
    # member.roles return a list of role object
    # go to the documentation and search "discord role"
    for role in member.roles:
        print("member roles :", role.name)

    # we can ban this member if the bot have this perm
    # i put this in triple quotation marck, because else, everbody who speak will be ban
    '''
    await member.ban()
    '''

    # also kick
    '''
    await member.kick()
    '''

    # if you want more, go to the doc and search "discord.Member"




bot.run("your tokken here")
