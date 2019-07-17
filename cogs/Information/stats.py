import discord
import psutil
from discord.ext import commands


class Stats(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command()
    async def stats(self, ctx):
        author = ctx.message.author
        guild_members = str(len(ctx.guild.members))
        guilds = str(len(self.client.guilds))
        cpu = str(psutil.cpu_percent())
        ram = str(psutil.virtual_memory()[3] / 1000000000)
        ram_round = ram[:3]
        disk = str(psutil.disk_usage('/')[1] / 1000000000)
        disk_round = disk[:4]
        boot_time = str(psutil.boot_time() / 100000000)
        boot_time_round = boot_time[:4]
        embed = discord.Embed(
            color=discord.Color.from_rgb(241, 90, 36)
        )

        embed.set_author(name="• Server Stats")
        embed.set_thumbnail(url="https://bit.ly/2JGhA94")
        embed.add_field(name="\n—", value="→ Shows info about the server in which the bot is running on! "
                                          "All values are accurate and updated each time the command is ran."
                                          "\n → Python is one of my favorite programming languages :)" + "\n—")
        embed.add_field(name="• Operating System:", inline=True, value=":computer: — Ubuntu 18.04 LTS")
        embed.add_field(name="• CPU Usage:", inline=True, value=":heavy_plus_sign: — " + cpu + " Percent used")
        embed.add_field(name="• RAM Usage:", inline=True,
                        value=":closed_book:  — " + ram_round + " / 8 " + " Gigabytes used")
        embed.add_field(name="• DISK Usage:", inline=True, value=":white_circle: — " + disk_round + " / 60 Gigabytes")
        embed.add_field(name="• BOOT Time: ", inline=True, value=":boot: — " + boot_time_round + " seconds")
        embed.add_field(name="• MEMBER Count:", inline=True, value=":bust_in_silhouette: — " + guild_members + " users")
        embed.add_field(name="• GUILD Count:", inline=True, value=":house: — " + guilds + " connected guilds")
        embed.add_field(name="• LIBRARY Version:", inline=True, value=":gear: — Discord.py version 1.2.3")
        embed.add_field(name="• PYTHON Version:", inline=True, value=":snake:  — Python version 3.7.3" + "\n—")
        embed.set_footer(text="• Made by TrackRunny#3900", icon_url="https://bit.ly/2SepdYi")

        await ctx.send(embed=embed)


def setup(client):
    client.add_cog(Stats(client))
