import discord
import asyncurban
from discord.ext import commands
from logging_files.utility_logging import logger


u = asyncurban.UrbanDictionary()


class Definition(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.group(invoke_without_command=True)
    async def word(self, ctx):
        embed = discord.Embed(
            color=discord.Color.from_rgb(241, 90, 36),
            title="→ Invalid Argument!",
            description="• Please put in a valid option! Example: `l!word <random / search> [Word name]`"
        )
        await ctx.send(embed=embed)

    @word.command()
    async def random(self, ctx):
        word = await u.get_random()
        embed = discord.Embed(
            color=discord.Color.from_rgb(241, 90, 36),
            title="→ Random Word",
            description=f"Word: `{word}`"
                        f"\n Definition: `{word.definition}`"
        )

        await ctx.send(embed=embed)

        logger.info(f"Utility | Sent Word Random: {ctx.author}")

    @word.command()
    async def search(self, ctx, *, query):
        word = await u.get_word(query)
        embed = discord.Embed(
            color=discord.Color.from_rgb(241, 90, 36),
            title="→ Searched word",
            description=f"Word: `{word}`"
                        f"\n Definition: `{word.definition}`"
        )

        await ctx.send(embed=embed)

        logger.info(f"Utility | Sent Word Search: {ctx.author} | Searched: {query}")

    @search.error
    async def currency_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            embed = discord.Embed(
                color=discord.Color.from_rgb(241, 90, 36),
                title="→ Invalid Argument!",
                description="• Please put in a valid option! Example: `l!word search <Word>`"
            )
            await ctx.send(embed=embed)


def setup(client):
    client.add_cog(Definition(client))
