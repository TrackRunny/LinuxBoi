import discord
from discord.ext import commands
import aiohttp


class Dog(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command()
    async def dog(self, ctx):
        async with aiohttp.ClientSession() as cs:
            async with cs.get('https://dog.ceo/api/breeds/image/random') as r:
                res = await r.json()
                embed = discord.Embed(
                    color=discord.Color.from_rgb(241, 90, 36)
                )
                embed.set_author(name="→ Random Dog! 🐕")
                embed.set_image(url=res['message'])

                await ctx.send(embed=embed)


def setup(client):
    client.add_cog(Dog(client))
