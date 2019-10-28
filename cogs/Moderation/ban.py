import discord
import traceback
from discord.ext import commands
from logging_files.moderation_logging import logger


class Ban(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command()
    @commands.has_permissions(ban_members=True)
    @commands.bot_has_permissions(ban_members=True)
    async def ban(self, ctx, member: discord.Member, *, reason="No reason provided!"):
        if ctx.guild.me.top_role < member.top_role:
            embed = discord.Embed(
                color=discord.Color.from_rgb(241, 90, 36)
            )
            embed.add_field(name="→ User information",
                            value="• The user has higher permissions than me!")
            await ctx.send(embed=embed)
        elif ctx.author.top_role <= member.top_role:
            embed = discord.Embed(
                color=discord.Color.from_rgb(241, 90, 36)
            )
            embed.add_field(name="→ User information",
                            value="• The user has higher permissions than you or equal permissions!")
            await ctx.send(embed=embed)
        elif ctx.guild.me.top_role > member.top_role:
            embed = discord.Embed(
                color=discord.Color.from_rgb(241, 90, 36)
            )
            sender = ctx.author
            await member.ban(reason=reason)
            embed.add_field(name="• Ban command", value=member.mention + " → has been **Banned!** Bye bye! :wave:")

            await ctx.send(embed=embed)

            embed2 = discord.Embed(
                color=discord.Color.from_rgb(241, 90, 36)
            )
            embed2.set_author(name=f"{member} → You have been banned!")
            embed2.add_field(name=f"• Moderator", value=f"{sender}")
            embed2.add_field(name="• Reason", value=f"{reason}")
            embed2.set_footer(text=f"Banned from: {ctx.guild}")

            await member.send(embed=embed2)

            await logger.info(f"Moderation | Sent Ban: {ctx.author} | Banned: {member} | Reason: {reason}")
        else:
            traceback.print_exc()

    @ban.error
    async def ban_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            embed = discord.Embed(
                color=discord.Color.from_rgb(241, 90, 36)
            )
            embed.add_field(name="→ Invalid Argument!",
                            value="• Please put a valid option! Example: `l!ban @user [reason]`")
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
    client.add_cog(Ban(client))
