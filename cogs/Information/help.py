import discord
from discord.ext import commands


class Help(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command()
    async def help(self, ctx):
        author = ctx.message.author
        embed = discord.Embed(
            color=discord.Color.from_rgb(255, 153, 34)
        )
        embed.set_author(name="• All available bot commands!")
        embed.set_thumbnail(url="https://bit.ly/2YQgsWL")
        embed.add_field(name="—", value="→ Shows info about all available bot commands!"
                                        "\n→ Capitalization does not matter for the bot prefix." +
                                        "\n—")
        embed.add_field(name="• Moderation Commands!", value="`l!purge`, `l!kick`, `l!ban`, `l!forceban` `l!unban`")
        embed.add_field(name="• Information Commands!", value="`l!help`, `l!stats`, `l!ping`, `l!whois`")
        embed.add_field(name="• Fun Commands!", value="`l!coinflip`, `l!avatar`, `l!howgay`, `l!invite`")

        await ctx.send(embed=embed)


def setup(client):
    client.add_cog(Help(client))
