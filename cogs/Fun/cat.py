import discord
from discord.ext import commands
import aiohttp


class Cat(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command()
    async def cat(self, ctx):
        async with aiohttp.ClientSession() as cs:
            async with cs.get('http://aws.random.cat/meow') as r:
                res = await r.json()
                embed = discord.Embed(
                    color=discord.Color.from_rgb(241, 90, 36)
                )
                embed.set_author(name="→ Random Cat! 🐈")
                embed.set_image(url=res['file'])

                await ctx.send(embed=embed)


def setup(client):
    client.add_cog(Cat(client))
