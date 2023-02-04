import sys
import traceback

import discord
from discord.ext import commands


TOKEN = ''  # Your Bots Token

bot = commands.Bot(command_prefix='')  # Your Prefix

extensions = ['cogs.command']  # Your cogs


@bot.event
async def on_ready():
    print(f"Logged in as {bot.user} (ID: {bot.user.id}")
    


if __name__ == '__main__':
    for extension in extensions:
        try:
            bot.load_extension(extension)
        except Exception as e:
            print(f'Failed to load extension {extension}.', file=sys.stderr)
            traceback.print_exc()

bot.run(TOKEN)
