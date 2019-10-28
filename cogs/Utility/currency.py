import discord
from forex_python.converter import CurrencyRates
from discord.ext import commands
from logging_files.utility_logging import logger


class Currency(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command(aliases=["convert"])
    async def currency(self, ctx, amount, currency1, currency2):
        try:
            c = CurrencyRates()
            amount = float(amount)
        except:
            embed = discord.Embed(
                color=discord.Color.from_rgb(241, 90, 36)
            )
            embed.add_field(name="→ Money error!",
                            value="• Not a valid amount of money!")
            return await ctx.send(embed=embed)
        try:
            amount2 = float((c.convert(currency1, currency2, amount)))
        except:
            embed = discord.Embed(
                color=discord.Color.from_rgb(241, 90, 36)
            )
            embed.add_field(name="→ Currency error!",
                            value="• Not a valid currency type!"
                                  "\n• Example: `l!currency 10 USD CAD`")
            return await ctx.send(embed=embed)
        embed = discord.Embed(
            color=discord.Color.from_rgb(241, 90, 36)
        )
        embed.add_field(name="→ Currency converting!",
                        value=f"• {amount} {currency1} is about {round(amount2)} {currency2}!")
        await ctx.send(embed=embed)

        await logger.info(f"Utility | Sent Currency: {ctx.author}")

    @currency.error
    async def currency_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            embed = discord.Embed(
                color=discord.Color.from_rgb(241, 90, 36)
            )
            embed.add_field(name="→ Invalid Argument!",
                            value="• Please put in a valid option! Example: `l!currency 10 USD CAD`")
            await ctx.send(embed=embed)


def setup(client):
    client.add_cog(Currency(client))
