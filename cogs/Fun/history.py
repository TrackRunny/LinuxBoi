import discord
import aiohttp
from discord.ext import commands


class History(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command()
    async def history(self, ctx):
        async with aiohttp.ClientSession() as cs:
            async with cs.get('http://numbersapi.com/random/date?json') as r:
                res = await r.json()
                embed = discord.Embed(
                    color=discord.Color.from_rgb(241, 90, 36)
                )
                embed.add_field(name="→ Random History Date", value=f"• Fact: {res['text']}"
                                                                    f"\n• Year: {res['year']}")

                await ctx.send(embed=embed)


def setup(client):
    client.add_cog(History(client))
