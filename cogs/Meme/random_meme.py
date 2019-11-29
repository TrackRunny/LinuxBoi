import discord
import aiohttp
import os
from discord.ext import commands
from logging_files.meme_logging import logger


class Meme(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command()
    async def meme(self, ctx):
        async with aiohttp.ClientSession() as cs:
            async with cs.get(f"https://api.ksoft.si/images/random-meme",
                              headers={"Authorization": f"Bearer {os.environ.get('ksoft_key')}"}) as r:
                res = await r.json()
                embed = discord.Embed(
                    color=discord.Color.from_rgb(241, 90, 36),
                    title=f"→ {res['title']}",
                )
                embed.set_image(url=res['image_url'])
                embed.set_footer(text=f"👍 {res['upvotes']} | 👎 {res['downvotes']}")

                await ctx.send(embed=embed)

                logger.info(f"Meme | Sent Random Meme: {ctx.author}")


def setup(client):
    client.add_cog(Meme(client))
