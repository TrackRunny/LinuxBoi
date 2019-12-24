"""
LinuxBoi - Discord bot
Copyright (C) 2019 TrackRunny

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program. If not, see <https://www.gnu.org/licenses/>.
"""

import discord
import traceback
from discord.ext import commands
from logging_files.moderation_logging import logger


class Moderation(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases=["addrole"])
    @commands.has_permissions(manage_roles=True)
    @commands.bot_has_permissions(manage_roles=True)
    async def add_role(self, ctx, role: discord.Role, member: discord.Member,):
        if ctx.guild.me.top_role < member.top_role:
            embed = discord.Embed(
                color=self.bot.embed_color,
                title="→ User information",
                description="• The user has higher permissions than me!"
            )
            await ctx.send(embed=embed)
        elif ctx.author.top_role <= member.top_role:
            embed = discord.Embed(
                color=self.bot.embed_color,
                title="→ User information",
                description="• The user has higher permissions than you or equal permissions!"
            )
            await ctx.send(embed=embed)
        elif ctx.guild.me.top_role > member.top_role:
            await member.add_roles(role)
            embed = discord.Embed(
                color=self.bot.embed_color,
                title="• Add Role command!",
                description=f"{member.mention} → Has been given the role `{role}`"
            )

            await ctx.send(embed=embed)

            logger.info(f"Moderation | Sent Addrole: {ctx.author} | Role added: {role} | To: {member}")
        else:
            traceback.print_exc()

    @add_role.error
    async def add_role_error(self, ctx, error):
        if isinstance(error, commands.BadArgument):
            embed = discord.Embed(
                color=self.bot.embed_color,
                title="→ Invalid Role / Member!",
                description="• Please select a valid role / member! Example: `l!addrole <role ID / rolename> @user`"
            )
            await ctx.send(embed=embed)
        elif isinstance(error, commands.MissingRequiredArgument):
            embed = discord.Embed(
                color=self.bot.embed_color,
                title="→ Invalid Argument!",
                description="• Please put a valid option! Example: `l!addrole <Role ID / Rolename> @user`"
            )
            await ctx.send(embed=embed)
        elif isinstance(error, commands.MissingPermissions):
            embed = discord.Embed(
                color=self.bot.embed_color,
                title="→ Missing Permissions",
                description="• You do not have permissions to run this command!"
            )
            await ctx.send(embed=embed)
        elif isinstance(error, commands.BotMissingPermissions):
            embed = discord.Embed(
                color=self.bot.embed_color,
                title="→ Bot Missing Permissions!",
                description="• Please give me permissions to use this command!"
            )
            await ctx.send(embed=embed)

    @commands.command()
    @commands.has_permissions(ban_members=True)
    @commands.bot_has_permissions(ban_members=True)
    async def ban(self, ctx, member: discord.Member, *, reason="No reason provided!"):
        if ctx.guild.me.top_role < member.top_role:
            embed = discord.Embed(
                color=self.bot.embed_color,
                title="→ User information",
                description="• The user has higher permissions than me!"
            )
            await ctx.send(embed=embed)
        elif ctx.author.top_role <= member.top_role:
            embed = discord.Embed(
                color=self.bot.embed_color,
                title="→ User information",
                description="• The user has higher permissions than you or equal permissions!"
            )
            await ctx.send(embed=embed)
        elif ctx.guild.me.top_role > member.top_role:
            embed = discord.Embed(
                color=self.bot.embed_color,
                title="• Ban command",
                description=f"{member.mention} → has been **Banned!** Bye bye! :wave:"
            )

            sender = ctx.author
            await member.ban(reason=reason)

            await ctx.send(embed=embed)

            embed2 = discord.Embed(
                color=self.bot.embed_color,
                title=f"{member} → You have been banned!"
            )
            embed2.add_field(name=f"• Moderator", value=f"{sender}")
            embed2.add_field(name="• Reason", value=f"{reason}")
            embed2.set_footer(text=f"Banned from: {ctx.guild}")

            await member.send(embed=embed2)

            logger.info(f"Moderation | Sent Ban: {ctx.author} | Banned: {member} | Reason: {reason}")
        else:
            traceback.print_exc()

    @ban.error
    async def ban_error(self, ctx, error):
        if isinstance(error, commands.BadArgument):
            embed = discord.Embed(
                color=self.bot.embed_color,
                title="→ Invalid Member!",
                description="• Please mention a valid member! Example: `l!ban @user [reason]`"
            )
            await ctx.send(embed=embed)
        elif isinstance(error, commands.MissingRequiredArgument):
            embed = discord.Embed(
                color=self.bot.embed_color,
                title="→ Invalid Argument!",
                description="• Please put a valid option! Example: `l!ban @user [reason]`"
            )
            await ctx.send(embed=embed)
        elif isinstance(error, commands.MissingPermissions):
            embed = discord.Embed(
                color=self.bot.embed_color,
                title="→ Missing Permissions",
                description="• You do not have permissions to run this command!"
            )
            await ctx.send(embed=embed)
        elif isinstance(error, commands.BotMissingPermissions):
            embed = discord.Embed(
                color=self.bot.embed_color,
                title="→ Bot Missing Permissions!",
                description="• Please give me permissions to use this command!"
            )
            await ctx.send(embed=embed)

    @commands.command()
    @commands.has_permissions(manage_nicknames=True)
    @commands.bot_has_permissions(manage_nicknames=True)
    async def nickname(self, ctx, member: discord.Member, *, nickname):
        if ctx.guild.me.top_role < member.top_role:
            embed = discord.Embed(
                color=self.bot.embed_color,
                title="→ User information",
                description="• The user has higher permissions than me!"
            )
            await ctx.send(embed=embed)
        elif ctx.author.top_role <= member.top_role:
            embed = discord.Embed(
                color=self.bot.embed_color,
                title="→ User information",
                description="• The user has higher permissions than you or equal permissions!"
            )
            await ctx.send(embed=embed)
        elif ctx.guild.me.top_role > member.top_role:
            embed = discord.Embed(
                color=self.bot.embed_color,
                title="• Nickname command",
                description=f"{member.mention}'s → Nickname has been **Changed!**"
            )

            await member.edit(nick=nickname)
            await ctx.send(embed=embed)

            logger.info(f"Moderation | Sent Change Nickname: {ctx.author} | Nickname: {nickname} | To: {member}")
        else:
            traceback.print_exc()

    @nickname.error
    async def nickname_error(self, ctx, error):
        if isinstance(error, commands.BadArgument):
            embed = discord.Embed(
                color=self.bot.embed_color,
                title="→ Invalid Member!",
                description="• Please mention a valid member! Example: `l!nickname @user <nickname>`"
            )
            await ctx.send(embed=embed)
        elif isinstance(error, commands.MissingRequiredArgument):
            embed = discord.Embed(
                color=self.bot.embed_color,
                title="→ Invalid Argument!",
                description="• Please put a valid option! Example: `l!nickname @user <nickname>`"
            )
            await ctx.send(embed=embed)
        elif isinstance(error, commands.MissingPermissions):
            embed = discord.Embed(
                color=self.bot.embed_color,
                title="→ Missing Permissions",
                description="• You do not have permissions to run this command!"
            )
            await ctx.send(embed=embed)
        elif isinstance(error, commands.BotMissingPermissions):
            embed = discord.Embed(
                color=self.bot.embed_color,
                title="→ Bot Missing Permissions!",
                description="• Please give me permissions to use this command!"
            )
            await ctx.send(embed=embed)

    @commands.command()
    @commands.has_permissions(ban_members=True)
    @commands.bot_has_permissions(ban_members=True)
    async def forceban(self, ctx, *, id: int):
        await ctx.guild.ban(discord.Object(id))
        embed = discord.Embed(
            color=self.bot.embed_color,
            title="• Forceban Command",
            description=f"<@{id}> → has been **Forcefully banned!** Bye bye! :wave:"
        )

        await ctx.send(embed=embed)

        logger.info(f"Moderation | Sent Force Ban: {ctx.author} | Force Banned: {id}")

    @forceban.error
    async def forceban_error(self, ctx, error):
        if isinstance(error, commands.BadArgument):
            embed = discord.Embed(
                color=self.bot.embed_color,
                title="→ Invalid ID!",
                description="• Please use a valid Discord ID! Example: `l!forceban <ID>`"
            )
            await ctx.send(embed=embed)
        elif isinstance(error, commands.MissingRequiredArgument):
            embed = discord.Embed(
                color=self.bot.embed_color,
                title="→ Invalid Argument!",
                description="• Please put a valid argument! Example: `l!forceban <ID>`"
            )
            await ctx.send(embed=embed)
        elif isinstance(error, commands.MissingPermissions):
            embed = discord.Embed(
                color=self.bot.embed_color,
                title="→ Missing Permissions",
                description="• You do not have permissions to run this command!"
            )
            await ctx.send(embed=embed)
        elif isinstance(error, commands.BotMissingPermissions):
            embed = discord.Embed(
                color=self.bot.embed_color,
                title="→ Bot Missing Permissions!",
                description="• Please give me permissions to use this command!"
            )
            await ctx.send(embed=embed)

    @commands.command(pass_context=True)
    @commands.has_permissions(kick_members=True)
    @commands.bot_has_permissions(kick_members=True)
    async def kick(self, ctx, member: discord.Member, *, reason="No reason provided!"):
        if ctx.guild.me.top_role < member.top_role:
            embed = discord.Embed(
                color=self.bot.embed_color,
                title="→ User information",
                description="• The user has higher permissions than me!"
            )
            await ctx.send(embed=embed)
        elif ctx.author.top_role <= member.top_role:
            embed = discord.Embed(
                color=self.bot.embed_color,
                title="→ User information",
                description="• The user has higher permissions than you or equal permissions!"
            )
            await ctx.send(embed=embed)
        elif ctx.guild.me.top_role > member.top_role:
            embed = discord.Embed(
                color=self.bot.embed_color,
                title="• Kick Command",
                description=f"{member.mention} → has been **kicked!** Bye bye! :wave:"
            )
            sender = ctx.author
            await member.kick(reason=reason)

            await ctx.send(embed=embed)

            embed2 = discord.Embed(
                color=self.bot.embed_color,
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
                color=self.bot.embed_color,
                title="→ Invalid Member!",
                description="• Please mention a valid member! Example: `l!kick @user [reason]`"
            )
            await ctx.send(embed=embed)
        elif isinstance(error, commands.MissingRequiredArgument):
            embed = discord.Embed(
                color=self.bot.embed_color,
                title="→ Invalid Argument!",
                description="• Please put a valid option! Example: `l!kick @user [reason]`"
            )
            await ctx.send(embed=embed)
        elif isinstance(error, commands.MissingPermissions):
            embed = discord.Embed(
                color=self.bot.embed_color,
                title="→ Missing Permissions",
                description="• You do not have permissions to run this command!"
            )
            await ctx.send(embed=embed)
        elif isinstance(error, commands.BotMissingPermissions):
            embed = discord.Embed(
                color=self.bot.embed_color,
                title="→ Bot Missing Permissions!",
                description="• Please give me permissions to use this command!"
            )
            await ctx.send(embed=embed)
        else:
            raise error

    @commands.command()
    @commands.has_permissions(manage_messages=True)
    @commands.bot_has_permissions(manage_messages=True)
    async def purge(self, ctx, amount: int):
        await ctx.channel.purge(limit=amount)

        logger.info(f"Moderation | Sent Purge: {ctx.author} | Purged: {amount} messages")

    @purge.error
    async def purge_error(self, ctx, error):
        if isinstance(error, commands.BadArgument):
            embed = discord.Embed(
                color=self.bot.embed_color,
                title="→ Invalid Amount Of Messages!",
                description="• Please put a valid number! Example: `l!purge <number>`"
            )
            await ctx.send(embed=embed)
        elif isinstance(error, commands.MissingRequiredArgument):
            embed = discord.Embed(
                color=self.bot.embed_color,
                title="→ Invalid Argument!",
                description="• Please put a valid option! Example: `l!purge <number>`"
            )
            await ctx.send(embed=embed)
        elif isinstance(error, commands.MissingPermissions):
            embed = discord.Embed(
                color=self.bot.embed_color,
                title="→ Missing Permissions",
                description="• You do not have permissions to run this command!"
            )
            await ctx.send(embed=embed)
        elif isinstance(error, commands.BotMissingPermissions):
            embed = discord.Embed(
                color=self.bot.embed_color,
                title="→ Bot Missing Permissions!",
                description="• Please give me permissions to use this command!"
            )
            await ctx.send(embed=embed)

    @commands.command(aliases=["removerole", "delrole"])
    @commands.has_permissions(manage_roles=True)
    @commands.bot_has_permissions(manage_roles=True)
    async def remove_role(self, ctx, role: discord.Role, member: discord.Member,):
        if ctx.guild.me.top_role < member.top_role:
            embed = discord.Embed(
                color=self.bot.embed_color,
                title="→ User information",
                description="• The user has higher permissions than me!"
            )
            await ctx.send(embed=embed)
        elif ctx.author.top_role <= member.top_role:
            embed = discord.Embed(
                color=self.bot.embed_color,
                title="→ User information",
                description="• The user has higher permissions than you or equal permissions!"
            )
            await ctx.send(embed=embed)
        elif ctx.guild.me.top_role > member.top_role:
            await member.remove_roles(role)
            embed = discord.Embed(
                color=self.bot.embed_color,
                title="• Remove Role Command",
                description=f"{member.mention} → Lost the role `{role}`"
            )

            await ctx.send(embed=embed)

            logger.info(f"Moderation | Sent Remove Role: {ctx.author} | Removed Role: {role} | To: {member}")
        else:
            traceback.print_exc()

    @remove_role.error
    async def remove_role_error(self, ctx, error):
        if isinstance(error, commands.BadArgument):
            embed = discord.Embed(
                color=self.bot.embed_color,
                title="→ Invalid Role / Member!",
                description="• Please select a valid role / member! Example: `l!delrole <role ID / rolename> @user`"
            )
            await ctx.send(embed=embed)
        elif isinstance(error, commands.MissingRequiredArgument):
            embed = discord.Embed(
                color=self.bot.embed_color,
                title="→ Invalid Argument!",
                description="• Please put a valid option! Example: `l!delrole <Role ID / Rolename> @user`"
            )
            await ctx.send(embed=embed)
        elif isinstance(error, commands.MissingPermissions):
            embed = discord.Embed(
                color=self.bot.embed_color,
                title="→ Missing Permissions",
                description="• You do not have permissions to run this command!"
            )
            await ctx.send(embed=embed)
        elif isinstance(error, commands.BotMissingPermissions):
            embed = discord.Embed(
                color=self.bot.embed_color,
                title="→ Bot Missing Permissions!",
                description="• Please give me permissions to use this command!"
            )
            await ctx.send(embed=embed)

    @commands.command()
    @commands.has_permissions(manage_nicknames=True)
    @commands.bot_has_permissions(manage_nicknames=True)
    async def resetnick(self, ctx, member: discord.Member):
        if ctx.guild.me.top_role < member.top_role:
            embed = discord.Embed(
                color=self.bot.embed_color,
                title="→ User information",
                description="• The user has higher permissions than me!"
            )
            await ctx.send(embed=embed)
        elif ctx.author.top_role <= member.top_role:
            embed = discord.Embed(
                color=self.bot.embed_color,
                title="→ User information",
                description="• The user has higher permissions than you or equal permissions!"
            )
            await ctx.send(embed=embed)
        elif ctx.guild.me.top_role > member.top_role:
            embed = discord.Embed(
                color=self.bot.embed_color,
                title="• Resetnick Command",
                description=f"{member.mention}'s → Nickname has been **Reset!**"
            )

            await member.edit(nick=None)
            await ctx.send(embed=embed)

            logger.info(f"Moderation | Sent Reset Nickname: {ctx.author} | To: {member}")
        else:
            traceback.print_exc()

    @resetnick.error
    async def nickname_error(self, ctx, error):
        if isinstance(error, commands.BadArgument):
            embed = discord.Embed(
                color=self.bot.embed_color,
                title="→ Invalid Member!",
                description="• Please mention a valid member! Example: `l!resetnick @user`"
            )
            await ctx.send(embed=embed)
        elif isinstance(error, commands.MissingRequiredArgument):
            embed = discord.Embed(
                color=self.bot.embed_color,
                title="→ Invalid Argument!",
                description="• Please put a valid option! Example: `l!resetnick @user`"
            )
            await ctx.send(embed=embed)
        elif isinstance(error, commands.MissingPermissions):
            embed = discord.Embed(
                color=self.bot.embed_color,
                title="→ Missing Permissions!",
                description="• You do not have permissions to run this command!"
            )

            await ctx.send(embed=embed)
        elif isinstance(error, commands.MissingPermissions):
            embed = discord.Embed(
                color=self.bot.embed_color,
                title="→ Missing Permissions",
                description="• You do not have permissions to run this command!"
            )
            await ctx.send(embed=embed)
        elif isinstance(error, commands.BotMissingPermissions):
            embed = discord.Embed(
                color=self.bot.embed_color,
                title="→ Bot Missing Permissions!",
                description="• Please give me permissions to use this command!"
            )
            await ctx.send(embed=embed)
        else:
            traceback.print_exc()

    @commands.command()
    @commands.has_permissions(ban_members=True)
    @commands.bot_has_permissions(ban_members=True)
    async def unban(self, ctx, *, id: int):
        await ctx.guild.unban(discord.Object(id))
        embed = discord.Embed(
            color=self.bot.embed_color,
            title="• Unban Command",
            description=f"<@{id}> → has been **Unbanned!** Welcome back! :wave:"
        )
        await ctx.send(embed=embed)

        logger.info(f"Moderation | Sent Unban: {ctx.author} | Unbanned: {id}")

    @unban.error
    async def unban_error(self, ctx, error):
        if isinstance(error, commands.BadArgument):
            embed = discord.Embed(
                color=self.bot.embed_color,
                title="→ Invalid ID!",
                description="• Please use a valid Discord ID! Example: `l!unban <ID>`"
            )
            await ctx.send(embed=embed)
        elif isinstance(error, commands.MissingRequiredArgument):
            embed = discord.Embed(
                color=self.bot.embed_color,
                title="→ Invalid Argument!",
                description="• Please put a valid Discord ID! Example: `l!unban 546812331213062144`"
            )
            await ctx.send(embed=embed)
        elif isinstance(error, commands.MissingPermissions):
            embed = discord.Embed(
                color=self.bot.embed_color,
                title="→ Missing Permissions",
                description="• You do not have permissions to run this command!"
            )
            await ctx.send(embed=embed)
        elif isinstance(error, commands.BotMissingPermissions):
            embed = discord.Embed(
                color=self.bot.embed_color,
                title="→ Bot Missing Permissions!",
                description="• Please give me permissions to use this command!"
            )
            await ctx.send(embed=embed)

    @commands.command()
    @commands.has_permissions(manage_messages=True)
    @commands.bot_has_permissions(manage_messages=True)
    async def warn(self, ctx, member: discord.Member, *, reason="No reason provided!"):
        if ctx.guild.me.top_role < member.top_role:
            embed = discord.Embed(
                color=self.bot.embed_color,
                title="→ User information",
                description="• The user has higher permissions than me!"
            )
            await ctx.send(embed=embed)
        elif ctx.guild.me.top_role > member.top_role:
            sender = ctx.author
            embed = discord.Embed(
                color=self.bot.embed_color,
                title="• Warn Command",
                description=f"{member.mention} → has been **Warned!**"
            )

            await ctx.send(embed=embed)

            embed2 = discord.Embed(
                color=self.bot.embed_color,
                title=f"{member} → You have been warned!"
            )
            embed2.add_field(name=f"• Moderator", value=f"`{sender}`")
            embed2.add_field(name="• Reason", value=f"`{reason}`")
            embed2.set_footer(text=f"Warning sent from: {ctx.guild}")

            await member.send(embed=embed2)

            logger.info(f"Moderation | Sent Warn: {ctx.author} | Warned: {member} | Reason: {reason}")

    @warn.error
    async def warn_error(self, ctx, error):
        if isinstance(error, commands.BadArgument):
            embed = discord.Embed(
                color=self.bot.embed_color,
                title="→ Invalid Member!",
                description="• Please mention a valid member! Example: `l!warn @user [reason]`"
            )
            await ctx.send(embed=embed)
        if isinstance(error, commands.MissingRequiredArgument):
            embed = discord.Embed(
                color=self.bot.embed_color,
                title="→ Invalid Argument!",
                description="• Please put a valid option! Example: `l!warn @user [reason]`"
            )
            await ctx.send(embed=embed)
        elif isinstance(error, commands.MissingPermissions):
            embed = discord.Embed(
                color=self.bot.embed_color,
                title="→ Missing Permissions",
                description="• You do not have permissions to run this command!"
            )
            await ctx.send(embed=embed)
        elif isinstance(error, commands.BotMissingPermissions):
            embed = discord.Embed(
                color=self.bot.embed_color,
                title="→ Bot Missing Permissions!",
                description="• Please give me permissions to use this command!"
            )
            await ctx.send(embed=embed)


def setup(bot):
    bot.add_cog(Moderation(bot))
