import discord
import random
from discord.ext import commands


class GetInvite(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.is_owner()
    @commands.command()
    async def get_invite(self, ctx, id: int):
        guild = self.client.get_guild(id)

        for channel in guild.text_channels:
            channels = [channel.id]

        picked = random.choice(channels)
        channel = self.client.get_channel(picked)

        embed = discord.Embed(
            color=discord.Color.from_rgb(241, 90, 36),
            title=f"→ Invite from guild",
            description=f"• Invite: {await channel.create_invite(max_uses=1)}"
        )

        await ctx.author.send(embed=embed)


def setup(client):
    client.add_cog(GetInvite(client))
