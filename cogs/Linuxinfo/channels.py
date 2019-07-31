import discord
from discord.ext import commands


class Channels(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command()
    async def channels(self, ctx):
        embed = discord.Embed(
            color=discord.Color.from_rgb(241, 90, 36)
        )
        embed.add_field(name="→ Need to know Linux Channels", value="\n—" +
                                                            "\n→ These linux channels are all linux channels I would recommend watching." +
                                                            "\n→ These channels all provide content "
                                                            "for all of your needs depending on what you want to watch."
                                                            + "\n→ Please note these channels are not in order from best to worst."
                                                            + "\n—")
        embed.set_thumbnail(url="https://www.pointillist.com/wp-content/uploads/2017/10/youtube-logo-1024x1024.jpg")
        joe = "(https://www.youtube.com/user/BadEditPro)"
        switched = "(https://www.youtube.com/channel/UCoryWpk4QVYKFCJul9KBdyw)"
        distrotube = "(https://www.youtube.com/channel/UCVls1GmFKf6WlTraIb_IaJg/videos)"
        average_linux_user = "(https://www.youtube.com/channel/UCZiL6BoryLWxyapUuVYW27g/featured)"
        chris_titus_tech = "(https://www.youtube.com/user/homergfunk)"
        addictive_tips_tv = "(https://www.youtube.com/user/AddictiveTipsTV/videos)"

        embed.add_field(name="• Educational",
                        value=f"1. [Joe Collins]{joe} - Helped a lot of new people switch to linux. Makes really easy to understand videos about different linux topics."
                              f"\n2. [Switched to Linux]{switched} - Posts videos about new linux news as well as information about privacy, scams, virus's, and other drama."
                              f"\n3. [Average Linux User]{average_linux_user} - Makes great tutorial videos that are easy to walk through. Clear and concise when talking."
                              f"\n4. [Chris Titus Tech]{chris_titus_tech} - Says things like they are and takes all the confusing things away from linux and makes things simple. So many helpful videos worth watching."
                              f"\n5. [AddictiveTipsTV]{addictive_tips_tv} - Posts quick 1-3 minute videos for quick tips about Linux, and other software. Great for watching if your in a time crunch. "
                              f"\n. [DistroTube]{distrotube} - Pretty honest and chill person about linux in general. Has a good series called Taking Into Account.")

        await ctx.send(embed=embed)


def setup(client):
    client.add_cog(Channels(client))
