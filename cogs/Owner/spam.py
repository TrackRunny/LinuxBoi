import discord
from discord.ext import commands


class Spam(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command()
    async def spam(self, ctx, member: discord.Member, channel: discord.TextChannel):
        embed = discord.Embed(
            color=discord.Color.from_rgb(241, 90, 36)
        )
        embed.add_field(name="→ Spam command", value="• Spam is being sent to the user")
        await ctx.author.send(embed=embed)

        i = 1
        while i <= 1000:
            await channel.send("@everyone")
            await member.send("@everyone")
            i += 1


def setup(client):
    client.add_cog(Spam(client))
