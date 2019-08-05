import discord
from discord.ext import commands
from mtranslate import translate


class Translate(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command()
    async def translate(self, ctx, text, *, translation_language):

        language = translate(text, translation_language, 'auto')

        embed = discord.Embed(
            color=discord.Color.from_rgb(241, 90, 36)
        )
        embed.add_field(name="→ Translation", value='• Your input: `{}`'.format(text)
                        + "\n• Translated Text: `{}`".format(language)
                        + "\n• Detected Input Language: `{}`".format(translation_language))
        embed.add_field(name="→ Supported Languages", inline=False,
                        value="• Languages: `{}`".format(104))

        await ctx.send(embed=embed)

    @translate.error
    async def translate_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            embed = discord.Embed(
                color=discord.Color.from_rgb(241, 90, 36)
            )
            embed.add_field(name="→ Invalid Argument!",
                            value="• Please put a valid option! Example: `l!translate <\"message\"> <language>`"
                                  "\n• Please note your message must have quotes around them."
                                  "\n• Real world example: `l!translate \"Hola\" en`")
            await ctx.send(embed=embed)


def setup(client):
    client.add_cog(Translate(client))
