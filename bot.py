from main import rc
import discord
from discord.ext import commands
import os

client = discord.ext.commands.Bot(command_prefix="!")


@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))


@client.command()
async def rcon(ctx, *, text):
    if rc(text):
        await ctx.send(f'{text} выполнена')
    await ctx.send(f'{text} возникла ошибка')

token = os.environ.get('BOT_TOKEN')
