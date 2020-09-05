# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# LinuxBoi - Discord bot                                                    #
# Copyright (C) 2019-2020 TrackRunny                                        #
#                                                                           #
# This program is free software: you can redistribute it and/or modify      #
# it under the terms of the GNU General Public License as published by      #
# the Free Software Foundation, either version 3 of the License, or         #
# (at your option) any later version.                                       #
#                                                                           #
# This program is distributed in the hope that it will be useful,           #
# but WITHOUT ANY WARRANTY; without even the implied warranty of            #
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the             #
# GNU General Public License for more details.                              #
#                                                                           #
# You should have received a copy of the GNU General Public License         #
# along with this program. If not, see <https://www.gnu.org/licenses/>.     #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
import io
import os

import aiohttp
import discord
from discord.ext import commands

from logging_files.images_logging import logger


class Image(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def captcha(self, ctx):
        avatar = ctx.author.avatar_url_as(size=1024, format=None, static_format='png')
        async with aiohttp.ClientSession() as cs:
            async with cs.get(f"https://nekobot.xyz/api/imagegen?type=captcha&url={avatar}&username=Orange") as r:
                res = await r.json()
                embed = discord.Embed(
                    color=self.bot.embed_color,
                    title="→ Captcha Verification",

                )
                embed.set_image(url=res["message"])

                await ctx.send(embed=embed)

                logger.info(f"Images | Sent Captcha: {ctx.author}")

    # - TODO: Check to see if this API is still alive

    @commands.command()
    async def cat(self, ctx):
        async with aiohttp.ClientSession() as cs:
            async with cs.get('https://some-random-api.ml/img/cat') as r:
                res = await r.json()
                embed = discord.Embed(
                    color=self.bot.embed_color,
                    title="→ Random Cat! 🐈"
                )
                embed.set_image(url=res['link'])

                await ctx.send(embed=embed)

                logger.info(f"Images | Sent Cat: {ctx.author}")

    @commands.command()
    async def dog(self, ctx):
        async with aiohttp.ClientSession() as cs:
            async with cs.get('https://dog.ceo/api/breeds/image/random') as r:
                res = await r.json()
                embed = discord.Embed(
                    color=self.bot.embed_color,
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
                    color=self.bot.embed_color,
                    title="→ Random Fox! "
                )
                embed.set_image(url=res['image'])

                await ctx.send(embed=embed)

                logger.info(f"Images | Sent Fox: {ctx.author}")

    @commands.command()
    async def bird(self, ctx):
        async with aiohttp.ClientSession() as cs:
            async with cs.get(f"https://api.ksoft.si/meme/random-image", params={"tag": "birb"},
                              headers={"Authorization": f"Bearer {os.environ.get('ksoft_key')}"}) as r:
                res = await r.json()
                embed = discord.Embed(
                    color=self.bot.embed_color,
                    title=f"→ Random Bird",
                )
                embed.set_image(url=res['url'])

                await ctx.send(embed=embed)

                logger.info(f"Images | Sent Random Bird: {ctx.author}")

    @commands.command()
    async def duck(self, ctx):
        async with aiohttp.ClientSession() as cs:
            async with cs.get("https://random-d.uk/api/v1/random") as r:
                res = await r.json()
                embed = discord.Embed(
                    color=self.bot.embed_color,
                    title="→ Random Duck"
                )
                embed.set_image(url=res['url'])

                await ctx.send(embed=embed)

                logger.info(f"Images | Sent Random Duck: {ctx.author}")

    @commands.command()
    async def panda(self, ctx):
        async with aiohttp.ClientSession() as cs:
            async with cs.get("https://some-random-api.ml/img/panda") as r:
                res = await r.json()
                embed = discord.Embed(
                    color=self.bot.embed_color,
                    title="→ Random Panda"
                )
                embed.set_image(url=res['link'])

                await ctx.send(embed=embed)

                logger.info(f"Images | Sent Random Panda: {ctx.author}")

    @commands.command()
    async def tweet(self, ctx, username: str, *, text: str):
        async with aiohttp.ClientSession() as cs:
            async with cs.get(f"https://nekobot.xyz/api/imagegen?type=tweet&username={username}&text={text}") as r:
                res = await r.json()
                embed = discord.Embed(
                    color=self.bot.embed_color,
                    title="→ User Tweet"
                )
                embed.set_image(url=res["message"])

                await ctx.send(embed=embed)

                logger.info(f"Images | Sent Tweet: {ctx.author} | Username: {username} | Text: {text}")

    @tweet.error
    async def tweet_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            embed = discord.Embed(
                color=self.bot.embed_color,
                title="→ Invalid Argument",
                description="• Please put in a valid option! Example: `l!tweet <username> <text>`"
            )

            await ctx.send(embed=embed)

    @commands.command()
    async def trumptweet(self, ctx, *, text: str):
        async with aiohttp.ClientSession() as cs:
            async with cs.get(f"https://nekobot.xyz/api/imagegen?type=trumptweet&text={text}") as r:
                res = await r.json()
                embed = discord.Embed(
                    color=self.bot.embed_color,
                    title="→ Trump Tweet"
                )
                embed.set_image(url=res["message"])

                await ctx.send(embed=embed)

                logger.info(f"Images | Sent Trump Tweet: {ctx.author} | Text: {text}")

    @trumptweet.error
    async def trumptweet_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            embed = discord.Embed(
                color=self.bot.embed_color,
                title="→ Invalid Argument",
                description="• Please put in a valid option! Example: `l!trumptweet <text>`"
            )

            await ctx.send(embed=embed)

    @commands.command()
    async def clyde(self, ctx, *, text):
        async with aiohttp.ClientSession() as cs:
            async with cs.get(f"https://nekobot.xyz/api/imagegen?type=clyde&text={text}") as r:
                res = await r.json()
                embed = discord.Embed(
                    color=self.bot.embed_color,
                    title="→ Clyde Bot 🤖"
                )
                embed.set_image(url=res['message'])

                await ctx.send(embed=embed)

                logger.info(f"Images | Sent Clyde: {ctx.author}")

    @clyde.error
    async def clyde_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            embed = discord.Embed(
                color=self.bot.embed_color,
                title="→ Invalid Argument",
                description="• Please put in a vaild option! Example: `l!clyde <text>`"
            )

            await ctx.send(embed=embed)

    @commands.command()
    async def vs(self, ctx, member1: discord.Member, member2: discord.Member):
        member1 = member1.avatar_url_as(size=1024, format=None, static_format='png')
        member2 = member2.avatar_url_as(size=1024, format=None, static_format='png')
        async with aiohttp.ClientSession() as cs:
            async with cs.get(
                    f"https://nekobot.xyz/api/imagegen?type=whowouldwin&user1={member1}&user2={member2}") as r:
                res = await r.json()
                embed = discord.Embed(
                    color=self.bot.embed_color,
                    title="→ Who Would Win"
                )
                embed.set_image(url=res["message"])

                await ctx.send(embed=embed)

                logger.info(f"Images | Sent Who Would Win: {ctx.author}")

    @vs.error
    async def vs_error(self, ctx, error):
        if isinstance(error, commands.BadArgument):
            embed = discord.Embed(
                color=self.bot.embed_color,
                title="→ Invalid Member!",
                description="• Please mention two valid members! Example: `l!vs @user1 @user2`"
            )

            await ctx.send(embed=embed)
        elif isinstance(error, commands.MissingRequiredArgument):
            embed = discord.Embed(
                color=self.bot.embed_color,
                title="→ Invalid Argument",
                description="• Please put in a vaild option! Example: `l!vs @user1 @user2`"
            )

            await ctx.send(embed=embed)

    @commands.command()
    async def magik(self, ctx, member: discord.Member, intensity: int = 5):
        avatar = member.avatar_url_as(size=1024, format=None, static_format='png')
        emoji = ":penguin:"

        message = await ctx.send(f"{emoji} — **Processing the image please wait!**")
        await message.delete(delay=3)

        async with aiohttp.ClientSession() as cs:
            async with cs.get(f"https://nekobot.xyz/api/imagegen?type=magik&image={avatar}&intensity={intensity}") as r:
                res = await r.json()
                embed = discord.Embed(
                    color=self.bot.embed_color,
                    title="→ Magik"
                )
                embed.set_image(url=res["message"])

                await ctx.send(embed=embed)

                logger.info(f"Images | Sent Magik: {ctx.author}")

    @magik.error
    async def magik_error(self, ctx, error):
        if isinstance(error, commands.BadArgument):
            embed = discord.Embed(
                color=self.bot.embed_color,
                title="→ Invalid Member!",
                description="• Please mention two valid members! Example: `l!magik @user`"
            )

            await ctx.send(embed=embed)
        elif isinstance(error, commands.MissingRequiredArgument):
            embed = discord.Embed(
                color=self.bot.embed_color,
                title="→ Invalid Argument",
                description="• Please put in a vaild option! Example: `l!magik @user`"
            )

            await ctx.send(embed=embed)

    @commands.command()
    async def threats(self, ctx):
        picture = ctx.author.avatar_url_as(size=1024, format=None, static_format='png')
        async with aiohttp.ClientSession() as cs:
            async with cs.get(f"https://nekobot.xyz/api/imagegen?type=threats&url={picture}") as r:
                res = await r.json()
                embed = discord.Embed(
                    color=self.bot.embed_color,
                    title="→ Threats"
                )
                embed.set_image(url=res["message"])

                await ctx.send(embed=embed)

                logger.info(f"Images | Sent Threats: {ctx.author}")

    @commands.command()
    async def mind(self, ctx, *, text):
        async with aiohttp.ClientSession() as cs:
            async with cs.get(f"https://nekobot.xyz/api/imagegen?type=changemymind&text={text}") as r:
                res = await r.json()
                embed = discord.Embed(
                    color=self.bot.embed_color,
                    title="→ Change My Mind"
                )
                embed.set_image(url=res["message"])

                await ctx.send(embed=embed)

                logger.info(f"Images | Sent mind: {ctx.author}")

    @mind.error
    async def mind_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            embed = discord.Embed(
                color=self.bot.embed_color,
                title="→ Invalid Argument",
                description="• Please put in a vaild option! Example: `l!mind <text>`"
            )

            await ctx.send(embed=embed)

    @commands.command()
    async def ph(self, ctx):
        picture = ctx.author.avatar_url_as(size=1024, format=None, static_format='png')
        async with aiohttp.ClientSession() as cs:
            async with cs.get(f"https://nekobot.xyz/api/imagegen?type=phcomment&image={picture}&text=That was pretty sick&username={ctx.author}") as r:
                res = await r.json()
                embed = discord.Embed(
                    color=self.bot.embed_color,
                    title="→ Cornhub"
                )
                embed.set_image(url=res["message"])

                await ctx.send(embed=embed)

                logger.info(f"Images | Sent PH: {ctx.author}")

    @commands.command()
    async def baguette(self, ctx):
        picture = ctx.author.avatar_url_as(size=1024, format=None, static_format='png')
        async with aiohttp.ClientSession() as cs:
            async with cs.get(f"https://nekobot.xyz/api/imagegen?type=baguette&url={picture}") as r:
                res = await r.json()
                embed = discord.Embed(
                    color=self.bot.embed_color,
                    title=f"→ {ctx.author.name} eating a baguette"
                )
                embed.set_image(url=res["message"])

                await ctx.send(embed=embed)

                logger.info(f"Images | Sent Baguette: {ctx.author}")

    @commands.command()
    async def iphone(self, ctx, member: discord.Member):
        picture = member.avatar_url_as(size=1024, format=None, static_format='png')
        async with aiohttp.ClientSession() as cs:
            async with cs.get(f"https://nekobot.xyz/api/imagegen?type=iphonex&url={picture}") as r:
                res = await r.json()
                print(res)
                embed = discord.Embed(
                    color=self.bot.embed_color,
                    title=f"→ Thats a nice wallpaper of {member}",
                )
                embed.set_image(url=res["message"])

                await ctx.send(embed=embed)

                logger.info(f"Images | Sent Trap {ctx.author}")

    @iphone.error
    async def iphone_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            embed = discord.Embed(
                color=self.bot.embed_color,
                title="→ Invalid Argument",
                description="• Please put in a vaild option! Example: `l!iphone @member`"
            )

            await ctx.send(embed=embed)

    @commands.command()
    async def coffee(self, ctx):
        async with aiohttp.ClientSession() as cs:
            async with cs.get("https://coffee.alexflipnote.dev/random.json") as r:
                res = await r.json()
                embed = discord.Embed(
                    color=self.bot.embed_color,
                    title="→ Daily Coffee",
                )
                embed.set_image(url=res["file"])

                await ctx.send(embed=embed)

                logger.info(f"Images | Sent Coffee: {ctx.author}")

    @commands.command()
    async def youtube(self, ctx, *, comment):
        picture = ctx.author.avatar_url_as(size=1024, format=None, static_format='png')
        async with aiohttp.ClientSession() as cs:
            async with cs.get(f"https://some-random-api.ml/canvas/youtube-comment?avatar={picture}&username={ctx.author.name}&comment={comment}") as r:
                res = io.BytesIO(await r.read())
                youtube_file = discord.File(res, filename=f"youtube.jpg")
                embed = discord.Embed(
                    color=self.bot.embed_color,
                    title="→ Youtube comment"
                )
                embed.set_image(url="attachment://youtube.jpg")

                await ctx.send(embed=embed, file=youtube_file)

                logger.info(f"Images | Sent Youtube: {ctx.author}")

    @youtube.error
    async def youtube_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            embed = discord.Embed(
                color=self.bot.embed_color,
                title="→ Invalid Argument",
                description="• Please put in a vaild option! Example: `l!youtube <comment>`"
            )

            await ctx.send(embed=embed)

    @commands.command()
    async def triggered(self, ctx):
        picture = ctx.author.avatar_url_as(size=1024, format=None, static_format='png')
        async with aiohttp.ClientSession() as cs:
            async with cs.get(f"https://some-random-api.ml/canvas/triggered?avatar={picture}") as r:
                res = io.BytesIO(await r.read())
                triggered_file = discord.File(res, filename=f"triggered.gif")
                embed = discord.Embed(
                    color=self.bot.embed_color,
                    title="→ Triggered",
                )
                embed.set_image(url="attachment://triggered.gif")

                await ctx.send(embed=embed, file=triggered_file)

                logger.info(f"Images | Sent Triggered: {ctx.author}")


def setup(bot):
    bot.add_cog(Image(bot))
