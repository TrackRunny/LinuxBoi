import discord
from discord.ext import commands
from google.cloud import translate


class Translate(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command()
    async def translate(self, ctx, language, *, text):
        try:
            # Instantiates a client
            translate_client = translate.Client()

            # The text to translate

            text = text
            # The target language
            language = language

            # Translates some text into Russian
            translation = translate_client.translate(text, target_language=language)

            # Shows languages
            languages = translate_client.get_languages()

            # print(f"Text: {text}")
            # print(u'Translation: {}'.format(translation['translatedText']))
            # print("Languages: {}".format(len(languages)))

            embed = discord.Embed(
                color=discord.Color.from_rgb(241, 90, 36)
            )
            embed.add_field(name="→ Translation", value='• Your input: `{}`'.format(text)
                            + "\n• Translated Text: `{}`".format(translation['translatedText'])
                            + "\n• Detected Input Language: `{}`".format(translation['detectedSourceLanguage']))
            embed.add_field(name="→ Supported Languages", inline=False,
                            value="• Languages: `{}`".format(len(languages)))

            await ctx.send(embed=embed)
        except Exception:
            embed = discord.Embed(
                color=discord.Color.from_rgb(241, 90, 36)
            )
            embed.add_field(name="→ Invalid Argument!",
                            value="• Please put a valid language to be translated to!")
            await ctx.send(embed=embed)

    @translate.error
    async def unban_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            embed = discord.Embed(
                color=discord.Color.from_rgb(241, 90, 36)
            )
            embed.add_field(name="→ Invalid Argument!",
                            value="• Please follow the foramt! Example: `l!translate <language> <message>`"
                                  "\n• Real World Example: `l!translate en Hola`")
            await ctx.send(embed=embed)


def setup(client):
    client.add_cog(Translate(client))
