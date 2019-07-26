import discord
from discord.ext import commands


class Kick(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command(pass_context=True)
    @commands.has_permissions(kick_members=True)
    async def kick(self, ctx, member: discord.Member, *, reason="No reason provided!"):
        embed = discord.Embed(
            color=discord.Color.from_rgb(241, 90, 36)
        )
        sender = ctx.author
        await member.kick(reason=reason)
        embed.set_author(name=sender)
        embed.add_field(name="• Kick command", value=f"{member.mention} → has been **kicked!** Bye bye! :wave:")

        await ctx.send(embed=embed)

        embed2 = discord.Embed(
            color=discord.Color.from_rgb(241, 90, 36)
        )
        embed2.set_author(name=f"{member} → You have been kicked!")
        embed2.add_field(name=f"• Moderator", value=f"{sender}")
        embed2.add_field(name="• Reason", value=f"{reason}")
        embed2.set_footer(text=f"Kicked from: {ctx.guild}")

        await member.send(embed=embed2)

    @kick.error
    async def kick_error(self, ctx, error):
        member = ctx.author
        if isinstance(error, commands.MissingRequiredArgument):
            embed = discord.Embed(
                color=discord.Color.from_rgb(241, 90, 36)
            )
            embed.set_author(name=member)
            embed.add_field(name="• Invalid Argument!",
                            value="Please put a valid option! Example: `l!kick @user <reason>`")

            await ctx.send(embed=embed)
        elif isinstance(error, commands.MissingPermissions):
            embed = discord.Embed(
                color=discord.Color.from_rgb(241, 90, 36)
            )
            embed.set_author(name=member)
            embed.add_field(name="• Missing Permissions!", value="You do not have permissions to run this command!")

            await ctx.send(embed=embed)
        else:
            raise error


def setup(client):
    client.add_cog(Kick(client))
