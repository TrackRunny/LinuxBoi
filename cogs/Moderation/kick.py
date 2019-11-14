import discord
import traceback
from discord.ext import commands
from logging_files.moderation_logging import logger


class Kick(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command(pass_context=True)
    @commands.has_permissions(kick_members=True)
    @commands.bot_has_permissions(kick_members=True)
    async def kick(self, ctx, member: discord.Member, *, reason="No reason provided!"):
        if ctx.guild.me.top_role < member.top_role:
            embed = discord.Embed(
                color=discord.Color.from_rgb(241, 90, 36),
                title="→ User information",
                description="• The user has higher permissions than me!"
            )
            await ctx.send(embed=embed)
        elif ctx.author.top_role <= member.top_role:
            embed = discord.Embed(
                color=discord.Color.from_rgb(241, 90, 36),
                title="→ User information",
                description="• The user has higher permissions than you or equal permissions!"
            )
            await ctx.send(embed=embed)
        elif ctx.guild.me.top_role > member.top_role:
            embed = discord.Embed(
                color=discord.Color.from_rgb(241, 90, 36),
                title="• Kick Command",
                description=f"{member.mention} → has been **kicked!** Bye bye! :wave:"
            )
            sender = ctx.author
            await member.kick(reason=reason)

            await ctx.send(embed=embed)

            embed2 = discord.Embed(
                color=discord.Color.from_rgb(241, 90, 36),
                title=f"{member} → You have been kicked!"
            )
            embed2.add_field(name=f"• Moderator", value=f"{sender}")
            embed2.add_field(name="• Reason", value=f"{reason}")
            embed2.set_footer(text=f"Kicked from: {ctx.guild}")

            await member.send(embed=embed2)

            logger.info(f"Moderation | Sent Kick: {ctx.author} | Kicked: {member} | Reason: {reason}")
        else:
            traceback.print_exc()

    @kick.error
    async def kick_error(self, ctx, error):
        if isinstance(error, commands.BadArgument):
            embed = discord.Embed(
                color=discord.Color.from_rgb(241, 90, 36),
                title="→ Invalid Member!",
                description="• Please mention a valid member! Example: `l!kick @user [reason]`"
            )
        elif isinstance(error, commands.MissingRequiredArgument):
            embed = discord.Embed(
                color=discord.Color.from_rgb(241, 90, 36),
                title="→ Invalid Argument!",
                description="• Please put a valid option! Example: `l!kick @user [reason]`"
            )
            await ctx.send(embed=embed)
        elif isinstance(error, commands.MissingPermissions):
            embed = discord.Embed(
                color=discord.Color.from_rgb(241, 90, 36),
                title="→ Missing Permissions",
                description="• You do not have permissions to run this command!"
            )
            await ctx.send(embed=embed)
        elif isinstance(error, commands.BotMissingPermissions):
            embed = discord.Embed(
                color=discord.Color.from_rgb(241, 90, 36),
                title="→ Bot Missing Permissions!",
                description="• Please give me permissions to use this command!"
            )
            await ctx.send(embed=embed)
        else:
            raise error


def setup(client):
    client.add_cog(Kick(client))
