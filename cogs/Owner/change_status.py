import discord
from discord.ext import commands


class Status(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    @commands.is_owner()
    async def status(self, ctx, activity, *, status):
        # Type 0 = Playing a game, Type 1 = Live on Twitch, Type 2 = Listening, Type 3 = Watching
        await self.client.change_presence(activity=discord.Activity(type=activity, name=status))
        embed = discord.Embed(
            color=discord.Color.from_rgb(241, 90, 36)
        )
        embed.add_field(name="→ Bot status changed!", value=f"• My status has been updated to: `{status}`")

        await ctx.send(embed=embed)

    @status.error
    async def change_status_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            embed = discord.Embed(
                color=discord.Color.from_rgb(241, 90, 36)
            )
            embed.add_field(name="→ Invalid Argument!",
                            value="Please put a valid option! Example: `l!status <type> <status>`")
            await ctx.send(embed=embed)


def setup(client):
    client.add_cog(Status(client))
