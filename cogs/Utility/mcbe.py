import discord
from discord.ext import commands
from mcstatus import MinecraftServer


class MinecraftBedrock(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def mcbe(self, ctx, server, port=19132):
        try:
            srv = MinecraftServer(f"{server}", int(port))
            motd = srv.query()
            embed = discord.Embed(
                color=discord.Color.from_rgb(241, 90, 36)
            )
            embed.set_author(name="→ Minecraft command")
            embed.add_field(name="• IP Address:", inline=True, value=f"`{server}`")
            embed.add_field(name="• Port:", inline=True, value=f"`{port}`")
            embed.add_field(name="• Players:", inline=True,
                            value=f"`{len(motd.players.names)}/{motd.players.max}`")
            embed.add_field(name="• Version:", inline=True, value=f"`{motd.software.version}`")
            embed.add_field(name="• Map:", inline=True, value=f"`{motd.map}`")
            embed.add_field(name="• Software:", inline=True, value=f"`{motd.software.brand}`")
            embed.add_field(name="• MOTD:", inline=False, value=f"`{motd.motd}`")
            embed.add_field(name="• Player names:", inline=False,
                            value='`' + '' + ', '.join(motd.players.names) + ', '[:-0] + '`')
            if not len(motd.software.plugins):
                embed.add_field(name="• Plugins", inline=False, value="`No Plugin Information / No Plugins`")
            else:
                embed.add_field(name="• Plugins", inline=False,
                                value='`' + '' + ', '.join(motd.software.plugins) + ', '[:-0] + '`')

            await ctx.send(embed=embed)

        except Exception:
            embed_error = discord.Embed(
                color=discord.Color.from_rgb(241, 90, 36)
            )
            embed_error.add_field(name="→ Timeout Error:",
                                  value=f"The server is offline or you entered invalid information!")

            await ctx.send(embed=embed_error)

    @mcbe.error
    async def mcbe_error(self, ctx, error):
        member = ctx.author
        if isinstance(error, commands.MissingRequiredArgument):
            embed = discord.Embed(
                color=discord.Color.from_rgb(241, 90, 36)
            )
            embed.set_author(name=member)
            embed.add_field(name="→ Invalid Argument!",
                            value="Please put in a valid Minecraft server and port number!\n— \n→ Example: "
                                  "`l!mcbe play.wither.fun 18323`"
                                  "\n→ Pro Tip: `If the server uses the "
                                  "regular default port \n(19132) "
                                  "you don't have to put in the port number!`")
            await ctx.send(embed=embed)


def setup(client):
    client.add_cog(MinecraftBedrock(client))
