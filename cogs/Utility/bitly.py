import bitly_api
import discord
import os
from discord.ext import commands
from logging_files.utility_logging import logger


class Bitly(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command(aliases=["shortenlink"])
    @commands.cooldown(rate=1, per=10, type=commands.BucketType.user)
    async def bitly(self, ctx, *, link):
        try:
            api_user = os.environ.get("bitly_user")
            api_key = os.environ.get("bitly_key")

            b = bitly_api.Connection(api_user, api_key)

            long_url = link
            response = b.shorten(uri=long_url)

            embed = discord.Embed(
                color=discord.Color.from_rgb(241, 90, 36)
            )
            embed.set_author(name="→ URL Shortener")
            embed.add_field(name="• Long link:", inline=False, value=link)
            embed.add_field(name="• Shortened link:", inline=False, value=response['url'])

            await ctx.send(embed=embed)

            logger.info(f"Utility | Sent Bitly: {ctx.author} | Long link: {long_url} | Shortened Link: {response['url']}")
        except Exception:
            embed = discord.Embed(
                color=discord.Color.from_rgb(241, 90, 36)
            )
            embed.add_field(name=f"→ Invalid URL",
                            value="• Please put a valid URL!"
                                  "\n• Example: `l!shortenlink https://google.com`")

            await ctx.send(embed=embed)
            ctx.command.reset_cooldown(ctx)

    @bitly.error
    async def shorten_link_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            embed = discord.Embed(
                color=discord.Color.from_rgb(241, 90, 36)
            )
            embed.add_field(name="→ Invalid Argument!",
                            value="• Please put in a valid option! Example: `l!shortenlink <URL>`")
            await ctx.send(embed=embed)
            ctx.command.reset_cooldown(ctx)
        elif isinstance(error, commands.CommandOnCooldown):
            embed = discord.Embed(
                color=discord.Color.from_rgb(241, 90, 36)
            )
            embed.add_field(name="→ Slow down!", value="• You can only shorten a link every 10 seconds!")

            await ctx.send(embed=embed)


def setup(client):
    client.add_cog(Bitly(client))
