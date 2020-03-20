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
import json
import random
import re

import aiohttp
import discord
import fortune

from cowpy import cow
from dadjokes import Dadjoke
from discord.ext import commands

from logging_files.fun_logging import logger


class Fun(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

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
            color=self.bot.embed_color,
            title="→ 8Ball Command"
        )
        embed.add_field(name="• Question :grey_question: ", inline=False, value=f"{question}")
        embed.add_field(name="• Answer :8ball: ", inline=False, value=f"{random.choice(responses)}")

        await ctx.send(embed=embed)

        logger.info(f"Fun | Sent 8ball: {ctx.author}")

    @_8ball.error
    async def _8ball_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            embed = discord.Embed(
                color=self.bot.embed_color
            )
            embed.add_field(name="→ Invalid Argument!",
                            value="• Please put in a valid option! Example: `l!8ball <question>`")
            await ctx.send(embed=embed)

    @commands.command()
    async def avatar(self, ctx, member: discord.Member):
        embed = discord.Embed(
            color=self.bot.embed_color,
            title="→ Avatar"
        )
        embed.set_image(url=member.avatar_url_as(size=1024, format=None, static_format="png"))

        await ctx.send(embed=embed)

        logger.info(f"Fun | Sent Avatar: {ctx.author}")

    @avatar.error
    async def avatar_error(self, ctx, error):
        if isinstance(error, commands.BadArgument):
            embed = discord.Embed(
                color=self.bot.embed_color,
                title="→ Invalid Member!",
                description="• Please mention a valid member! Example: `l!avatar @user`"
            )
            await ctx.send(embed=embed)
        elif isinstance(error, commands.MissingRequiredArgument):
            embed = discord.Embed(
                color=self.bot.embed_color,
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
                    color=self.bot.embed_color,
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
            color=self.bot.embed_color,
            title="→ Coinflip Command",
            description=f"• {coin}"
        )

        await ctx.send(embed=embed)

        logger.info(f"Fun | Sent Coinflip: {ctx.author}")

    @commands.command()
    async def cowsay(self, ctx, *, message):
        moo = cow.Cowacter(thoughts=True)
        msg = moo.milk(msg=message)
        embed = discord.Embed(
            color=self.bot.embed_color,
            title="→ Cowsay 🐮",
            description=f"Moo! ```{msg}                                             ```"
        )

        await ctx.send(embed=embed)

        logger.info(f"Fun | Sent Cowsay: {ctx.author}")

    @cowsay.error
    async def cowsay_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            embed = discord.Embed(
                color=self.bot.embed_color,
                title="→ Invalid Argument!",
                description="• Please put in a valid option! Example: `l!cowsay Moo!`"
            )
            await ctx.send(embed=embed)

    @commands.command()
    async def dadjoke(self, ctx):
        random_dadjoke = Dadjoke()
        embed = discord.Embed(
            color=self.bot.embed_color,
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
            color=self.bot.embed_color,
            title="→ Dice Command"
        )
        # ' '.join(dice_rolls)
        embed.add_field(name="• Rolled Dice Numbers:", value=f" ".join(dice_rolls))
        embed.add_field(name="• Total number:", inline=False, value=f" {sum(dice_roll_ints)}")
        await ctx.send('', embed=embed)

        logger.info(f"Fun | Sent Dice: {ctx.author}")

    @commands.command()
    async def fortune(self, ctx):
        file = "./resources/fortunes.txt"
        embed = discord.Embed(
            color=self.bot.embed_color,
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
                    color=self.bot.embed_color,
                    title="→ Random Joke!",
                    description=f"• Question: {res[0]['setup']}"
                                f"\n• Joke: {res[0]['punchline']}"
                )
                await ctx.send(embed=embed)

                logger.info(f"Fun | Sent Joke: {ctx.author}")

    @commands.command()
    async def geekjoke(self, ctx):
        def random_digits(joke_count):
            # Return a joke index between first and last joke in data
            return random.randint(1, joke_count)

        def get_joke():
            # Return random joke
            with open('./resources/geekjokes.json', encoding="utf8") as data_file:
                data = json.load(data_file)
            joke = data[random_digits(len(data))]
            return joke

        embed = discord.Embed(
            color=discord.Color.from_rgb(241, 90, 36),
            title="→ Random Geek joke!",
            description=f"• {get_joke()}"
        )

        await ctx.send(embed=embed)

        logger.info(f"Fun | Sent Geekjoke: {ctx.author}")

    @commands.command()
    async def history(self, ctx):
        async with aiohttp.ClientSession() as cs:
            async with cs.get('http://numbersapi.com/random/date?json') as r:
                res = await r.json()
                embed = discord.Embed(
                    color=self.bot.embed_color,
                    title="→ Random History Date!",
                    description=f"• Fact: {res['text']}"
                                f"\n• Year: {res['year']}"
                )

                await ctx.send(embed=embed)

                logger.info(f"Fun | Sent History: {ctx.author}")

    @commands.command()
    async def howgay(self, ctx, member: discord.Member):
        embed = discord.Embed(
            color=self.bot.embed_color,
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
                color=self.bot.embed_color,
                title="→ Invalid Member!",
                description="• Please mention a valid member! Example: `l!howgay @user`"
            )
            await ctx.send(embed=embed)
        elif isinstance(error, commands.MissingRequiredArgument):
            embed = discord.Embed(
                color=self.bot.embed_color,
                title="→ Invalid Argument!",
                description="• Please put a valid option! Example: `l!howgay @user`"
            )
            await ctx.send(embed=embed)

    @commands.command()
    async def math(self, ctx):
        async with aiohttp.ClientSession() as cs:
            async with cs.get('http://numbersapi.com/random/math?json') as r:
                res = await r.json()
                embed = discord.Embed(
                    color=self.bot.embed_color,
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
            color=self.bot.embed_color,
            title="→ Listen to the Tux :penguin:",
            description=f"```{msg}                                         ```"
        )

        await ctx.send(embed=embed)

        logger.info(f"Fun | Sent Penguinsay: {ctx.author}")

    @penguinsay.error
    async def penguinsay_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            embed = discord.Embed(
                color=self.bot.embed_color,
                title="→ Invalid Argument!",
                description="• Please put in a valid option! Example: `l!penguinsay <text>`"
            )
            await ctx.send(embed=embed)

    @commands.command()
    async def shrug(self, ctx):
        embed = discord.Embed(
            color=self.bot.embed_color,
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
                    color=self.bot.embed_color,
                    title="→ Yo Momma Joke",
                    description=f"• Joke: {res['joke']}"
                )

                await ctx.send(embed=embed)

                logger.info(f"Fun | Sent Yo Momma Joke: {ctx.author}")

    @commands.command()
    async def rps(self, ctx, choice):
        robot_choices = [":fist:", ":hand_splayed:", "<:scissorshand:663864190078812203>"]
        picked = random.choice(robot_choices)

        player_choices = [":fist:", ":hand_splayed:", "<:scissorshand:663864190078812203>"]

        embed = discord.Embed(
            color=self.bot.embed_color,
            title="→ Invalid Choice!",
            description="• Please put a valid option! Example: `l!rps <rock/paper/scissors>`"
        )

        embed2 = discord.Embed(
            color=self.bot.embed_color,
            title="→ Rock Paper Scissors Game"
        )

        if str(choice) == "rock":
            embed2.add_field(name="• Player Choice", inline=False, value=player_choices[0])
            embed2.add_field(name="• Robot Choice", inline=False, value=picked)

            await ctx.send(embed=embed2)
        elif str(choice) == "paper":
            embed2.add_field(name="• Player Choice", inline=False, value=player_choices[1])
            embed2.add_field(name="• Robot Choice", inline=False, value=picked)

            await ctx.send(embed=embed2)
        elif str(choice) == "scissors":
            embed2.add_field(name="• Player Choice", inline=False, value=player_choices[2])
            embed2.add_field(name="• Robot Choice", inline=False, value=picked)

            await ctx.send(embed=embed2)
        else:
            await ctx.send(embed=embed)

        logger.info(f"Fun | Sent RPS: {ctx.author}")

    @rps.error
    async def rps_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            embed = discord.Embed(
                color=self.bot.embed_color,
                title="→ Invalid Argument!",
                description="• Please put a valid option! Example: `l!rps <rock/paper/scissors>`"
            )
            await ctx.send(embed=embed)

    @commands.command()
    async def advice(self, ctx):
        async with aiohttp.ClientSession() as cs:
            async with cs.get('https://api.adviceslip.com/advice') as r:
                res = await r.json(content_type="text/html")
                embed = discord.Embed(
                    color=self.bot.embed_color,
                    title="→ Random Advice!",
                    description=f"• Advice: {res['slip']['advice']}"
                )

                await ctx.send(embed=embed)

                logger.info(f"Fun | Sent Advice: {ctx.author}")

    @commands.command()
    async def catfact(self, ctx):
        async with aiohttp.ClientSession() as cs:
            async with cs.get('https://cat-fact.herokuapp.com/facts/random') as r:
                res = await r.json()
                embed = discord.Embed(
                    color=self.bot.embed_color,
                    title="→ Cat Fact",
                    description=f"• Fact: {res['text']}"
                )

                await ctx.send(embed=embed)

                logger.info(f"Fun | Sent CatFact: {ctx.author}")

    @commands.command()
    async def slot(self, ctx):
        emojis = "🍎🍊🍐🍋🍉🍇🍓🍒"

        first = random.choice(emojis)
        second = random.choice(emojis)
        third = random.choice(emojis)

        slot_machine = f"{first} | {second} | {third}"

        embed = discord.Embed(
            color=self.bot.embed_color,
            title="→ Slot Machine"
        )

        if first == second == third:
            embed.add_field(name="**• Winner! All Matching Fruits!**", value=slot_machine)
        elif (first == second) or (first == third) or (second == third):
            embed.add_field(name="**• Winner! Two in a Row!**", value=slot_machine)
        else:
            embed.add_field(name="**• Loser! No Matches!**", value=slot_machine)

        await ctx.send(embed=embed)

    @commands.command()
    async def question(self, ctx, question):
        async with aiohttp.ClientSession() as cs:
            async with cs.get('https://yesno.wtf/api') as r:
                res = await r.json()
                embed = discord.Embed(
                    color=self.bot.embed_color,
                    title=f"→ {res['answer'].title()}.",
                )
                embed.set_image(url=res['image'])

                await ctx.send(embed=embed)

    @question.error
    async def question_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            embed = discord.Embed(
                color=self.bot.embed_color,
                title="→ Invalid Argument!",
                description="• Please put a valid option! Example: `l!question <question>`"
            )
            await ctx.send(embed=embed)

    @commands.command()
    async def bill(self, ctx):
        async with aiohttp.ClientSession() as cs:
            async with cs.get('https://belikebill.ga/billgen-API.php?default=1') as r:
                res = io.BytesIO(await r.read())
                bill_file = discord.File(res, filename=f"bill.jpg")

                await ctx.send(file=bill_file)

                logger.info(f"Fun | Sent Bill: {ctx.author}")


def setup(bot):
    bot.add_cog(Fun(bot))
