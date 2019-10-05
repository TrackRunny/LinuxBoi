import discord
from discord.ext import commands


class Shrug(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command()
    async def shrug(self, ctx):
        embed = discord.Embed(
            color=discord.Color.from_rgb(241, 90, 36)
        )
        embed.add_field(name="→ What is life?", value="• I gave up on it. ¯\_(ツ)_/¯")

        await ctx.send(embed=embed)


def setup(client):
    client.add_cog(Shrug(client))
