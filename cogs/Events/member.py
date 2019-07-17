from discord.ext import commands


class MemberInTerminal(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command()
    async def on_member_join(self, member):
        print(f"{member} has joined a server.")

    async def on_member_remove(self, member):
        print(f"{member} has left a server.")


def setup(client):
    client.add_cog(MemberInTerminal(client))
