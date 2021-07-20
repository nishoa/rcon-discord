from main import rc
import discord
from discord.ext import commands

client = discord.ext.commands.Bot(command_prefix="!")


@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))


@client.command()
async def rcon(ctx, *, text):
    if rc(text):
        await ctx.send(f'{text} выполнена')
    await ctx.send(f'{text} возникла ошибка')

client.run('ODY2NzQxMTUxNzUzODMwNDMw.YPW9mQ.DutQ43FhvoN-PRJSq9ct88D0xG8')

# import discord
# from threading import Thread
# from main import rc
#
# class MyClient(discord.Client):
#     async def on_ready(self):
#         print('Logged on as', self.user)
#
#     async def on_message(self, message):
#         # don't respond to ourselves
#         if message.author == self.user:
#             return
#
#         def mess():
#             if message:
#                 mes = message
#                 return mes
#                 # await message.channel.send(res)
#
# client = MyClient()
# client.run('ODY2NzQxMTUxNzUzODMwNDMw.YPW9mQ.c9656VfiAvaBWJvcMzytOq7gMZs')
