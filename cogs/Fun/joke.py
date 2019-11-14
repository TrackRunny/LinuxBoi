import discord
import aiohttp
from discord.ext import commands
from logging_files.fun_logging import logger


class Joke(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command()
    async def joke(self, ctx):
        async with aiohttp.ClientSession() as cs:
            async with cs.get('https://official-joke-api.appspot.com/jokes/general/random') as r:
                res = await r.json()
                embed = discord.Embed(
                    color=discord.Color.from_rgb(241, 90, 36),
                    title="→ Random Joke!",
                    description=f"• Question: {res[0]['setup']}"
                                "\n• Joke: {res[0]['punchline']}"
                )
                await ctx.send(embed=embed)

                logger.info(f"Fun | Sent Joke: {ctx.author}")


def setup(client):
    client.add_cog(Joke(client))
