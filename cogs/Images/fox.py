import discord
from discord.ext import commands
import aiohttp


class Fox(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command()
    async def fox(self, ctx):
        async with aiohttp.ClientSession() as cs:
            async with cs.get('https://randomfox.ca/floof/') as r:
                res = await r.json()
                embed = discord.Embed(
                    color=discord.Color.from_rgb(241, 90, 36)
                )
                embed.set_author(name="→ Random Fox! 🦊")
                embed.set_image(url=res['image'])

                await ctx.send(embed=embed)


def setup(client):
    client.add_cog(Fox(client))
