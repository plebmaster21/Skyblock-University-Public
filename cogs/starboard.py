import discord
from discord.ext import commands
from discord.utils import get
import sqlite3
import datetime

class Starboard(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        conn = sqlite3.connect('starboard.db')
        c = conn.cursor()   
        c.execute("""CREATE TABLE IF NOT EXISTS starboard (
            message_id integer,
            reactions integer
        )""")
        conn.commit()
        conn.close()
        print(f'SQLite databases initialized')

    @commands.Cog.listener()
    async def on_raw_reaction_add(self, payload):
        if payload.emoji.name == "⭐" or payload.emoji.name == "kekboard":
            if payload.channel_id == 805842777350995988:
                return
            message = await self.bot.get_channel(payload.channel_id).fetch_message(payload.message_id)
            conn = sqlite3.connect('starboard.db')
            c = conn.cursor()
            c.execute(f"""SELECT * FROM starboard WHERE message_id = {message.id}
            """)
            values = c.fetchone()
            stars = 1
            if values == None:
                c.execute(f"""INSERT INTO starboard VALUES (
                    {message.id},
                    {stars}
                    )""")
                conn.commit()
                conn.close
                return
            else:
                stars = values[1] + 1
                c.execute(f"""DELETE FROM starboard WHERE message_id = {message.id}""")
                c.execute(f"""INSERT INTO starboard VALUES (
                    {message.id},
                    {stars}
                    )""")
                conn.commit()
                conn.close
            if stars == 5:
                embed = discord.Embed(
                            description=message.content,
                            colour=message.author.colour,
                            timestamp=message.created_at)
                if len(message.attachments):
                    embed.set_image(url=message.attachments[0].url)
                if message.author.avatar == None:
                    embed.set_author(name=message.author)
                else:
                    embed.set_author(name=message.author, icon_url=message.author.avatar)
                embed.add_field(name='Message', value=f'[Jump]({message.jump_url})')
                embed.set_footer(text='Skyblock University Starboard')
                channel = self.bot.get_channel(805842777350995988)
                message = await channel.send(embed=embed)
                await message.add_reaction("⭐")
                
            else:
                return

    @commands.command()
    @commands.has_role("Council")
    async def forcestar(self, ctx, msg):
        channel = ctx.channel
        message = await channel.fetch_message(msg)
        conn = sqlite3.connect('starboard.db')
        c = conn.cursor()
        stars = 6
        c.execute(f"""INSERT INTO starboard VALUES (
                    {message.id},
                    {stars}
                    )""")
        conn.commit()
        conn.close
        conn.commit()
        conn.close
        embed = discord.Embed(
                            description=message.content,
                            colour=message.author.colour,
                            timestamp=message.created_at)
        if len(message.attachments):
            embed.set_image(url=message.attachments[0].url)
        if message.author.avatar == None:
            embed.set_author(name=message.author)
        else:
            embed.set_author(name=message.author, icon_url=message.author.avatar)
        embed.add_field(name='Message', value=f'[Jump]({message.jump_url})')
        embed.set_footer(text='Skyblock University Starboard')
        channel = self.bot.get_channel(805842777350995988)
        message = await channel.send(embed=embed)
        await message.add_reaction("⭐")
        await ctx.send('Message forced on starboard.')


def setup(bot):
    bot.add_cog(Starboard(bot))
