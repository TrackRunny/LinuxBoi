import strgen
import discord
from discord.ext import commands


class Password(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def password(self, ctx, character_length):
        if int(character_length) > int("120"):
            embed = discord.Embed(
                color=discord.Color.from_rgb(241, 90, 36)
            )
            embed.add_field(name="→ Password Error!",
                            value=f"• Please put in a value equal to or less than 120 characters.")
            await ctx.send(embed=embed)
        elif int(character_length) < int("10"):
            embed = discord.Embed(
                color=discord.Color.from_rgb(241, 90, 36)
            )
            embed.add_field(name="→ Password Error!",
                            value=f"• Password length must be at least 10 characters.")
            await ctx.send(embed=embed)
        elif int(character_length) <= int("120"):
            password = strgen.StringGenerator(f"[\w\d\p]{{{int(character_length)}}}").render()
            embed = discord.Embed(
                color=discord.Color.from_rgb(241, 90, 36)
            )
            embed.add_field(name="→ Password sent!",
                            value=f"• The {character_length} "
                                  f"character length password has been generated and sent in your Direct Messages!")
            await ctx.send(embed=embed)

            embed2 = discord.Embed(
                color=discord.Color.from_rgb(241, 90, 36)
            )
            embed2.add_field(name="→ Generated Password:", value=f"• Password: ```{password}```")
            await ctx.author.send(embed=embed2)

    @password.error
    async def password_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            embed = discord.Embed(
                color=discord.Color.from_rgb(241, 90, 36)
            )
            embed.add_field(name="→ Invalid Argument!",
                            value="• Please put in a valid option! Example: `l!password <Character Length>`"
                                  "\n• Real world example: `l!password 25`")
            await ctx.send(embed=embed)


def setup(client):
    client.add_cog(Password(client))
