import discord
from discord.ext import commands
import asyncurban

u = asyncurban.UrbanDictionary()


class Definition(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.group(invoke_without_command=True)
    async def word(self, ctx):
        embed = discord.Embed(
            color=discord.Color.from_rgb(241, 90, 36)
        )
        embed.add_field(name="→ Invalid Argument!",
                        value="• Please put in a valid option! Example: `l!word <random / search> [Word name]`")
        await ctx.send(embed=embed)

    @word.command()
    async def random(self, ctx):
        word = await u.get_random()
        embed = discord.Embed(
            color=discord.Color.from_rgb(241, 90, 36)
        )
        embed.add_field(name="→ Random Word", value=f"Word: `{word}`"
                                                    f"\n Definition: `{word.definition}`")
        await ctx.send(embed=embed)

    @word.command()
    async def search(self, ctx, *, query):
        word = await u.get_word(query)
        embed = discord.Embed(
            color=discord.Color.from_rgb(241, 90, 36)
        )
        embed.add_field(name="→ Searched word", value=f"Word: `{word}`"
                                                      f"\n Definition: `{word.definition}`")
        await ctx.send(embed=embed)

    @search.error
    async def currency_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            embed = discord.Embed(
                color=discord.Color.from_rgb(241, 90, 36)
            )
            embed.add_field(name="→ Invalid Argument!",
                            value="• Please put in a valid option! Example: `l!word search <Word>`")
            await ctx.send(embed=embed)


def setup(client):
    client.add_cog(Definition(client))
