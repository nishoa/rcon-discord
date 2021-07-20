from main import rc
import discord
from discord.ext import commands
import os

client = discord.ext.commands.Bot(command_prefix="/")


@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))


@client.command()
async def rcon(ctx, *, text):
    rc(text)
    await ctx.send(f'{text} выполнена')

token = os.environ.get('BOT_TOKEN')
client.run(str(token))
