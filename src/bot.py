# bot.py
import os

import discord
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')

client = discord.Client()

from discord.ext import commands
prefix = "_"
bot = commands.Bot(command_prefix=prefix)


@bot.event
async def on_ready():
    print("Dash is online and awaiting a command...~")

@bot.command()
async def ping(ctx):
    '''
    This text will be shown in the help command
    '''

    # Get the latency of the bot
    latency = bot.latency  # Included in the Discord.py library
    # Send it to the user
    await ctx.send(latency)


@bot.command()
async def echo(ctx, *, content:str):
    await ctx.send(content)


bot.run(TOKEN)  # Where 'TOKEN' is your bot token
