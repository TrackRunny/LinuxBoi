import os
import discord
from discord.ext import commands

client = commands.Bot("> ", owner_id=546812331213062144, case_insensitive=False, self_bot=True)
# client = commands.Bot("> ", owner_id=546812331213062144, case_insensitive=False)
client.remove_command('help')
line_divide = "\n———————————————————————————————"


def read_token():
    with open("token.txt", "r") as f:
        lines = f.readlines()
        return lines[0].strip()


@client.event
async def on_ready():
    print(f"---------------DiscordBot---------------"
          f"\nBot is online and connected to " + str(client.user) +
          f"\nCreated by TrackRunny#3900 on Discord"
          f"\n----------------------------------------------")


@client.command(pass_context=True)
@commands.is_owner()
async def load_information(ctx, extension):
    client.load_extension(f"cogs.Information.{extension}")
    embed = discord.Embed(
        color=discord.Color.from_rgb(241, 90, 36)
    )
    embed.set_author(name="• Information")
    embed.add_field(name="Cog command", value=ctx.author.mention + " → One of the information cogs has been loaded!")
    await ctx.send(embed=embed)


@load_information.error
async def load_information_error(ctx, error):
    member = ctx.author
    if isinstance(error, commands.MissingRequiredArgument):
        embed = discord.Embed(
            color=discord.Color.from_rgb(241, 90, 36)
        )
        embed.set_author(name="• Invalid Argument!")
        embed.add_field(name=member, value="Please put a valid option! Example: `l!load_information stats`")
        await ctx.send(embed=embed)


@client.command(pass_contxt=True)
@commands.is_owner()
async def unload_information(ctx, extension):
    client.unload_extension(f"cogs.Information.{extension}")
    embed = discord.Embed(
        color=discord.Color.from_rgb(241, 90, 36)
    )
    embed.set_author(name="• Information")
    embed.add_field(name="Cog command", value=ctx.author.mention + " → One of the information cogs has been unloaded!")
    await ctx.send(embed=embed)


@unload_information.error
async def unload_information_error(ctx, error):
    member = ctx.author
    if isinstance(error, commands.MissingRequiredArgument):
        embed = discord.Embed(
            color=discord.Color.from_rgb(241, 90, 36)
        )
        embed.set_author(name="• Invalid Argument!")
        embed.add_field(name=member, value="Please put a valid option! Example: `l!unload_information stats`")
        await ctx.send(embed=embed)


@client.command(pass_context=True)
@commands.is_owner()
async def reload_information(ctx, extension):
    client.reload_extension(f"cogs.Information.{extension}")
    embed = discord.Embed(
        color=discord.Color.from_rgb(241, 90, 36)
    )
    embed.set_author(name="• Information")
    embed.add_field(name="Cog command", value=ctx.author.mention + " → One of the information cogs has been reloaded!")
    await ctx.send(embed=embed)


@reload_information.error
async def reload_information_error(ctx, error):
    member = ctx.author
    if isinstance(error, commands.MissingRequiredArgument):
        embed = discord.Embed(
            color=discord.Color.from_rgb(241, 90, 36)
        )
        embed.set_author(name="• Invalid Argument!")
        embed.add_field(name=member, value="Please put a valid option! Example: `l!reload_information stats`")
        await ctx.send(embed=embed)


for filename in os.listdir('./cogs/Information'):
    if filename.endswith('.py'):
        client.load_extension(f"cogs.Information.{filename[:-3]}")

# ————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————
# ————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————
# ————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————


@client.command(pass_context=True)
@commands.is_owner()
async def load_fun(ctx, extension):
    client.load_extension(f"cogs.Fun.{extension}")
    embed = discord.Embed(
        color=discord.Color.from_rgb(241, 90, 36)
    )
    embed.set_author(name="• Fun")
    embed.add_field(name="Cog command", value=ctx.author.mention + " → One of the Fun cogs has been loaded!")
    await ctx.send(embed=embed)


@load_fun.error
async def load_fun_error(ctx, error):
    member = ctx.author
    if isinstance(error, commands.MissingRequiredArgument):
        embed = discord.Embed(
            color=discord.Color.from_rgb(241, 90, 36)
        )
        embed.set_author(name="• Invalid Argument!")
        embed.add_field(name=member, value="Please put a valid option! Example: `l!load_fun whois`")
        await ctx.send(embed=embed)


@client.command(pass_context=True)
@commands.is_owner()
async def unload_fun(ctx, extension):
    client.unload_extension(f"cogs.Fun.{extension}")
    embed = discord.Embed(
        color=discord.Color.from_rgb(241, 90, 36)
    )
    embed.set_author(name="• Fun")
    embed.add_field(name="Cog command", value=ctx.author.mention + " → One of the Fun cogs has been unloaded!")
    await ctx.send(embed=embed)


@unload_fun.error
async def unload_fun_error(ctx, error):
    member = ctx.author
    if isinstance(error, commands.MissingRequiredArgument):
        embed = discord.Embed(
            color=discord.Color.from_rgb(241, 90, 36)
        )
        embed.set_author(name="• Invalid Argument!")
        embed.add_field(name=member, value="Please put a valid option! Example: `l!unload_fun whois`")
        await ctx.send(embed=embed)


@client.command(pass_context=True)
@commands.is_owner()
async def reload_fun(ctx, extension):
    client.reload_extension(f"cogs.Fun.{extension}")
    embed = discord.Embed(
        color=discord.Color.from_rgb(241, 90, 36)
    )
    embed.set_author(name="• Fun")
    embed.add_field(name="Cog command", value=ctx.author.mention + " → One of the Fun cogs has been reloaded!")
    await ctx.send(embed=embed)


@reload_fun.error
async def reload_fun_error(ctx, error):
    member = ctx.author
    if isinstance(error, commands.MissingRequiredArgument):
        embed = discord.Embed(
            color=discord.Color.from_rgb(241, 90, 36)
        )
        embed.set_author(name="• Invalid Argument!")
        embed.add_field(name=member, value="Please put a valid option! Example: `l!reload_fun whois`")
        await ctx.send(embed=embed)


for filename in os.listdir('./cogs/Fun'):
    if filename.endswith('.py'):
        client.load_extension(f"cogs.Fun.{filename[:-3]}")

# ————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————
# ————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————
# ————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————


@client.command(pass_context=True)
@commands.is_owner()
async def load_moderation(ctx, extension):
    client.load_extension(f"cogs.Moderation.{extension}")
    embed = discord.Embed(
        color=discord.Color.from_rgb(241, 90, 36)
    )
    embed.set_author(name="• Moderation")
    embed.add_field(name="Cog command", value=ctx.author.mention + " → One of the moderation cogs has been loaded!")
    await ctx.send(embed=embed)


@load_moderation.error
async def load_moderation_error(ctx, error):
    member = ctx.author
    if isinstance(error, commands.MissingRequiredArgument):
        embed = discord.Embed(
            color=discord.Color.from_rgb(241, 90, 36)
        )
        embed.set_author(name="• Invalid Argument!")
        embed.add_field(name=member, value="Please put a valid option! Example: `l!load_moderation purge`")
        await ctx.send(embed=embed)


@client.command()
@commands.is_owner()
async def unload_moderation(ctx, extension):
    client.unload_extension(f"cogs.Moderation.{extension}")
    embed = discord.Embed(
        color=discord.Color.from_rgb(241, 90, 36)
    )
    embed.set_author(name="• Moderation")
    embed.add_field(name="Cog command", value=ctx.author.mention + " → One of the moderation cogs has been unloaded!")
    await ctx.send(embed=embed)


@unload_moderation.error
async def unload_moderation_error(ctx, error):
    member = ctx.author
    if isinstance(error, commands.MissingRequiredArgument):
        embed = discord.Embed(
            color=discord.Color.from_rgb(241, 90, 36)
        )
        embed.set_author(name="• Invalid Argument!")
        embed.add_field(name=member, value="Please put a valid option! Example: `l!unload_moderation purge`")
        await ctx.send(embed=embed)


@client.command(pass_context=True)
@commands.is_owner()
async def reload_moderation(ctx, extension):
    client.reload_extension(f"cogs.Moderation.{extension}")
    embed = discord.Embed(
        color=discord.Color.from_rgb(241, 90, 36)
    )
    embed.set_author(name="• Moderation")
    embed.add_field(name="Cog command", value=ctx.author.mention + " → One of the moderation cogs has been reloaded!")
    await ctx.send(embed=embed)


@reload_moderation.error
async def reload_moderation_error(ctx, error):
    member = ctx.author
    if isinstance(error, commands.MissingRequiredArgument):
        embed = discord.Embed(
            color=discord.Color.from_rgb(241, 90, 36)
        )
        embed.set_author(name="• Invalid Argument!")
        embed.add_field(name=member, value="Please put a valid option! Example: `l!reload_moderation kick`")
        await ctx.send(embed=embed)


for filename in os.listdir('./cogs/Moderation'):
    if filename.endswith('.py'):
        client.load_extension(f"cogs.Moderation.{filename[:-3]}")

# ————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————
# ————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————
# ————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————


@client.command(pass_context=True)
@commands.is_owner()
async def load_events(ctx, extension):
    client.load_extension(f"cogs.Events.{extension}")
    embed = discord.Embed(
        color=discord.Color.from_rgb(241, 90, 36)
    )
    embed.set_author(name="• Events")
    embed.add_field(name="Cog command", value=ctx.author.mention + " → One of the information cogs has been loaded!")
    await ctx.send(embed=embed)


@load_events.error
async def load_events_error(ctx, error):
    member = ctx.author
    if isinstance(error, commands.MissingRequiredArgument):
        embed = discord.Embed(
            color=discord.Color.from_rgb(241, 90, 36)
        )
        embed.set_author(name="• Invalid Argument!")
        embed.add_field(name=member, value="Please put a valid option! Example: `l!load_events member`")
        await ctx.send(embed=embed)


@client.command(pass_contxt=True)
@commands.is_owner()
async def unload_events(ctx, extension):
    client.unload_extension(f"cogs.Events.{extension}")
    embed = discord.Embed(
        color=discord.Color.from_rgb(241, 90, 36)
    )
    embed.set_author(name="• Events")
    embed.add_field(name="Cog command", value=ctx.author.mention + " → One of the moderation cogs has been unloaded!")
    await ctx.send(embed=embed)


@unload_events.error
async def unload_events_error(ctx, error):
    member = ctx.author
    if isinstance(error, commands.MissingRequiredArgument):
        embed = discord.Embed(
            color=discord.Color.from_rgb(241, 90, 36)
        )
        embed.set_author(name="• Invalid Argument!")
        embed.add_field(name=member, value="Please put a valid option! Example: `l!unload_events member`")
        await ctx.send(embed=embed)


@client.command(pass_context=True)
@commands.is_owner()
async def reload_events(ctx, extension):
    client.reload_extension(f"cogs.Events.{extension}")
    embed = discord.Embed(
        color=discord.Color.from_rgb(241, 90, 36)
    )
    embed.set_author(name="• Events")
    embed.add_field(name="Cog command", value=ctx.author.mention + " → One of the moderation cogs has been reloaded!")
    await ctx.send(embed=embed)


@reload_events.error
async def reload_events_error(ctx, error):
    member = ctx.author
    if isinstance(error, commands.MissingRequiredArgument):
        embed = discord.Embed(
            color=discord.Color.from_rgb(241, 90, 36)
        )
        embed.set_author(name="• Invalid Argument!")
        embed.add_field(name=member, value="Please put a valid option! Example: `l!reload_events member`")
        await ctx.send(embed=embed)


for filename in os.listdir('./cogs/Events'):
    if filename.endswith('.py'):
        client.load_extension(f"cogs.Events.{filename[:-3]}")

# ————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————
# ————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————
# ————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————

"""
@client.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
        await ctx.send(":facepalm: — Invalid command! Run `l!help` to see all commands.")
"""


# Work in progress

"""
@client.command(pass_context=True)
async def weather(ctx,):
    owm = pyowm.OWM('1596858fc52ce6e8121fab7aa5e7d964')
    observation = owm.weather_at_place("London,GB")
    w = observation.get_weather()
    await ctx.send(f"{w.get_wind()}")
"""


# client.run(read_token())
client.run(read_token(), bot=False)
