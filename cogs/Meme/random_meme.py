import discord
import ksoftapi
import os
from discord.ext import commands
from logging_files.meme_logging import logger


class Meme(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command()
    async def meme(self, ctx):
        client = ksoftapi.Client(api_key=os.environ.get("ksoft_key"))
        img = await client.random_meme()

        embed = discord.Embed(
            color=discord.Color.from_rgb(241, 90, 36),
            title=f"→ {img.title}",
        )
        embed.set_image(url=img.image_url)
        embed.set_footer(text=f"👍 {img.upvotes} | 👎 {img.downvotes}")

        await ctx.send(embed=embed)

        logger.info(f"Meme | Sent Random Meme: {ctx.author}")


def setup(client):
    client.add_cog(Meme(client))
