import discord
import aiohttp
from discord.ext import commands


class ChuckNorris(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command(aliases=["chuck-norris"])
    async def chuck_norris(self, ctx):
        async with aiohttp.ClientSession() as cs:
            async with cs.get('https://api.icndb.com/jokes/random?limitTo=[nerdy]') as r:
                res = await r.json()
                embed = discord.Embed(
                    color=discord.Color.from_rgb(241, 90, 36)
                )
                embed.add_field(name="→ Chuck Norris Joke", value=f"• Joke: {res['value']['joke']}")

                await ctx.send(embed=embed)


def setup(client):
    client.add_cog(ChuckNorris(client))
