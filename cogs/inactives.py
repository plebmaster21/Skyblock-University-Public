import discord
from discord.ext import commands
from discord.utils import get
import requests
import datetime
import time
import dotenv
import os


class GuildInactiveCheck(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @commands.cooldown(1, 60)
    async def inactive(self, ctx, *, guild: str = None):
        if guild is None:
            embed = discord.Embed(title=f'Error',
                                  description='No guild inputted. The format is `+inactive GUILDNAME`',
                                  colour=0xFF0000)
            await ctx.reply(embed=embed)
            return

        key = os.getenv("apikey")
        guild_id = requests.get(f"https://api.hypixel.net/findGuild?key={key}&byName={guild}").json()["guild"]
        guilds = ["6111fcb48ea8c95240436c57", "604a765e8ea8c962f2bb3b7a",
                  "607a0d7c8ea8c9c0ff983976", "608d91e98ea8c9925cdb91b7",
                  "60a16b088ea8c9bb7f6d9052", "60b923478ea8c9a3aefbf3dd", "6125800e8ea8c92e1833e851",
                  "570940fb0cf2d37483e106b3"]
        if guild_id not in guilds:
            embed = discord.Embed(title=f'Error',
                                  description='Inputted guild is not an SBU Guild. The format is `+inactive GUILDNAME`',
                                  colour=0xFF0000)
            await ctx.reply(embed=embed)
            return
        embed = discord.Embed(title=f'Processing ',
                              description='Your request is being processed. This message will be edited once it '
                                          'is complete.',
                              colour=0xFF0000)
        message = await ctx.reply(embed=embed)
        guild_data = requests.get(f"https://api.hypixel.net/guild?key={key}&id={guild_id}").json()

        unix = time.mktime(time.gmtime())
        unix -= (86400 * 7)
        embed = discord.Embed(title=f'Members to be kicked from {guild}',
                              description='The list below includes all members to be kicked from the guild',
                              colour=discord.Color.blue())
        try:
            inactive_list = ["PlaceHolder"]
            inactive_list.remove("PlaceHolder")
            for member in guild_data["guild"]["members"]:
                member_uuid = member["uuid"]
                data = requests.get(
                    url="https://api.hypixel.net/player", params={"key": key, "uuid": member_uuid}).json()
                try:
                    member_name = data["player"]["displayname"]
                except:
                    await ctx.send("API issues, likely being rate limited, try again in a few minutes")
                    print("API issues, likely being rate limited, try again in a few minutes")
                try:
                    member_lastlogout = data["player"]["lastLogout"]
                    member_lastlogout = member_lastlogout / 1000
                    if member_lastlogout < unix:
                        inactive_list.append(member_name)
                        embed.add_field(name=f'Kick: {member_name}',
                                        value=datetime.datetime.fromtimestamp(member_lastlogout))
                except:
                    await ctx.send(
                        f"Member {member_name} has their api off, please check them manually under ``profile > "
                        f"guild`` and searching last online in reversed order.")
            print(f"Inactive check for {guild} done")
            await message.edit(embed=embed)
        except:
            await ctx.send("Request failed, check Guild name and try again. Or rather API is not being supportive")

    @inactive.error
    async def check_error(self, ctx, error):
        if isinstance(error, commands.MissingRole):
            await ctx.send("Insufficient Permissions, only moderators can use this command.")
        elif isinstance(error, commands.CommandOnCooldown):
            await ctx.send(error)


def setup(bot):
    bot.add_cog(GuildInactiveCheck(bot))
