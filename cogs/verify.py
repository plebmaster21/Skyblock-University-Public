import asyncio
import discord
import psycopg2
import psycopg2.extras
from discord.ext import commands, tasks
from discord.utils import get
import requests
import os
import sqlite3


hostname = 'localhost'
database = 'SBU'
username = 'postgres'
pwd = 'obbytrusty'
port_id = 5432



class Verify(commands.Cog):
    def __init__(self, bot):
        self.index = 0
        self.bot = bot
        self.checkverification.start()
        
    def cog_unload(self):
        self.checkverification.cancel()
    
    @tasks.loop(hours=24)
    async def checkverification(self):
        conn = sqlite3.connect('verify.db')
        c = conn.cursor()
        c.execute('SELECT * FROM VERIFIED')
        values = c.fetchall()
        
        
        
    @checkverification.before_loop
    async def before_checkverification(self):
        await self.bot.wait_until_ready()
        
    @commands.Cog.listener()
    async def on_ready(self):
        conn = sqlite3.connect('verify.db')
        c = conn.cursor()   
        c.execute("""CREATE TABLE IF NOT EXISTS verified (
            discordid integer,
            uuid text,
            guild text
        )""")
        conn.commit()
        conn.close()
        print(f'SQLite Verification databases initialized')
    
    @commands.command(description="Add the role if in guild")
    async def verify(self, ctx, arg1: str = None):
        key = os.getenv("apikey")
        if arg1 is None:
            embed = discord.Embed(title=f'Error', description='Please enter a user \n `+verify ObbyTrusty`',
                                colour=0xFF0000)
            await ctx.reply(embed=embed)
            return
        member = ctx.message.author
        tempvar = "Attempt to verify: " + str(ctx.message.author)
        print(tempvar)
        response = requests.get(f'https://api.mojang.com/users/profiles/minecraft/{arg1}')
        try:
            uuid = response.json()['id']
            print(uuid)
        except KeyError as e:
            print(e)
            embed = discord.Embed(title=f'Error',
                                description='Error fetching information from the API. Recheck the spelling of your '
                                            'IGN',
                                colour=0xFF0000)
            await ctx.reply(embed=embed)
            return
        for role1 in ["SB Lambda Pi Member", "SB Theta Tau Member", "SB Delta Omega Member", "SB Iota Theta Member",
                    "SB University Member", "SB Rho Xi Member", "SB Kappa Eta Member", "SB Alpha Psi Member",
                    "SB Masters Member"]:

            role = discord.utils.get(ctx.guild.roles, name=role1)
            if role in member.roles:
                await member.remove_roles(role)
        response = requests.get(f'https://api.hypixel.net/player?key={key}&uuid={uuid}')
        if response.status_code != 200:
            embed = discord.Embed(title=f'Error',
                                description='Error fetching information from the API. Try again later',
                                colour=0xFF0000)
            await ctx.reply(embed=embed)
            return
        player = response.json()
        response = requests.get(f'https://api.hypixel.net/guild?key={key}&player={uuid}')
        guild = response.json()
        check = False
        try:
            if player['player']['socialMedia']['links']['DISCORD'] == str(ctx.author):
                pass
            else:
                embed = discord.Embed(title=f'Error',
                                    description='The discord linked with your hypixel account is not the same as '
                                                'the one you are trying to verify with. \n You can connect your '
                                                'discord following https://youtu.be/6ZXaZ-chzWI',
                                    colour=0xFF0000)
                await ctx.reply(embed=embed)
                return
        except KeyError:
            embed = discord.Embed(title=f'Error',
                                description='The discord linked with your hypixel account is not the same as '
                                            'the one you are trying to verify with. \n You can connect your '
                                            'discord following https://youtu.be/6ZXaZ-chzWI',
                                colour=0xFF0000)
            await ctx.reply(embed=embed)
            return
        insertguild = None
        temptest = False
        try:
            if guild["guild"]["name"] in ["SB Lambda Pi", "SB Theta Tau", "SB Delta Omega", "SB Iota Theta",
                                        "SB Uni", "SB Rho Xi", "SB Kappa Eta", "SB Alpha Psi", "SB Masters"]:
                pass
        except:
            temptest = True
            embed = discord.Embed(title=f'Verification',
                                description='You are not in any of the SBU guilds. You are now verified without '
                                            'the guild member roles.',
                                colour=0x800080)
            pass
        if temptest:
            pass
        else:
            if guild["guild"]["name"] in ["SB Lambda Pi", "SB Theta Tau", "SB Delta Omega", "SB Iota Theta",
                                    "SB Uni", "SB Rho Xi", "SB Kappa Eta", "SB Alpha Psi", "SB Masters"]:
                check = True
                insertguild = guild["guild"]["name"]
                pass
            else:
                embed = discord.Embed(title=f'Verification',
                                        description='You are not in any of the SBU guilds. You are now verified without '
                                                    'the guild member roles.',
                                        colour=0x800080)
            temp = False
            if guild["guild"]["name"] == "SB Uni":
                temp = True
                guildrole = "SB University Member"
                embed = discord.Embed(title=f'Verification',
                                        description=f'You have been verified as a member of {guild["guild"]["name"]}',
                                        colour=0x008000)
            if check and temp != True:
                embed = discord.Embed(title=f'Verification',
                                    description=f'You have been verified as a member of {guild["guild"]["name"]}',
                                    colour=0x008000)
                guildrole = guild["guild"]["name"] + " Member"
        conn = psycopg2.connect(
            host=hostname,
            dbname=database,
            user=username,
            password=pwd,
            port=port_id)
        cur = conn.cursor()
        role = get(member.guild.roles, name="Verified")
        role1 = get(member.guild.roles, name="Guild Member")
        if check:
            role2 = get(member.guild.roles, name=guildrole)
            await member.add_roles(role1)
            await member.add_roles(role2)
        await member.add_roles(role)

        deleteid = "'" + str(ctx.author.id) + "'"
        delete_script = f'DELETE FROM verified WHERE id={deleteid}'
        cur.execute(delete_script)
        conn.commit()
        insert_values = (ctx.message.author.id, uuid, insertguild)
        cur.execute(insert_script, insert_values)
        conn.commit()
        try:
            await member.edit(nick=player['player']["displayname"])
        except:
            embed.add_field(name="Nickname:", value="Unable to edit nickname.")
        member = ctx.message.author
        role = get(member.guild.roles, name="Verified")
        await member.add_roles(role)
        await ctx.reply(embed=embed)

    @commands.command()
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
        member = ctx.message.author
        for role1 in ["SB Lambda Pi Member", "SB Theta Tau Member", "SB Delta Omega Member",
                    "SB Iota Theta Member",
                    "SB University Member", "SB Rho Xi Member", "SB Kappa Eta Member", "SB Alpha Psi Member",
                    "SB Masters Member", "Verified", "MVP", "MVP+", "MVP++", "VIP", "VIP+", "Guild Member"]:
            role = discord.utils.get(ctx.guild.roles, name=role1)
            if role in member.roles:
                await member.remove_roles(role)
        for record in cur1.fetchall():
            temp = int(record['id'])
            if temp == ctx.message.author.id:
                temp3 = "'" + str(ctx.message.author.id) + "'"
                delete_script = f'DELETE FROM verified WHERE id={temp3}'
                cur.execute(delete_script)
                conn.commit()
                cur.close()
                conn.close()
        embed = discord.Embed(title=f'Verification',
                            description=f'You have been unverified.',
                            colour=0x008000)
        await ctx.reply(embed=embed)

    @commands.command()
    async def cleanup(self, ctx):
        embed = discord.Embed(title=f'Processing',
                            description=f'This message will be edited once it has completed running',
                            colour=0x008000)
        message = await ctx.reply(embed=embed)
        conn = psycopg2.connect(
            host=hostname,
            dbname=database,
            user=username,
            password=pwd,
            port=port_id)
        cur1 = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
        cur1.execute('SELECT * FROM VERIFIED')
        role1 = get(ctx.guild.roles, name="Guild Member")
        role2 = get(ctx.guild.roles, name="SB Lambda Pi Member")
        role3 = get(ctx.guild.roles, name="SB Theta Tau Member")
        role4 = get(ctx.guild.roles, name="SB Delta Omega Member")
        role5 = get(ctx.guild.roles, name="SB Iota Theta Member")
        role6 = get(ctx.guild.roles, name="SB University Member")
        role7 = get(ctx.guild.roles, name="SB Rho Xi Member")
        role8 = get(ctx.guild.roles, name="SB Kappa Eta Member")
        role9 = get(ctx.guild.roles, name="SB Alpha Psi Member")
        role0 = get(ctx.guild.roles, name="SB Masters Member")
        currentlyverified = []
        for record in cur1.fetchall():
            currentlyverified.append(int(record['id']))
        print(currentlyverified)
        for user in ctx.guild.members:
            if user.id in currentlyverified:
                print(user)
                print("True")
            else:
                if role1 in user.roles:
                    await user.remove_roles(role1)
                if role2 in user.roles:
                    await user.remove_roles(role2)
                if role3 in user.roles:
                    await user.remove_roles(role3)
                if role4 in user.roles:
                    await user.remove_roles(role4)
                if role5 in user.roles:
                    await user.remove_roles(role5)
                if role6 in user.roles:
                    await user.remove_roles(role6)
                if role7 in user.roles:
                    await user.remove_roles(role7)
                if role8 in user.roles:
                    await user.remove_roles(role8)
                if role9 in user.roles:
                    await user.remove_roles(role9)
                if role0 in user.roles:
                    await user.remove_roles(role0)
        embed = discord.Embed(title=f'Completed',
                              description=f'Task Completed Successfully',
                              colour=0x008000)
        await message.edit(embed=embed)
        cur1.close()
        conn.close()


def setup(bot):
    bot.add_cog(Verify(bot))

