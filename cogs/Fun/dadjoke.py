import discord
from discord.ext import commands
from dadjokes import Dadjoke
from logging_files.fun_logging import logger


class DadJoke(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command()
    async def dadjoke(self, ctx):
        random_dadjoke = Dadjoke()
        embed = discord.Embed(
            color=discord.Color.from_rgb(241, 90, 36)
        )
        embed.add_field(name="→ Random Dad Joke!", value=f"• {random_dadjoke.joke}")

        await ctx.send(embed=embed)

        logger.info(f"Fun | Sent Dadjoke: {ctx.author}")


def setup(client):
    client.add_cog(DadJoke(client))
