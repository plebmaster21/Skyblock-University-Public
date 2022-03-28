import discord
import psycopg2
import psycopg2.extras
from discord.ext import commands
from discord.utils import get
import requests

hostname = 'localhost'
database = 'SBU'
username = 'postgres'
pwd = 'obbytrusty'
port_id = 5432

insert_script = 'INSERT INTO VERIFIED (id, uuid, guild) VALUES (%s, %s, %s)'


class Verify(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(description="Add the role if in guild")
    async def verify(self, ctx, arg1: str = None):
        if arg1 is None:
            embed = discord.Embed(title=f'Error', description='Please enter a user \n `+verify ObbyTrusty`',
                                  colour=0xFF0000)
            await ctx.reply(embed=embed)
            return
        member = ctx.message.author
        tempvar = "Attempt to verify: " + str(ctx.message.author)
        print(tempvar)
        for role1 in ["SB Lambda Pi Member", "SB Theta Tau Member", "SB Delta Omega Member", "SB Iota Theta Member",
                      "SB University Member", "SB Rho Xi Member", "SB Kappa Eta Member", "SB Alpha Psi Member",
                      "SB Masters Member"]:
            role = discord.utils.get(ctx.guild.roles, name=role1)
            if role in member.roles:
                await member.remove_roles(role)
        response = requests.get(f'https://api.slothpixel.me/api/players/{arg1}')
        if response.status_code != 200:
            embed = discord.Embed(title=f'Error',
                                      description='Error fetching information from the API. Try again later',
                                      colour=0xFF0000)
            await ctx.reply(embed=embed)
            return
        player = response.json()
        response = requests.get(f'https://api.slothpixel.me/api/guilds/{arg1}')
        guild = response.json()
        if response.status_code != 200 and guild["guild"] is not None:
            embed = discord.Embed(title=f'Error',
                                      description='Error fetching information from the API. Try again later',
                                      colour=0xFF0000)
            await ctx.reply(embed=embed)
            return
        if player['links']['DISCORD'] == str(ctx.author):
            pass
        else:
            embed = discord.Embed(title=f'Error',
                                      description='The discord linked with your hypixel account is not the same as '
                                                  'the one you are trying to verify with. \n You can connect your '
                                                  'discord following https://youtu.be/6ZXaZ-chzWI',
                                      colour=0xFF0000)
            await ctx.reply(embed=embed)
            return
        if guild["name"] in ["SB Lambda Pi", "SB Theta Tau", "SB Delta Omega", "SB Iota Theta",
                                 "SB Uni", "SB Rho Xi", "SB Kappa Eta", "SB Alpha Psi", "SB Masters"]:
            pass
        else:
            embed = discord.Embed(title=f'Verification',
                                      description='You are not in any of the SBU guilds. You are now verified without '
                                                  'the guild member roles.',
                                      colour=0x800080)
        if guild["name"] == "SB Uni":
            guildrole = "SB University Member"
            embed = discord.Embed(title=f'Verification',
                                      description=f'You have been verified as a member of {guild["name"]}',
                                      colour=0x008000)
        else:
            embed = discord.Embed(title=f'Verification',
                                      description=f'You have been verified as a member of {guild["name"]}',
                                      colour=0x008000)
            guildrole = guild["name"] + " Member"
        conn = psycopg2.connect(
            host=hostname,
            dbname=database,
            user=username,
            password=pwd,
            port=port_id)
        cur = conn.cursor()
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
        deleteid = "'" + str(ctx.author.id) + "'"
        delete_script = f'DELETE FROM verified WHERE id={deleteid}'
        cur.execute(delete_script)
        conn.commit()
        insert_values = (ctx.message.author.id, player["uuid"], guild["name"])
        cur.execute(insert_script, insert_values)
        conn.commit()
        try:
            await member.edit(nick=player["username"])
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
        for record in cur1.fetchall():
            temp = int(record['id'])
            if temp == ctx.message.author.id:
                for role1 in ["SB Lambda Pi Member", "SB Theta Tau Member", "SB Delta Omega Member",
                              "SB Iota Theta Member",
                              "SB University Member", "SB Rho Xi Member", "SB Kappa Eta Member", "SB Alpha Psi Member",
                              "SB Masters Member", "Verified", "MVP", "MVP+", "MVP++", "VIP", "VIP+", "Guild Member"]:
                    role = discord.utils.get(ctx.guild.roles, name=role1)
                    if role in member.roles:
                        await member.remove_roles(role)
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


def setup(bot):
    bot.add_cog(Verify(bot))
