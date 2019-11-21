import discord
import aiohttp
from discord.ext import commands
from logging_files.images_logging import logger


class Clyde(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command()
    async def clyde(self, ctx, *, text):
        async with aiohttp.ClientSession() as cs:
            async with cs.get(f"https://nekobot.xyz/api/imagegen?type=clyde&text={text}") as r:
                res = await r.json()
                embed = discord.Embed(
                    color=discord.Color.from_rgb(241, 90, 36),
                    title="→ Clyde Bot 🤖"
                )
                embed.set_image(url=res['message'])

                await ctx.send(embed=embed)

                logger.info(f"Images | Sent Clyde: {ctx.author}")

    @clyde.error
    async def clyde_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            embed = discord.Embed(
                color=discord.Color.from_rgb(241, 90, 36),
                title="→ Invalid Argument",
                description="• Please put in a vaild option! Example: `l!clyde <text>`"
            )

            await ctx.send(embed=embed)


def setup(client):
    client.add_cog(Clyde(client))