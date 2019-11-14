import discord
from discord.ext import commands
from logging_files.moderation_logging import logger


class Unban(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    @commands.has_permissions(ban_members=True)
    @commands.bot_has_permissions(ban_members=True)
    async def unban(self, ctx, *, id: int):
        await ctx.guild.unban(discord.Object(id))
        embed = discord.Embed(
            color=discord.Color.from_rgb(241, 90, 36),
            title="• Unban Command",
            description=f"<@{id}> → has been **Unbanned!** Welcome back! :wave:"
        )
        await ctx.send(embed=embed)

        logger.info(f"Moderation | Sent Unban: {ctx.author} | Unbanned: {id}")

    @unban.error
    async def unban_error(self, ctx, error):
        if isinstance(error, commands.BadArgument):
            embed = discord.Embed(
                color=discord.Color.from_rgb(241, 90, 36),
                title="→ Invalid ID!",
                description="• Please use a valid Discord ID! Example: `l!unban <ID>`"
            )
        elif isinstance(error, commands.MissingRequiredArgument):
            embed = discord.Embed(
                color=discord.Color.from_rgb(241, 90, 36),
                title="→ Invalid Argument!",
                description="• Please put a valid Discord ID! Example: `l!unban 546812331213062144`"
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
            await ctx.send(embed=embed)


def setup(client):
    client.add_cog(Unban(client))
