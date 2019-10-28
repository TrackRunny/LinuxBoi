import discord
import asyncio
from discord.ext import commands
from logging_files.utility_logging import logger


class Remind(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command()
    async def remind(self, ctx, time, time_measurement, *, reminder):
        embed = discord.Embed(
            color=discord.Color.from_rgb(241, 90, 36)
        )

        embed2 = discord.Embed(
            color=discord.Color.from_rgb(241, 90, 36)
        )

        if str(time_measurement) == "s":
            if float(time) <= 1:
                embed.add_field(name=f"→ Reminder set for {time} Second!", value=f"• Reminder: `{reminder}`")

                await ctx.send(embed=embed)
            else:
                embed.add_field(name=f"→ Reminder set for {time} Seconds!", value=f"• Reminder: `{reminder}`")

                await ctx.send(embed=embed)

            embed2.add_field(name="→ Time is up!", value=f"• Reminder set: `{reminder}`"
                                                         f"\n• Time set for: `{time} Second(s)`")

            await asyncio.sleep(float(time))
            await ctx.send(embed=embed2)

            ping = await ctx.send(ctx.author.mention)
            await ping.delete()

            logger.info(f"Utility | Sent Remind: {ctx.author} | Time: {time} | Time Measurement: {time_measurement} | Reminder: {reminder}")

        elif str(time_measurement) == "m":
            if float(time) <= 1:
                embed.add_field(name=f"→ Reminder set for {time} Minute!", value=f"• Reminder: `{reminder}`")

                await ctx.send(embed=embed)
            else:
                embed.add_field(name=f"→ Reminder set for {time} Minutes!", value=f"• Reminder: `{reminder}`")

                await ctx.send(embed=embed)

            embed2.add_field(name="→ Time is up!", value=f"• Reminder set: `{reminder}`"
                                                         f"\n• Time set for: `{time} Minute(s)`")
            seconds_to_minutes = float(time) * 60

            await asyncio.sleep(seconds_to_minutes)
            await ctx.send(embed=embed2)

            ping = await ctx.send(ctx.author.mention)
            await ping.delete()

            logger.info(f"Utility | Sent Remind: {ctx.author} | Time: {time} | Time Measurement: {time_measurement} | Reminder: {reminder}")

        elif str(time_measurement) == "h":
            if float(time) <= 1:
                embed.add_field(name=f"→ Reminder set for {time} Hour!", value=f"• Reminder: `{reminder}`")

                await ctx.send(embed=embed)
            else:
                embed.add_field(name=f"→ Reminder set for {time} Hours!", value=f"• Reminder: `{reminder}`")

                await ctx.send(embed=embed)

            embed2.add_field(name="→ Time is up!", value=f"• Reminder set: `{reminder}`"
                                                         f"\n• Time set for: `{time} Hour(s)`")
            seconds_to_hours = (10 * 360) * float(time)

            await asyncio.sleep(seconds_to_hours)
            await ctx.send(embed=embed2)

            ping = await ctx.send(ctx.author.mention)
            await ping.delete()

            logger.info(f"Utility | Sent Remind: {ctx.author} | Time: {time} | Time Measurement: {time_measurement} | Reminder: {reminder}")
        else:
            embed.add_field(name="→ Invalid Argument!",
                            value="• Please put a valid option! Example: `l!remind <time> <time measurement> "
                                  "<reminder>` "
                                  "\n• Units of time: `s = seconds`, `m = minutes`, `h = hours`"
                                  "\n• Real world example: `l!remind 20 m this reminder will go off in 20 minutes.`")

            await ctx.send(embed=embed)

    @remind.error
    async def remind_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            embed = discord.Embed(
                color=discord.Color.from_rgb(241, 90, 36)
            )
            embed.add_field(name="→ Invalid Argument!",
                            value="• Please put a valid option! Example: `l!remind <time> <time measurement> "
                                  "<reminder>` "
                                  "\n• Units of time: `s = seconds`, `m = minutes`, `h = hours`"
                                  "\n• Real world example: `l!remind 20 m this reminder will go off in 20 minutes.`")
            await ctx.send(embed=embed)


def setup(client):
    client.add_cog(Remind(client))
