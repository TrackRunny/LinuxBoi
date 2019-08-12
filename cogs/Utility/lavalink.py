"""
This is an example cog that shows how you would make use of Lavalink.py.
This example cog requires that you have python 3.6 or higher due to the f-strings.
"""
import math
import re

import discord
import lavalink
from discord.ext import commands

url_rx = re.compile('https?:\\/\\/(?:www\\.)?.+')  # noqa: W605


class Music(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

        if not hasattr(bot, 'lavalink'):  # This ensures the client isn't overwritten during cog reloads.
            bot.lavalink = lavalink.Client(bot.user.id)
            bot.lavalink.add_node('127.0.0.1', 2333, 'Runningboy12?', 'us',
                                  'default-node')  # Host, Port, Password, Region, Name
            bot.add_listener(bot.lavalink.voice_update_handler, 'on_socket_response')

        bot.lavalink.add_event_hook(self.track_hook)

    def cog_unload(self):
        self.bot.lavalink._event_hooks.clear()

    async def cog_before_invoke(self, ctx):
        guild_check = ctx.guild is not None
        #  This is essentially the same as `@commands.guild_only()`
        #  except it saves us repeating ourselves (and also a few lines).

        if guild_check:
            await self.ensure_voice(ctx)
            #  Ensure that the bot and command author share a mutual voicechannel.

        return guild_check
    """
    async def cog_command_error(self, ctx, error):
        if isinstance(error, commands.CommandInvokeError):
            await ctx.send(error.original)
            # The above handles errors thrown in this cog and shows them to the user.
            # This shouldn't be a problem as the only errors thrown in this cog are from `ensure_voice`
            # which contain a reason string, such as "Join a voicechannel" etc. You can modify the above
    """        # if you want to do things differently.

    async def track_hook(self, event):
        if isinstance(event, lavalink.events.QueueEndEvent):
            guild_id = int(event.player.guild_id)
            await self.connect_to(guild_id, None)
            # Disconnect from the channel -- there's nothing else to play.

    async def connect_to(self, guild_id: int, channel_id: str):
        """ Connects to the given voicechannel ID. A channel_id of `None` means disconnect. """
        ws = self.bot._connection._get_websocket(guild_id)
        await ws.voice_state(str(guild_id), channel_id)
        # The above looks dirty, we could alternatively use `bot.shards[shard_id].ws` but that assumes
        # the bot instance is an AutoShardedBot.

    @commands.command(aliases=['p'])
    async def play(self, ctx, *, query: str):
        """ Searches and plays a song from a given query. """
        player = self.bot.lavalink.players.get(ctx.guild.id)

        query = query.strip('<>')

        if not url_rx.match(query):
            query = f'ytsearch:{query}'

        results = await player.node.get_tracks(query)
        """
        position = lavalink.utils.format_time(player.position)
        if player.current.stream:
            duration = '🔴 LIVE'
        else:
            duration = lavalink.utils.format_time(player.current.duration)
        song = f'**[{player.current.title}]({player.current.uri})**\n({position}/{duration})'
        """
        if not results or not results['tracks']:
            return await ctx.send('Nothing found!')

        if results['loadType'] == 'PLAYLIST_LOADED':
            tracks = results['tracks']

            for track in tracks:
                player.add(requester=ctx.author.id, track=track)
                embed = discord.Embed(color=discord.Color.from_rgb(241, 90, 36),
                                      description=f'— {results["playlistInfo"]["name"]} - {len(tracks)} tracks',
                                      title="→ Playlist added!")

                embed.add_field(name="• Duration:", value="test")
                await ctx.send(embed=embed)
        else:
            track = results['tracks'][0]
            embed = discord.Embed(color=discord.Color.from_rgb(241, 90, 36),
                                  description=f'— [{track["info"]["title"]}]({track["info"]["uri"]})',
                                  title="→ Song added to queue!")
            player.add(requester=ctx.author.id, track=track)

            await ctx.send(embed=embed)

        if not player.is_playing:
            await player.play()

    @play.error
    async def play_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            embed = discord.Embed(
                color=discord.Color.from_rgb(241, 90, 36)
            )
            embed.add_field(name="→ Invalid Argument!",
                            value="• Please put a valid option! Example: `l!play <Song name>`")
            await ctx.send(embed=embed)

    @commands.command()
    async def seek(self, ctx, *, seconds: int):
        """ Seeks to a given position in a track. """
        player = self.bot.lavalink.players.get(ctx.guild.id)

        track_time = player.position + (seconds * 1000)
        await player.seek(track_time)

        embed = discord.Embed(
            color=discord.Color.from_rgb(241, 90, 36)
        )
        embed.add_field(name="→ Resumed!",
                        value=f"• Song time has been moved to: `{lavalink.utils.format_time(track_time)}`")
        await ctx.send(embed=embed)
        await ctx.send(f'Moved track to **{lavalink.utils.format_time(track_time)}**')

    @commands.command(aliases=['forceskip'])
    async def skip(self, ctx):
        """ Skips the current track. """
        player = self.bot.lavalink.players.get(ctx.guild.id)

        if not player.is_playing:
            embed = discord.Embed(color=discord.Color.from_rgb(241, 90, 36))
            embed.add_field(name="→ Not playing!", value="• No song is playing is currently playing!")
            await ctx.send(embed=embed)

        await player.skip()
        embed = discord.Embed(color=discord.Color.from_rgb(241, 90, 36))
        embed.add_field(name="→ Skipped!", value="• The current song you have requested has been skipped!")
        await ctx.send(embed=embed)

    @commands.command()
    async def stop(self, ctx):
        """ Stops the player and clears its queue. """
        player = self.bot.lavalink.players.get(ctx.guild.id)

        if not player.is_playing:
            embed = discord.Embed(color=discord.Color.from_rgb(241, 90, 36))
            embed.add_field(name="→ No songs!", value="• Nothing is playing at the moment!!")
            return await ctx.send(embed=embed)

        player.queue.clear()
        await player.stop()
        embed = discord.Embed(color=discord.Color.from_rgb(241, 90, 36))
        embed.add_field(name="→ Stopped!", value="• The DJ has stopped the party!")
        await ctx.send(embed=embed)

    @commands.command(aliases=['np', 'n', 'playing'])
    async def now(self, ctx):
        """ Shows some stats about the currently playing song. """
        player = self.bot.lavalink.players.get(ctx.guild.id)

        if not player.current:
            embed = discord.Embed(color=discord.Color.from_rgb(241, 90, 36))
            embed.add_field(name="→ No songs!", value="• Nothing is playing at the moment!!")
            return await ctx.send(embed=embed)

        position = lavalink.utils.format_time(player.position)
        if player.current.stream:
            duration = '🔴 LIVE'
        else:
            duration = lavalink.utils.format_time(player.current.duration)
        song = f'**[{player.current.title}]({player.current.uri})**\n—\n({position}/{duration})'

        embed = discord.Embed(color=discord.Color.from_rgb(241, 90, 36),
                              title='→ Currently Playing:', description=song)
        await ctx.send(embed=embed)

    @commands.command(aliases=['q'])
    async def queue(self, ctx, page: int = 1):
        """ Shows the player's queue. """
        player = self.bot.lavalink.players.get(ctx.guild.id)

        if not player.queue:
            embed = discord.Embed(color=discord.Color.from_rgb(241, 90, 36))
            embed.add_field(name="→ No queue!", value="• No songs are in the queue at the moment!")
            return await ctx.send(embed=embed)

        items_per_page = 10
        pages = math.ceil(len(player.queue) / items_per_page)

        start = (page - 1) * items_per_page
        end = start + items_per_page

        queue_list = ''
        for index, track in enumerate(player.queue[start:end], start=start):
            queue_list += f'`{index + 1}.` [**{track.title}**]({track.uri})\n'

        embed = discord.Embed(color=discord.Color.from_rgb(241, 90, 36))
        # embed.set_author(name=f'→ List of songs: {len(player.queue)} \n\n{queue_list}')
        embed.add_field(name=f'→ List of songs:', value=f'\n\n{queue_list}')
        embed.set_footer(text=f'• On page: {page}/{pages}')
        await ctx.send(embed=embed)

    @commands.command(aliases=['resume'])
    async def pause(self, ctx):
        """ Pauses/Resumes the current track. """
        player = self.bot.lavalink.players.get(ctx.guild.id)

        if not player.is_playing:
            embed = discord.Embed(color=discord.Color.from_rgb(241, 90, 36))
            embed.add_field(name="→ Not playing!", value="• No song is playing is currently playing!")
            return await ctx.send(embed=embed)

        if player.paused:
            await player.set_pause(False)
            embed = discord.Embed(
                color=discord.Color.from_rgb(241, 90, 36)
            )
            embed.add_field(name="→ Resumed!",
                            value=f"• The current song has been resumed successfully!")
            await ctx.send(embed=embed)
        else:
            await player.set_pause(True)
            embed = discord.Embed(
                color=discord.Color.from_rgb(241, 90, 36)
            )
            embed.add_field(name="→ Paused!",
                            value=f"• The current song has been paused successfully!")
            await ctx.send(embed=embed)

    @commands.command(aliases=['vol'])
    async def volume(self, ctx, volume: int = None):
        """ Changes the player's volume (0-1000). """
        player = self.bot.lavalink.players.get(ctx.guild.id)

        if not volume:
            return await ctx.send(f'🔈 | {player.volume}%')

        await player.set_volume(volume)  # Lavalink will automatically cap values between, or equal to 0-1000.
        await ctx.send(f'🔈 | Set to {player.volume}%')

    @commands.command()
    async def shuffle(self, ctx):
        """ Shuffles the player's queue. """
        player = self.bot.lavalink.players.get(ctx.guild.id)
        if not player.is_playing:
            embed = discord.Embed(color=discord.Color.from_rgb(241, 90, 36))
            embed.add_field(name="→ Not playing!", value="• No song is playing is currently playing!")
            return await ctx.send(embed=embed)

        player.shuffle = not player.shuffle
        embed = discord.Embed(color=discord.Color.from_rgb(241, 90, 36))
        embed.add_field(name="→ Shuffle command!", value="• Song shuffling has been"
                        + (' Enabled!' if player.shuffle else ' Disabled!'))
        await ctx.send(embed=embed)

    @commands.command(aliases=['loop'])
    async def repeat(self, ctx):
        """ Repeats the current song until the command is invoked again. """
        player = self.bot.lavalink.players.get(ctx.guild.id)

        if not player.is_playing:
            embed = discord.Embed(
                color=discord.Color.from_rgb(241, 90, 36)
            )
            embed.add_field(name="→ No songs!",
                            value=f"• Nothing is playing at the moment!")
            return await ctx.send(embed=embed)

        player.repeat = not player.repeat
        embed = discord.Embed(
            color=discord.Color.from_rgb(241, 90, 36)
        )
        embed.add_field(name="→ Loop command!",
                        value='• Looping has been' + (' Enabled!' if player.repeat else ' Disabled!'))
        await ctx.send(embed=embed)

    @commands.command(aliases=['rm'])
    async def remove(self, ctx, index: int):
        """ Removes an item from the player's queue with the given index. """
        player = self.bot.lavalink.players.get(ctx.guild.id)

        if not player.queue:
            embed = discord.Embed(
                color=discord.Color.from_rgb(241, 90, 36)
            )
            embed.add_field(name="→ No queued items!",
                            value=f"• There is nothing queued at the moment!")
            return await ctx.send(embed=embed)

        if index > len(player.queue) or index < 1:
            embed = discord.Embed(
                color=discord.Color.from_rgb(241, 90, 36)
            )
            embed.add_field(name="→ No queued items!",
                            value=f"• Remove number have to be between 1 and{len(player.queue)}")
            return await ctx.send(embed=embed)
        removed = player.queue.pop(index - 1)  # Account for 0-index.

        embed = discord.Embed(
            color=discord.Color.from_rgb(241, 90, 36)
        )
        embed.add_field(name="→ Item removed!",
                        value=f"• Removed `{removed.title}` from the queue.")
        await ctx.send(embed=embed)

    @commands.command()
    async def find(self, ctx, *, query):
        """ Lists the first 10 search results from a given query. """
        player = self.bot.lavalink.players.get(ctx.guild.id)

        if not query.startswith('ytsearch:') and not query.startswith('scsearch:'):
            query = 'ytsearch:' + query

        results = await player.node.get_tracks(query)

        if not results or not results['tracks']:
            embed = discord.Embed(
                color=discord.Color.from_rgb(241, 90, 36)
            )
            embed.add_field(name="→ No results!",
                            value=f"• Nothing was found in your search term!")
            return await ctx.send(embed=embed)

        tracks = results['tracks'][:5]  # First 10 results

        o = ''
        for index, track in enumerate(tracks, start=1):
            track_title = track['info']['title']
            track_uri = track['info']['uri']
            o += f'`{index}.` [{track_title}]({track_uri})\n'
        embed = discord.Embed(
            color=discord.Color.from_rgb(241, 90, 36)
        )
        embed.add_field(name="→ Top 5 results:",
                        value=f"{o}")
        await ctx.send(embed=embed)

    @commands.command(aliases=['dc'])
    async def disconnect(self, ctx):
        """ Disconnects the player from the voice channel and clears its queue. """
        player = self.bot.lavalink.players.get(ctx.guild.id)

        if not player.is_connected:
            embed = discord.Embed(
                color=discord.Color.from_rgb(241, 90, 36)
            )
            embed.add_field(name="→ Not connected!",
                            value="• You need to join a voice channel to play music!")
            return await ctx.send(embed=embed)

        if not ctx.author.voice or (player.is_connected and ctx.author.voice.channel.id != int(player.channel_id)):
            embed = discord.Embed(
                color=discord.Color.from_rgb(241, 90, 36)
            )
            embed.add_field(name="→ Not connected!",
                            value="• You are not in my voice channel that I am connected to!")
            return await ctx.send(embed=embed)

        player.queue.clear()
        await player.stop()
        await self.connect_to(ctx.guild.id, None)
        embed = discord.Embed(
            color=discord.Color.from_rgb(241, 90, 36)
        )
        embed.add_field(name="→ Disconnected!",
                        value="• I have disconnected from the voice channel!")
        return await ctx.send(embed=embed)

    async def ensure_voice(self, ctx):
        """ This check ensures that the bot and command author are in the same voicechannel. """
        player = self.bot.lavalink.players.create(ctx.guild.id, endpoint=str(ctx.guild.region))
        # Create returns a player if one exists, otherwise creates.

        should_connect = ctx.command.name in ('play')  # Add commands that require joining voice to work.

        if not ctx.author.voice or not ctx.author.voice.channel:
            embed = discord.Embed(
                color=discord.Color.from_rgb(241, 90, 36)
            )
            embed.add_field(name="→ Voice channel error!",
                            value="• Please make sure to join a voice channel first!")
            raise commands.CommandInvokeError(await ctx.send(embed=embed))

        if not player.is_connected:
            if not should_connect:
                embed = discord.Embed(
                    color=discord.Color.from_rgb(241, 90, 36)
                )
                embed.add_field(name="→ Voice channel error!",
                                value="• I am not connected to a voice chat!")
                raise commands.CommandInvokeError(await ctx.send(embed=embed))

            permissions = ctx.author.voice.channel.permissions_for(ctx.me)

            if not permissions.connect or not permissions.speak:  # Check user limit too?
                embed = discord.Embed(
                    color=discord.Color.from_rgb(241, 90, 36)
                )
                embed.add_field(name="→ Permission error!",
                                value="• Please give me connect permissions, or speaking permissions!")
                await ctx.send(embed=embed)

            player.store('channel', ctx.channel.id)
            await self.connect_to(ctx.guild.id, str(ctx.author.voice.channel.id))
        else:
            if int(player.channel_id) != ctx.author.voice.channel.id:
                embed = discord.Embed(
                    color=discord.Color.from_rgb(241, 90, 36)
                )
                embed.add_field(name="→ Voice channel error!",
                                value="• Please make sure you are in my voice channel!")
                raise commands.CommandInvokeError(await ctx.send(embed=embed))


def setup(bot):
    bot.add_cog(Music(bot))
