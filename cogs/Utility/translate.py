import discord
from discord.ext import commands
from mtranslate import translate
import aiogoogletrans

t = aiogoogletrans.Translator()


class Translate(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command(aliases=["gt", "trans"])
    async def translate(self, ctx, lang, *, sentence):
        data = await t.translate(sentence, dest=lang)
        translated = data.src.upper()
        translation = data.text
        language = lang.upper()
        embed = discord.Embed(
            color=discord.Color.from_rgb(241, 90, 36)
        )
        embed.add_field(name="→ Translation", value='• Input Language: `{}`'.format(translated)
                        + "\n• Translated Language: `{}`".format(language)
                        + "\n• Translated Text: `{}`".format(translation))

        await ctx.send(embed=embed)

    @translate.error
    async def translate_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            embed = discord.Embed(
                color=discord.Color.from_rgb(241, 90, 36)
            )
            embed.add_field(name="→ Invalid Argument!",
                            value="• Please put a valid option! Example: `l!translate <language> <message>`"
                                  "\n• Real world example: `l!translate english Hola`")
            await ctx.send(embed=embed)


def setup(client):
    client.add_cog(Translate(client))
