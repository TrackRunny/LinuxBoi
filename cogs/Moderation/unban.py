import random
import discord
from discord.ext import commands


class Unban(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    @commands.has_permissions(ban_members=True, manage_roles=True)
    async def unban(self, ctx, *, id: int):
        await ctx.guild.unban(discord.Object(id))
        embed = discord.Embed(
            color=discord.Color.from_rgb(241, 90, 36)
        )
        sender = ctx.author
        embed.set_author(name=f"{sender}")
        embed.add_field(name="• Unban command", value=f"<@{id}> → has been **Unbanned!** Welcome back! :wave:")
        await ctx.send(embed=embed)

    @unban.error
    async def unban_error(self, ctx, error):
        member = ctx.author
        if isinstance(error, commands.MissingRequiredArgument):
            embed = discord.Embed(
                color=discord.Color.from_rgb(241, 90, 36)
            )
            embed.set_author(name="• Invalid Argument!")
            embed.add_field(name=member, value="Please put a valid Discord ID! Example: `l!unban 546812331213062144`")
            await ctx.send(embed=embed)
        elif isinstance(error, commands.MissingPermissions):
            embed = discord.Embed(
                color=discord.Color.from_rgb(241, 90, 36)
            )
            embed.set_author(name="• Missing Permissions!")
            embed.add_field(name=member, value="You do not have permissions to run this command!")

            await ctx.send(embed=embed)


def setup(client):
    client.add_cog(Unban(client))
