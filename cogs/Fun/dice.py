import discord
from discord.ext import commands
import random
import re


class Dice(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def dice(self, ctx, *, msg='1'):
        try:
            await ctx.message.delete()
        except:
            pass
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
            color=discord.Color.from_rgb(241, 90, 36)
        )
        # ' '.join(dice_rolls)
        embed.add_field(name="→ Rolled Dice Numbers:", value=f" ".join(dice_rolls))
        embed.add_field(name="→ Total number:", inline=False, value=f" {sum(dice_roll_ints)}")
        await ctx.send('', embed=embed)


def setup(client):
    client.add_cog(Dice(client))
