import discord
from discord.ext import commands
from logging_files.utility_logging import logger


class Newsletter(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    @commands.has_permissions(mention_everyone=True)
    @commands.bot_has_permissions(mention_everyone=True)
    async def newsletter(self, ctx, channel: discord.TextChannel, choice, *, message):
        sender = ctx.author
        guild = ctx.guild
        embed = discord.Embed(
            color=discord.Color.from_rgb(241, 90, 36),
            title="→ Announcement!",
            description=f"• {message}"
        )
        if choice == "everyone":
            at_everyone = await ctx.send("@everyone — Check out this new announcement!")
            await at_everyone.delete()
        elif choice == "here":
            at_here = await ctx.send("@here — Check out this new announcement!")
            await at_here.delete()
        elif choice == "none":
            pass
        embed.set_thumbnail(url=guild.icon_url_as(size=4096, format="png"))
        embed.set_footer(text=f"— Sent from: {sender}", icon_url=ctx.author.avatar_url)

        await ctx.message.delete()
        await channel.send(embed=embed)

        logger.info(f"Utility | Sent Newsletter: {ctx.author}")

    @newsletter.error
    async def newsletter_error(self, ctx, error):
        if isinstance(error, commands.BadArgument):
            embed = discord.Embed(
                color=discord.Color.from_rgb(241, 90, 36),
                title="→ Invalid Channel!",
                description="\n• Please put in a valid channel! "
                            "Example: `l!newsletter #channel <here / everyone / none> <message>`"
            )
            await ctx.send(embed=embed)
        elif isinstance(error, commands.MissingRequiredArgument):
            embed = discord.Embed(
                color=discord.Color.from_rgb(241, 90, 36),
                title="→ Invalid Argument!",
                description="\n• Please put in a valid option!"
                            "Example: `l!newsletter #channel <here / everyone / none> <message>`"
            )
            await ctx.send(embed=embed)
        elif isinstance(error, commands.MissingPermissions):
            embed = discord.Embed(
                color=discord.Color.from_rgb(241, 90, 36),
                title="→ Missing Permissions!",
                description="• You do not have permissions to run this command!"
            )
            await ctx.send(embed=embed)


def setup(client):
    client.add_cog(Newsletter(client))
