import discord
from discord.ext import commands
from logging_files.fun_logging import logger


class Say(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.is_owner()
    @commands.command()
    async def say(self, ctx, channel: discord.TextChannel, *, message):
        await channel.send(message)

        logger.info(f"Fun | Sent Say: {ctx.author}")

    @say.error
    async def say_error(self, ctx, error):
        if isinstance(error, commands.BadArgument):
            embed = discord.Embed(
                color=discord.Color.from_rgb(241, 90, 36),
                title="→ Invalid Channel!",
                description="• Please put a valid channel! Example: `l!say #channel <message>`"
            )
            await ctx.send(embed=embed)
        elif isinstance(error, commands.MissingRequiredArgument):
            embed = discord.Embed(
                color=discord.Color.from_rgb(241, 90, 36),
                title="→ Invalid Argument!",
                description="• Please put a valid option! Example: `l!say #channel <message>`"
            )
            await ctx.send(embed=embed)


def setup(client):
    client.add_cog(Say(client))
