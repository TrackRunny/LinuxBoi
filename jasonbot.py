import discord
import random
import asyncio
import psutil
from discord.ext import commands, tasks
from itertools import cycle
from discord.utils import get

client = commands.Bot(command_prefix =['j!' , 'J!'])
client.remove_command('help')

@client.event
async def on_ready():
	print('The Bot is Online')	

@client.event
async def on_command_error(ctx, error):
	if isinstance(error, commands.CommandNotFound):
		await ctx.send("<:rjaslogo:596877216361742359> — Uh oh! → That command doesn't exists")

@client.event
async def on_member_join(member):
	print(f'{memer}Just hoped in the server.')
	
@client.event
async def on_member_remove(member):
	print(f'{member} Has dropped out of the server.')	

@client.command(pass_context=True)
@commands.has_role('+')
async def clear(ctx, amount : int):
	await ctx.channel.purge(limit=amount)

@clear.error
async def clear_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send( "<:rjaslogo:596877216361742359> — Uh oh! → You may not have permissions or you need to put all the required fields | `Ex: j!clear 10`" )

@client.command(pass_context=True)
@commands.has_role('+')
async def kick(ctx, member : discord.Member, *, reason=None):
	await member.kick(reason=reason)
	await ctx.send('<:gjaslogo:596877377582268426> — User has been kicked!!')
	print("Requested kick")

@kick.error
async def kick_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send( "<:rjaslogo:596877216361742359> — Uh oh! → You may not have permissions or you need to put all the required fields | `Ex: j!kick @user`" )

@client.command(pass_context=True)
@commands.has_role('+')
async def ban(ctx, member : discord.Member, *, reason=None):
	await member.ban(reason=reason)			
	await ctx.send('<:rjaslogo:596877216361742359> — User has been banned!!')
	print("Requested ban")

@ban.error
async def ban_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send( "<:rjaslogo:596877216361742359> — Uh oh! → You may not have permissions or you need to put all the required fields | `Ex: j!ban @user`" )

@client.command()
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

@client.command()
@commands.has_role( "+" )
async def addmod(ctx, member: discord.Member):
    role = discord.utils.get(ctx.guild.roles, name="+")
    await member.add_roles(role)
    await ctx.send("<:gjaslogo:596877377582268426> — User has been added as a moderator")
    print("Requested addmod")

@client.command()
@commands.has_role("-")
async def delmod(ctx, member: discord.Member):
	role = discord.utils.get(ctx.guild.roles, name="+")
	await member.remove_roles(role)
	await ctx.send("<:gjaslogo:596877377582268426> — User is no longer a moderator")
	print("Requested delmod")

@addmod.error
async def addmod_error(ctx, error):
	if isinstance(error, commands.MissingRequiredArgument):
		await ctx.send("<:rjaslogo:596877216361742359> — Uh oh! → You may not have permissions or you need to put all the required fields | `Ex: j!addmod @user`" )

@delmod.error
async def delmod_error(ctx, error):
	if isinstance(error, commands.MissingRequiredArgument):
		await ctx.send("<:rjaslogo:596877216361742359> — Uh oh! → You may not have permissions or you need to put all the required fields | `Ex: j!delmod @user`" )

@client.command()
@commands.has_role("+")
async def mute(ctx, member: discord.Member):
	role = discord.utils.get(ctx.guild.roles, name="• Muted")
	await member.add_roles(role)
	await ctx.send("<:gjaslogo:596877377582268426> — User is now muted!!")
	print('Requested Mute')

@client.command()
@commands.has_role("+")
async def unmute(ctx, member: discord.Member):
	role = discord.utils.get(ctx.guild.roles, name="• Muted")
	await member.remove_roles(role)
	await ctx.send("<:gjaslogo:596877377582268426> — User is no longer muted")
	print("Requested unmute")

@client.command(pass_context=True)
async def poop(ctx):
	await ctx.send("https://cdn.friendlystock.com/wp-content/uploads/2018/04/16-nervous-poop-emoji-cartoon-clipart.jpg")
	print("Requested Poop")
	
@client.command(pass_context=True)
async def coinflip(ctx):
	choices = ("Heads!!", "Tails!!")
	rancoin = random.choice(choices)
	await ctx.send(rancoin)
	print("Requested Coinflip")

@client.command(pass_context=True , aliases=['8ball'])
async def _8ball(ctx):
	choices = ("Maybe", "Certainly", "Ask God", "Nah", "Of course", "totally", "As i see it, yes", "Ask again later", "Better not tell you now", "Cannot predict now", "Concentrate and ask again", "Don't count on it", "It is certain", "It is decidedly so", "Most likely", "Only if you subscribe to JasonMC", "My reply is no", "My sources say no", "Outlook good", "ask alexa", "Outlook not so good", "Reply hazy try again", "Signs point to yes", "Very doubtful", "Without a doubt", "Yes!", "Yes, definitely", "you may rely on it")
	ranball = random.choice(choices)
	await ctx.send(ranball)
	print("Requested 8ball")

@client.command(pass_context=True)
async def roast(ctx):
	choices = ("You look like something that I would draw with my left hand.", "You're so ugly, you scared the crap out of the toilet.", "No I'm not insulting you, I'm describing you.", "It's better to let someone think you are an Idiot than to open your mouth and prove it.", "If I had a face like yours, I'd sue my parents.", "Your birth certificate is an apology letter from the abortion center.", "I guess your ugly face proves that even god makes mistakes sometimes.", "Roses are red violets are blue, God made me pretty, what happened to you?", "I'd slap you, but that would be animal abuse.", "If your gonna be two faced, honey at least make one of them pretty.", "Keep rolling your eyes, perhaps you'll find a brain back there.", "You're so fat, you could sell shade.", "Don't you need a license to be that ugly?", "Stupidity is not a crime so you are free to go.", "You are so old, your birth-certificate expired.", " Did your parents ever ask you to run away from home?", "Hi! I'm a human being! What are you?", "Your so ugly that when you had plastic surgery the doctors sued you")
	ranroast = random.choice(choices)
	await ctx.send(ranroast)
	print("requested roast")

@client.command(pass_context=True)
async def help(ctx):
				author = ctx.message.author
				
				
				embed = discord.Embed(
						colour = discord.Colour.blue()
				)
			
					
				embed.set_author(name="help")
				embed.set_thumbnail(url="https://encrypted-tbn0.gstatic.com/images?q=tbn%3AANd9GcS_xu3Wf1VldKKdzQWYcVHOdDyUGAm1WPLISYslN0CO2yGKxiH1")
				embed.add_field(name=":game_die: | FUN", value="`roast, poop, coinflip, 8ball`", inline=False)
				embed.add_field(name=":tools: | UTILITY", value="`avatar, mb, help`", inline=False)
				embed.add_field(name=":card_box: | Information", value="`stats, info, userinfo, help,`", inline = False)
				embed.add_field(name=":construction: | Moderation", value="`clear, kick, unban, ban, mute, unmute`", inline=False)
				embed.add_field(name=":loudspeaker: | Administrative", value="`addmod, delmod`")
			
				await ctx.send(embed=embed)
				print("Requested commands")

@client.command()
async def userinfo(ctx, member: discord.Member):
				author = ctx.message.author
	
				
				embed = discord.Embed(
						colour=discord.Colour.blue()
				
				)
				
				roles = [role for role in member.roles]
				
				embed.set_author(name=f"User Info — {member}")
				embed.set_thumbnail(url=member.avatar_url)
				embed.set_footer(text=f"Requested by {ctx.author}", icon_url=ctx.author.avatar_url)
				
				embed.add_field(name=":id: | ID", value=member.id)
				embed.add_field(name=":name_badge: | User Name", value=member.display_name)
				
				embed.add_field(name=":calendar: | Created at", value=member.created_at.strftime("%A, %d. %B %Y @ %H:%M%S UTC"))
				embed.add_field(name=":date: | Joined at", value=member.joined_at.strftime("%A, %d. %B %Y @ %H:%M:%S UTC"))
				
				embed.add_field(name=f":military_medal: | Roles", value=" ".join([role.mention for role in roles]))
				embed.add_field(name=":arrow_up: | Top Role", value=member.top_role.mention)
				
				embed.add_field(name=":robot: | Bot?", value=member.bot)
				
				await ctx.send(embed=embed)
				print("Requested userinfo")

@client.command(pass_context=True , aliases=['info'])
async def stats(ctx):
	            author = ctx.message.author
	            
	            
	            embed = discord.Embed(
	                    colour=discord.Colour.orange()
	            
	            )
	            
	            
	            embed.set_author(name="Voltage 1.5.1")
	            embed.add_field(name="—", value="This bot was made for the benefits of Voltage GFX/Hangout and it is coded by yours truly JasonMC", inline=False)
	            embed.add_field(name=":new: | What's New!!", value="• Error Handler\n• Bot Status\n• New Mod Commands", inline=False)
	            embed.add_field(name=":bookmark: | Library", value="Discord.py v1.2.3")
	            embed.add_field(name=":radioactive: | Ping", inline=False, value=(f'{round(client.latency * 1000)}ms'))
	            embed.add_field(name=":desktop: | CPU Usage", inline=False, value=str(psutil.cpu_percent()))
	            embed.add_field(name=":iphone: | Operating System", value='Ubuntu 18.04 LTS', inline=False)
	            embed.add_field(name=":bar_chart: | Member Count", value=(len(ctx.guild.members)), inline=False)
	            embed.add_field(name=":satellite_orbital: | Guild Count", value=(len(client.guilds)), inline=False)
	            embed.add_field(name=":love_letter: | Invite Me", value="[Click Here](https://discordapp.com/api/oauth2/authorize?client_id=517804128878198785&permissions=8&redirect_uri=https%3A%2F%2Fdiscordapp.com%2Fapi%2Foauth2%2Fauthorize%3Fclient_id%3D517804128878198785%26permissions%3D8%26scope%3Dbot&scope=bot)")
	            
	            await ctx.send(embed=embed)
	            print("Requested Stats/info")

@client.command()
async def avatar(ctx, member:discord.Member):
	await ctx.send(member.avatar_url)
	print("Requested avatar")
	         
@client.command()
async def mb(ctx):
	await ctx.send(len(ctx.guild.members))
	
client.run('NTE3ODA0MTI4ODc4MTk4Nzg1.D2IITQ.UI9dY9cYkLmaYOvsd0Tx9RXFEbk')
