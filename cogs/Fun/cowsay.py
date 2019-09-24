import discord
from discord.ext import commands
from cowpy import cow


class CowSay(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command()
    async def cowsay(self, ctx, *, message):
        moo = cow.Cowacter(thoughts=True)
        msg = moo.milk(msg=message)
        embed = discord.Embed(
            color=discord.Color.from_rgb(241, 90, 36)
        )
        embed.add_field(name="→ Cowsay 🐮", value=f"Moo! ```{msg}                                             ```")

        await ctx.send(embed=embed)

    @cowsay.error
    async def cowsay_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            embed = discord.Embed(
                color=discord.Color.from_rgb(241, 90, 36)
            )
            embed.add_field(name="→ Invalid Argument!",
                            value="• Please put in a valid option! Example: `l!cowsay Moo!`")
            await ctx.send(embed=embed)


def setup(client):
    client.add_cog(CowSay(client))
