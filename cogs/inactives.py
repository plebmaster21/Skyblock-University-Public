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
    async def inactive(self, ctx, *,guild = None):
        
        if guild == None:
            embedVar = discord.Embed(color=ctx.author.color,
                        description=f"No guild inputted, `+inactive GUILD`")
            await ctx.send(embed=embedVar)
            return
        if guild.lower() in ["sb lambda pi", "sb theta tau", "sb delta omega", "sb iota theta",
                                        "sb uni", "sb rho xi", "sb kappa eta", "sb alpha psi", "sb masters"]:
            pass
        else:
            embedVar = discord.Embed(color=ctx.author.color,
                    description=f"Inputted guild is not an SBU guild")
            await ctx.send(embed=embedVar)
            return
        key = os.getenv("apikey")
        amount = 1
        data = requests.get(
            url="https://api.hypixel.net/guild",
            params={
                "key": key,
                "name": guild
            }).json()
        embedVar = discord.Embed(color=ctx.author.color, title=f"Inactive List for {data['guild']['name']}",
                        description=f"<a:loading:978732444998070304> Skyblock University is thinking")
        message=await ctx.send(embed=embedVar)
        if data["guild"] is not None:
            embedmsg = ""
            totalmembers = 0

            for i in data["guild"]["members"]:
                total = 0
                for i2 in i["expHistory"]:
                    total += i["expHistory"][i2]
                uuid = i["uuid"]
                if total <= int(amount):
                    data2 = requests.get(
                    url=f"https://api.mojang.com/user/profile/{uuid}").json()
                    username = data2["name"]
                    embedmsg += f"{username}\n"
                    totalmembers += 1
            embedVar = discord.Embed(color=ctx.author.color, title=f"Inactive List for {data['guild']['name']}",
                                        description=f"{totalmembers} members were found to be under {amount} GEXP." + f"\n\n{embedmsg}")
            await message.edit(embed=embedVar)
                    
    @inactive.error
    async def check_error(self, ctx, error):
        if isinstance(error, commands.MissingRole):
            await ctx.send("Insufficient Permissions, only moderators can use this command.")
        elif isinstance(error, commands.CommandOnCooldown):
            await ctx.send(error)


def setup(bot):
    bot.add_cog(GuildInactiveCheck(bot))
