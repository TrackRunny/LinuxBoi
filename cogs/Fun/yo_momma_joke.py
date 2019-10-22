import discord
import aiohttp
from discord.ext import commands


class YoMamaJoke(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command(aliases=["momma-joke", "yo-momma-joke"])
    async def yo_momma_joke(self, ctx):
        async with aiohttp.ClientSession() as cs:
            async with cs.get('https://api.yomomma.info/') as r:
                res = await r.json(content_type='text/html')
                embed = discord.Embed(
                    color=discord.Color.from_rgb(241, 90, 36)
                )
                embed.add_field(name="→ Yo Momma Joke", value=f"• Joke: {res['joke']}")

                afwait ctx.send(embed=embed)


def setup(client):
    client.add_cog(YoMamaJoke(client))
