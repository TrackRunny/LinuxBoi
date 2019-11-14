import random
import discord
from logging_files.fun_logging import logger
from discord.ext import commands


class Coinflip(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def coinflip(self, ctx):
        choices = ("Heads!", "Tails!")
        coin = random.choice(choices)
        embed = discord.Embed(
            color=discord.Color.from_rgb(241, 90, 36),
            title="→ Coinflip Command",
            description=coin
        )

        await ctx.send(embed=embed)

        logger.info(f"Fun | Sent Coinflip: {ctx.author}")


def setup(client):
    client.add_cog(Coinflip(client))
