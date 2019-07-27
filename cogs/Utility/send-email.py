import smtplib
from email.message import EmailMessage
import discord
from discord.ext import commands


class Email(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command()
    async def email(self, ctx, emailto, subject, *, content):
        email = 'linuxboi.discordbot@gmail.com'  # Your email
        password = 'tJhIPc9Qfzipr537yfrJnVI#gH^mk&go%E8gf6!aB7Y$xBAs2Ua8eYPm9DjQg9Y74v4P%V2mhIQtXkSfuwP!gyW^r%n5IIQ#*I5h'

        msg = EmailMessage()
        msg['Subject'] = subject
        msg['From'] = "LinuxBoi.com"
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
                <h4>I don't want to see anymore emails from whoever is running the command anymore please.</h4>
                    <ul>
                        <li>Sure! Just block this email address and you will never see another email again!</li>
                    </ul>
                <h4>Why does the person not just send a email through their regular address / email client?</h4>
                    <ul>
                        <li>They could not have access to their email right now! However they could be just doing this to save time and not open their email client and send a email.</li>
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
            color=discord.Color.from_rgb(241, 90, 36)
        )
        link = "https://digitalsynopsis.com/wp-content/uploads/2015/10/gif-icons-menu-transition-animations-send-mail.gif"
        embed.set_author(name=f"→ Email Sent!")
        embed.set_thumbnail(url=link)
        embed.add_field(name="• Email Sent to:", inline=False, value=f"```{emailto}```")
        embed.add_field(name="• Subject:", inline=False,  value=f"```{subject}```")
        embed.add_field(name="• Content:", inline=False, value=f"```{content}```")

        await ctx.send(embed=embed)

    @email.error
    async def email_error(self, ctx, error):
        member = ctx.author
        if isinstance(error, commands.MissingRequiredArgument):
            embed = discord.Embed(
                color=discord.Color.from_rgb(241, 90, 36)
            )
            invalid = "Please put a valid option! " \
                      "\nExample: `l!email address@emailproider.com \"<subject>\" <content>`" \
                      "\n Please note: Subjects with more than one word need to have quotes around them."
            embed.set_author(name=member)
            embed.add_field(name="• Invalid Argument!",
                            value=invalid)
            await ctx.send(embed=embed)


def setup(client):
    client.add_cog(Email(client))
