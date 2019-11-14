import discord
import random
import re
from discord.ext import commands
from logging_files.fun_logging import logger


class Dice(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def dice(self, ctx, *, msg='1'):
        dice_rolls = []
        dice_roll_ints = []
        try:
            (dice, sides) = re.split('[d\\s]', msg)
        except ValueError:
            dice = msg
            sides = '6'
        try:
            for roll in range(int(dice)):
                result = random.randint(1, int(sides))
                dice_rolls.append(str(result))
                dice_roll_ints.append(result)
        except ValueError:
            pass
        embed = discord.Embed(
            color=discord.Color.from_rgb(241, 90, 36),
            title="→ Dice Command"
        )
        # ' '.join(dice_rolls)
        embed.add_field(name="→ Rolled Dice Numbers:", value=f" ".join(dice_rolls))
        embed.add_field(name="→ Total number:", inline=False, value=f" {sum(dice_roll_ints)}")
        await ctx.send('', embed=embed)

        logger.info(f"Fun | Sent Dice: {ctx.author}")


def setup(client):
    client.add_cog(Dice(client))
