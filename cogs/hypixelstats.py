import discord
import aiohttp
import datetime
import discord.utils
from discord.ext import commands
import requests

class HypixelStats(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="hypixel", description="Get hypixel stats")
    async def hypixel(self, ctx, arg1: str = None, arg2: str = None):
        channel = ctx.message.channel
        response = requests.get(f'https://api.slothpixel.me/api/players/{arg1}')
        player = response.json()
        if arg1 is None:
            await ctx.send("I need an IGN", delete_after=5)
            return
        if 'error' in player:
            await ctx.send(f'`{arg1}` is not a valid username')
        else:
            if arg2 is None:
                async with channel.typing():
                    async with aiohttp.ClientSession() as session:
                        async with session.get(f'https://api.slothpixel.me/api/players/{arg1}') as resp:
                            player = await resp.json()
                        async with session.get(f'https://api.slothpixel.me/api/guilds/{arg1}') as resp:
                            guild = await resp.json()

                    color = ctx.author.color
                    embed = discord.Embed(title=f'{arg1} Hypixel stats', colour=color,
                                          timestamp=datetime.datetime.utcnow())
                    if player['rank'] == "MVP_PLUS_PLUS":
                        embed.add_field(name="PlayerRank", value="MVP++", inline=False)
                    elif player['rank'] == "MVP_PLUS":
                        embed.add_field(name="PlayerRank", value="MVP+", inline=False)
                    elif player['rank'] == "VIP_PLUS":
                        embed.add_field(name="PlayerRank", value="VIP+", inline=False)
                    else:
                        embed.add_field(name="PlayerRank", value=player['rank'], inline=False)
                    embed.add_field(name="Level:", value=player["level"], inline=False)
                    if "error" in guild:
                        embed.add_field(name="Guild:", value=f"{arg1} isn't in a guild")
                    else:
                        embed.add_field(name="Guild:", value=guild["name"])
                    embed.add_field(name="Discord:", value=player["links"]["DISCORD"], inline=False)
                    embed.add_field(name="Online:", value=player['online'], inline=False)
                    embed.add_field(name="Minecraft version:", value=player['mc_version'], inline=False)
                    embed.add_field(name="Last game played:", value=player['last_game'], inline=False)
                    await ctx.send(embed=embed)
                    print(player)


def setup(bot):
    bot.add_cog(HypixelStats(bot))

