import discord
from discord.ext import commands


class Serverinfo(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command(aliases=['server'])
    async def serverinfo(self, ctx):
        embed = discord.Embed(
            color=discord.Color.from_rgb(241, 90, 36)
        )
        guild = ctx.guild
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
            "none": "⚪ — No Verification",
            "low": "🟢 — Low Verification",
            "medium": "🟠 — Medium Verification",
            "high": "🔴 — High Verification",
            "extreme": "⚫ — Extreme Verification",
        }
        sender = ctx.author
        embed.set_author(name="• Server Info → " + str(guild.name))
        embed.set_thumbnail(url=guild.icon_url_as(size=4096, format="png"))
        embed.add_field(name="—", value="→ Shows all information about a guild. The information will be listed below!"
                                        "\n —")
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

    """
    @serverinfo.error
    async def serverinfo_error(self, ctx, error):
        member = ctx.author
        if isinstance(error, commands.MissingRequiredArgument):
            embed = discord.Embed(
                color=discord.Color.from_rgb(241, 90, 36)
            )
            embed.set_author(name="• Invalid Argument!")
            embed.add_field(name=member, value="Please put a valid Discord Guild ID! Example: `l!server 330548417996783616`"
                                               "\nPlease **Note** the command only works if the bot is in the server that you requested!")
            await ctx.send(embed=embed)
    """


def setup(client):
    client.add_cog(Serverinfo(client))
