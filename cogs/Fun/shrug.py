import discord
from discord.ext import commands
from logging_files.fun_logging import logger


class Shrug(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command()
    async def shrug(self, ctx):
        embed = discord.Embed(
            color=discord.Color.from_rgb(241, 90, 36),
            title="→ What is life?",
            description="• I gave up on it. ¯\_(ツ)_/¯"
        )

        await ctx.send(embed=embed)

        logger.info(f"Fun | Sent Shrug: {ctx.author}")


def setup(client):
    client.add_cog(Shrug(client))
