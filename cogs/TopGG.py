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


import os

import dbl
from discord.ext import commands

from logging_files.top_gg_logging import logger


class TopGG(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
        self.token = os.environ.get("top_gg_token")
        self.dblpy = dbl.DBLClient(self.bot, self.token, autopost=True)

    @commands.Cog.listener()
    async def on_dbl_test(self, data):
        print(data)

    @commands.Cog.listener()
    async def on_dbl_vote(self, data):
        user = await self.bot.fetch_user(int(data['user']))
        logger.info(f"TopGG | Vote From: {str(user)}")

    @commands.Cog.listener()
    async def on_guild_join(self, guild):
        await self.bot.dblpy.post_guild_count()

    @commands.Cog.listener()
    async def on_guild_remove(self, guild):
        await self.bot.dblpy.post_guild_count()

    @commands.Cog.listener()
    async def on_guild_post(self):
        logger.info(f"TopGG | Posted Updated Guild Count")


def setup(bot):
    bot.add_cog(TopGG(bot))
