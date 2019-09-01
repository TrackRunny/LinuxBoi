import discord
from discord.ext import commands


class Temperatures(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.group(aliases=["temp"], invoke_without_command=True)
    async def temperature(self, ctx):
        embed = discord.Embed(
            color=discord.Color.from_rgb(241, 90, 36)
        )
        embed.add_field(name="→ Invalid Argument!",
                        value="• Please put in a valid option! Example: `l!temperature <fahrenheit / celsius> <number>`")
        await ctx.send(embed=embed)

    @temperature.command(aliases=["fahrenheit"])
    async def fahrenheit_to_celsius(self, ctx, fahrenheit):
        celsius = (int(fahrenheit) - 32) * 5 / 9
        embed = discord.Embed(
            color=discord.Color.from_rgb(241, 90, 36)
        )
        embed.add_field(name="→ Fahrenheit to Celsius", value=f"• Celsius Temperature: `{int(celsius)}`")
        await ctx.send(embed=embed)

    @temperature.command(aliases=["celsius"])
    async def celsius_to_fahrenheit(self, ctx, celsius):
        fahrenheit = (int(celsius) * 9 / 5) + 32
        embed = discord.Embed(
            color=discord.Color.from_rgb(241, 90, 36)
        )
        embed.add_field(name="→ Celsius to Fahrenheit", value=f"• Fahrenheit Temperature: `{int(fahrenheit)}`")
        await ctx.send(embed=embed)


def setup(client):
    client.add_cog(Temperatures(client))


