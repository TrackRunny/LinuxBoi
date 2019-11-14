import random
import discord
from discord.ext import commands
from logging_files.fun_logging import logger


class HowGay(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def howgay(self, ctx, member: discord.Member):
        embed = discord.Embed(
            color=discord.Color.from_rgb(241, 90, 36),
            title="→ Howgay?"
        )
        embed.add_field(name="The account is...",
                        value=f"{random.randint(1, 100)}% gay :gay_pride_flag: → {str(member.mention)}")

        await ctx.send(embed=embed)

        logger.info(f"Fun | Sent Howgay: {ctx.author}")

    @howgay.error
    async def howgay_error(self, ctx, error):
        if isinstance(error, commands.BadArgument):
            embed = discord.Embed(
                color=discord.Color.from_rgb(241, 90, 36),
                title="→ Invalid Member!",
                description="• Please mention a valid member! Example: `l!howgay @user`"
            )
            await ctx.send(embed=embed)
        elif isinstance(error, commands.MissingRequiredArgument):
            embed = discord.Embed(
                color=discord.Color.from_rgb(241, 90, 36),
                title="→ Invalid Argument!",
                description="• Please put a valid option! Example: `l!howgay @user`"
            )
            await ctx.send(embed=embed)


def setup(client):
    client.add_cog(HowGay(client))
