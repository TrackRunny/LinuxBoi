import discord
from discord.ext import commands
import random
import aiohttp


class Meme(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command()
    async def linux_meme(self, ctx):
        async with aiohttp.ClientSession() as cs:
            async with cs.get('https://www.reddit.com/r/memes/hot.json') as r:
                res = await r.json()

                embed = discord.Embed(
                    color=discord.Color.from_rgb(241, 90, 36)
                )
                embed.set_author(name="→ Linux Meme! 🐧")
                embed.set_image(url=res[''])

                await ctx.send(embed=embed)


def setup(client):
    client.add_cog(Meme(client))


"""
reddit = praw.Reddit(client_id='4kxGyFxq5djiXg',
                     client_secret='tETeShOxuNT30gp84uUk9FwFK8I',
                     user_agent='LinuxBoi')
memes_submissions = reddit.subreddit('Linuxmemes').hot()
post_to_pick = random.randint(1, 100)
for i in range(0, post_to_pick):
    submission = next(x for x in memes_submissions if not x.stickied)
comments = submission.comments.list()

        if submission.url.endswith('.gifv'):
            embed.set_author(name="→ Memes.. - 🔥")
            embed.set_image(url=submission.url[:-1])
            embed.set_footer(text=f"👍 {submission.ups} - 💬 {len(comments)}")

            await ctx.send(embed=embed)
        elif submission.url.endswith(".png"):
            embed.set_author(name="→ Memes.. - 🔥")
            embed.set_image(url=submission.url)
            embed.set_footer(text=f"👍 {submission.ups} - 💬 {len(comments)}")

            await ctx.send(embed=embed)
        else:
            await ctx.send("Rip")
"""

