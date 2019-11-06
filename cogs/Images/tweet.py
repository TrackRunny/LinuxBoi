import discord
import aiohttp
from discord.ext import commands
from logging_files.images_logging import logger


class Tweet(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command()
    async def tweet(self, ctx, username: str, *, text: str):
        async with aiohttp.ClientSession() as cs:
            async with cs.get(f"https://nekobot.xyz/api/imagegen?type=tweet&username={username}&text={text}") as r:
                res = await r.json()
                embed = discord.Embed(
                    color=discord.Color.from_rgb(241, 90, 36)
                )
                embed.set_author(name="→ User Tweet")
                embed.set_image(url=res["message"])

                await ctx.send(embed=embed)

                logger.info(f"Images | Sent Tweet: {ctx.author} | Username: {username} | Text: {text}")

    @tweet.error
    async def tweet_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            embed = discord.Embed(
                color=discord.Color.from_rgb(241, 90, 36)
            )
            embed.add_field(name="→ Invalid Argument!",
                            value="• Please put in a vaild option! Example: `l!tweet <username> <text>`")

            await ctx.send(embed=embed)


def setup(client):
    client.add_cog(Tweet(client))
