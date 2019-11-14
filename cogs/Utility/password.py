import strgen
import discord
from discord.ext import commands
from logging_files.utility_logging import logger


class Password(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def password(self, ctx, character_length):
        if int(character_length) > int("120"):
            embed = discord.Embed(
                color=discord.Color.from_rgb(241, 90, 36),
                title="→ Password Error!",
                description="• Please put in a value equal to or less than 120 characters."
            )
            await ctx.send(embed=embed)
        elif int(character_length) < int("9"):
            embed = discord.Embed(
                color=discord.Color.from_rgb(241, 90, 36),
                title="→ Password Error!",
                description="• Password length must be at least 10 characters."
            )
            await ctx.send(embed=embed)
        elif int(character_length) <= int("120"):
            password = strgen.StringGenerator(f"[\w\d\p]{{{int(character_length)}}}").render()
            embed = discord.Embed(
                color=discord.Color.from_rgb(241, 90, 36),
                title="→ Password sent!",
                description=f"• The {character_length} "
                            f"character length password has been generated and sent in your Direct Messages!"
            )

            await ctx.send(embed=embed)

            embed2 = discord.Embed(
                color=discord.Color.from_rgb(241, 90, 36),
                title="→ Generated Password:",
                description=f"• Password: ```{password}```"
            )

            await ctx.author.send(embed=embed2)

            logger.info(f"Utility | Sent Password: {ctx.author}")

    @password.error
    async def password_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            embed = discord.Embed(
                color=discord.Color.from_rgb(241, 90, 36),
                title="→ Invalid Argument!",
                description="• Please put in a valid option! Example: `l!password <character length>`"
                            "\n• Real world example: `l!password 25`"
            )
            await ctx.send(embed=embed)


def setup(client):
    client.add_cog(Password(client))
