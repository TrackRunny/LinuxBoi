import discord
from discord.ext import commands


class Commands(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command()
    async def commands(self, ctx):
        embed = discord.Embed(
            color=discord.Color.from_rgb(255, 153, 34)
        )
        embed.set_author(name="→ All available bot commands!")
        embed.set_thumbnail(url="https://bit.ly/2YQgsWL")
        embed.add_field(name="—", value="→ Shows info about all available bot commands!"
                                        "\n→ Capitalization does not matter for the bot prefix." +
                                        "\n—")

        moderation = "`l!purge`, `l!warn`, `l!kick`, `l!ban`, `l!forceban`, `l!unban`," \
                     " `l!nickname`, `l!resetnick`, `l!addrole`, `l!delrole`"
        information = "`l!help`, `l!commands`, `l!ping`, `l!whois`, `l!server`, `l!invite`"
        fun = "`l!say`, `l!coinflip`, `l!avatar`, `l!howgay`, `l!8ball`, `l!dice`, `l!dadjoke`, `l!geekjoke`, " \
              "`l!cowsay`, `l!penguinsay`, `l!fortune`, `l!shrug`, `l!history`"
        utility = "`l!newsletter`, `l!poll`, `l!weather`, " \
                  "`l!mcbe`, `l!email`, `l!translate`, `l!bitly`, `l!hastebin`, `l!randomcolor`," \
                  " `l!bitcoin`, `l!tobtc`, `l!currency`, " \
                  "`l!word random`, `l!word search`, `l!password`, `l!ip`, `l!remind`"
        image = "`l!cat`, `l!dog`, `l!fox`"
        music = "`l!play`, `l!pause`, `l!resume`, `l!skip`, `l!queue`, `l!np`, \
                 `l!volume`, `l!seek`, `l!shuffle`, `l!loop`, `l!search`, `l!stop`, `l!disconnect`"
        # memes = "`l!meme`"
        # linux_info = "`l!wheretostart`, `l!channels`"

        embed.add_field(name="• Moderation Commands!", inline=False, value=moderation)
        embed.add_field(name="• Information Commands!", inline=False, value=information)
        embed.add_field(name="• Fun Commands!", inline=False, value=fun)
        # embed.add_field(name="• Memes!", inline=False, value=memes)
        embed.add_field(name="• Utility Commands!", inline=False, value=utility)
        embed.add_field(name="• Image Commands!", inline=False, value=image)
        embed.add_field(name="• Music Commands [BETA]!", inline=False, value=music)
        # embed.add_field(name="• Linux information!", inline=False, value=linux_info)

        await ctx.send(embed=embed)


def setup(client):
    client.add_cog(Commands(client))
