import discord
from discord.ext import commands
from forex_python.bitcoin import BtcConverter


class Bitcoin(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command(aliases=["btc"])
    async def bitcoin(self, ctx, currency="USD"):
        try:
            b = BtcConverter()
            amount = round(b.get_latest_price(currency), 2)
        except:
            embed = discord.Embed(
                color=discord.Color.from_rgb(241, 90, 36)
            )
            embed.add_field(name="→ Currency error!",
                            value="• Not a valid currency type!"
                                  "\n• Example: `l!bitcoin CAD`")
            return await ctx.send(embed=embed)
        embed = discord.Embed(
            color=discord.Color.from_rgb(241, 90, 36)
        )
        embed.add_field(name="→ BTC to Currency",
                        value=f"• One Bitcoin is {amount} {currency}")
        await ctx.send(embed=embed)


def setup(client):
    client.add_cog(Bitcoin(client))
