import discord
import aiohttp
from discord.ext import commands
from logging_files.images_logging import logger


class Cat(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command()
    async def cat(self, ctx):
        async with aiohttp.ClientSession() as cs:
            async with cs.get('http://aws.random.cat/meow') as r:
                res = await r.json()
                embed = discord.Embed(
                    color=discord.Color.from_rgb(241, 90, 36),
                    title="→ Random Cat! 🐈"
                )
                embed.set_image(url=res['file'])

                await ctx.send(embed=embed)

                logger.info(f"Images | Sent Cat: {ctx.author}")


def setup(client):
    client.add_cog(Cat(client))
