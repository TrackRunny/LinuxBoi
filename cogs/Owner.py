# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# LinuxBoi - Discord bot                                                    #
# Copyright (C) 2019-2020 TrackRunny                                        #
#                                                                           #
# This program is free software: you can redistribute it and/or modify      #
# it under the terms of the GNU General Public License as published by      #
# the Free Software Foundation, either version 3 of the License, or         #
# (at your option) any later version.                                       #
#                                                                           #
# This program is distributed in the hope that it will be useful,           #
# but WITHOUT ANY WARRANTY; without even the implied warranty of            #
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the             #
# GNU General Public License for more details.                              #
#                                                                           #
# You should have received a copy of the GNU General Public License         #
# along with this program. If not, see <https://www.gnu.org/licenses/>.     #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

import random

import discord
import requests
from discord.ext import commands

from logging_files.owner_logging import logger


class Owner(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def status(self, ctx, online_status):
        if str(online_status).lower() == "dnd":
            await self.bot.change_presence(status=discord.Status.dnd)
        elif str(online_status).lower() == "idle":
            await self.bot.change_presence(status=discord.Status.idle)
        elif str(online_status).lower() == "offline":
            await self.bot.change_presence(status=discord.Status.offline)
        else:
            await self.bot.change_presence(status=discord.Status.online)

        embed = discord.Embed(
            color=self.bot.embed_color,
            title="→ Online Status Changed!",
            description=f"• My status has been updated to: `{online_status.lower()}`"
        )

        await ctx.send(embed=embed)

        logger.info(f"Owner | Sent Status: {ctx.author} | Online Status: {online_status}")

    @status.error
    async def change_status_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            embed = discord.Embed(
                color=self.bot.embed_color,
                title="→ Invalid Argument!",
                description="• Please put a valid option! Example: `l!status <online status>`"
            )
            await ctx.send(embed=embed)

    @commands.is_owner()
    @commands.command()
    async def name(self, ctx, name):
        await self.bot.user.edit(username=name)

        embed = discord.Embed(
            color=self.bot.embed_color,
            title="→ Bot Name Changed!",
            description=f"• My name has been updated to: `{name}`"
        )

        await ctx.send(embed=embed)

        logger.info(f"Owner | Sent Name: {ctx.author} | Name: {name}")

    @name.error
    async def name_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            embed = discord.Embed(
                color=self.bot.embed_color,
                title="→ Invalid Argument!",
                description="• Please put a valid option! Example: `l!name <name>`"
            )
            await ctx.send(embed=embed)
        elif isinstance(error, commands.CommandError):
            embed = discord.Embed(
                color=self.bot.embed_color,
                title="→ Unknown Error Has Occurred ",
                description=f"```python"
                            f"{error}"
                            f"```"
            )
            await ctx.send(embed=embed)

    @commands.is_owner()
    @commands.command()
    async def guilds(self, ctx):
        post = requests.post("https://hasteb.in/documents", data=f"\n".join([guild.name for guild in self.bot.guilds]).encode("utf-8"))

        embed = discord.Embed(
            color=self.bot.embed_color,
            title=f"→ Current amount of Guilds",
            description=f"• Guilds: **https://hasteb.in/{post.json()['key']}**"
        )

        await ctx.send(embed=embed)

        logger.info(f"Owner | Sent guilds: {ctx.author}")

    @commands.is_owner()
    @commands.command()
    async def get_invite(self, ctx, id: int):
        guild = self.bot.get_guild(id)

        for channel in guild.text_channels:
            channels = [channel.id]

        picked = random.choice(channels)
        channel = self.bot.get_channel(picked)

        embed = discord.Embed(
            color=self.bot.embed_color,
            title=f"→ Invite From Guild",
            description=f"• Invite: {await channel.create_invite(max_uses=1)}"
        )

        await ctx.author.send(embed=embed)

        logger.info(f"Owner | Sent Get Invite: {ctx.author}")

    @commands.is_owner()
    @commands.command()
    async def say(self, ctx, channel: discord.TextChannel, *, message):
        await channel.send(message)

        logger.info(f"Fun | Sent Say: {ctx.author}")

    @say.error
    async def say_error(self, ctx, error):
        if isinstance(error, commands.BadArgument):
            embed = discord.Embed(
                color=self.bot.embed_color,
                title="→ Invalid Channel!",
                description="• Please put a valid channel! Example: `l!say #channel <message>`"
            )
            await ctx.send(embed=embed)
        elif isinstance(error, commands.MissingRequiredArgument):
            embed = discord.Embed(
                color=self.bot.embed_color,
                title="→ Invalid Argument!",
                description="• Please put a valid option! Example: `l!say #channel <message>`"
            )
            await ctx.send(embed=embed)

    @commands.command()
    @commands.is_owner()
    async def shutdown(self, ctx):
        embed = discord.Embed(
            color=self.bot.embed_color,
            title="→ Shutdown",
            description="• Performing a shutdown on the bot... ( :wave: )"
        )

        await ctx.send(embed=embed)
        await self.bot.logout()

        logger.info(f"Owner | Sent Shutdown: {ctx.author}")

    @commands.command(aliases=["updatenews"])
    @commands.is_owner()
    async def update_news(self, ctx, *, news):
        self.bot.cursor.execute("UPDATE bot_information SET NEWS = ? WHERE ROWID = 1", (news,))
        self.bot.db.commit()

        embed = discord.Embed(
            color=self.bot.embed_color,
            title="→ News Updated",
            description=f"• News is now set to: `{news}`"
        )

        await ctx.send(embed=embed)

        logger.info(f"Owner | Sent Update News : {ctx.author}")

    @commands.command()
    @commands.is_owner()
    async def activity(self, ctx, number, *, activity):
        # Type 0 = Playing a game, Type 1 = Live on Twitch, Type 2 = Listening, Type 3 = Watching
        await self.bot.change_presence(activity=discord.Activity(type=number, name=activity))

        self.bot.cursor.execute("UPDATE bot_information SET ACTIVITY = ? WHERE ROWID = 1", (activity,))
        self.bot.cursor.execute("UPDATE bot_information SET ACTIVITY_TYPE = ? WHERE ROWID = 1", (number,))

        self.bot.db.commit()

        embed = discord.Embed(
            color=self.bot.embed_color,
            title="→ Bot Activity Changed!",
            description=f"• My activity has been updated to: `{activity}`"
        )

        await ctx.send(embed=embed)

        logger.info(f"Owner | Sent Activity: {ctx.author} | Activity: {number} | Status: {activity}")

    @activity.error
    async def activity_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            embed = discord.Embed(
                color=self.bot.embed_color,
                title="→ Invalid Argument!",
                description="• Please put a valid option! Example: `l!activity <type> <status>`"
            )
            await ctx.send(embed=embed)


def setup(client):
    client.add_cog(Owner(client))
