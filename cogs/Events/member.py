import discord
from discord.ext import commands, tasks
import os
import pyowm
import psutil
import random


class Member_In_Terminal(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command()
    async def on_member_join(self, member):
        print(f"{member} has joined a server.")

    async def on_member_remove(self, member):
        print(f"{member} has left a server.")


def setup(client):
    client.add_cog(Member_In_Terminal(client))
