# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# LinuxBoi - Discord bot                                                    #
# Copyright (C) 2019-2020 TrackRunny                                        #
#                                                                           #
# This program is free software: you can redistribute it and/or modify      #
# it under the terms of the GNU General Public License as published by      #
# the Free Software Foundation, either version 3 of the License, or         #
# (at your option) any later version.                                       #
#                                                                           #
# This program is distributed in the hope that it will be useful,           #
# but WITHOUT ANY WARRANTY; without even the implied warranty of            #
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the             #
# GNU General Public License for more details.                              #
#                                                                           #
# You should have received a copy of the GNU General Public License         #
# along with this program. If not, see <https://www.gnu.org/licenses/>.     #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

import asyncio
import datetime
import os
import random
import smtplib
from email.message import EmailMessage

import aiogoogletrans
import aiohttp
import asyncurban
import discord
import ipinfo
import requests
import strgen
from bitlyshortener import Shortener
from discord.ext import commands
from forex_python.bitcoin import BtcConverter
from forex_python.converter import CurrencyRates
from mcstatus import MinecraftServer

from logging_files.utility_logging import logger
from utils.default import uptime
from utils.color_converting import *


class Utility(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
        self.u = asyncurban.UrbanDictionary()
        self.t = aiogoogletrans.Translator
        self.bot_start_time = datetime.datetime.now()

    @commands.command(aliases=["btc"])
    async def bitcoin(self, ctx, currency="USD"):
        try:
            b = BtcConverter()
            amount = round(b.get_latest_price(currency), 2)
        except:
            embed = discord.Embed(
                color=self.bot.embed_color,
                title="→ Currency error!",
                description="• Not a valid currency type!"
                            "\n• Example: `l!bitcoin CAD`"
            )
            await ctx.send(embed=embed)
        embed = discord.Embed(
            color=self.bot.embed_color,
            title="→ BTC to Currency",
            description=f"• One Bitcoin is {amount} {currency}"
        )
        await ctx.send(embed=embed)

        logger.info(f"Utility | Sent Bitcoin: {ctx.author}")

    @commands.command(aliases=["shortenlink"])
    @commands.cooldown(rate=1, per=10, type=commands.BucketType.user)
    async def bitly(self, ctx, *, link):
        try:
            access_token = os.environ.get("bitly_access_token")
            access_token = [access_token]

            shortener = Shortener(tokens=access_token, max_cache_size=8192)
            shortened_link = shortener.shorten_urls([link])

            embed = discord.Embed(
                color=self.bot.embed_color,
                title="→ URL Shortener"
            )
            embed.add_field(name="• Long link:", inline=False, value=link)
            embed.add_field(name="• Shortened link:", inline=False, value=shortened_link[0])

            await ctx.send(embed=embed)

            logger.info(f"Utility | Sent Bitly: {ctx.author} | Long link: {link} | Shortened Link: {shortened_link[0]}")
        except Exception:
            embed = discord.Embed(
                color=self.bot.embed_color,
                title="→ Invalid URL",
                description="• Please put a valid URL!"
                            "\n• Example: `l!shortenlink https://google.com`"

            )

            await ctx.send(embed=embed)
            ctx.command.reset_cooldown(ctx)

    @bitly.error
    async def shorten_link_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            embed = discord.Embed(
                color=self.bot.embed_color,
                title="Invalid Argument!",
                description="• Please put in a valid option! Example: `l!shortenlink <URL>`"
            )
            await ctx.send(embed=embed)
            ctx.command.reset_cooldown(ctx)
        elif isinstance(error, commands.CommandOnCooldown):
            embed = discord.Embed(
                color=self.bot.embed_color,
                title="→ Slow Down!",
                description="• You can only shorten a link every 10 seconds!"
            )
            await ctx.send(embed=embed)

    @commands.command(aliases=["convert"])
    async def currency(self, ctx, amount, currency1, currency2):
        try:
            c = CurrencyRates()
            amount = float(amount)
        except:
            embed = discord.Embed(
                color=self.bot.embed_color,
                title="→ Money Error!",
                description="• Not a valid amount of money!"
            )
            await ctx.send(embed=embed)
        try:
            amount2 = float((c.convert(currency1, currency2, amount)))
        except:
            embed = discord.Embed(
                color=self.bot.embed_color,
                title="→ Currency Error!",
                description="• Not a valid currency type!"
                            "\n• Example: `l!currency 10 USD CAD`"
            )
            await ctx.send(embed=embed)
        embed = discord.Embed(
            color=self.bot.embed_color,
            title="→ Currency Converting",
            description=f"• {amount} {currency1} is about {round(amount2)} {currency2}!"
        )

        await ctx.send(embed=embed)

        logger.info(f"Utility | Sent Currency: {ctx.author}")

    @currency.error
    async def currency_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            embed = discord.Embed(
                color=self.bot.embed_color,
                title="→ Invalid Argument!",
                description="• Please put in a valid option! Example: `l!currency 10 USD CAD`"
            )
            await ctx.send(embed=embed)

    @commands.command(aliases=["tobtc"])
    async def currency_to_bitcoin(self, ctx, amount, currency="USD"):
        try:
            b = BtcConverter()
            amount = int(amount)
        except:
            embed = discord.Embed(
                color=self.bot.embed_color,
                title="→ Money Error!",
                description="• Not a valid amount of money!"
            )
            await ctx.send(embed=embed)
        try:
            btc = round(b.convert_to_btc(amount, currency), 4)
        except:
            embed = discord.Embed(
                color=self.bot.embed_color,
                title="→ Currency Error!",
                description="• Not a valid currency!"
                            "\n• Example: `l!tobtc 10 CAD`"
                            "\n• Pro Tip: `If you use USD currency, you do not have to specify the currency in the command.`"
            )
            await ctx.send(embed=embed)
        embed = discord.Embed(
            color=self.bot.embed_color,
            title="→ Currency To Bitcoin!",
            description=f"• {amount} {currency} is around {btc} Bitcoin!"
        )

        await ctx.send(embed=embed)

        logger.info(f"Utility | Sent Currency_To_btc: {ctx.author}")

    @currency_to_bitcoin.error
    async def currency_to_bitcoin_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            embed = discord.Embed(
                color=self.bot.embed_color,
                title="→ Invalid Argument!",
                description="• Please put in a valid option! Example: `l!tobtc 10 CAD`"
                            "\n• Pro Tip: `If you use USD currency, you do not have to specify the currency in the command.`")
            await ctx.send(embed=embed)

    @commands.group(invoke_without_command=True)
    async def word(self, ctx):
        embed = discord.Embed(
            color=self.bot.embed_color,
            title="→ Invalid Argument!",
            description="• Please put in a valid option! Example: `l!word <random / search> [Word name]`"
        )
        await ctx.send(embed=embed)

    @word.command()
    async def random(self, ctx):
        word = await self.u.get_random()
        embed = discord.Embed(
            color=self.bot.embed_color,
            title="→ Random Word",
            description=f"Word: `{word}`"
                        f"\n Definition: `{word.definition}`"
        )

        await ctx.send(embed=embed)

        logger.info(f"Utility | Sent Word Random: {ctx.author}")

    @word.command()
    async def search(self, ctx, *, query):
        word = await self.u.get_word(query)
        embed = discord.Embed(
            color=self.bot.embed_color,
            title="→ Searched word",
            description=f"Word: `{word}`"
                        f"\n Definition: `{word.definition}`"
        )

        await ctx.send(embed=embed)

        logger.info(f"Utility | Sent Word Search: {ctx.author} | Searched: {query}")

    @commands.command()
    @commands.cooldown(rate=1, per=1800, type=commands.BucketType.user)
    async def email(self, ctx, emailto, subject, *, content):
        email = os.environ.get("email")  # Your email
        password = os.environ.get("email_password")

        msg = EmailMessage()
        msg['Subject'] = subject
        msg['From'] = email
        msg['To'] = emailto

        msg.set_content("<p>" + content + "</p>" + """\
    <!DOCTYPE html>
    <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <meta http-equiv="X-UA-Compatible" content="ie=edge">
            <title>Document</title>
            <link href="https://fonts.googleapis.com/css?family=Ubuntu&display=swap" rel="stylesheet">
        </head>
        <style>
            * {
                font-family: 'Ubuntu', sans-serif;
                box-sizing: border-box;
            }
        </style>

        <style>
            .linebreak {
                width: 50%;
                size: 10;
            }
        </style>
        <body>
            <footer>
                <div class="info">
                    <hr class="linebreak">
                    <h1 style="text-align: center">FAQ</h1>
                    <h4 style="margin-top: 15px">What is this email?</h4>
                        <ul>
                            <li>This was email sent from a Discord Bot known as LinuxBoi!</li>
                        </ul>
                    <h4>Why was this sent to me?</h4>
                        <ul>
                            <li>This email was sent to you because someone in Discord ran this command and they entered your email address.</li>
                        </ul>
                    <h4>Is this email a scam, spam, ect?</h4>
                        <ul>
                            <li>No of course not! Someone just wanted to send you a email using a Discord bot. Thats all it is to it!</li>
                        </ul>
                    <h4>Can someone spam this and bomb people's emails?</h4>
                        <ul>
                            <li>No, the command has built in protection that allows 1 email to be sent every 30 minutes.</li>
                        </ul>
                    <h4>I don't want to see anymore emails from whoever is running the command anymore please.</h4>
                        <ul>
                            <li>Sure! Just block this email address and you will never see another email again!</li>
                        </ul>
                    <h4>Why does the person not just send a email through their regular address / email client?</h4>
                        <ul>
                            <li>They could not have access to their email right now!
                             However they could be just doing this to save time 
                             and not open their email bot and send a email.</li>
                        </ul>
                    <h4>Okay, this sounds alright then can I have a invite link to the Discord Bot please?</h4>
                        <ul>
                            <li>Of course! Invite the bot here:<a style="text-decoration: none" href="https://bit.ly/2ZfozfL"> Click here!</a></li>
                        </ul>
                </div>
            </footer>
        </body>
    </html>
    """, subtype='html')

        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smpt:
            smpt.login(email, password)
            smpt.send_message(msg)

        embed = discord.Embed(
            color=self.bot.embed_color,
            title="→ Email Sent!"
        )
        link = "https://digitalsynopsis.com/wp-content/uploads/2015/10/gif-icons-menu-transition-animations-send-mail.gif"
        embed.set_thumbnail(url=link)
        embed.add_field(name="• Email Sent to:", inline=False, value=f"```{emailto}```")
        embed.add_field(name="• Subject:", inline=False, value=f"```{subject}```")
        embed.add_field(name="• Content:", inline=False, value=f"```{content}```")

        await ctx.send(embed=embed)

        logger.info(f"Utility | Sent Email: {ctx.author} | To: {emailto} | Subject: {subject} | Content: {content}")

    @email.error
    async def email_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            embed = discord.Embed(
                color=self.bot.embed_color,
                title="→ Invalid Argument!",
                description="• Please put a valid option! " \
                            "\n• Example: `l!email address@emailproider.com \"<subject>\" <content>`" \
                            "\n• Please note: Subjects with more than one word need to have quotes around them."
            )
            await ctx.send(embed=embed)
            ctx.command.reset_cooldown(ctx)
        elif isinstance(error, commands.CommandOnCooldown):
            embed = discord.Embed(
                color=self.bot.embed_color,
                title="→ Slow Down!",
                description="• You can only send a email every 30 minutes!"
            )

            await ctx.send(embed=embed)

    @commands.command()
    async def hastebin(self, ctx, *, code):
        post = requests.post("https://hasteb.in/documents", data=code.encode('utf-8'))
        embed = discord.Embed(
            color=self.bot.embed_color,
            title="→ Uploaded Code!",
            description=f"• Link (Dark Mode): **https://hasteb.in/{post.json()['key']}**"
        )

        await ctx.send(embed=embed)

        logger.info(f"Utility | Sent HasteBin: {ctx.author} | Code: {code}")

    @hastebin.error
    async def hastebin_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            embed = discord.Embed(
                color=self.bot.embed_color,
                title="→ Invalid Argument!",
                description="• Please put in a valid option! Example: `l!hastebin <code>`"
                            "\n• Real World Example: `l!hastebin print(\"Python is amazing!\")`"
            )
            await ctx.send(embed=embed)

    @commands.command(aliases=["ip"])
    async def ip_lookup(self, ctx, ip):
        try:
            token = os.environ.get("ip_info")
            handler = ipinfo.getHandler(token)
            ip_address = ip
            details = handler.getDetails(ip_address)
            info = details.all

            embed = discord.Embed(
                color=self.bot.embed_color,
                title="→ IP Address Lookup"
            )
            embed.set_footer(text="— Note: Locations and Latitude & Longitude may not be 100% accurate.")
            embed.add_field(name="• IP Address:", value=f"`{info['ip']}`")

            if not len(info["latitude"]) and not len(info["longitude"]):
                embed.add_field(name="• Latitude & Longitude", value="`Latitude & Longitude not found!`")
            else:
                embed.add_field(name="• Latitude & Longitude", value=f"`{info['latitude']}, {info['longitude']}`")
            if not len(info["city"]):
                embed.add_field(name="• City:", value="`City not found!`")
            else:
                embed.add_field(name="• City:", value=f"`{info['city']}`")
            if not len(info["region"]):
                embed.add_field(name="• Region / State:", value="`Region / State not found!`")
            else:
                embed.add_field(name="• Region / State:", value=f"`{info['region']}`")
            if not len(info["country_name"]):
                embed.add_field(name="• Country", value="`Country not found!`")
            else:
                embed.add_field(name="• Country:", value=f"`{info['country_name']}`")
            try:
                embed.add_field(name="• Postal code:", value=f"`{info['postal']}`")
            except KeyError:
                embed.add_field(name="• Postal code:", value="`Postal code not found!`")
            if not len(info["org"]):
                embed.add_field(name="• ISP-Name:", value="`ISP-Name not found!`")
            else:
                embed.add_field(name="• ISP-Name:", value=f"`{info['org']}`")

            await ctx.send(embed=embed)

            logger.info(f"Utility | Sent IP: {ctx.author} | IP Address: {ip}")

        except Exception:
            embed_error = discord.Embed(
                color=self.bot.embed_color,
                title="→ Invalid IP Address!",
                description="• The IP address you entered is not valid."
            )

            await ctx.send(embed=embed_error)

    @ip_lookup.error
    async def ip_lookup_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            embed = discord.Embed(
                color=self.bot.embed_color,
                title="→ Invalid Argument!",
                description="• Please put in a IP Address! Example: `l!ip 172.217.2.238`"
            )
            await ctx.send(embed=embed)

    @commands.command()
    async def mcbe(self, ctx, server, port=19132):
        try:
            srv = MinecraftServer(f"{server}", int(port))
            motd = srv.query()
        except Exception:
            embed_error = discord.Embed(
                color=self.bot.embed_color,
                title="→ Timeout Error:",
                description="• The server is offline or you entered invalid information!"
            )
            await ctx.send(embed=embed_error)
        else:
            players_string = ", ".join(str(p) for p in motd.players.names)
            plugins_string = ", ".join(str(l) for l in motd.software.plugins)

            players_string_hastebin = ", \n".join(str(p) for p in motd.players.names)
            plugins_string_hastebin = ", \n".join(str(l) for l in motd.software.plugins)

            players_post = requests.post("https://hasteb.in/documents", data=players_string_hastebin.encode('utf-8'))
            hastebin_players_link = f"https://hasteb.in/{players_post.json()['key']}"

            plugins_post = requests.post("https://hasteb.in/documents", data=plugins_string_hastebin.encode('utf-8'))
            hastebin_plugins_link = f"https://hasteb.in/{plugins_post.json()['key']}"

            embed = discord.Embed(
                color=self.bot.embed_color,
                title="→ Minecraft Bedrock Command"
            )
            embed.add_field(name="• IP Address:", inline=True, value=f"`{server}`")
            embed.add_field(name="• Port:", inline=True, value=f"`{port}`")
            embed.add_field(name="• Players:", inline=True,
                            value=f"`{len(motd.players.names)}/{motd.players.max}`")
            embed.add_field(name="• Map:", inline=True, value=f"`{motd.map}`")
            embed.add_field(name="• Software:", inline=True, value=f"`{motd.software.brand}`")
            embed.add_field(name="• MOTD:", inline=True, value=f"`{motd.motd}`")
            embed.add_field(name="• Version:", inline=False, value=f"`{motd.software.version}`")

            if not len(motd.players.names):
                embed.add_field(name="• Player names:", inline=False,
                                value="`No Player Information / No Players Online!`")
            elif len(players_string) > 1024:
                players_string = players_string[:1018]
                players_string, _, _ = players_string.rpartition(', ')
                players_string = '`' + players_string + '...`'
                embed.add_field(name="• Player names:", inline=False,
                                value=players_string)
            else:
                embed.add_field(name="• Player names:", inline=False,
                                value='`' + '' + ', '.join(motd.players.names) + ', '[:-0] + '`')

            if not len(plugins_string):
                embed.add_field(name="• Plugins:", inline=False, value="`No Plugin Information / No Plugins`")
            elif len(plugins_string) > 1024:
                plugins_string = plugins_string[:1018]
                plugins_string, _, _ = plugins_string.rpartition(', ')
                plugins_string = '`' + plugins_string + '...`'
                embed.add_field(name="• Plugins:", inline=False, value=plugins_string)
            else:
                embed.add_field(name="• Plugins:", inline=False,
                                value='`' + '' + ', '.join(motd.software.plugins) + ', '[:-0] + '`')

            embed.add_field(name="• Full plugins and players list:", value=f"[**Players**]({hastebin_players_link})"
                                                                           f"\n[**Plugins**]({hastebin_plugins_link})")

            await ctx.send(embed=embed)

            logger.info(f"Utility | Sent MCBE: {ctx.author} | Server: {server} | Port: {port}")

    @mcbe.error
    async def mcbe_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            embed = discord.Embed(
                color=self.bot.embed_color,
                title="→ Invalid Argument!",
                description="• Please put in a valid Minecraft server and port number!\n— \n• Example: "
                            "`l!mcbe <server> <port>`"
                            "\n• Pro Tip: `If the server uses the "
                            "regular default port \n(19132) "
                            "you don't have to put in the port number!`"
            )

            await ctx.send(embed=embed)

    @commands.command()
    @commands.has_permissions(mention_everyone=True)
    @commands.bot_has_permissions(mention_everyone=True)
    async def newsletter(self, ctx, channel: discord.TextChannel, choice, *, message):
        sender = ctx.author
        guild = ctx.guild
        embed = discord.Embed(
            color=self.bot.embed_color,
            title="→ Announcement!",
            description=f"• {message}"
        )
        if choice == "everyone":
            at_everyone = await ctx.send("@everyone — Check out this new announcement!")
            await at_everyone.delete()
        elif choice == "here":
            at_here = await ctx.send("@here — Check out this new announcement!")
            await at_here.delete()
        elif choice == "none":
            pass
        embed.set_thumbnail(url=guild.icon_url_as(size=4096, format="png"))
        embed.set_footer(text=f"— Sent from: {sender}", icon_url=ctx.author.avatar_url)

        await ctx.message.delete()
        await channel.send(embed=embed)

        logger.info(f"Utility | Sent Newsletter: {ctx.author}")

    @newsletter.error
    async def newsletter_error(self, ctx, error):
        if isinstance(error, commands.BadArgument):
            embed = discord.Embed(
                color=self.bot.embed_color,
                title="→ Invalid Channel!",
                description="\n• Please put in a valid channel! "
                            "Example: `l!newsletter #channel <here / everyone / none> <message>`"
            )
            await ctx.send(embed=embed)
        elif isinstance(error, commands.MissingRequiredArgument):
            embed = discord.Embed(
                color=self.bot.embed_color,
                title="→ Invalid Argument!",
                description="\n• Please put in a valid option!"
                            "Example: `l!newsletter #channel <here / everyone / none> <message>`"
            )
            await ctx.send(embed=embed)
        elif isinstance(error, commands.MissingPermissions):
            embed = discord.Embed(
                color=self.bot.embed_color,
                title="→ Missing Permissions!",
                description="• You do not have permissions to run this command!"
            )
            await ctx.send(embed=embed)

    @commands.command()
    async def password(self, ctx, character_length):
        if int(character_length) > int("120"):
            embed = discord.Embed(
                color=self.bot.embed_color,
                title="→ Password Error!",
                description="• Please put in a value equal to or less than 120 characters."
            )
            await ctx.send(embed=embed)
        elif int(character_length) < int("9"):
            embed = discord.Embed(
                color=self.bot.embed_color,
                title="→ Password Error!",
                description="• Password length must be at least 10 characters."
            )
            await ctx.send(embed=embed)
        elif int(character_length) <= int("120"):
            password = strgen.StringGenerator(f"[\w\d\p]{{{int(character_length)}}}").render()
            embed = discord.Embed(
                color=self.bot.embed_color,
                title="→ Password Sent!",
                description=f"• The {character_length} "
                            f"character length password has been generated and sent in your Direct Messages!"
            )

            await ctx.send(embed=embed)

            embed2 = discord.Embed(
                color=self.bot.embed_color,
                title="→ Generated Password:",
                description=f"• Password: ```{password}```"
            )

            await ctx.author.send(embed=embed2)

            logger.info(f"Utility | Sent Password: {ctx.author}")

    @password.error
    async def password_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            embed = discord.Embed(
                color=self.bot.embed_color,
                title="→ Invalid Argument!",
                description="• Please put in a valid option! Example: `l!password <character length>`"
                            "\n• Real world example: `l!password 25`"
            )
            await ctx.send(embed=embed)

    @commands.command()
    async def poll(self, ctx, channel: discord.TextChannel, *, question):
        sender = ctx.author
        embed = discord.Embed(
            color=self.bot.embed_color,
            title="→ Quick Poll 📊"
        )
        embed.add_field(name="• Question", inline=False, value=question)
        embed.set_footer(text=f"— Poll from {sender}", icon_url=ctx.author.avatar_url)
        await ctx.message.delete()

        message = await channel.send(embed=embed)
        await message.add_reaction("👍")
        await message.add_reaction("👎")

        logger.info(f"Utility | Sent Poll: {ctx.author}")

    @poll.error
    async def poll_error(self, ctx, error):
        if isinstance(error, commands.BadArgument):
            embed = discord.Embed(
                color=self.bot.embed_color,
                title="→ Invalid Channel!",
                description="• Please put in a channel! Example: `l!poll #channel <question>`"
            )
            await ctx.send(embed=embed)
        elif isinstance(error, commands.MissingRequiredArgument):
            embed = discord.Embed(
                color=self.bot.embed_color,
                title="→ Invalid Argument!",
                description="• Please put in a valid option! Example: `l!poll #channel <question>`"
            )
            await ctx.send(embed=embed)

    @commands.command(aliases=["randomcolor"])
    async def random_color(self, ctx):
        r = lambda: random.randint(0, 255)
        hex_color = f'{f"{r():x}":0>2}{f"{r():x}":0>2}{f"{r():x}":0>2}'
        rgb = tuple(int(hex_color[i:i + 2], 16) for i in (0, 2, 4))

        embed = discord.Embed(
            color=(discord.Color(int(f"0x{hex_color}", 16))),
            title="→ Random Color"
        )
        embed.set_thumbnail(url="https://www.script-tutorials.com/demos/315/images/colorwheel1.png")
        embed.set_footer(text="— Note: CMYK, HSV, HSL Colors are converted from RGB.")
        embed.add_field(name='• HEX value:', inline=True, value=f"`#{hex_color}`")
        embed.add_field(name='• RGB value:', inline=True, value=f"`{rgb}`")
        embed.add_field(name='• CMYK value:', inline=True, value=f"`{rgb_to_cmyk(rgb[0], rgb[1], rgb[2])}`")
        embed.add_field(name='• HSV value:', inline=True, value=f"`{rgb_to_hsv(rgb[0], rgb[1], rgb[2])}`")
        embed.add_field(name='• HSL value:', inline=True, value=f"`{rgb_to_hsl(rgb[0], rgb[1], rgb[2])}`")
        embed.add_field(name="• COLOR accuracy:", inline=True, value=f"`{random.randint(96, 99)}%`")

        await ctx.send(embed=embed)

        logger.info(f"Utility | Sent Random Color: {ctx.author}")

    @commands.command()
    async def remind(self, ctx, time, time_measurement, *, reminder):
        if str(time_measurement) == "s":
            if float(time) <= 1:
                embed = discord.Embed(
                    color=self.bot.embed_color,
                    title=f"→ Reminder Set For {time} Second!",
                    description=f"• Reminder: `{reminder}`"
                )

                await ctx.send(embed=embed)
            else:
                embed = discord.Embed(
                    color=self.bot.embed_color,
                    title=f"→ Reminder Set For {time} Seconds!",
                    description=f"• Reminder: `{reminder}`"
                )

                await ctx.send(embed=embed)

            embed2 = discord.Embed(
                color=self.bot.embed_color,
                title="→ Time Is Up!",
                description=f"• Reminder set: `{reminder}`"
                            f"\n• Time set for: `{time} Second(s)`"
            )

            await asyncio.sleep(float(time))
            await ctx.send(embed=embed2)

            ping = await ctx.send(ctx.author.mention)
            await ping.delete()

            logger.info(
                f"Utility | Sent Remind: {ctx.author} | Time: {time} | Time Measurement: {time_measurement} | Reminder: {reminder}")

        elif str(time_measurement) == "m":
            if float(time) <= 1:
                embed = discord.Embed(
                    color=self.bot.embed_color,
                    title=f"→ Reminder Set For {time} Minute!",
                    description=f"• Reminder: `{reminder}`"
                )

                await ctx.send(embed=embed)
            else:
                embed = discord.Embed(
                    color=self.bot.embed_color,
                    title=f"→ Reminder Set For {time} Minutes!",
                    description=f"• Reminder: `{reminder}`"
                )

                await ctx.send(embed=embed)

            embed3 = discord.Embed(
                color=self.bot.embed_color,
                title="→ Time Is Up!",
                description=f"• Reminder set: `{reminder}`"
                            f"\n• Time set for: `{time} Second(s)`"
            )

            seconds_to_minutes = float(time) * 60

            await asyncio.sleep(seconds_to_minutes)
            await ctx.send(embed=embed3)

            ping = await ctx.send(ctx.author.mention)
            await ping.delete()

            logger.info(
                f"Utility | Sent Remind: {ctx.author} | Time: {time} | Time Measurement: {time_measurement} | Reminder: {reminder}")

        elif str(time_measurement) == "h":
            if float(time) <= 1:
                embed = discord.Embed(
                    color=self.bot.embed_color,
                    title=f"→ Reminder Set For {time} Hour!",
                    description=f"• Reminder: `{reminder}`"
                )

                await ctx.send(embed=embed)
            else:
                embed = discord.Embed(
                    color=self.bot.embed_color,
                    title=f"→ Reminder Set For {time} Hours!",
                    description=f"• Reminder: `{reminder}`"
                )

                await ctx.send(embed=embed)

            embed4 = discord.Embed(
                color=self.bot.embed_color,
                title="→ Time Is Up!",
                description=f"• Reminder set: `{reminder}`"
                            f"\n• Time set for: `{time} Second(s)`"
            )

            seconds_to_hours = (10 * 360) * float(time)

            await asyncio.sleep(seconds_to_hours)
            await ctx.send(embed=embed4)

            ping = await ctx.send(ctx.author.mention)
            await ping.delete()

            logger.info(
                f"Utility | Sent Remind: {ctx.author} | Time: {time} | Time Measurement: {time_measurement} | Reminder: {reminder}")
        else:
            embed = discord.Embed(
                color=self.bot.embed_color,
                title="→ Invalid Argument!",
                description="• Please put a valid option! Example: `l!remind <time> <time measurement> "
                            "<reminder>` "
                            "\n• Units of time: `s = seconds`, `m = minutes`, `h = hours`"
                            "\n• Real world example: `l!remind 20 m this reminder will go off in 20 minutes.`"
            )

            await ctx.send(embed=embed)

    @remind.error
    async def remind_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            embed = discord.Embed(
                color=self.bot.embed_color,
                title="→ Invalid Argument!",
                description="• Please put a valid option! Example: `l!remind <time> <time measurement> "
                            "<reminder>` "
                            "\n• Units of time: `s = seconds`, `m = minutes`, `h = hours`"
                            "\n• Real world example: `l!remind 20 m this reminder will go off in 20 minutes.`"
            )
            await ctx.send(embed=embed)

    @commands.group(aliases=["temp"], invoke_without_command=True)
    async def temperature(self, ctx):
        embed = discord.Embed(
            color=self.bot.embed_color,
            title="→ Invalid Argument!",
            description="• Please put in a valid option! Example: `l!temperature <fahrenheit / celsius> <number>`"
        )

        await ctx.send(embed=embed)

    @temperature.command(aliases=["fahrenheit"])
    async def fahrenheit_to_celsius(self, ctx, fahrenheit):
        celsius = (int(fahrenheit) - 32) * 5 / 9
        embed = discord.Embed(
            color=self.bot.embed_color,
            title="→ Fahrenheit To Celsius",
            description=f"• Celsius Temperature: `{int(celsius)}`"
        )
        await ctx.send(embed=embed)

        logger.info(f"Utility | Sent Temperatures: {ctx.author}")

    @temperature.command(aliases=["celsius"])
    async def celsius_to_fahrenheit(self, ctx, celsius):
        fahrenheit = (int(celsius) * 9 / 5) + 32
        embed = discord.Embed(
            color=self.bot.embed_color,
            title="→ Celsius To Fahrenheit",
            description=f"• Fahrenheit Temperature: `{int(fahrenheit)}`"
        )

        await ctx.send(embed=embed)

        logger.info(f"Utility | Sent Temperatures: {ctx.author}")

    @commands.command(aliases=["gt", "trans"])
    async def translate(self, ctx, lang, *, sentence):
        data = await self.t.translate(sentence, dest=lang)
        translated = data.src.upper()
        translation = data.text
        language = lang.upper()
        embed = discord.Embed(
            color=self.bot.embed_color,
            title="→ Translation",
            description=f"• Input Language: `{translated}`"
                        f"\n• Translated Language: `{language}`"
                        f"\n• Translated Text: `{translation}`"
        )

        await ctx.send(embed=embed)

        logger.info(f"Utility | Sent Translate: {ctx.author} | Language: {lang} | Sentence: {sentence}")

    @translate.error
    async def translate_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            embed = discord.Embed(
                color=self.bot.embed_color,
                title="→ Invalid Argument!",
                description="• Please put a valid option! Example: `l!translate <language> <message>`"
                            "\n• Real world example: `l!translate english Hola`"
            )
            await ctx.send(embed=embed)

    @commands.command()
    async def weather(self, ctx, *, location: str):
        try:
            async with aiohttp.ClientSession() as cs:
                async with cs.get(f"https://api.ksoft.si/kumo/weather/currently",
                                  params={"q": location, "units": "us", "icons": "original"},
                                  headers={"Authorization": f"Bearer {os.environ.get('ksoft_key')}"}) as r:
                    res = await r.json()
                    celsius_temperature = round((int(res['data']['temperature']) - 32) * 5 / 9)

                    embed = discord.Embed(
                        color=self.bot.embed_color,
                        title="→ Weather Command"
                    )
                    embed.set_thumbnail(url=res['data']['icon_url'])
                    embed.add_field(name="• Weather:", value=res['data']['summary'])
                    embed.add_field(name="• Temperature:",
                                    value=f"{res['data']['temperature']}℉ — ({celsius_temperature}℃)")
                    embed.add_field(name="• Humidity:", value=f"{int(res['data']['humidity'] * 100)}%")
                    embed.add_field(name="• Wind:", value=f"{res['data']['windSpeed']} MPH")
                    embed.add_field(name="• Cloud coverage:", value=f"{int(res['data']['cloudCover'] * 100)}%")
                    embed.add_field(name="• Location:", value=f"{res['data']['location']['address']}")
                    embed.add_field(name="• Sunrise time:",
                                    value=f"{res['data']['sunriseTime'] or 'Sunrise information not available'}")
                    embed.add_field(name="• Sunset time:",
                                    value=f"{res['data']['sunsetTime'] or 'Sunset information not available'}")

                    await ctx.send(embed=embed)

                    logger.info(f"Utility | Sent Weather: {ctx.author}")
        except:
            embed = discord.Embed(
                color=self.bot.embed_color,
                title="→ Invalid City / Zip code",
                description="• The city or zip code you put is not valid."
            )

            await ctx.send(embed=embed)

    @weather.error
    async def weather_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            embed = discord.Embed(
                color=self.bot.embed_color,
                title="→ Invalid Argument!",
                description="• Please put a valid option! Example: `l!weather <city>`"
                            "\n• You can also use a zip code! Example: `l!weather <zip-code>`"
            )
            await ctx.send(embed=embed)

    @commands.command()
    async def uptime(self, ctx):
        embed = discord.Embed(
            color=self.bot.embed_color,
            title="→ Current Uptime",
            description=uptime(datetime.datetime.now() - self.bot_start_time)
        )

        await ctx.send(embed=embed)

        logger.info(f"Sent Uptime: {ctx.author}")


def setup(bot):
    bot.add_cog(Utility(bot))
