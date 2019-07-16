import discord
from discord.ext import commands, tasks
import os
import pyowm
import psutil
import random


class Avatar(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command()
    async def avatar(self, ctx, member: discord.Member):

        embed = discord.Embed(
            color=discord.Color.from_rgb(241, 90, 36)
        )
        embed.set_author(name=f"• Avatar")
        embed.set_image(url=member.avatar_url)

        await ctx.send(embed=embed)


def setup(client):
    client.add_cog(Avatar(client))
