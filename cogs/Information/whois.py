import discord
from discord.ext import commands
from logging_files.information_logging import logger


class UserInfo(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command(aliases=['userinfo'])
    async def whois(self, ctx, member: discord.Member):
        embed = discord.Embed(
            color=discord.Color.from_rgb(241, 90, 36),
            title=f"• Userinfo → {member}",
            description="— "
                        "\n→ Shows all information about a user. The information will be listed below!"
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

        embed.set_thumbnail(url=member.avatar_url_as(size=4096, format=None, static_format="png"))
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
                color=discord.Color.from_rgb(241, 90, 36),
                title="→ Invalid Member!",
                description="• Please mention a valid member! Example: `l!whois @user`"
            )
            await ctx.send(embed=embed)
        elif isinstance(error, commands.MissingRequiredArgument):
            embed = discord.Embed(
                color=discord.Color.from_rgb(241, 90, 36),
                title="→ Invalid Argument!",
                description="• Please put a valid option! Example: `l!whois @user`"
            )
            await ctx.send(embed=embed)


def setup(client):
    client.add_cog(UserInfo(client))
