import discord
from discord.ext import commands


class Guilds(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.is_owner()
    @commands.command()
    async def guilds(self, ctx):
        for guild in self.client.guilds:
            embed = discord.Embed(
                color=discord.Color.from_rgb(241, 90, 36),
                title=f"→ Current List Of Guilds",
                description=f"```Guild: {guild} | ID: {guild.id}```"
            )

            await ctx.send(embed=embed)


def setup(client):
    client.add_cog(Guilds(client))