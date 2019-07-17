import discord
from discord.ext import commands


class Userinfo(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command(aliases=['userinfo'])
    async def whois(self, ctx, member: discord.Member):
        embed = discord.Embed(
            color=discord.Color.from_rgb(241, 90, 36)
        )
        roles = [role for role in member.roles]
        sender = ctx.author
        embed.set_author(name="• Userinfo → " + str(member))
        embed.set_thumbnail(url=member.avatar_url)
        embed.add_field(name="—", value="→ Shows all information about a user. The information will be listed below!"
                                        "\n —")
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
            embed.add_field(name="• Discord bot? ", value="Yes, a bot!")
        else:
            embed.add_field(name="• Discord bot?", value="Not a bot!")
        if member.is_on_mobile() is True:
            embed.add_field(name="• On mobile? ", value="Yes, on mobile!")
        else:
            embed.add_field(name="• On mobile? ", value="Not on a mobile device!")
        embed.add_field(name="• Status: ", value=f"{member.status}")
        embed.add_field(name="• Top role: ", value=f"`@{member.top_role}`")
        embed.add_field(name="• Roles: ", inline=False,  value=f" ".join([f"`@{role}`, " for role in roles]))

        await ctx.send(embed=embed)

    @whois.error
    async def kick_error(self, ctx, error):
        member = ctx.author
        if isinstance(error, commands.MissingRequiredArgument):
            embed = discord.Embed(
                color=discord.Color.from_rgb(241, 90, 36)
            )
            embed.set_author(name="• Invalid Argument!")
            embed.add_field(name=member, value="Please put a valid option! Example: `l!whois @user`")
            await ctx.send(embed=embed)


def setup(client):
    client.add_cog(Userinfo(client))
