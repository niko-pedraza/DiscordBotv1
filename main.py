# Discord bot
import asyncio
import random
import re
import urllib.parse
import urllib.request
from itertools import cycle

import discord
from discord.ext import commands

client = commands.Bot(command_prefix=".")
boys = cycle(['Frankie', 'Alexis', 'Rigel', 'John'])



# event
@client.event
async def on_ready():
    await client.change_presence(status=discord.Status.idle, activity=discord.Game("Working to please."))

    print("Ready to load.")


@client.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
        await ctx.send('Command not found, check commands using .help :)')


# commands
@client.command()
async def load(ctx, extension):
    client.load_extension(f'cogs.{extension}')
    await ctx.send(f'{extension} Cog Activated')


@client.command()
async def unload(ctx, extension):
    client.unload_extension(f'cogs.{extension}')
    await ctx.send(f'{extension} Cog Deactivated')


@client.command()
async def reload(ctx, extension):
    client.unload_extension(f'cogs.{extension}')
    client.load_extension(f'cogs.{extension}')
    await ctx.send(f'{extension} Cog Reloaded')

@client.command()
async def change_yt_index(index):
    video_index = index


@client.command()
async def yt(ctx, *, search):
    search_keyword = urllib.parse.urlencode({"search_query": search})
    html = urllib.request.urlopen("https://www.youtube.com/results?" + search_keyword)

    video_ids = re.findall(r"watch\?v=(\S{11})", html.read().decode())

    await ctx.send("https://www.youtube.com/watch?v=" + video_ids[0])




@client.command()
async def activate_compliment(ctx):
    client.loop.create_task(compliment(ctx))


@client.command()
async def deactivate_compliment(ctx):
    await ctx.send("Compliments deactivated")
    client.loop.stop()


async def compliment(ctx):
    while True:
        compliments = ['you are handsome', 'you are really smart', 'you will be successful'
            , 'you are sooo big ;)', 'I love you', 'attack the day', 'does it hurt being so smart?']

        await ctx.send(f'{next(boys)}, {random.choice(compliments)}')
        await asyncio.sleep(3600)


# loads cogs in our directory at runtime (modes)
# for filename in os.listdir('./cogs'):
#     if filename.endswith('.py'):
#         client.load_extension(f'cogs.{filename[:-3]}')





client.run("Nzc4MzQ3NDY2OTE0NjYwMzUy.X7QqkQ.AdYVwsPBIeCB9coyzVOpBvrXFLc")
