import discord
from discord.ext import commands


class Say(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def say(self, ctx, channel: discord.TextChannel, *, message):
        await channel.send(message)

    @say.error
    async def say_error(self, ctx, error):
        member = ctx.author
        if isinstance(error, commands.MissingRequiredArgument):
            embed = discord.Embed(
                color=discord.Color.from_rgb(241, 90, 36)
            )
            embed.set_author(name=member)
            embed.add_field(name="→ Invalid Argument!",
                            value="Please put a valid option! Example: `l!say <channel> <message>`")

            await ctx.send(embed=embed)


def setup(client):
    client.add_cog(Say(client))
