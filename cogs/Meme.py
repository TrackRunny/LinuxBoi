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
import aiohttp
import os
from discord.ext import commands
from logging_files.meme_logging import logger


class Meme(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command()
    async def random_meme(self, ctx):
        async with aiohttp.ClientSession() as cs:
            async with cs.get(f"https://api.ksoft.si/images/random-meme",
                              headers={"Authorization": f"Bearer {os.environ.get('ksoft_key')}"}) as r:
                res = await r.json()
                embed = discord.Embed(
                    color=discord.Color.from_rgb(241, 90, 36),
                    title=f"→ {res['title']}",
                )
                embed.set_image(url=res['image_url'])
                embed.set_footer(text=f"👍 {res['upvotes']} | 👎 {res['downvotes']}")

                await ctx.send(embed=embed)

                logger.info(f"Meme | Sent Random Meme: {ctx.author}")


def setup(client):
    client.add_cog(Meme(client))
