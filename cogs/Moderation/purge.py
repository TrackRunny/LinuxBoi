import discord
from discord.ext import commands
from logging_files.moderation_logging import logger


class Purge(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command(pass_context=True)
    @commands.has_permissions(manage_messages=True)
    @commands.bot_has_permissions(manage_messages=True)
    async def purge(self, ctx, amount: int):
        await ctx.channel.purge(limit=amount)

        await logger.info(f"Moderation | Sent Purge: {ctx.author} | Purged: {amount} messages")

    @purge.error
    async def kick_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            embed = discord.Embed(
                color=discord.Color.from_rgb(241, 90, 36)
            )
            embed.add_field(name="→ Invalid Argument!", value="• Please put a valid option! Example: `l!purge 5`")
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
    client.add_cog(Purge(client))
