"""
LinuxBoi - Discord bot
Copyright (C) 2019 TrackRunny

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program. If not, see <https://www.gnu.org/licenses/>.
"""

import discord
import aiohttp
import random
import re
import fortune
from discord.ext import commands
from cowpy import cow
from dadjokes import Dadjoke
from logging_files.fun_logging import logger


class Fun(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command(aliases=["8ball"])
    async def _8ball(self, ctx, *, question, ):
        responses = ["It is certain.",
                     "It is decidedly so.",
                     "Without a doubt.",
                     "Yes - definitely.",
                     "You may rely on it.",
                     "As I see it, yes.",
                     "Most likely.",
                     "Outlook good.",
                     "Yes.",
                     "Signs point to yes.",
                     "Reply hazy, try again.",
                     "Ask again later.",
                     "Better not tell you now.",
                     "Cannot predict now.",
                     "Concentrate and ask again.",
                     "Don't count on it.",
                     "My reply is no.",
                     "My sources say no.",
                     "Outlook not so good.",
                     "Very doubtful."]
        embed = discord.Embed(
            color=discord.Color.from_rgb(241, 90, 36),
            title="→ 8Ball command"
        )
        embed.add_field(name="• Question :grey_question: ", inline=False, value=f"{question}")
        embed.add_field(name="• Answer :8ball: ", inline=False, value=f"{random.choice(responses)}")

        await ctx.send(embed=embed)

        logger.info(f"Fun | Sent 8ball: {ctx.author}")

    @_8ball.error
    async def _8ball_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            embed = discord.Embed(
                color=discord.Color.from_rgb(241, 90, 36)
            )
            embed.add_field(name="→ Invalid Argument!",
                            value="• Please put in a valid option! Example: `l!8ball <question>`")
            await ctx.send(embed=embed)

    @commands.command()
    async def avatar(self, ctx, member: discord.Member):
        embed = discord.Embed(
            color=discord.Color.from_rgb(241, 90, 36),
            title="→ Avatar"
        )
        embed.set_image(url=member.avatar_url_as(size=4096, format=None, static_format="png"))

        await ctx.send(embed=embed)

        logger.info(f"Fun | Sent Avatar: {ctx.author}")

    @avatar.error
    async def avatar_error(self, ctx, error):
        if isinstance(error, commands.BadArgument):
            embed = discord.Embed(
                color=discord.Color.from_rgb(241, 90, 36),
                title="→ Invalid Member!",
                description="• Please mention a valid member! Example: `l!avatar @user`"
            )
            await ctx.send(embed=embed)
        elif isinstance(error, commands.MissingRequiredArgument):
            embed = discord.Embed(
                color=discord.Color.from_rgb(241, 90, 36),
                title="→ Invalid Argument",
                description="• Please put a valid option! Example: `l!avatar @user`"
            )
            await ctx.send(embed=embed)

    @commands.command(aliases=["chuck-norris"])
    async def chuck_norris(self, ctx):
        async with aiohttp.ClientSession() as cs:
            async with cs.get('https://api.icndb.com/jokes/random?limitTo=[nerdy]') as r:
                res = await r.json()
                embed = discord.Embed(
                    color=discord.Color.from_rgb(241, 90, 36),
                    title="→ Chuck Norris Joke",
                    description=f"• Joke: {res['value']['joke']}"
                )

                await ctx.send(embed=embed)

                logger.info(f"Fun | Sent Chuck Norris: {ctx.author}")

    @commands.command()
    async def coinflip(self, ctx):
        choices = ("Heads!", "Tails!")
        coin = random.choice(choices)
        embed = discord.Embed(
            color=discord.Color.from_rgb(241, 90, 36),
            title="→ Coinflip Command",
            description=coin
        )

        await ctx.send(embed=embed)

        logger.info(f"Fun | Sent Coinflip: {ctx.author}")
        
    @commands.command()
    async def cowsay(self, ctx, *, message):
        moo = cow.Cowacter(thoughts=True)
        msg = moo.milk(msg=message)
        embed = discord.Embed(
            color=discord.Color.from_rgb(241, 90, 36),
            title="→ Cowsay 🐮",
            description=f"Moo! ```{msg}                                             ```"
        )

        await ctx.send(embed=embed)

        logger.info(f"Fun | Sent Cowsay: {ctx.author}")

    @cowsay.error
    async def cowsay_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            embed = discord.Embed(
                color=discord.Color.from_rgb(241, 90, 36),
                title="→ Invalid Argument!",
                description="• Please put in a valid option! Example: `l!cowsay Moo!`"
            )
            await ctx.send(embed=embed)

    @commands.command()
    async def dadjoke(self, ctx):
        random_dadjoke = Dadjoke()
        embed = discord.Embed(
            color=discord.Color.from_rgb(241, 90, 36),
            title="→ Random Dad Joke!",
            description=f"• {random_dadjoke.joke}"
        )

        await ctx.send(embed=embed)

        logger.info(f"Fun | Sent Dadjoke: {ctx.author}")
        
    @commands.command()
    async def dice(self, ctx, *, msg='1'):
        dice_rolls = []
        dice_roll_ints = []
        try:
            (dice, sides) = re.split('[d\\s]', msg)
        except ValueError:
            dice = msg
            sides = '6'
        try:
            for roll in range(int(dice)):
                result = random.randint(1, int(sides))
                dice_rolls.append(str(result))
                dice_roll_ints.append(result)
        except ValueError:
            pass
        embed = discord.Embed(
            color=discord.Color.from_rgb(241, 90, 36),
            title="→ Dice Command"
        )
        # ' '.join(dice_rolls)
        embed.add_field(name="→ Rolled Dice Numbers:", value=f" ".join(dice_rolls))
        embed.add_field(name="→ Total number:", inline=False, value=f" {sum(dice_roll_ints)}")
        await ctx.send('', embed=embed)

        logger.info(f"Fun | Sent Dice: {ctx.author}")
        
    @commands.command()
    async def fortune(self, ctx):
        file = "./External_Command_Files/fortunes.txt"
        embed = discord.Embed(
            color=discord.Color.from_rgb(241, 90, 36),
            title="→ Random Fortune!",
            description=f"• {fortune.get_random_fortune(file)}"
        )

        await ctx.send(embed=embed)

        logger.info(f"Fun | Sent Fortune: {ctx.author}")
        
    @commands.command()
    async def joke(self, ctx):
        async with aiohttp.ClientSession() as cs:
            async with cs.get('https://official-joke-api.appspot.com/jokes/general/random') as r:
                res = await r.json()
                embed = discord.Embed(
                    color=discord.Color.from_rgb(241, 90, 36),
                    title="→ Random Joke!",
                    description=f"• Question: {res[0]['setup']}"
                                f"\n• Joke: {res[0]['punchline']}"
                )
                await ctx.send(embed=embed)

                logger.info(f"Fun | Sent Joke: {ctx.author}")
    
    @commands.command()
    async def history(self, ctx):
        async with aiohttp.ClientSession() as cs:
            async with cs.get('http://numbersapi.com/random/date?json') as r:
                res = await r.json()
                embed = discord.Embed(
                    color=discord.Color.from_rgb(241, 90, 36),
                    title="→ Random History Date!",
                    description=f"• Fact: {res['text']}"
                                f"\n• Year: {res['year']}"
                )

                await ctx.send(embed=embed)

                logger.info(f"Fun | Sent History: {ctx.author}")
                
    @commands.command()
    async def howgay(self, ctx, member: discord.Member):
        embed = discord.Embed(
            color=discord.Color.from_rgb(241, 90, 36),
            title="→ Howgay?"
        )
        embed.add_field(name="The account is...",
                        value=f"{random.randint(1, 100)}% gay :gay_pride_flag: → {str(member.mention)}")

        await ctx.send(embed=embed)

        logger.info(f"Fun | Sent Howgay: {ctx.author}")

    @howgay.error
    async def howgay_error(self, ctx, error):
        if isinstance(error, commands.BadArgument):
            embed = discord.Embed(
                color=discord.Color.from_rgb(241, 90, 36),
                title="→ Invalid Member!",
                description="• Please mention a valid member! Example: `l!howgay @user`"
            )
            await ctx.send(embed=embed)
        elif isinstance(error, commands.MissingRequiredArgument):
            embed = discord.Embed(
                color=discord.Color.from_rgb(241, 90, 36),
                title="→ Invalid Argument!",
                description="• Please put a valid option! Example: `l!howgay @user`"
            )
            await ctx.send(embed=embed)
            
    @commands.command()
    async def joke(self, ctx):
        async with aiohttp.ClientSession() as cs:
            async with cs.get('https://official-joke-api.appspot.com/jokes/general/random') as r:
                res = await r.json()
                embed = discord.Embed(
                    color=discord.Color.from_rgb(241, 90, 36),
                    title="→ Random Joke!",
                    description=f"• Question: {res[0]['setup']}"
                                f"\n• Joke: {res[0]['punchline']}"
                )
                await ctx.send(embed=embed)

                logger.info(f"Fun | Sent Joke: {ctx.author}")
                
    @commands.command()
    async def math(self, ctx):
        async with aiohttp.ClientSession() as cs:
            async with cs.get('http://numbersapi.com/random/math?json') as r:
                res = await r.json()
                embed = discord.Embed(
                    color=discord.Color.from_rgb(241, 90, 36),
                    title="→ Random Math Fact!",
                    description=f"• Fact: {res['text']}"
                                f"\n• Number: {res['number']}"
                )
                await ctx.send(embed=embed)

                logger.info(f"Fun | Sent Math: {ctx.author}")
                
    @commands.command()
    async def penguinsay(self, ctx, *, message):
        moo = cow.Tux(thoughts=True)
        msg = moo.milk(msg=message)
        embed = discord.Embed(
            color=discord.Color.from_rgb(241, 90, 36),
            title="→ Listen to the penguin",
            description=f"```{msg}                                         ```"
        )

        await ctx.send(embed=embed)

        logger.info(f"Fun | Sent Penguinsay: {ctx.author}")

    @penguinsay.error
    async def penguinsay_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            embed = discord.Embed(
                color=discord.Color.from_rgb(241, 90, 36),
                title="→ Invalid Argument!",
                description="• Please put in a valid option! Example: `l!penguinsay <text>`"
            )
            await ctx.send(embed=embed)
            
    @commands.command()
    async def shrug(self, ctx):
        embed = discord.Embed(
            color=discord.Color.from_rgb(241, 90, 36),
            title="→ What is life?",
            description="• I gave up on it. ¯\_(ツ)_/¯"
        )

        await ctx.send(embed=embed)

        logger.info(f"Fun | Sent Shrug: {ctx.author}")
        
    @commands.command(aliases=["momma-joke", "yo-momma-joke"])
    async def yo_momma_joke(self, ctx):
        async with aiohttp.ClientSession() as cs:
            async with cs.get('https://api.yomomma.info/') as r:
                res = await r.json(content_type='text/html')
                embed = discord.Embed(
                    color=discord.Color.from_rgb(241, 90, 36),
                    title="→ Yo Momma Joke",
                    description=f"• Joke: {res['joke']}"
                )

                await ctx.send(embed=embed)

                logger.info(f"Fun | Sent Yo Momma Joke: {ctx.author}")


def setup(client):
    client.add_cog(Fun(client))