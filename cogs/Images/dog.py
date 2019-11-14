import discord
import aiohttp
from discord.ext import commands
from logging_files.images_logging import logger


class Dog(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command()
    async def dog(self, ctx):
        async with aiohttp.ClientSession() as cs:
            async with cs.get('https://dog.ceo/api/breeds/image/random') as r:
                res = await r.json()
                embed = discord.Embed(
                    color=discord.Color.from_rgb(241, 90, 36),
                    title="→ Random Dog! 🐕"
                )
                embed.set_image(url=res['message'])

                await ctx.send(embed=embed)

                logger.info(f"Images | Sent Dog: {ctx.author}")


def setup(client):
    client.add_cog(Dog(client))
