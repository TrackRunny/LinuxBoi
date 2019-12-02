import discord
import aiohttp
from discord.ext import commands
from logging_files.images_logging import logger


class Image(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command()
    async def captcha(self, ctx):
        avatar = ctx.author.avatar_url_as(size=4096, format=None, static_format='png')
        async with aiohttp.ClientSession() as cs:
            async with cs.get(f"https://nekobot.xyz/api/imagegen?type=captcha&url={avatar}&username=Orange") as r:
                res = await r.json()
                embed = discord.Embed(
                    color=discord.Color.from_rgb(241, 90, 36),
                    title="→ Captcha Verification",

                )
                embed.set_image(url=res["message"])

                await ctx.send(embed=embed)

                logger.info(f"Images | Sent Captcha: {ctx.author}")

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

    @commands.command()
    async def fox(self, ctx):
        async with aiohttp.ClientSession() as cs:
            async with cs.get('https://randomfox.ca/floof/') as r:
                res = await r.json()
                embed = discord.Embed(
                    color=discord.Color.from_rgb(241, 90, 36),
                    title="→ Random Fox! "
                )
                embed.set_image(url=res['image'])

                await ctx.send(embed=embed)

                logger.info(f"Images | Sent Fox: {ctx.author}")

    @commands.command()
    async def tweet(self, ctx, username: str, *, text: str):
        async with aiohttp.ClientSession() as cs:
            async with cs.get(f"https://nekobot.xyz/api/imagegen?type=tweet&username={username}&text={text}") as r:
                res = await r.json()
                embed = discord.Embed(
                    color=discord.Color.from_rgb(241, 90, 36),
                    title="→ User Tweet"
                )
                embed.set_image(url=res["message"])

                await ctx.send(embed=embed)

                logger.info(f"Images | Sent Tweet: {ctx.author} | Username: {username} | Text: {text}")

    @tweet.error
    async def tweet_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            embed = discord.Embed(
                color=discord.Color.from_rgb(241, 90, 36),
                title="→ Invalid Argument",
                description="• Please put in a vaild option! Example: `l!tweet <username> <text>`"
            )

            await ctx.send(embed=embed)


def setup(client):
    client.add_cog(Image(client))
