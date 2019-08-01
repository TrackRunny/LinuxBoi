import discord
import psutil
from discord.ext import commands

client = commands.Bot(["j!", ], owner_id=417864220667936778, case_insensitive=False)
client.remove_command('help')


@client.event
async def on_ready():
    await client.change_presence(activity=discord.Activity(type=3, name="Voltage Bot — !help"))
    print('The Bot is Online')


@client.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
        await ctx.send("Uh oh! → That command doesn't exists")


@client.command(pass_context=True, aliases=['commands'])
async def help(ctx):
    author = ctx.message.author

    embed = discord.Embed(
        colour=discord.Colour.blue()
    )

    embed.set_author(name="help")
    embed.set_thumbnail(
        url="https://encrypted-tbn0.gstatic.com/images?q=tbn%3AANd9GcS_xu3Wf1VldKKdzQWYcVHOdDyUGAm1WPLISYslN0CO2yGKxiH1")
    embed.add_field(name=":first_place: | Tools", value="`avatar, help, stats, userinfo,\nhelp`", inline=True)
    embed.add_field(name=":second_place: | Mod Commands", value="`kick, ban, unban,\nmute, unmute, clear,\nreport`",
                    inline=True)
    embed.add_field(name=":third_place: | Owner Only Commands", value="`status`", inline=True)

    await ctx.send(embed=embed)
    print("Requested commands")


@client.command(pass_context=True, aliases=["whois"])
async def userinfo(ctx, member: discord.Member):
    author = ctx.message.author

    embed = discord.Embed(
        colour=discord.Colour.blue()

    )

    roles = [role for role in member.roles]

    embed.set_author(name=f"User Info — {member}")
    embed.set_thumbnail(url=member.avatar_url)
    embed.set_footer(text=f"Requested by {ctx.author}", icon_url=ctx.author.avatar_url)

    embed.add_field(name=":id: | ID", value=member.id, inline=True)
    embed.add_field(name=":name_badge: | User Name", value=member.display_name, inline=True)

    embed.add_field(name=":calendar: | Created at", value=member.created_at.strftime("%A, %d. %B %Y @ %H:%M%S UTC"),
                    inline=True)
    embed.add_field(name=":date: | Joined at", value=member.joined_at.strftime("%A, %d. %B %Y @ %H:%M:%S UTC"),
                    inline=True)

    embed.add_field(name=f":military_medal: | Roles", value=" ".join([role.mention for role in roles]), inline=True)
    embed.add_field(name=":arrow_up: | Top Role", value=member.top_role.mention, inline=True)

    embed.add_field(name=":robot: | Bot?", value=member.bot, inline=True)

    await ctx.send(embed=embed)
    print("Requested userinfo")


@userinfo.error
async def userinfo_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send(
            ":white_check_mark: — Uh oh! → You may not have permissions or you need to put all the required fields | `Ex: j!userinfo @user`")


@client.command(pass_context=True, aliases=['info'])
async def stats(ctx):
    author = ctx.message.author

    embed = discord.Embed(
        colour=discord.Colour.orange()

    )

    embed.set_author(name="Voltage")
    embed.add_field(name="—", value="This bot was made by JasonMC, Just a simple Moderation Bot!!", inline=True)
    embed.add_field(name=":new: | What's New!!", value="• Bug Fixes\n•Inlined embeds(for pc)\n•Report Command!!",
                    inline=True)
    embed.add_field(name=":bookmark: | Library", value="Discord.py v1.2.3", inline=True)
    embed.add_field(name=":radioactive: | Ping", inline=True, value=f'{round(client.latency * 1000)}ms')
    embed.add_field(name=":desktop: | CPU Usage", inline=True, value=str(psutil.cpu_percent()))
    embed.add_field(name=":iphone: | Operating System", value='Ubuntu 18.04 LTS', inline=True)
    embed.add_field(name=":bar_chart: | Member Count", value=(len(ctx.guild.members)), inline=True)
    embed.add_field(name=":satellite_orbital: | Guild Count", value=(len(client.guilds)), inline=True)
    embed.add_field(name=":love_letter: | Invite Me",
                    value="[Click Here](https://discordapp.com/api/oauth2/authorize?client_id=517804128878198785&permissions=8&redirect_uri=https%3A%2F%2Fdiscordapp.com%2Fapi%2Foauth2%2Fauthorize%3Fclient_id%3D517804128878198785%26permissions%3D8%26scope%3Dbot&scope=bot)",
                    inline=True)

    await ctx.send(embed=embed)
    print("Stats/info Sent")


@client.command(pass_context=True)
async def avatar(ctx, member: discord.Member):
    embed = discord.Embed(
        colour=discord.Colour.blue()

    )
    embed.set_author(name="—Avatar")
    embed.set_image(url=member.avatar_url_as(size=4096, format="png"))

    await ctx.send(embed=embed)


@client.command()
@commands.is_owner()
async def status(ctx, *, status="None"):
    await client.change_presence(status=discord.Status.idle, activity=discord.Game(status))
    await ctx.send('Status changed to', status)


@client.command(pass_context=True)
@commands.has_permissions(kick_members=True)
async def warn(ctx, member: discord.Member, *, reason="No reason was stated"):
    author = ctx.message.author

    embed = discord.Embed(
        colour=discord.Colour.blue()
    )

    embed.set_author(name=f"{member} has been warned")

    await ctx.send(embed=embed)

    embed2 = discord.Embed(
        colour=discord.Colour.blue()
    )

    embed2.set_author(name="—You have been warned")
    embed2.add_field(name="Moderator", value=f"{ctx.author}", inline=True)
    embed2.add_field(name="Reason", value=reason, inline=True)

    await member.send(embed=embed2)


@warn.error
async def warn_error(ctx, error):
    if isinstance(error, commands.MissingPermissions):
        await ctx.send(
            ":white_check_mark: — Uh oh! → You may not have permissions or you need to put all the required fields | `Ex: j!warn @user`")


@client.command(pass_context=True)
@commands.cooldown(rate=1, per=86400, type=commands.BucketType.user)
async def report(ctx, member: discord.Member, *, reason="The reporter did not state a reason"):
    author = ctx.message.author

    embed = discord.Embed(
        colour=discord.Colour.red()
    )

    embed.set_author(name=f"{member} has been reported to the staff member that you have mentioned")

    await ctx.send(embed=embed)

    embed2 = discord.Embed(
        colour=discord.Colour.red()
    )

    embed2.set_author(name="Someone sent a report!!")
    embed2.add_field(name="Reporter", value=f"||{ctx.author}||", inline=True)
    embed2.add_field(name="Person Reported", value=f"{member}", inline=True)
    embed2.add_field(name="Reason", value=reason, inline=True)

    await member.send(embed=embed2)


@report.error
async def report_error(ctx, error):
    member = ctx.author
    if isinstance(error, commands.CommandOnCooldown):
        await ctx.send(":white_check_mark: — This command has a 1 hour cooldown, please be patient")


@client.command(pass_context=True)
@commands.has_permissions(manage_messages=True)
async def clear(ctx, amount: int):
    await ctx.channel.purge(limit=amount)


@clear.error
async def clear_error(ctx, error):
    if isinstance(error, commands.MissingPermissions):
        await ctx.send(
            ":white_check_mark: — Uh oh! → You may not have permissions or you need to put all the required fields | `Ex: j!clear 10`")


@client.command(pass_context=True)
@commands.has_permissions(kick_members=True)
async def kick(ctx, member: discord.Member, *, reason=None):
    await member.kick(reason=reason)
    await ctx.send(':white_check_mark: — User has been kicked!!')
    print("Requested kick")


@kick.error
async def kick_error(ctx, error):
    if isinstance(error, commands.MissingPermissions):
        await ctx.send(
            ":exclamation: — Uh oh! → You may not have permissions or you need to put all the required fields | `Ex: j!kick @user`")


@client.command(pass_context=True)
@commands.has_permissions(kick_members=True, ban_members=True)
async def ban(ctx, member: discord.Member, *, reason=None):
    await member.ban(reason=reason)
    await ctx.send(':white_check_mark: — User has been banned!!')
    print("Requested ban")


@ban.error
async def ban_error(ctx, error):
    if isinstance(error, commands.MissingPermissions):
        await ctx.send(
            ":exclamation: — Uh oh! → You may not have permissions or you need to put all the required fields | `Ex: j!ban @user`")


@client.command()
@commands.has_permissions(ban_members=True)
async def unban(ctx, *, member):
    banned_users = await ctx.guild.bans()
    member_name, member_discriminator = member.split('#')

    for ban_entry in banned_users:
        user = ban_entry.user

        if (user.name, user.discriminator) == (member_name, member_discriminator):
            await ctx.guild.unban(user)
            await ctx.send(f' I have unbanned {user.name}#{user.discriminator}')
            return

        print('Requested unban command')


@unban.error
async def unban_error(ctx, error):
    if isinstance(error, commands.MissingPermissions):
        await ctx.send(
            ":exclamation: — Uh oh! → You may not have permissions or you need to put all the required fields | `Ex: j!ban JasonMC#7185`")


@client.command()
@commands.has_permissions(kick_members=True)
async def mute(ctx, member: discord.Member):
    role = discord.utils.get(ctx.guild.roles, name="Mute")
    await member.add_roles(role)
    await ctx.send(":white_check_mark: — User has been muted")
    print("Requested mute")


@mute.error
async def mute_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send(":exclamation: — Uh oh! → Please specify a user | `Ex: j!mute @user`")


@client.command()
@commands.has_permissions(kick_members=True)
async def unmute(ctx, member: discord.Member):
    role = discord.utils.get(ctx.guild.roles, name="Mute")
    await member.remove_roles(role)
    await ctx.send(":white_check_mark: — User is no longer muted")
    print("Requested unmute")


@unmute.error
async def unmute_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send(":exclamation: — Uh oh! → Please specify a user | `Ex: j!unmute @user`")


client.run('NTE3ODA0MTI4ODc4MTk4Nzg1.D2IITQ.UI9dY9cYkLmaYOvsd0Tx9RXFEbk')
