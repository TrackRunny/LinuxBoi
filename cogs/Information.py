"""
LinuxBoi - Discord bot
Copyright (C) 2019-2020 TrackRunny

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program. If not, see <https://www.gnu.org/licenses/>.
"""

import discord
import psutil
from discord.ext import commands

from logging_files.information_logging import logger


class Information(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases=["commands"])
    async def robot_commands(self, ctx):
        embed = discord.Embed(
            color=self.bot.embed_color,
            title="→ All available bot commands!",
            description="— "
                        "\n→ Shows info about all available bot commands!"
                        "\n→ Capitalization does not matter for the bot prefix." +
                        "\n—"
        )
        embed.set_thumbnail(url="https://i.imgur.com/BUlgakY.png")
        moderation = "`l!purge`, `l!warn`, `l!kick`, `l!ban`, `l!forceban`, `l!unban`," \
                     " `l!nickname`, `l!resetnick`, `l!addrole`, `l!delrole`"
        information = "`l!help`, `l!commands`, `l!ping`, `l!whois`, `l!server`, `l!invite`"
        fun = "`l!coinflip`, `l!avatar`, `l!howgay`, `l!8ball`, `l!dice`, `l!dadjoke`, `l!geekjoke`, " \
              "`l!cowsay`, `l!penguinsay`, `l!fortune`, `l!shrug`, `l!history`, `l!math`, `l!yo-momma-joke`, " \
              "`l!joke`, `l!chuck-norris`"
        utility = "`l!newsletter`, `l!poll`, `l!weather`, " \
                  "`l!mcbe`, `l!email`, `l!translate`, `l!bitly`, `l!hastebin`, `l!randomcolor`," \
                  " `l!bitcoin`, `l!tobtc`, `l!currency`, " \
                  "`l!word random`, `l!word search`, `l!password`, `l!ip`, `l!remind`, `l!temperature fahrenheit`, " \
                  "`l!temperature celsius`, `l!uptime`"
        image = "`l!cat`, `l!dog`, `l!fox`, `l!bird`, `l!tweet`," \
                "`l!trumptweet`, `l!captcha`, `l!clyde`, `l!vs`, `l!magik`"
        music = "`l!play`, `l!pause`, `l!resume`, `l!skip`, `l!queue`, `l!np`, \
                 `l!volume`, `l!seek`, `l!shuffle`, `l!loop`, `l!search`, `l!stop`, `l!disconnect`"
        memes = "`l!meme`, `l!wikihow`"
        # linux_info = "`l!wheretostart`, `l!channels`"

        embed.add_field(name="• Moderation Commands!", inline=False, value=moderation)
        embed.add_field(name="• Information Commands!", inline=False, value=information)
        embed.add_field(name="• Fun Commands!", inline=False, value=fun)
        embed.add_field(name="• Memes!", inline=False, value=memes)
        embed.add_field(name="• Utility Commands!", inline=False, value=utility)
        embed.add_field(name="• Image Commands!", inline=False, value=image)
        embed.add_field(name="• Music Commands!", inline=False, value=music)
        # embed.add_field(name="• Linux information!", inline=False, value=linux_info)

        await ctx.send(embed=embed)

        logger.info(f"Information | Sent Commands: {ctx.author}")

    @commands.command()
    async def help(self, ctx):
        guild_members = str(len(ctx.guild.members))
        guilds = str(len(self.bot.guilds))
        vote_link = "[**Vote link**](http://bit.ly/2mLoBOs)"
        sourcecode_link = "[**Source Code**](https://github.com/TrackRunny/LinuxBoi)"
        cpu = str(psutil.cpu_percent())
        ram = str(psutil.virtual_memory()[3] / 1000000000)
        ram_round = ram[:3]
        disk = str(psutil.disk_usage('/')[1] / 1000000000)
        disk_round = disk[:4]
        boot_time = str(psutil.boot_time() / 100000000)
        boot_time_round = boot_time[:4]
        embed = discord.Embed(
            color=self.bot.embed_color,
            title=f"→ LinuxBoi",
            description=f"— "
                        f"\n ➤ Shows info about the server in which the bot is running on! "
                        f"All values are accurate and updated each time the command is ran."
                        f"\n ➤ Python is one of my favorite programming languages :)"
                        f"\n ➤ Make sure to support The Free Software Movement!"
                        f"\n ➤ To view my commands run, `l!commands`"
                        f"\n ➤ Source code for this bot is available here: {sourcecode_link}"
                        f"\n ➤ If you like my bot, consider voting: {vote_link}" + "\n—"
        )
        embed.set_thumbnail(url="https://bit.ly/2JGhA94")
        embed.add_field(name=f"• Operating System:", inline=True, value=f":computer: — Ubuntu server 18.04 LTS")
        embed.add_field(name=f"• CPU Usage:", inline=True, value=f":heavy_plus_sign: — {cpu} Percent used")
        embed.add_field(name=f"• RAM Usage:", inline=True,
                        value=f":closed_book:  —  {ram_round}  / 3  Gigabytes used")
        embed.add_field(name=f"• DISK Usage:", inline=True, value=f":white_circle: — {disk_round} / 40 Gigabytes")
        embed.add_field(name=f"• BOOT Time: ", inline=True, value=f":boot: —  {boot_time_round} seconds")
        embed.add_field(name=f"• MEMBER Count:", inline=True, value=f":bust_in_silhouette: —  {guild_members} users")
        embed.add_field(name=f"• GUILD Count:", inline=True, value=f":house: — {guilds} connected guilds")
        embed.add_field(name=f"• LIBRARY Version:", inline=True, value=f":gear: — Discord.py version 1.2.5")
        embed.add_field(name=f"• PYTHON Version:", inline=True, value=f":snake:  — Python version 3.7.5")
        embed.set_footer(text=f"\n\nMade by TrackRunny#0001", icon_url=f"\n\nhttps://i.imgur.com/TiUqRH8.gif")

        await ctx.send(embed=embed)

        logger.info(f"Information | Sent Help: {ctx.author}")

    @commands.command()
    async def invite(self, ctx):
        url = "(http://bit.ly/2Zm5XyP)"
        embed = discord.Embed(
            color=self.bot.embed_color,
            title="→ Invite me to your server!",
            description=f"• [Click Here]{url}"
        )
        await ctx.message.add_reaction('\U00002705')

        await ctx.author.send(embed=embed)

        logger.info(f"Information | Sent Invite: {ctx.author}")

    @commands.command()
    async def ping(self, ctx):
        ping = str(round(self.bot.latency * 1000))
        embed = discord.Embed(
            color=self.bot.embed_color,
            title="→ Ping Command",
            description=f"• The latency is {ping} ms"
        )

        await ctx.send(embed=embed)

        logger.info(f"Information | Sent Ping: {ctx.author}")

    @commands.command(aliases=['server'])
    async def serverinfo(self, ctx):
        guild = ctx.guild
        embed = discord.Embed(
            color=self.bot.embed_color,
            title=f"→ Server Info for {guild.name}",
            description="\n— "
                        "\n➤ Shows all information about a guild."
                        "\n➤The information will be listed below!"
                        "\n —"
        )
        regions = {
            "us_west": ":flag_us: — USA West",
            "us_east": ":flag_us: — USA East",
            "us_central": ":flag_us: — USA Central",
            "us_south": ":flag_us: — USA South",
            "sydney": ":flag_au: — Sydney",
            "eu_west": ":flag_eu: — Europe West",
            "eu_east": ":flag_eu: — Europe East",
            "eu_central": ":flag_eu: — Europe Central",
            "singapore": ":flag_sg: — Singapore",
            "russia": ":flag_ru: — Russia",
            "southafrica": ":flag_za:  — South Africa",
            "japan": ":flag_jp: — Japan",
            "brazil": ":flag_br: — Brazil",
            "india": ":flag_in: — India",
            "hongkong": ":flag_hk: — Hong Kong",
        }
        verifications = {
            "none": "<:white__circle:625695417782239234> — No Verification",
            "low": "<:green_circle:625541294525251643> — Low Verification",
            "medium": "<:yellow_circle:625540435820937225> — Medium Verification",
            "high": "<:orange_circle:625542217100165135> — High Verification",
            "extreme": "<:red__circle:625833379258040330> — Extreme Verification"
        }
        embed.set_thumbnail(url=guild.icon_url_as(size=1024, format=None, static_format="png"))
        embed.add_field(name="• Guild name: ", value=str(guild.name))
        embed.add_field(name="• Guild ID: ", value=str(guild.id))
        embed.add_field(name="• Guild owner: ", value=guild.owner)
        embed.add_field(name="• Guild owner ID: ", value=guild.owner_id)
        embed.add_field(name="• Guild made in: ", value=guild.created_at.strftime("%A %d, %B %Y"))
        embed.add_field(name="• Channels count: ", value=len(guild.channels))
        embed.add_field(name="• Guild region: ", value=regions[guild.region.name])
        embed.add_field(name="• Guild verification: ", value=verifications[guild.verification_level.name])
        embed.add_field(name="• Member count: ", value=f"{guild.member_count}")
        embed.add_field(name="• Nitro boosters: ", value=guild.premium_subscription_count or "No Nitro Boosters!")

        await ctx.send(embed=embed)

        logger.info(f"Information | Sent Serverinfo : {ctx.author}")

    @commands.command(aliases=['userinfo'])
    async def whois(self, ctx, member: discord.Member):
        embed = discord.Embed(
            color=self.bot.embed_color,
            title=f"→ Userinfo for {member}",
            description="— "
                        "\n➤ Shows all information about a user. "
                        "\n➤ The information will be listed below!"
                        "\n —"
        )

        status = {
            "online": "<:online:648195346186502145>",
            "idle": "<:idle:648195345800757260>",
            "offline": "<:offline:648195346127912970>",
            "dnd": "<:dnd:648195345985175554>"
        }

        roles = [role for role in member.roles]
        roles = f" ".join([f"`@{role}`, " for role in roles])

        embed.set_thumbnail(url=member.avatar_url_as(size=1024, format=None, static_format="png"))
        embed.add_field(name="• Account name: ", value=str(member))
        embed.add_field(name="• Discord ID: ", value=str(member.id))
        embed.add_field(name="• Nickname: ", value=member.nick or "No nickname!")
        embed.add_field(name="• Account created at: ", value=member.created_at.strftime("%A %d, %B %Y."))
        embed.add_field(name="• Account joined at: ", value=member.joined_at.strftime("%A %d, %B %Y"))
        if member.activity is None:
            embed.add_field(name="• Activity: ", value="No activity!")
        else:
            embed.add_field(name="• Activity: ", value=member.activity.name)
        if member.bot is True:
            embed.add_field(name="• Discord bot? ", value="<:bot_tag:648198074094583831> = <:tick_yes:648198008076238862>")
        else:
            embed.add_field(name="• Discord bot?", value="<:bot_tag:648198074094583831> = <:tick_no:648198035435945985>")
        if member.is_on_mobile() is True:
            embed.add_field(name="• On mobile? ", value=":iphone:")
        else:
            embed.add_field(name="• On mobile? ", value=":no_mobile_phones:")
        embed.add_field(name="• Status: ", value=status[member.status.name])
        embed.add_field(name="• Top role: ", value=f"`@{member.top_role}`")
        embed.add_field(name="• Roles: ", inline=False, value=roles)

        await ctx.send(embed=embed)

        logger.info(f"Information | Sent Whois: {ctx.author}")

    @whois.error
    async def whois_error(self, ctx, error):
        if isinstance(error, commands.BadArgument):
            embed = discord.Embed(
                color=self.bot.embed_color,
                title="→ Invalid Member!",
                description="• Please mention a valid member! Example: `l!whois @user`"
            )
            await ctx.send(embed=embed)
        elif isinstance(error, commands.MissingRequiredArgument):
            embed = discord.Embed(
                color=self.bot.embed_color,
                title="→ Invalid Argument!",
                description="• Please put a valid option! Example: `l!whois @user`"
            )
            await ctx.send(embed=embed)


def setup(bot):
    bot.add_cog(Information(bot))
