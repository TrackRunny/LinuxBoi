import discord
from discord.ext import commands
from logging_files.moderation_logging import logger


class ForceBan(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    @commands.has_permissions(ban_members=True)
    @commands.bot_has_permissions(ban_members=True)
    async def forceban(self, ctx, *, id: int):
        await ctx.guild.ban(discord.Object(id))
        embed = discord.Embed(
            color=discord.Color.from_rgb(241, 90, 36),
            title="• Forceban Command",
            description=f"<@{id}> → has been **Forcefully banned!** Bye bye! :wave:"
        )

        await ctx.send(embed=embed)

        logger.info(f"Moderation | Sent Force Ban: {ctx.author} | Force Banned: {id}")

    @forceban.error
    async def forceban_error(self, ctx, error):
        if isinstance(error, commands.BadArgument):
            embed = discord.Embed(
                color=discord.Color.from_rgb(241, 90, 36),
                title="→ Invalid ID!",
                description="• Please use a valid Discord ID! Example: `l!forceban <ID>`"
            )
            await ctx.send(embed=embed)
        elif isinstance(error, commands.MissingRequiredArgument):
            embed = discord.Embed(
                color=discord.Color.from_rgb(241, 90, 36),
                title="→ Invalid Argument!",
                description="• Please put a valid argument! Example: `l!forceban <ID>`"
            )
            await ctx.send(embed=embed)
        elif isinstance(error, commands.MissingPermissions):
            embed = discord.Embed(
                color=discord.Color.from_rgb(241, 90, 36),
                title="→ Missing Permissions",
                description="• You do not have permissions to run this command!"
            )
            await ctx.send(embed=embed)
        elif isinstance(error, commands.BotMissingPermissions):
            embed = discord.Embed(
                color=discord.Color.from_rgb(241, 90, 36),
                title="→ Bot Missing Permissions!",
                description="• Please give me permissions to use this command!"
            )


def setup(client):
    client.add_cog(ForceBan(client))
