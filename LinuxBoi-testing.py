#!/usr/bin/env python3

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

import os
import sys
from datetime import datetime

import discord
from discord.ext import commands

bot = commands.Bot("lt!", owner_id=546812331213062144, case_insensitive=False)
line_divide = "\n———————————————————————————————"

linuxboi_testing_token = os.environ.get('linuxboi_testing_token')

cogs = [
    "Fun",
    "Information",
    "Meme",
    "Moderation",
    "Owner",
    "Utility",
    "Images",
    "Music",
    "TopGG"
]


class LinuxBoiTesting(commands.AutoShardedBot):
    def __init__(self):
        super().__init__(command_prefix="lt!", owner_id=546812331213062144, reconnect=True, case_insensitive=False)

        self.bot = bot
        self.embed_color = 0xF15A24

        self.load_extension('jishaku')
        self.remove_command('help')

    async def on_ready(self):
        # change_status.start()
        await self.change_presence(activity=discord.Activity(type=3, name="Linux videos! | lt!help"))

        if not hasattr(self, 'uptime'):
            self.uptime = datetime.utcnow()

        try:
            for cog in cogs:
                self.load_extension(f"cogs.{cog}")
        except Exception as e:
            print(f"Could not load extension {e}")

        print(f"---------------LinuxBoi-testing-----------------------"
              f"\nBot is online and connected to {self.user}"
              f"\nCreated by TrackRunny#0001 on Discord"
              f"\nConnected to {(len(self.guilds))} Guilds."
              f"\nDetected Operating System: {sys.platform.title()}"
              f"\n----------------------------------------------------")


LinuxBoiTesting().run(linuxboi_testing_token)
# client.run(read_token(), bot=False)
