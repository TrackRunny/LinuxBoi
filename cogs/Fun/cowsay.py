import discord
from discord.ext import commands
from cowpy import cow
from logging_files.fun_logging import logger


class CowSay(commands.Cog):

    def __init__(self, client):
        self.client = client

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


def setup(client):
    client.add_cog(CowSay(client))
