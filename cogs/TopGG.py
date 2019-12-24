import dbl
import os
import discord
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
