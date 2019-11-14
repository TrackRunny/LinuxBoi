import ipinfo
import discord
import os
from discord.ext import commands
from logging_files.utility_logging import logger


class IpAddress(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command(aliases=["ip"])
    async def ip_lookup(self, ctx, ip):
        try:
            token = os.environ.get("ip_info")
            handler = ipinfo.getHandler(token)
            ip_address = ip
            details = handler.getDetails(ip_address)
            info = details.all

            embed = discord.Embed(
                color=discord.Color.from_rgb(241, 90, 36),
                title="→ IP Address lookup"
            )
            embed.set_footer(text="— Note: Locations and Latitude & Longitude may not be 100% accurate.")
            embed.add_field(name="• IP Address:", value=info["ip"])
            if not len(info["latitude"]) and not len(info["longitude"]):
                embed.add_field(name="• Latitude & Longitude", value="Latitude & Longitude not found!")
            else:
                embed.add_field(name="• Latitude & Longitude", value=f"{info['latitude']}, {info['longitude']}")
            if not len(info["city"]):
                embed.add_field(name="• City:", value="City not found!")
            else:
                embed.add_field(name="• City:", value=info["city"])
            if not len(info["region"]):
                embed.add_field(name="• Region / State:", value="Region / State not found!")
            else:
                embed.add_field(name="• Region / State:", value=info["region"])
            if not len(info["country_name"]):
                embed.add_field(name="• Country", value="Country not found!")
            else:
                embed.add_field(name="• Country:", value=info["country_name"])
            try:
                embed.add_field(name="• Postal code:", value=info["postal"])
            except KeyError:
                embed.add_field(name="• Postal code:", value="Postal code not found!")
            if not len(info["org"]):
                embed.add_field(name="• ISP-Name:", value="ISP-Name not found!")
            else:
                embed.add_field(name="• ISP-Name:", value=info["org"])

            await ctx.send(embed=embed)

            logger.info(f"Utility | Sent IP: {ctx.author} | IP Address: {ip}")

        except Exception:
            embed_error = discord.Embed(
                color=discord.Color.from_rgb(241, 90, 36),
                title="→ Invalid IP Address!",
                description="• The IP address you entered is not valid."
            )

            await ctx.send(embed=embed_error)

    @ip_lookup.error
    async def ip_lookup_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            embed = discord.Embed(
                color=discord.Color.from_rgb(241, 90, 36),
                title="→ Invalid Argument!",
                description="• Please put in a IP Address! Example: `l!ip 172.217.2.238`"
            )
            await ctx.send(embed=embed)


def setup(client):
    client.add_cog(IpAddress(client))
