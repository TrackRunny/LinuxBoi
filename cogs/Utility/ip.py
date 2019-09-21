import ipinfo
import discord
import os
from discord.ext import commands


class IpAddress(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command(aliases=["ip"])
    async def ip_lookup(self, ctx, ip):
        token = os.environ.get("ip_info")
        handler = ipinfo.getHandler(token)
        ip_address = ip
        details = handler.getDetails(ip_address)
        info = details.all

        embed = discord.Embed(
            color=discord.Color.from_rgb(241, 90, 36)
        )
        embed.set_author(name="→ IP Address lookup")
        embed.add_field(name="• IP Address:", value=info["ip"])
        embed.add_field(name="• Latitude & Longitude", value=f"{info['latitude']}, {info['longitude']}")
        embed.add_field(name="• City:", value=info["city"])
        embed.add_field(name="• Region / State:", value=info["region"])
        embed.add_field(name="• Country:", value=info["country_name"])
        embed.add_field(name="• Postal code:", value=info["postal"])
        embed.add_field(name="• ISP-Name:", value=info["org"])

        await ctx.send(embed=embed)


def setup(client):
    client.add_cog(IpAddress(client))
