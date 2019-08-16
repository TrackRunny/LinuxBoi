import asyncio

import aiohttp
import discord
from discord.ext import commands
from forex_python.bitcoin import BtcConverter

b = BtcConverter()


class ToBitcoin(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command(aliases=["tobtc"])
    async def currency_to_bitcoin(self, ctx, amount, currency="USD"):
        try:
            amount = int(amount)
        except:
            embed = discord.Embed(
                color=discord.Color.from_rgb(241, 90, 36)
            )
            embed.add_field(name="→ Money error!",
                            value="• Not a valid amount of money!")
            return await ctx.send(embed=embed)
        try:
            btc = round(b.convert_to_btc(amount, currency), 4)
        except:
            embed = discord.Embed(
                color=discord.Color.from_rgb(241, 90, 36)
            )
            embed.add_field(name="→ Currency error!",
                            value="• Not a valid currency!"
                                  "\n• Example: `l!tobtc 10 CAD`"
                                  "\n• Pro tip: `If you use USD currency you only have to put the amount!`")
            return await ctx.send(embed=embed)
        embed = discord.Embed(
            color=discord.Color.from_rgb(241, 90, 36)
        )
        embed.add_field(name="→ Currency to Bitcoin!",
                        value=f"• {amount} {currency} is around {btc} Bitcoin!")
        await ctx.send(embed=embed)

    @currency_to_bitcoin.error
    async def currency_to_bitcoin_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            embed = discord.Embed(
                color=discord.Color.from_rgb(241, 90, 36)
            )
            embed.add_field(name="→ Invalid Argument!",
                            value="• Please put in a valid option! Example: `l!tobtc 10 CAD`")
            await ctx.send(embed=embed)


def setup(client):
    client.add_cog(ToBitcoin(client))
