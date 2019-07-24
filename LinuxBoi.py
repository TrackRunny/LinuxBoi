import os
import discord
from discord.ext import commands, tasks
from itertools import cycle

# client = commands.Bot("l!", owner_id=54681233121306214, case_insensitive=False, self_bot=True)
client = commands.Bot("l!", owner_id=546812331213062144, case_insensitive=False)
client.remove_command('help')
status = cycle([f'Linux videos | l!help', 'FOSS software | l!help', 'Windows getting worse',
                'Server members | l!help', 'Cryptocurrency | l!help', 'Linux getting popular'])
valid = "TrackRunny#3900"
line_divide = "\n———————————————————————————————"


def read_token():
    with open("TestingSelfBot.txt", "r") as f:
        lines = f.readlines()
        return lines[0].strip()


@client.event
async def on_ready():
    change_status.start()
    print(f"---------------LinuxBoi---------------"
          f"\nBot is online and connected to " + str(client.user) +
          f"\nCreated by TrackRunny#3900 on Discord"
          f"\n----------------------------------------------")


@tasks.loop(seconds=15)
async def change_status():
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name=next(status)))


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
async def load_utility(ctx, extension):
    client.load_extension(f"cogs.Utility.{extension}")
    embed = discord.Embed(
        color=discord.Color.from_rgb(241, 90, 36)
    )
    embed.set_author(name="• Utility")
    embed.add_field(name="Cog command", value=ctx.author.mention + " → One of the Utility cogs has been loaded!")
    await ctx.send(embed=embed)


@load_utility.error
async def load_utility_error(ctx, error):
    member = ctx.author
    if isinstance(error, commands.MissingRequiredArgument):
        embed = discord.Embed(
            color=discord.Color.from_rgb(241, 90, 36)
        )
        embed.set_author(name="• Invalid Argument!")
        embed.add_field(name=member, value="Please put a valid option! Example: `l!load_utility minecraft`")
        await ctx.send(embed=embed)


@client.command(pass_context=True)
@commands.is_owner()
async def unload_utility(ctx, extension):
    client.unload_extension(f"cogs.Utility.{extension}")
    embed = discord.Embed(
        color=discord.Color.from_rgb(241, 90, 36)
    )
    embed.set_author(name="• Utility")
    embed.add_field(name="Cog command", value=ctx.author.mention + " → One of the Utility cogs has been unloaded!")
    await ctx.send(embed=embed)


@unload_utility.error
async def unload_utility_error(ctx, error):
    member = ctx.author
    if isinstance(error, commands.MissingRequiredArgument):
        embed = discord.Embed(
            color=discord.Color.from_rgb(241, 90, 36)
        )
        embed.set_author(name="• Invalid Argument!")
        embed.add_field(name=member, value="Please put a valid option! Example: `l!unload_utility minecraft`")
        await ctx.send(embed=embed)


@client.command(pass_context=True)
@commands.is_owner()
async def reload_utility(ctx, extension):
    client.reload_extension(f"cogs.Utility.{extension}")
    embed = discord.Embed(
        color=discord.Color.from_rgb(241, 90, 36)
    )
    embed.set_author(name="• Utility")
    embed.add_field(name="Cog command", value=ctx.author.mention + " → One of the Utility cogs has been reloaded!")
    await ctx.send(embed=embed)


@reload_utility.error
async def reload_utility_error(ctx, error):
    member = ctx.author
    if isinstance(error, commands.MissingRequiredArgument):
        embed = discord.Embed(
            color=discord.Color.from_rgb(241, 90, 36)
        )
        embed.set_author(name="• Invalid Argument!")
        embed.add_field(name=member, value="Please put a valid option! Example: `l!reload_utility minecraft`")
        await ctx.send(embed=embed)


for filename in os.listdir('./cogs/Utility'):
    if filename.endswith('.py'):
        client.load_extension(f"cogs.Utility.{filename[:-3]}")

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


@client.command(pass_context=True)
@commands.is_owner()
async def load_owner(ctx, extension):
    client.load_extension(f"cogs.Owner.{extension}")
    embed = discord.Embed(
        color=discord.Color.from_rgb(241, 90, 36)
    )
    embed.set_author(name="• Owner")
    embed.add_field(name="Cog command", value=ctx.author.mention + " → One of the owner cogs has been loaded!")
    await ctx.send(embed=embed)


@load_owner.error
async def load_owner_error(ctx, error):
    member = ctx.author
    if isinstance(error, commands.MissingRequiredArgument):
        embed = discord.Embed(
            color=discord.Color.from_rgb(241, 90, 36)
        )
        embed.set_author(name="• Invalid Argument!")
        embed.add_field(name=member, value="Please put a valid option! Example: `l!load_owner shutdown`")
        await ctx.send(embed=embed)


@client.command(pass_context=True)
@commands.is_owner()
async def unload_owner(ctx, extension):
    client.unload_extension(f"cogs.Owner.{extension}")
    embed = discord.Embed(
        color=discord.Color.from_rgb(241, 90, 36)
    )
    embed.set_author(name="• Owner")
    embed.add_field(name="Cog command", value=ctx.author.mention + " → One of the owner cogs has been unloaded!")
    await ctx.send(embed=embed)


@unload_owner.error
async def unload_owner_error(ctx, error):
    member = ctx.author
    if isinstance(error, commands.MissingRequiredArgument):
        embed = discord.Embed(
            color=discord.Color.from_rgb(241, 90, 36)
        )
        embed.set_author(name="• Invalid Argument!")
        embed.add_field(name=member, value="Please put a valid option! Example: `l!unload_owner shutdown`")
        await ctx.send(embed=embed)


@client.command(pass_context=True)
@commands.is_owner()
async def reload_owner(ctx, extension):
    client.reload_extension(f"cogs.Owner.{extension}")
    embed = discord.Embed(
        color=discord.Color.from_rgb(241, 90, 36)
    )
    embed.set_author(name="• Owner")
    embed.add_field(name="Cog command", value=ctx.author.mention + " → One of the owner cogs has been reloaded!")
    await ctx.send(embed=embed)


@reload_owner.error
async def reload_owner_error(ctx, error):
    member = ctx.author
    if isinstance(error, commands.MissingRequiredArgument):
        embed = discord.Embed(
            color=discord.Color.from_rgb(241, 90, 36)
        )
        embed.set_author(name="• Invalid Argument!")
        embed.add_field(name=member, value="Please put a valid option! Example: `l!reload_owner shutdown`")
        await ctx.send(embed=embed)


for filename in os.listdir('./cogs/Owner'):
    if filename.endswith('.py'):
        client.load_extension(f"cogs.Owner.{filename[:-3]}")

# ————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————
# ————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————
# ————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————

"""
@client.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
        await ctx.send(":facepalm: — Invalid command! Run `l!help` to see all commands.")
"""


client.run(read_token())
# client.run(read_token(), bot=False)
