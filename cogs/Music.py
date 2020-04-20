# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# LinuxBoi - Discord bot                                                    #
# Copyright (C) 2019-2020 TrackRunny                                        #
#                                                                           #
# This program is free software: you can redistribute it and/or modify      #
# it under the terms of the GNU General Public License as published by      #
# the Free Software Foundation, either version 3 of the License, or         #
# (at your option) any later version.                                       #
#                                                                           #
# This program is distributed in the hope that it will be useful,           #
# but WITHOUT ANY WARRANTY; without even the implied warranty of            #
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the             #
# GNU General Public License for more details.                              #
#                                                                           #
# You should have received a copy of the GNU General Public License         #
# along with this program. If not, see <https://www.gnu.org/licenses/>.     #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

import math
import re

import discord
import lavalink
from discord.ext import commands

url_rx = re.compile(r'https?://(?:www\.)?.+')


class Music(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.votes = []

        if not hasattr(bot, 'lavalink'):  # This ensures the client isn't overwritten during cog reloads.
            bot.lavalink = lavalink.Client(bot.user.id)
            bot.lavalink.add_node('127.0.0.1', 2333, 'Runningboy12?', 'us', 'default-node')  # Host, Port, Password, Region, Name
            bot.add_listener(bot.lavalink.voice_update_handler, 'on_socket_response')

        lavalink.add_event_hook(self.track_hook)

    def cog_unload(self):
        self.bot.lavalink._event_hooks.clear()

    async def cog_before_invoke(self, ctx):
        guild_check = ctx.guild is not None

        if guild_check:
            await self.ensure_voice(ctx)

        return guild_check

    """
    async def cog_command_error(self, ctx, error):
        if isinstance(error, commands.CommandInvokeError):
            await ctx.send(error.original)
            # The above handles errors thrown in this cog and shows them to the user.
            # This shouldn't be a problem as the only errors thrown in this cog are from `ensure_voice`
            # which contain a reason string, such as "Join a voicechannel" etc. You can modify the above
    """  # if you want to do things differently.

    async def ensure_voice(self, ctx):
        """ This check ensures that the bot and command author are in the same voicechannel. """
        player = self.bot.lavalink.player_manager.create(ctx.guild.id, endpoint=str(ctx.guild.region))

        should_connect = ctx.command.name in ('play', )  # Add commands that require joining voice to work.

        if not ctx.author.voice or not ctx.author.voice.channel:
            embed = discord.Embed(
                color=self.bot.embed_color,
                title="→ Voice Channel Error!",
                description="• Please make sure to join a voice channel first!"
            )
            raise commands.CommandInvokeError(await ctx.send(embed=embed))

        if not player.is_connected:
            if not should_connect:
                embed = discord.Embed(
                    color=self.bot.embed_color,
                    title="→ Voice Channel Error!",
                    description="• I am not connected to a voice channel"
                )
                raise commands.CommandInvokeError(await ctx.send(embed=embed))

            permissions = ctx.author.voice.channel.permissions_for(ctx.me)

            if not permissions.connect or not permissions.speak:  # Check user limit too?
                embed = discord.Embed(
                    color=self.bot.embed_color,
                    title="→ Permission Error!",
                    description="• Please give me connect permissions, or speaking permissions!"
                )
                await ctx.send(embed=embed)

            player.store('channel', ctx.channel.id)
            await self.connect_to(ctx.guild.id, str(ctx.author.voice.channel.id))
        else:
            if int(player.channel_id) != ctx.author.voice.channel.id:
                embed = discord.Embed(
                    color=self.bot.embed_color,
                    title="→ Voice Channel Error!",
                    description="• Please make sure you are in my voice channel!"
                )
                raise commands.CommandInvokeError(await ctx.send(embed=embed))

    async def track_hook(self, event):
        if isinstance(event, lavalink.events.QueueEndEvent):
            guild_id = int(event.player.guild_id)
            await self.connect_to(guild_id, None)

    async def connect_to(self, guild_id: int, channel_id: str):
        ws = self.bot._connection._get_websocket(guild_id)
        await ws.voice_state(str(guild_id), channel_id)

    @commands.command(aliases=['p'])
    async def play(self, ctx, *, query: str):
        """ Searches and plays a song from a given query. """
        player = self.bot.lavalink.player_manager.get(ctx.guild.id)

        query = query.strip('<>')

        if not url_rx.match(query):
            query = f'ytsearch:{query}'

        results = await player.node.get_tracks(query)

        if not results or not results['tracks']:
            embed = discord.Embed(
                color=self.bot.embed_color,
                title="→ Playing Error!",
                description="• The query you searched for was not found."
            )
            return await ctx.send(embed=embed)

        # position = lavalink.utils.format_time(player.position)

        if results['loadType'] == 'PLAYLIST_LOADED':
            tracks = results['tracks']

            for track in tracks:
                player.add(requester=ctx.author.id, track=track)

            embed = discord.Embed(color=self.bot.embed_color,
                                  description=f'• **{results["playlistInfo"]["name"]}** - {len(tracks)} tracks',
                                  title="→ Playlist Added!")
            embed.set_thumbnail(url=f'https://img.youtube.com/vi/{track["info"]["identifier"]}/default.jpg')
            await ctx.send(embed=embed)
        else:
            track = results['tracks'][0]

            embed = discord.Embed(color=self.bot.embed_color,
                                  description=f'• [**{track["info"]["title"]}**]({track["info"]["uri"]})',
                                  title="→ Song Added To Queue!")
            embed.set_thumbnail(url=f'https://img.youtube.com/vi/{track["info"]["identifier"]}/default.jpg')

            track = lavalink.models.AudioTrack(track, ctx.author.id, recommended=True)
            player.add(requester=ctx.author.id, track=track)

            await ctx.send(embed=embed)

        if not player.is_playing:
            await player.play()

    @play.error
    async def play_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            embed = discord.Embed(
                color=self.bot.embed_color,
                title="→ Invalid Argument!",
                description="• Please put a valid option! Example: `l!play <Song Name / URL>`"
            )
            await ctx.send(embed=embed)

    @commands.command()
    async def seek(self, ctx, *, seconds: int):
        """ Seeks to a given position in a track. """
        player = self.bot.lavalink.player_manager.get(ctx.guild.id)

        track_time = player.position + (seconds * 1000)
        await player.seek(track_time)

        embed = discord.Embed(
            color=self.bot.embed_color,
            title="→ Resumed!",
            description=f"• Song time has been moved to: `{lavalink.utils.format_time(track_time)}`"
        )
        await ctx.send(embed=embed)

    @seek.error
    async def seek_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            embed = discord.Embed(
                color=self.bot.embed_color,
                title="→ Invalid Argument!",
                description="• Please put a valid option! Example: `l!seek <time>`"
            )
            await ctx.send(embed=embed)

    @commands.command(aliases=['s'])
    async def skip(self, ctx):
        """ Skips the current track. """
        player = self.bot.lavalink.player_manager.get(ctx.guild.id)

        await player.skip()
        embed = discord.Embed(
            color=self.bot.embed_color,
            title="→ Skipped",
            description="• The current song you have requested has been **skipped!**"
        )
        await ctx.send(embed=embed)

    @commands.command()
    async def stop(self, ctx):
        """ Stops the player and clears its queue. """
        player = self.bot.lavalink.player_manager.get(ctx.guild.id)

        if not player.is_playing:
            embed = discord.Embed(
                color=self.bot.embed_color,
                title="→ No Songs!",
                description="• Nothing is playing at the moment!"
            )
            return await ctx.send(embed=embed)

        player.queue.clear()
        await player.stop()

        embed = discord.Embed(
            color=self.bot.embed_color,
            title="→ Stopped!",
            description="• The music has been stopped!"
        )
        await ctx.send(embed=embed)

    @commands.command(aliases=['np', 'n', 'playing'])
    async def now(self, ctx):
        """ Shows some stats about the currently playing song. """
        player = self.bot.lavalink.player_manager.get(ctx.guild.id)

        if not player.current:
            embed = discord.Embed(
                color=self.bot.embed_color,
                title="→ No Songs!",
                description="• Nothing is playing at the moment!"
            )
            return await ctx.send(embed=embed)

        position = lavalink.utils.format_time(player.position)
        if player.current.stream:
            duration = '🔴 Live Video'
        else:
            duration = lavalink.utils.format_time(player.current.duration)
        song = f'**• [{player.current.title}]({player.current.uri})**'

        embed = discord.Embed(
            color=self.bot.embed_color,
            title='→ Currently Playing:',
            description=f"{song}"
                        f"\n**•** Current time: **({position}/{duration})**"
        )
        embed.set_thumbnail(url=f'https://img.youtube.com/vi/{player.current.identifier}/default.jpg')
        await ctx.send(embed=embed)

    @commands.command(aliases=['q'])
    async def queue(self, ctx, page: int = 1):
        """ Shows the player's queue. """
        player = self.bot.lavalink.player_manager.get(ctx.guild.id)

        if not player.queue:
            embed = discord.Embed(
                color=self.bot.embed_color,
                title="→ No Queue!",
                description="• No songs are in the queue at the moment!"
            )
            return await ctx.send(embed=embed)

        items_per_page = 10
        pages = math.ceil(len(player.queue) / items_per_page)

        start = (page - 1) * items_per_page
        end = start + items_per_page

        queue_list = ''
        for index, track in enumerate(player.queue[start:end], start=start):
            queue_list += f'`{index + 1}.` [**{track.title}**]({track.uri})\n'

        embed = discord.Embed(
            color=self.bot.embed_color,
            title="→ List Of Songs:",
            description=f"\n{queue_list}"
        )
        # embed.set_author(name=f'→ List of songs: {len(player.queue)} \n\n{queue_list}')
        embed.set_footer(text=f'• On page: {page}/{pages}')
        await ctx.send(embed=embed)

    @commands.command(aliases=['resume'])
    async def pause(self, ctx):
        """ Pauses/Resumes the current track. """
        player = self.bot.lavalink.player_manager.get(ctx.guild.id)

        if not player.is_playing:
            embed = discord.Embed(
                color=self.bot.embed_color,
                title="→ Not Playing!",
                description="• No song is playing is currently playing!"
            )
            return await ctx.send(embed=embed)

        if player.paused:
            await player.set_pause(False)
            embed = discord.Embed(
                color=self.bot.embed_color,
                title="→ Resumed!",
                description="• The current song has been **resumed successfully!**"
            )
            await ctx.send(embed=embed)
        else:
            await player.set_pause(True)
            embed = discord.Embed(
                color=self.bot.embed_color,
                title="→ Paused!",
                description="• The current song has been **paused successfully!**"
            )
            await ctx.send(embed=embed)

    @commands.command(aliases=['v'])
    async def volume(self, ctx, volume: int = None):
        """ Changes the player's volume (0-1000). """
        player = self.bot.lavalink.player_manager.get(ctx.guild.id)

        if not volume:
            embed = discord.Embed(
                color=self.bot.embed_color,
                title="→ Current Volume!",
                description=f"• Volume: **{player.volume}%**"
            )
            return await ctx.send(embed=embed)

        await player.set_volume(volume)  # Lavalink will automatically cap values between, or equal to 0-1000.

        embed = discord.Embed(
            color=self.bot.embed_color,
            title="→ Volume Updated!",
            description=f"• Volume set to: **{player.volume}%**"
        )

        await ctx.send(embed=embed)

    @commands.command(aliases=['shuff'])
    async def shuffle(self, ctx):
        """ Shuffles the player's queue. """
        player = self.bot.lavalink.player_manager.get(ctx.guild.id)
        if not player.is_playing:
            embed = discord.Embed(
                color=self.bot.embed_color,
                title="→ Not Playing!",
                description="• No song is playing is currently playing!"
            )
            return await ctx.send(embed=embed)

        player.shuffle = not player.shuffle
        embed = discord.Embed(
            color=self.bot.embed_color,
            title="→ Song Shuffling",
            description="• Song shuffling has been"
                        + (' **enabled!**' if player.shuffle else ' **disabled!**')
        )
        await ctx.send(embed=embed)

    @commands.command(aliases=['loop'])
    async def repeat(self, ctx):
        """ Repeats the current song until the command is invoked again. """
        player = self.bot.lavalink.player_manager.get(ctx.guild.id)

        if not player.is_playing:
            embed = discord.Embed(
                color=self.bot.embed_color,
                title="→ No Songs!",
                description="• Nothing is playing at the moment!"
            )
            return await ctx.send(embed=embed)

        player.repeat = not player.repeat
        embed = discord.Embed(
            color=self.bot.embed_color,
            title="→ Song looping!",
            description="• Looping has been" + (' **enabled!**' if player.repeat else ' **disabled!**')
        )
        await ctx.send(embed=embed)

    @commands.command(aliases=['rm'])
    async def remove(self, ctx, index: int):
        """ Removes an item from the player's queue with the given index. """
        player = self.bot.lavalink.player_manager.get(ctx.guild.id)

        if not player.queue:
            embed = discord.Embed(
                color=self.bot.embed_color,
                title="→ No Queued Items!",
                description="• There is nothing queued at the moment!"
            )
            return await ctx.send(embed=embed)

        if index > len(player.queue) or index < 1:
            embed = discord.Embed(
                color=self.bot.embed_color,
                title="→ No Queued Items!",
                description=f"• Your remove number needs to be between 1 and {len(player.queue)}"
            )
            return await ctx.send(embed=embed)
        removed = player.queue.pop(index - 1)  # Account for 0-index.

        embed = discord.Embed(
            color=self.bot.embed_color,
            title="→ Item Removed!",
            description=f"• Removed `{removed.title}` from the queue."
        )
        await ctx.send(embed=embed)

    @remove.error
    async def remove_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            embed = discord.Embed(
                color=self.bot.embed_color,
                title="→ Invalid Argument!",
                description="• Please put a valid option! Example: `l!remove 1`"
            )
            await ctx.send(embed=embed)

    @commands.command(aliases=["find"])
    async def search(self, ctx, *, query):
        """ Lists the first 10 search results from a given query. """
        player = self.bot.lavalink.player_manager.get(ctx.guild.id)

        if not query.startswith('ytsearch:') and not query.startswith('scsearch:'):
            query = 'ytsearch:' + query

        results = await player.node.get_tracks(query)

        if not results or not results['tracks']:
            embed = discord.Embed(
                color=self.bot.embed_color,
                title="→ No Results!",
                description="• Nothing was found in your search term!"
            )
            return await ctx.send(embed=embed)

        tracks = results['tracks'][:10]  # First 10 results

        o = ''
        for index, track in enumerate(tracks, start=1):
            track_title = track['info']['title']
            track_uri = track['info']['uri']
            o += f'`{index}.` [{track_title}]({track_uri})\n'

        embed = discord.Embed(
            color=self.bot.embed_color,
            title="→ Top 5 Results:",
            description=f"{o}"
        )
        await ctx.send(embed=embed)

    @search.error
    async def find_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            embed = discord.Embed(
                color=self.bot.embed_color,
                title="→ Invalid Argument!",
                description="• Please put a valid option! Example: `l!search <song>`"
            )
            await ctx.send(embed=embed)

    @commands.command(aliases=['dc'])
    async def disconnect(self, ctx):
        """ Disconnects the player from the voice channel and clears its queue. """
        player = self.bot.lavalink.player_manager.get(ctx.guild.id)

        if not player.is_connected:
            embed = discord.Embed(
                color=self.bot.embed_color,
                title="→ Not Connected!",
                description="• You need to join a voice channel to play music!"
            )
            return await ctx.send(embed=embed)

        if not ctx.author.voice or (player.is_connected and ctx.author.voice.channel.id != int(player.channel_id)):
            embed = discord.Embed(
                color=self.bot.embed_color,
                title="→ Not Connected!",
                description="• You are not in my voice channel that I am connected to!"
            )
            return await ctx.send(embed=embed)

        player.queue.clear()
        await player.stop()
        await self.connect_to(ctx.guild.id, None)

        embed = discord.Embed(
            color=self.bot.embed_color,
            title="→ Disconnected!",
            description="• I have **disconnected** from the voice channel!"
        )
        return await ctx.send(embed=embed)


def setup(bot):
    bot.add_cog(Music(bot))
