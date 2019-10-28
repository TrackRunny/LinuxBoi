import discord
import aiohttp
from discord.ext import commands
from logging_files.images_logging import logger


class Fox(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command()
    async def fox(self, ctx):
        async with aiohttp.ClientSession() as cs:
            async with cs.get('https://randomfox.ca/floof/') as r:
                res = await r.json()
                embed = discord.Embed(
                    color=discord.Color.from_rgb(241, 90, 36)
                )
                embed.set_author(name="→ Random Fox! 🦊")
                embed.set_image(url=res['image'])

                await ctx.send(embed=embed)

                await logger.info(f"Images | Sent Fox: {ctx.author}")


def setup(client):
    client.add_cog(Fox(client))
