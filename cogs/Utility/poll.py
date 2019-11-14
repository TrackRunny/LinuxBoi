import discord
from discord.ext import commands
from logging_files.utility_logging import logger


class Poll(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def poll(self, ctx, channel: discord.TextChannel, *, question):
        sender = ctx.author
        embed = discord.Embed(
            color=discord.Color.from_rgb(241, 90, 36),
            title="→ Quick poll 📊"
        )
        embed.add_field(name="• Question", inline=False, value=question)
        embed.set_footer(text=f"— Poll from {sender}", icon_url=ctx.author.avatar_url)
        await ctx.message.delete()

        message = await channel.send(embed=embed)
        await message.add_reaction("👍")
        await message.add_reaction("👎")

        logger.info(f"Utility | Sent Poll: {ctx.author}")

    @poll.error
    async def poll_error(self, ctx, error):
        if isinstance(error, commands.BadArgument):
            embed = discord.Embed(
                color=discord.Color.from_rgb(241, 90, 36),
                title="→ Invalid Channel!",
                description="• Please put in a channel! Example: `l!poll #channel <question>`"
            )
            await ctx.send(embed=embed)
        elif isinstance(error, commands.MissingRequiredArgument):
            embed = discord.Embed(
                color=discord.Color.from_rgb(241, 90, 36),
                title="→ Invalid Argument!",
                description="• Please put in a valid option! Example: `l!poll #channel <question>`"
            )
            await ctx.send(embed=embed)


def setup(client):
    client.add_cog(Poll(client))
