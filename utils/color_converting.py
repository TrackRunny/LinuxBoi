# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# LinuxBoi - Discord bot                                                    #
# Copyright (C) 2019-2020 TrackRunny                                        #
#                                                                           #
# This program is free software: you can redistribute it and/or modify      #
# it under the terms of the GNU General Public License as published by      #
# the Free Software Foundation, either version 3 of the License, or         #
# (at your option) any later version.                                       #
#                                                                           #
# This program is distributed in the hope that it will be useful,           #
# but WITHOUT ANY WARRANTY; without even the implied warranty of            #
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the             #
# GNU General Public License for more details.                              #
#                                                                           #
# You should have received a copy of the GNU General Public License         #
# along with this program. If not, see <https://www.gnu.org/licenses/>.     #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

import colorsys
import random

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
    hsl = (round(360 * h), round(100 * l), round(100 * s))
    return hsl
