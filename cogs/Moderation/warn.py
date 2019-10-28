import discord
from discord.ext import commands
from logging_files.moderation_logging import logger


class Warn(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command()
    @commands.has_permissions(manage_messages=True)
    @commands.bot_has_permissions(manage_messages=True)
    async def warn(self, ctx, member: discord.Member, *, reason="No reason provided!"):
        if ctx.guild.me.top_role < member.top_role:
            embed = discord.Embed(
                color=discord.Color.from_rgb(241, 90, 36)
            )
            embed.add_field(name="→ User information",
                            value="• The user has higher permissions than me!")
            await ctx.send(embed=embed)
        elif ctx.guild.me.top_role > member.top_role:
            sender = ctx.author
            embed = discord.Embed(
                color=discord.Color.from_rgb(241, 90, 36)
            )
            embed.add_field(name="• Warn command", value=f"{member.mention} → has been **Warned!** ")
            await ctx.send(embed=embed)

            embed2 = discord.Embed(
                color=discord.Color.from_rgb(241, 90, 36)
            )
            embed2.set_author(name=f"{member} → You have been warned!")
            embed2.add_field(name=f"• Moderator", value=f"`{sender}`")
            embed2.add_field(name="• Reason", value=f"`{reason}`")
            embed2.set_footer(text=f"Warning sent from: {ctx.guild}")

            await member.send(embed=embed2)

            await logger.info(f"Moderation | Sent Warn: {ctx.author} | Warned: {member} | Reason: {reason}")

    @warn.error
    async def warn_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            embed = discord.Embed(
                color=discord.Color.from_rgb(241, 90, 36)
            )
            embed.add_field(name="→ Invalid Argument!",
                            value="• Please put a valid option! Example: `l!warn @user [reason]`")
            await ctx.send(embed=embed)
        elif isinstance(error, commands.MissingPermissions):
            embed = discord.Embed(
                color=discord.Color.from_rgb(241, 90, 36)
            )
            embed.add_field(name="→ Missing Permissions!", value="• You do not have permissions to run this command!")

            await ctx.send(embed=embed)
        elif isinstance(error, commands.BotMissingPermissions):
            embed = discord.Embed(
                color=discord.Color.from_rgb(241, 90, 36)
            )
            embed.add_field(name="→ Bot Missing Permissions!",
                            value="• Please give me permissions to use this command!")

            await ctx.send(embed=embed)


def setup(client):
    client.add_cog(Warn(client))
