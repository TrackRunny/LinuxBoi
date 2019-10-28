import discord
import traceback
from discord.ext import commands
from logging_files.moderation_logging import logger


class AddRole(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command(aliases=["addrole"])
    @commands.has_permissions(manage_roles=True)
    @commands.bot_has_permissions(manage_roles=True)
    async def add_role(self, ctx, role: discord.Role, member: discord.Member,):
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
            await member.add_roles(role)
            embed = discord.Embed(
                color=discord.Color.from_rgb(241, 90, 36)
            )
            embed.add_field(name="• Add Role command!", value=f"{member.mention} → Has been given the role `{role}`")

            await ctx.send(embed=embed)

            await logger.info(f"Moderation | Sent Addrole: {ctx.author} | Role added: {role} | To: {member}")
        else:
            traceback.print_exc()

    @add_role.error
    async def add_role_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            embed = discord.Embed(
                color=discord.Color.from_rgb(241, 90, 36)
            )
            embed.add_field(name="→ Invalid Argument!",
                            value="• Please put a valid option! Example: `l!addrole <Role ID / Rolename> @user`")
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
    client.add_cog(AddRole(client))
