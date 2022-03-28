import datetime
import aiohttp
import discord
from discord import Guild
import psycopg2
import psycopg2.extras
from discord.ext import commands
from discord.utils import get
from main import bot

hostname = 'localhost'
database = 'SBU'
username = 'postgres'
pwd = 'obbytrusty'
port_id = 5432

insert_script = 'INSERT INTO VERIFIED (id, uuid, guild) VALUES (%s, %s, %s)'


class Verify(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def verifyping(self, ctx):
        await ctx.send("pong")

    @commands.command(description="Add the role if in guild")
    async def verify(self, ctx, arg1: str = None, arg2: str = None, ):
        if arg1 is None:
            await ctx.send("I need an IGN", delete_after=5)
            return
        if arg2 is None:
            member = ctx.message.author
            tempvar = "Attempt to verify: " + str(ctx.message.author)
            print(tempvar)
            for role1 in ["SB Lambda Pi Member", "SB Theta Tau Member", "SB Delta Omega Member", "SB Iota Theta Member",
                          "SB University Member", "SB Rho Xi Member", "SB Kappa Eta Member", "SB Alpha Psi Member", "SB Masters Member"]:
                role = discord.utils.get(ctx.guild.roles, name=role1)
                if role in member.roles:
                    await member.remove_roles(role)
            async with aiohttp.ClientSession() as session:
                async with session.get(f'https://api.slothpixel.me/api/players/{arg1}') as resp:
                    player = await resp.json()
                async with session.get(f'https://api.slothpixel.me/api/guilds/{arg1}') as resp:
                    guild = await resp.json()
                    if player['links']['DISCORD'] == str(ctx.author):
                        if guild["name"] in ["SB Lambda Pi", "SB Theta Tau", "SB Delta Omega", "SB Iota Theta",
                                             "SB Uni", "SB Rho Xi", "SB Kappa Eta", "SB Alpha Psi","SB Masters"]:
                            if guild["name"] in ["SB Lambda Pi", "SB Theta Tau", "SB Delta Omega", "SB Iota Theta",
                                                 "SB Rho Xi", "SB Kappa Eta", "SB Alpha Psi","SB Masters"]:
                                guildrole = guild["name"] + " Member"
                            elif guild["name"] == "SB Uni":
                                guildrole = "SB University Member"
                            conn = psycopg2.connect(
                                host=hostname,
                                dbname=database,
                                user=username,
                                password=pwd,
                                port=port_id)
                            cur = conn.cursor()
                            cur1 = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)

                            role = get(member.guild.roles, name="Verified")
                            role1 = get(member.guild.roles, name="Guild Member")
                            if player["rank"] == "MVP_PLUS":
                                rankrole = get(member.guild.roles, name="MVP+")
                                await member.add_roles(rankrole)
                            elif player["rank"] == "MVP_PLUS_PLUS":
                                rankrole = get(member.guild.roles, name="MVP++")
                                await member.add_roles(rankrole)
                            elif player["rank"] == "VIP":
                                rankrole = get(member.guild.roles, name="VIP")
                                await member.add_roles(rankrole)
                            elif player["rank"] == "VIP_PLUS":
                                rankrole = get(member.guild.roles, name="VIP+")
                                await member.add_roles(rankrole)
                            elif player["rank"] == "MVP":
                                rankrole = get(member.guild.roles, name="MVP")
                                await member.add_roles(rankrole)

                            role2 = get(member.guild.roles, name=guildrole)
                            await member.add_roles(role)
                            await member.add_roles(role1)
                            await member.add_roles(role2)

                            cur1.execute('SELECT * FROM VERIFIED')
                            catch = False
                            for record in cur1.fetchall():
                                temp = int(record['id'])
                                if temp == ctx.message.author.id:
                                    catch = True
                                    if record['guild'] == guild["name"]:
                                        await ctx.send("You are verified and have not changed guilds")
                                    else:
                                        temp2 = "'" + player["uuid"] + "'"
                                        delete_script = f'DELETE FROM verified WHERE uuid={temp2}'
                                        cur.execute(delete_script)
                                        conn.commit()
                                        insert_values = (ctx.message.author.id, player["uuid"], guild["name"])
                                        cur.execute(insert_script, insert_values)
                                        conn.commit()
                            if not catch:
                                insert_values = (ctx.message.author.id, player["uuid"], guild["name"])
                                cur.execute(insert_script, insert_values)
                                conn.commit()
                            cur.close()
                            conn.close()
                            rolecheck = discord.utils.get(ctx.guild.roles, name="Council")
                            if rolecheck in ctx.author.roles:
                                await ctx.send(f'I cannot change your nick due to insufficient permissions')
                            else:
                                await member.edit(nick=player["username"])
                            if guild["name"] == "SB Iota Theta":
                                await ctx.send("Iota Theta is being closed for remodel. Please join another guild "
                                               "by opening ticket in <#803383229906157600>")

                            await ctx.send(
                                f'{ctx.author.mention} is now a verified guild member with ign {player["username"]}')
                        else:
                            await ctx.send("You are not in the guild")
                            member = ctx.message.author
                            role = get(member.guild.roles, name="Verified")
                            await member.add_roles(role)
                            await ctx.send("You are now verified without guild member role.")
                    else:
                        await ctx.send("Connect your discord and try again, or maybe you're just not in the guild",
                                       )

    @commands.command(description="Add the role if in guild")
    async def unverify(self, ctx):

        conn = psycopg2.connect(
            host=hostname,
            dbname=database,
            user=username,
            password=pwd,
            port=port_id)
        cur = conn.cursor()
        cur1 = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
        cur1.execute('SELECT * FROM VERIFIED')
        catch = False
        member = ctx.message.author
        for record in cur1.fetchall():
            temp = int(record['id'])
            if temp == ctx.message.author.id:
                catch = True
                uuid = record['uuid']
                async with aiohttp.ClientSession() as session:
                    async with session.get(f'https://api.slothpixel.me/api/players/{uuid}') as resp:
                        player = await resp.json()
                    async with session.get(f'https://api.slothpixel.me/api/guilds/{uuid}') as resp:
                        guild = await resp.json()
                temp3 = "'" + str(ctx.message.author.id) + "'"
                delete_script = f'DELETE FROM verified WHERE id={temp3}'
                cur.execute(delete_script)
                conn.commit()
                cur.close()
                conn.close()
                role = get(member.guild.roles, name="Verified")
                role1 = get(member.guild.roles, name="Guild Member")
                guildrole = guild["name"] + " Member"
                if player["rank"] == "MVP_PLUS":
                    rankrole = get(member.guild.roles, name="MVP+")
                    await member.remove_roles(rankrole)
                elif player["rank"] == "MVP_PLUS_PLUS":
                    rankrole = get(member.guild.roles, name="MVP++")
                    await member.remove_roles(rankrole)
                elif player["rank"] == "VIP":
                    rankrole = get(member.guild.roles, name="VIP")
                    await member.remove_roles(rankrole)
                elif player["rank"] == "VIP_PLUS":
                    rankrole = get(member.guild.roles, name="VIP+")
                    await member.remove_roles(rankrole)
                elif player["rank"] == "MVP":
                    rankrole = get(member.guild.roles, name="MVP")
                    await member.remove_roles(rankrole)

                await member.remove_roles(role)
                if guild["name"] in ["SB Lambda Pi", "SB Theta Tau", "SB Delta Omega", "SB Iota Theta",
                                     "SB Uni", "SB Rho Xi", "SB Kappa Eta", "SB Alpha Psi"]:
                    if guild["name"] in ["SB Lambda Pi", "SB Theta Tau", "SB Delta Omega", "SB Iota Theta",
                                         "SB Rho Xi", "SB Kappa Eta", "SB Alpha Psi","SB Masters"]:
                        guildrole = guild["name"] + " Member"
                    elif guild["name"] == "SB Uni":
                        guildrole = "SB University Member"
                    role2 = get(member.guild.roles, name=guildrole)
                    await member.remove_roles(role2)
                    await member.remove_roles(role1)

        for role1 in ["SB Lambda Pi Member", "SB Theta Tau Member", "SB Delta Omega Member",
                      "SB Iota Theta Member",
                      "SB University Member", "SB Rho Xi Member", "SB Kappa Eta Member", "SB Alpha Psi Member"
            , "Verified"]:
            role = discord.utils.get(ctx.guild.roles, name=role1)
            if role in member.roles:
                await member.remove_roles(role)
        id = ctx.message.author.id
        await ctx.send(f"<@{id}> has been unverified.")


def setup(bot):
    bot.add_cog(Verify(bot))