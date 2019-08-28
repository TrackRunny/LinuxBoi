import colorsys
import random
import discord
from discord.ext import commands


class RandomColor(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command(aliases=["randomcolor"])
    async def random_color(self, ctx):
        r = lambda: random.randint(0, 255)
        hex_color = f'{f"{r():x}":0>2}{f"{r():x}":0>2}{f"{r():x}":0>2}'
        rgb = tuple(int(hex_color[i:i + 2], 16) for i in (0, 2, 4))

        def rgb_to_cmyk(a=rgb[0], g=rgb[1], b=rgb[2]):
            cmyk_scale = 100
            if a == 0:
                if g == 0:
                    pass
                return b == 0 and (
                    0, 0, 0, cmyk_scale)
            else:
                c = 1 - a / 255.0
                m = 1 - g / 255.0
                y = 1 - b / 255.0
                min_cmy = min(c, m, y)
                c = (c - min_cmy) / (1 - min_cmy)
                m = (m - min_cmy) / (1 - min_cmy)
                y = (y - min_cmy) / (1 - min_cmy)
                k = min_cmy
                converted = (
                    round(c * cmyk_scale), round(m * cmyk_scale), round(y * cmyk_scale), round(k * cmyk_scale))
                return converted

        def rgb_to_hsv(a=rgb[0], b=rgb[1], c=rgb[2]):
            h, s, v = colorsys.rgb_to_hsv(a / 255.0, b / 255.0, c / 255.0)
            hsv = (round(360 * h), round(100 * s), round(100 * v))
            return hsv

        def rgb_to_hsl(a=rgb[0], b=rgb[1], c=rgb[2]):
            h, s, l = colorsys.rgb_to_hls(a / 255.0, b / 255.0, c / 255.0)
            hsl = (round(360 * h),  round(100 * l), round(100 * s))
            return hsl

        # embed = discord.Embed(color=(discord.Color(int(f"0x{hex_color}", 16))))
        embed = discord.Embed(
            color=(discord.Color(int(f"0x{hex_color}", 16)))
        )
        embed.set_author(name='→ Random color')
        embed.set_thumbnail(url="https://www.script-tutorials.com/demos/315/images/colorwheel1.png")
        embed.set_footer(text="— Note: CMYK, HSV, HSL Colors are converted from RGB.")
        embed.add_field(name='• HEX value:', inline=True, value=f"`#{hex_color}`")
        embed.add_field(name='• RGB value:', inline=True, value=f"`{rgb}`")
        embed.add_field(name='• CMYK value:', inline=True, value=f"`{rgb_to_cmyk()}`")
        embed.add_field(name='• HSV value:', inline=True, value=f"`{rgb_to_hsv()}`")
        embed.add_field(name='• HSL value:', inline=True, value=f"`{rgb_to_hsl()}`")
        embed.add_field(name="• COLOR accuracy:", inline=True, value=f"`{random.randint(96, 99)}%`")

        await ctx.send(embed=embed)


def setup(client):
    client.add_cog(RandomColor(client))
