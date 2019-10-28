import discord
import pyowm
import os
from discord.ext import commands
from logging_files.utility_logging import logger


class Weather(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command()
    async def weather(self, ctx, *, city):
        try:
            key = os.environ.get("weather_key")
            owm = pyowm.OWM(key)
            observation = owm.weather_at_place(city)
            weather = observation.get_weather()
            temperature = weather.get_temperature('fahrenheit')['temp']
            temperature2 = weather.get_temperature('celsius')['temp']
            wind = weather.get_wind('miles_hour')['speed']
            cloud = weather.get_clouds()
            max_temp = weather.get_temperature('fahrenheit')['temp_max']
            max_temp2 = weather.get_temperature('celsius')['temp_max']
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
            embed.add_field(name="• Max Temperature:", value=f"{max_temp}℉ — ({max_temp2}℃)")
            embed.add_field(name="• Humidity:", value=f"{humidity}%")
            embed.add_field(name="• Wind:", value=f"{round(wind)} MPH")
            embed.add_field(name="• Cloud coverage:", value=f"{cloud}%")
            embed.add_field(name="• Sunrise time:", value=f"{sunrise[:-5]} GMT")
            embed.add_field(name="• Sunset time:", value=f"{sunset[:-5]} GMT")

            await ctx.send(embed=embed)

            logger.info(f"Utility | Sent Weather: {ctx.author}")
        except Exception:
            member = ctx.author
            embed = discord.Embed(
                color=discord.Color.from_rgb(241, 90, 36)
            )
            embed.set_author(name=member)
            embed.add_field(name="→ Invalid City / Zip code", value="• The city or zip code you entered is "
                                                                    "not spelled right, or the format is incorrect."
                                                                    "\n• However the city you entered possibly "
                                                                    "not being tracked with the weather API!")
            await ctx.send(embed=embed)

    @weather.error
    async def weather_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            embed = discord.Embed(
                color=discord.Color.from_rgb(241, 90, 36)
            )
            embed.add_field(name="→ Invalid Argument!",
                            value="• Please put a valid option! Example: `l!weather Las Vegas, Nevada`"
                                  "\n• You can also use a zip code! Example: `l!weather 15024, US`")
            await ctx.send(embed=embed)


def setup(client):
    client.add_cog(Weather(client))
