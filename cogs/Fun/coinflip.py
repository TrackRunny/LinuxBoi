import random

import discord
from discord.ext import commands


class Coinflip(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def coinflip(self, ctx):
        choices = ("Heads!", "Tails!")
        coin = random.choice(choices)
        embed = discord.Embed(
            color=discord.Color.from_rgb(241, 90, 36)
        )
        sender = ctx.author
        embed.set_author(name=sender)
        embed.add_field(name="• Coinflip command", value=coin)

        await ctx.send(embed=embed)


def setup(client):
    client.add_cog(Coinflip(client))
