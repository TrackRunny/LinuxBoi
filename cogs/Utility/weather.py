import pyowm
import discord
from discord.ext import commands


class Weather(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command()
    async def weather(self, ctx, city, country):
        try:
            owm = pyowm.OWM('1596858fc52ce6e8121fab7aa5e7d964')
            observation = owm.weather_at_place(f"{city} {country}")
            weather = observation.get_weather()
            temperature = weather.get_temperature('fahrenheit')['temp']
            temperature2 = weather.get_temperature('celsius')['temp']
            wind = weather.get_wind('miles_hour')['speed']
            humidity = weather.get_humidity()
            status = weather.get_status()
            sunrise = weather.get_sunrise_time(timeformat='iso')
            sunset = weather.get_sunset_time(timeformat='iso')
            picture = weather.get_weather_icon_url()
            embed = discord.Embed(
                color=discord.Color.from_rgb(241, 90, 36)
            )
            embed.set_author(name=f"→ Weather Command")
            embed.set_thumbnail(url=picture)
            embed.add_field(name="• Weather:", value=f"{status}")
            embed.add_field(name="• Temperature:", value=f"{temperature}℉ — ({temperature2}℃)")
            embed.add_field(name="• Humidity:", value=f"{humidity}%")
            embed.add_field(name="• Wind:", value=f"{round(wind)} MPH")
            embed.add_field(name="• Sunrise time:", value=f"{sunrise[:-5]} GMT")
            embed.add_field(name="• Sunset time:", value=f"{sunset[:-5]} GMT")

            await ctx.send(embed=embed)
        except Exception:
            member = ctx.author
            embed = discord.Embed(
                color=discord.Color.from_rgb(241, 90, 36)
            )
            embed.set_author(name="• Invalid Argument!")
            embed.add_field(name=member, value="Please put a valid option! Example: `l!weather Las Vegas US`"
                                               "\n Example for a city with one word: `l!weather Woodland, California`"
                                               "\nYou can also use a zip code! Example: `l!weather 15024, US`")
            await ctx.send(embed=embed)

    @weather.error
    async def weather_error(self, ctx, error):
        member = ctx.author
        if isinstance(error, commands.MissingRequiredArgument):
            embed = discord.Embed(
                color=discord.Color.from_rgb(241, 90, 36)
            )
            embed.set_author(name="• Invalid Argument!")
            embed.add_field(name=member, value="Please put a valid option! Example: `l!weather Las Vegas Nevada`"
                                               "\n Example for a city with one word: `l!weather Woodland, California`"
                                               "\nYou can also use a zip code! Example: `l!weather 15024, US`")
            await ctx.send(embed=embed)


def setup(client):
    client.add_cog(Weather(client))

