import discord
from discord.ext import commands
from logging_files.information_logging import logger


class Invite(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command()
    async def invite(self, ctx):
        url = "(http://bit.ly/2Zm5XyP)"
        embed = discord.Embed(
            color=discord.Color.from_rgb(241, 90, 36)
        )
        embed.add_field(name="→ Invite me to your server!",
                        value=f"• [Click Here]{url}")
        await ctx.message.add_reaction('\U00002705')

        await ctx.author.send(embed=embed)

        await logger.info(f"Information | Sent Invite: {ctx.author}")


def setup(client):
    client.add_cog(Invite(client))
