import discord
import requests
from discord.ext import commands
from logging_files.utility_logging import logger


class HasteBin(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command()
    async def hastebin(self, ctx, *, code):
        post = requests.post("https://hastebin.com/documents", data=code.encode('utf-8'))
        embed = discord.Embed(
            color=discord.Color.from_rgb(241, 90, 36)
        )
        embed.add_field(name="→ Uploaded code!", value="• https://hastebin.com/" + post.json()["key"])

        await ctx.send(embed=embed)

        await logger.info(f"Utility | Sent HasteBin: {ctx.author} | Code: {code}")

    @hastebin.error
    async def hastebin_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            embed = discord.Embed(
                color=discord.Color.from_rgb(241, 90, 36)
            )
            embed.add_field(name="→ Invalid Argument!",
                            value="• Please put in a valid option! Example: `l!hastebin <code>`"
                                  "\n• Real World Example: `l!hastebin print(\"Python is amazing!\")`")
            await ctx.send(embed=embed)


def setup(client):
    client.add_cog(HasteBin(client))
