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
import sqlite3
from datetime import datetime

import discord
from discord.ext import commands
from colorama import Style, Fore

line_divide = "\n———————————————————————————————"

linuxboi_testing_token = os.environ.get('linuxboi_testing_token')

intents = discord.Intents.default()
intents.members = True
intents.presences = True

cogs = [
    "Events",
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
        super().__init__(command_prefix="lt!", intents=intents, owner_id=546812331213062144, reconnect=True, case_insensitive=False)

        self.embed_color = 0xF15A24
        self.db = sqlite3.connect("database.db")
        self.cursor = self.db.cursor()
        self.console_info_format = f"{Fore.BLUE}{datetime.now().strftime('%H:%M:%S')}{Fore.RESET} {Style.BRIGHT}[{Fore.BLUE}INFO{Fore.RESET}]{Style.RESET_ALL}"

        self.load_extension('jishaku')
        self.remove_command('help')

    async def on_connect(self):
        os.system("clear")
        print(f"{self.console_info_format} LinuxBoi-testing is starting up...")

        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS bot_information (
            ACTIVITY TEXT NOT NULL,
            ACTIVITY_TYPE INTEGER NOT NULL,
            NEWS TEXT NOT NULL);
        """)

        self.cursor.execute("SELECT rowid, * FROM bot_information")

        if self.cursor.fetchone() is None:
            self.cursor.execute("INSERT INTO bot_information VALUES ('Linux videos! | l!help', '3', 'No current news yet!')")
        else:
            pass

        self.db.commit()

    async def on_ready(self):
        os.system("clear")

        get_activity = self.cursor.execute("SELECT rowid, * FROM bot_information")
        activity = get_activity.fetchall()[0][1]

        get_type = self.cursor.execute("SELECT rowid, * FROM bot_information")
        type = get_type.fetchall()[0][2]

        await self.change_presence(activity=discord.Activity(type=type, name=activity))

        if not hasattr(self, 'uptime'):
            self.uptime = datetime.utcnow()

        try:
            for cog in cogs:
                self.load_extension(f"cogs.{cog}")
        except Exception as e:
            print(f"Could not load extension {e}")

        print(f"{self.console_info_format} ---------------LinuxBoi-testing-----------------------"
              f"\n{self.console_info_format} Bot is online and connected to {self.user}"
              f"\n{self.console_info_format} Created by TrackRunny#0001 on Discord"
              f"\n{self.console_info_format} Connected to {(len(self.guilds))} Guilds."
              f"\n{self.console_info_format} Detected Operating System: {sys.platform.title()}"
              f"\n{self.console_info_format} ----------------------------------------------------")


LinuxBoiTesting().run(linuxboi_testing_token)
