import discord
import aiohttp
from discord.ext import commands
from logging_files.fun_logging import logger


class Math(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command()
    async def math(self, ctx):
        async with aiohttp.ClientSession() as cs:
            async with cs.get('http://numbersapi.com/random/math?json') as r:
                res = await r.json()
                embed = discord.Embed(
                    color=discord.Color.from_rgb(241, 90, 36)
                )
                embed.add_field(name="→ Random Math Fact", value=f"• Fact: {res['text']}"
                                                                 f"\n• Number: {res['number']}")

                await ctx.send(embed=embed)

                logger.info(f"Fun | Sent Math: {ctx.author}")


def setup(client):
    client.add_cog(Math(client))
