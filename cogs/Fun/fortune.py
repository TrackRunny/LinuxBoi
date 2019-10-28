import discord
import fortune
from discord.ext import commands
from logging_files.fun_logging import logger


class Fortune(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command()
    async def fortune(self, ctx):
        embed = discord.Embed(
            color=discord.Color.from_rgb(241, 90, 36)
        )
        file = "./External_Command_Files/fortunes.txt"
        embed.add_field(name="→ Random Fortune!", value=f"• {fortune.get_random_fortune(file)}")

        await ctx.send(embed=embed)

        logger.info(f"Fun | Sent Fortune: {ctx.author}")


def setup(client):
    client.add_cog(Fortune(client))
