import discord
from discord.ext import commands


class Invite(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command()
    async def invite(self, ctx):
        url = "(https://discordapp.com/api/oauth2/authorize?client_id=554841921185382400&permissions=8&scope=bot)"
        embed = discord.Embed(
            color=discord.Color.from_rgb(241, 90, 36)
        )
        embed.add_field(name="→ Invite me to your server!",
                        value=f"• [Click Here]{url}")
        await ctx.message.add_reaction('\U00002705')

        await ctx.author.send(embed=embed)


def setup(client):
    client.add_cog(Invite(client))
