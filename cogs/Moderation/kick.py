import discord
from discord.ext import commands, tasks
import os
import pyowm
import psutil
import random


class Kick(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command(pass_context=True)
    @commands.has_permissions(manage_roles=True, ban_members=True, kick_members=True)
    async def kick(self, ctx, member: discord.Member, *, reason=None):
        embed = discord.Embed(
            color=discord.Color.from_rgb(241, 90, 36)
        )
        sender = ctx.author
        await member.kick(reason=reason)
        embed.set_author(name=sender)
        embed.add_field(name="• Kick command", value=member.mention + " → has been **kicked!** Bye bye! :wave:")

        await ctx.send(embed=embed)

    @kick.error
    async def kick_error(self, ctx, error):
        member = ctx.author
        if isinstance(error, commands.MissingRequiredArgument):
            embed = discord.Embed(
                color=discord.Color.from_rgb(241, 90, 36)
            )
            embed.set_author(name="• Invalid Argument!")
            embed.add_field(name=member, value="Please put a valid option! Example: `>>> kick @user`")
            await ctx.send(embed=embed)
        elif isinstance(error, commands.MissingPermissions):
            embed = discord.Embed(
                color=discord.Color.from_rgb(241, 90, 36)
            )
            embed.set_author(name="• Missing Permissions!")
            embed.add_field(name=member, value="You do not have permissions to run this command!")

            await ctx.send(embed=embed)


def setup(client):
    client.add_cog(Kick(client))
