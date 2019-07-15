import discord
from discord.ext import commands, tasks
import os
import pyowm
import psutil
import random


class Purge(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command(pass_context=True)
    @commands.has_permissions(manage_messages=True, manage_roles=True, ban_members=True, kick_members=True)
    async def purge(self, ctx, amount: int):
        await ctx.channel.purge(limit=amount)

    @purge.error
    async def kick_error(self, ctx, error):
        member = ctx.author
        if isinstance(error, commands.MissingRequiredArgument):
            embed = discord.Embed(
                color=discord.Color.from_rgb(241, 90, 36)
            )
            embed.set_author(name="• Invalid Argument!")
            embed.add_field(name=member, value="Please put a valid option! Example: `> purge 5`")
            await ctx.send(embed=embed)
        elif isinstance(error, commands.MissingPermissions):
            embed = discord.Embed(
                color=discord.Color.from_rgb(241, 90, 36)
            )
            embed.set_author(name="• Missing Permissions!")
            embed.add_field(name=member, value="You do not have permissions to run this command!")

            await ctx.send(embed=embed)


def setup(client):
    client.add_cog(Purge(client))
