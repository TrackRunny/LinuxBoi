import discord
from discord.ext import commands


class Poll(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def poll(self, ctx, channel: discord.TextChannel, *, question):
        sender = ctx.author
        embed = discord.Embed(
            color=discord.Color.from_rgb(241, 90, 36)
        )
        embed.set_author(name="→ Quick poll 📊")
        embed.add_field(name="• Question", inline=False, value=question)
        embed.set_footer(text=f"— Poll from {sender}", icon_url=ctx.author.avatar_url)
        await ctx.message.delete()

        message = await channel.send(embed=embed)
        await message.add_reaction("👍")
        await message.add_reaction("👎")

    @poll.error
    async def poll_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            embed = discord.Embed(
                color=discord.Color.from_rgb(52, 54, 60)
            )
            embed.add_field(name="→ Invalid Argument!",
                            value="• Please put in a valid option! Example: `l!poll #channel <question>`")
            await ctx.send(embed=embed)


def setup(client):
    client.add_cog(Poll(client))
