import smtplib
import os
import discord
from email.message import EmailMessage
from discord.ext import commands
from logging_files.utility_logging import logger


class Email(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command()
    @commands.cooldown(rate=1, per=1800, type=commands.BucketType.user)
    async def email(self, ctx, emailto, subject, *, content):
        email = os.environ.get("email")  # Your email
        password = os.environ.get("email_password")

        msg = EmailMessage()
        msg['Subject'] = subject
        msg['From'] = email
        msg['To'] = emailto

        msg.set_content("<p>" + content + "</p>" + """\
<!DOCTYPE html>
<html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <meta http-equiv="X-UA-Compatible" content="ie=edge">
        <title>Document</title>
        <link href="https://fonts.googleapis.com/css?family=Ubuntu&display=swap" rel="stylesheet">
    </head>
    <style>
        * {
            font-family: 'Ubuntu', sans-serif;
            box-sizing: border-box;
        }
    </style>

    <style>
        .linebreak {
            width: 50%;
            size: 10;
        }
    </style>
    <body>
        <footer>
            <div class="info">
                <hr class="linebreak">
                <h1 style="text-align: center">FAQ</h1>
                <h4 style="margin-top: 15px">What is this email?</h4>
                    <ul>
                        <li>This was email sent from a Discord Bot known as LinuxBoi!</li>
                    </ul>
                <h4>Why was this sent to me?</h4>
                    <ul>
                        <li>This email was sent to you because someone in Discord ran this command and they entered your email address.</li>
                    </ul>
                <h4>Is this email a scam, spam, ect?</h4>
                    <ul>
                        <li>No of course not! Someone just wanted to send you a email using a Discord bot. Thats all it is to it!</li>
                    </ul>
                <h4>Can someone spam this and bomb people's emails?</h4>
                    <ul>
                        <li>No, the command has built in protection that allows 1 email to be sent every 30 minutes.</li>
                    </ul>
                <h4>I don't want to see anymore emails from whoever is running the command anymore please.</h4>
                    <ul>
                        <li>Sure! Just block this email address and you will never see another email again!</li>
                    </ul>
                <h4>Why does the person not just send a email through their regular address / email client?</h4>
                    <ul>
                        <li>They could not have access to their email right now!
                         However they could be just doing this to save time 
                         and not open their email client and send a email.</li>
                    </ul>
                <h4>Okay, this sounds alright then can I have a invite link to the Discord Bot please?</h4>
                    <ul>
                        <li>Of course! Invite the bot here:<a style="text-decoration: none" href="https://bit.ly/2ZfozfL"> Click here!</a></li>
                    </ul>
            </div>
        </footer>
    </body>
</html>
""", subtype='html')

        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smpt:
            smpt.login(email, password)
            smpt.send_message(msg)

        embed = discord.Embed(
            color=discord.Color.from_rgb(241, 90, 36),
            title="→ Email Sent!"
        )
        link = "https://digitalsynopsis.com/wp-content/uploads/2015/10/gif-icons-menu-transition-animations-send-mail.gif"
        embed.set_thumbnail(url=link)
        embed.add_field(name="• Email Sent to:", inline=False, value=f"```{emailto}```")
        embed.add_field(name="• Subject:", inline=False, value=f"```{subject}```")
        embed.add_field(name="• Content:", inline=False, value=f"```{content}```")

        await ctx.send(embed=embed)

        logger.info(f"Utility | Sent Email: {ctx.author} | To: {emailto} | Subject: {subject} | Content: {content}")

    @email.error
    async def email_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            embed = discord.Embed(
                color=discord.Color.from_rgb(241, 90, 36),
                title="→ Invalid Argument!",
                description="• Please put a valid option! " \
                      "\n• Example: `l!email address@emailproider.com \"<subject>\" <content>`" \
                      "\n• Please note: Subjects with more than one word need to have quotes around them."
            )
            await ctx.send(embed=embed)
            ctx.command.reset_cooldown(ctx)
        elif isinstance(error, commands.CommandOnCooldown):
            embed = discord.Embed(
                color=discord.Color.from_rgb(241, 90, 36),
                title="→ Slow down!",
                description="• You can only send a email every 30 minutes!"
            )

            await ctx.send(embed=embed)


def setup(client):
    client.add_cog(Email(client))
