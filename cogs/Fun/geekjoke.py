# -*- coding: utf-8 -*-

import discord
import json
from discord.ext import commands
from random import randint
from logging_files.fun_logging import logger


class GeekJoke(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command()
    async def geekjoke(self, ctx):
        def random_digits(joke_count):
            # Return a joke index between first and last joke in data
            return randint(1, joke_count)

        def get_joke():
            # Return random joke
            with open('./External_Command_Files/geekjokes.json', encoding="utf8") as data_file:
                data = json.load(data_file)
            joke = data[random_digits(len(data))]
            return joke

        embed = discord.Embed(
            color=discord.Color.from_rgb(241, 90, 36)
        )
        embed.add_field(name="→ Random Geek joke!", value=f"• {get_joke()}")

        await ctx.send(embed=embed)

        logger.info(f"Fun | Sent Geekjoke: {ctx.author}")


def setup(client):
    client.add_cog(GeekJoke(client))
