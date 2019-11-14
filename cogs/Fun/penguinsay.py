import discord
from discord.ext import commands
from cowpy import cow
from logging_files.fun_logging import logger


class PenguinSay(commands.Cog):

    def __init__(self, client):
        self.client = client

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


def setup(client):
    client.add_cog(PenguinSay(client))
