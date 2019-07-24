import discord
from discord.ext import commands
import os

class Shutdown(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command()
    @commands.is_owner()
    async def shutdown(self, ctx):
        member = ctx.author
        embed = discord.Embed(
            color=discord.Color.from_rgb(241, 90, 36)
        )
        embed.set_author(name="• Shutdown")
        embed.add_field(name=member, value="→ Performing a shutdown on the bot... ( :wave: )")
        await ctx.send(embed=embed)
        await self.client.logout()


def setup(client):
    client.add_cog(Shutdown(client))
