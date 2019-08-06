import discord
from discord.ext import commands


class Newsletter(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    @commands.has_permissions(mention_everyone=True)
    @commands.bot_has_permissions(mention_everyone=True)
    async def newsletter(self, ctx, channel: discord.TextChannel, choice, *, message):
        embed = discord.Embed(
            color=discord.Color.from_rgb(241, 90, 36)
        )
        sender = ctx.author
        guild = ctx.guild
        if choice == "everyone":
            at_everyone = await ctx.send("@everyone — Check out this new announcement!")
            await at_everyone.delete()
        elif choice == "here":
            at_here = await ctx.send("@here — Check out this new announcement!")
            await at_here.delete()
        elif choice == "none":
            pass
        embed.set_thumbnail(url=guild.icon_url_as(size=4096, format="png"))
        embed.add_field(name="→ Announcement!", value=f"• {message}")
        embed.set_footer(text=f"— Sent from: {sender}", icon_url=ctx.author.avatar_url)
        await ctx.message.delete()
        await channel.send(embed=embed)

    @newsletter.error
    async def newsletter_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            embed = discord.Embed(
                color=discord.Color.from_rgb(241, 90, 36)
            )
            embed.add_field(name="→ Invalid Argument!",
                            value="• Please put a valid option! "
                                  "\n• Example: `l!newsletter #channel <here / everyone / none> <message>`")
            await ctx.send(embed=embed)
        elif isinstance(error, commands.MissingPermissions):
            embed = discord.Embed(
                color=discord.Color.from_rgb(241, 90, 36)
            )
            embed.add_field(name="→ Missing Permissions!", value="• You do not have permissions to run this command!")

            await ctx.send(embed=embed)


def setup(client):
    client.add_cog(Newsletter(client))
