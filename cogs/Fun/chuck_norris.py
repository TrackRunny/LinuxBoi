import discord
import aiohttp
from logging_files.fun_logging import logger
from discord.ext import commands


class ChuckNorris(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command(aliases=["chuck-norris"])
    async def chuck_norris(self, ctx):
        async with aiohttp.ClientSession() as cs:
            async with cs.get('https://api.icndb.com/jokes/random?limitTo=[nerdy]') as r:
                res = await r.json()
                embed = discord.Embed(
                    color=discord.Color.from_rgb(241, 90, 36),
                    title="→ Chuck Norris Joke",
                    description=f"• Joke: {res['value']['joke']}"
                )

                await ctx.send(embed=embed)

                logger.info(f"Fun | Sent Chuck Norris: {ctx.author}")


def setup(client):
    client.add_cog(ChuckNorris(client))
