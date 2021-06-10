import sys
import traceback

import discord
from discord.ext import commands


TOKEN = ''  # Dein Token hier

bot = commands.Bot(command_prefix='')  # Dein Prefix hier

extensions = ['cogs.command']


@bot.event
async def on_ready():
    print('--------------------------------------')
    print('Bot is ready.')
    print('Eingeloggt als')
    print(bot.user.name)
    print(bot.user.id)
    print('--------------------------------------')


#######################################################################

if __name__ == '__main__':
    for extension in extensions:
        try:
            bot.load_extension(extension)
        except Exception as e:
            print(f'Failed to load extension {extension}.', file=sys.stderr)
            traceback.print_exc()

bot.run(TOKEN)
