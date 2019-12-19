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
from discord.ext import commands


class LinuxInfo(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command()
    async def channels(self, ctx):
        embed = discord.Embed(
            color=self.client.embed_color
        )
        embed.add_field(name="→ Need to know Linux Channels",
                        value=f"\n—"
                        f"\n→ These linux channels are all linux channels I would recommend watching."
                        f"\n→ These channels all provide content "
                        f"for all of your needs depending on what you want to watch."
                        f"\n→ Please note these channels are not in order from best to worst."
                        f"\n—")
        embed.set_thumbnail(url="https://www.pointillist.com/wp-content/uploads/2017/10/youtube-logo-1024x1024.jpg")
        joe = "(http://bit.ly/301xNkj)"
        switched = "(http://bit.ly/2I8Xswn)"
        average_linux_user = "(http://bit.ly/2O1bpAg)"
        chris_titus_tech = "(http://bit.ly/2O2TM30)"
        addictive_tips_tv = "(http://bit.ly/2O1fx3m)"
        the_linux_experiment = "(http://bit.ly/302zRZp)"

        embed.add_field(name="• Educational",
                        value=f"1. [Joe Collins]{joe} - Helped a lot of new people switch to Linux. Makes really easy to understand videos about different Linux topics."
                              f"\n2. [Switched to Linux]{switched} - Posts videos about new Linux news as well as information about privacy, scams, virus's, and other drama."
                              f"\n3. [Average Linux User]{average_linux_user} - Makes great tutorial videos that are easy to walk through. Clear and concise when talking."
                              f"\n4. [Chris Titus Tech]{chris_titus_tech} - Says things like they are and takes all the confusing things away from Linux and makes things simple. So many helpful videos worth watching."
                              f"\n5. [AddictiveTipsTV]{addictive_tips_tv} - Posts quick 1-3 minute videos for quick tips about Linux, and other software. Great for watching if your in a time crunch. "
                              f"\n6. [The Linux Experiment]{the_linux_experiment} - Clean, elegant, and simple videos. Posts linux news that you could have missed each month that no other Linux youtuber currently does.")

        await ctx.send(embed=embed)


def setup(client):
    client.add_cog(LinuxInfo(client))
