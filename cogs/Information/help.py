import discord
import psutil
from discord.ext import commands
from logging_files.information_logging import logger


class Help(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command()
    async def help(self, ctx):
        guild_members = str(len(ctx.guild.members))
        guilds = str(len(self.client.guilds))
        vote_link = "[**Vote link**](http://bit.ly/2mLoBOs)"
        cpu = str(psutil.cpu_percent())
        ram = str(psutil.virtual_memory()[3] / 1000000000)
        ram_round = ram[:3]
        disk = str(psutil.disk_usage('/')[1] / 1000000000)
        disk_round = disk[:4]
        boot_time = str(psutil.boot_time() / 100000000)
        boot_time_round = boot_time[:4]
        embed = discord.Embed(
            color=discord.Color.from_rgb(241, 90, 36),
            title="• LinuxBoi",
            description="— "
                        "\n→ Shows info about the server in which the bot is running on! "
                        "All values are accurate and updated each time the command is ran."
                        "\n → Python is one of my favorite programming languages :)" +
                        "\n → Make sure to support The Free Software Movement!" +
                        "\n → To view my commands run, `l!commands`"
                        f"\n → If you like my bot, consider voting: {vote_link}" + "\n—"
        )
        embed.set_thumbnail(url="https://bit.ly/2JGhA94")
        embed.add_field(name="• Operating System:", inline=True, value=":computer: — Ubuntu 18.04 LTS")
        embed.add_field(name="• CPU Usage:", inline=True, value=":heavy_plus_sign: — " + cpu + " Percent used")
        embed.add_field(name="• RAM Usage:", inline=True,
                        value=":closed_book:  — " + ram_round + " / 8 " + " Gigabytes used")
        embed.add_field(name="• DISK Usage:", inline=True, value=":white_circle: — " + disk_round + " / 60 Gigabytes")
        embed.add_field(name="• BOOT Time: ", inline=True, value=":boot: — " + boot_time_round + " seconds")
        embed.add_field(name="• MEMBER Count:", inline=True, value=":bust_in_silhouette: — " + guild_members + " users")
        embed.add_field(name="• GUILD Count:", inline=True, value=":house: — " + guilds + " connected guilds")
        embed.add_field(name="• LIBRARY Version:", inline=True, value=":gear: — Discord.py version 1.2.5")
        embed.add_field(name="• PYTHON Version:", inline=True, value=":snake:  — Python version 3.7.3")
        embed.set_footer(text="\n\nMade by TrackRunny#0001", icon_url="\n\nhttps://i.imgur.com/ZwWigTq.png")

        await ctx.send(embed=embed)

        logger.info(f"Information | Sent Help: {ctx.author}")


def setup(client):
    client.add_cog(Help(client))
