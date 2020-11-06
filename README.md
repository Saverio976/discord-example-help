# Discord Help by Saverio976

## purpose

this repository is not to replace the right documentation [discord.py doc here](https://discordpy.readthedocs.io/en/latest/) but just to show some lightweight example of what can be complicated

## Topic

1. [object](https://github.com/Saverio976/discord-example-help/tree/master/topic/object)
    1. [message](https://github.com/Saverio976/discord-example-help/tree/master/topic/object/message)
    1. [member](https://github.com/Saverio976/discord-example-help/tree/master/topic/object/member)
    1. [channel](https://github.com/Saverio976/discord-example-help/tree/master/topic/object/channel)
    1. [guild](https://github.com/Saverio976/discord-example-help/tree/master/topic/object/guild)
1. [commands](https://github.com/Saverio976/discord-example-help/tree/master/topic/commands)
1. [cogs](https://github.com/Saverio976/discord-example-help/tree/master/topic/cogs)
    1. [cogs_basic](https://github.com/Saverio976/discord-example-help/tree/master/topic/cogs/cogs_basic)
    1. [cogs_less_basic](https://github.com/Saverio976/discord-example-help/tree/master/topic/cogs/cogs_advanced)
    1. [some_info](https://github.com/Saverio976/discord-example-help/tree/master/topic/cogs/some_info)
1. [tasks](https://github.com/Saverio976/discord-example-help/tree/master/topic/tasks)
    1. [tasks_basic](https://github.com/Saverio976/discord-example-help/tree/master/topic/tasks/tasks_basic)
    1. [tasks_less_basic](https://github.com/Saverio976/discord-example-help/tree/master/topic/tasks/tasks_advanced)

## use doc

if you don't know how to use the doc, [click here](https://discordpy.readthedocs.io/en/latest/api.html) and look all diferents sections.


![use_doc](/assets/image/use_doc.png)

you see that this is the member object

and it have an attribute "joined_at"


if you want to use it, type object.joined_at

```py
member = message.member

print(member.joined_at)
```

will return "A datetime object that specifies the date and time in UTC that the member joined the guild for the first time. In certain cases, this can be None."
