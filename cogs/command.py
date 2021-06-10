from discord.ext import commands


class Commands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def hallo(self, ctx):
        await ctx.send("Hallo")


def setup(bot):
    bot.add_cog(Commands(bot))
