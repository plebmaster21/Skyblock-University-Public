import asyncio

import discord
from discord.ext import commands
from discord.utils import get


class Raid(commands.Cog, name="raid command"):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases=['raid'])
    @commands.has_role("Junior Administrator")
    @commands.cooldown(1, 60, commands.BucketType.guild)
    async def crisis(self, ctx):
        lockdown_channels = ["general-chat", "irl-help", "birthdays", "masters-general"
            , "sb-masters-bridge", "masters-bot-commands", "masters-general"
            , "bot-commands", "verify", "count-to-59mil", "sb-uni-bridge"
            , "alpha-psi-bridge", "kappa-eta-bridge", "delta-omega-bridge"
            , "lambda-pi-bridge", "theta-tau-bridge", "rho-xi-bridge"
            , "skyblock-help-1", "skyblock-help-2", "crafting-and-reforge-assistance"
            , "essence-trading", "item-lending", "trades-and-auctions", "rep-commands"
            , "self-advertising", "smp-chat", "community-bulletin-board", "party-finder"]
        await ctx.send(":lock: Crisis mode activated. Putting channels under lockdown.")
        for channel in ctx.guild.channels:
            if channel.name in lockdown_channels:
                if ctx.guild.default_role not in channel.overwrites:
                    overwrites = {
                        ctx.guild.default_role: discord.PermissionOverwrite(send_messages=False)
                    }
                    await channel.edit(overwrites=overwrites)
                elif channel.overwrites[ctx.guild.default_role].send_messages == True or channel.overwrites[
                    ctx.guild.default_role].send_messages is None:
                    overwrites = channel.overwrites[ctx.guild.default_role]
                    overwrites.send_messages = False
                    await channel.set_permissions(ctx.guild.default_role, overwrite=overwrites)
            await asyncio.sleep(0.1)
        length = len(lockdown_channels)

        await ctx.send(f":lock: Lockdown completed, {length} channels locked.")
        channel = get(ctx.guild.channels, name="mod-action-log")
        author = str(ctx.message.author.id)
        log1 = discord.Embed(
            title='Moderation Log',
            description='',
            colour=discord.Colour.light_gray()
        )
        log1.set_footer(text='mhm SBU bot')
        log1.add_field(name="Moderator", value="<@" + author + ">", inline=True)
        log1.add_field(name="Action", value='Server lockdown', inline=False)
        await channel.send(embed=log1)
        channel = get(ctx.guild.channels, name="admin-chat")
        raidmode = discord.Embed(
            title='Raid Mode Information',
            description='Administration information for SBU CRISIS Mode',
            colour=discord.Colour.red()
        )
        raidmode.set_footer(text='WEEWOO CRISIS MODE')
        raidmode.add_field(name="Command ran by", value=f":lock: <@{author}>", inline=False)
        raidmode.add_field(name="How many channels locked", value=f"{length}", inline=False)
        raidmode.add_field(name="Errors locking Channels", value=f"None", inline=False)
        await channel.send(embed=raidmode)

    @crisis.error
    async def check_error(self, ctx, error):
        if isinstance(error, commands.MissingRole):
            await ctx.send("Insufficient Permissions")
        elif isinstance(error, commands.CommandOnCooldown):
            await ctx.send(error)

    @commands.command(aliases=['raidend'])
    @commands.has_role("Administrator")
    @commands.cooldown(1, 60, commands.BucketType.guild)
    async def crisisend(self, ctx):
        lockdown_channels = ["general-chat", "irl-help", "birthdays", "masters-general"
            , "sb-masters-bridge", "masters-bot-commands", "masters-general"
            , "bot-commands", "verify", "count-to-59mil", "sb-uni-bridge"
            , "alpha-psi-bridge", "kappa-eta-bridge", "delta-omega-bridge"
            , "lambda-pi-bridge", "theta-tau-bridge", "rho-xi-bridge"
            , "skyblock-help-1", "skyblock-help-2", "crafting-and-reforge-assistance"
            , "essence-trading", "item-lending", "trades-and-auctions", "rep-commands"
            , "self-advertising", "smp-chat", "community-bulletin-board", "party-finder"]
        await ctx.send(":unlock: Crisis mode ended. Remove channels from under lockdown.")
        for channel in ctx.guild.channels:
            if channel.name in lockdown_channels:
                if channel.overwrites[ctx.guild.default_role].send_messages == True or channel.overwrites[
                    ctx.guild.default_role].send_messages is None:
                    overwrites = channel.overwrites[ctx.guild.default_role]
                    overwrites.send_messages = True
                    await channel.set_permissions(ctx.guild.default_role, overwrite=overwrites)
            await asyncio.sleep(0.1)
        length = len(lockdown_channels)
        await ctx.send(f":unlock: Lockdown end completed, {length} channels unlocked.")
        channel = get(ctx.guild.channels, name="mod-action-log")
        author = str(ctx.message.author.id)
        log1 = discord.Embed(
            title='Moderation Log',
            description='',
            colour=discord.Colour.light_gray()
        )
        log1.set_footer(text='mhm SBU bot')
        log1.add_field(name="Moderator", value="<@" + author + ">", inline=True)
        log1.add_field(name="Action", value='Server lockdown Remove', inline=False)
        channel = get(ctx.guild.channels, name="admin-chat")
        raidmode = discord.Embed(
            title='Raid Mode Information',
            description='Administration information for SBU CRISIS Mode',
            colour=discord.Colour.red()
        )
        raidmode.set_footer(text='WEEWOO CRISIS MODE')
        raidmode.add_field(name="Command ran by", value=f":unlock: <@{author}>", inline=False)
        raidmode.add_field(name="How many channels unlocked", value=f"{length}", inline=False)
        raidmode.add_field(name="Errors unlocking Channels", value=f"None", inline=False)
        await channel.send(embed=raidmode)


    @crisisend.error
    async def check_error(self, ctx, error):
        if isinstance(error, commands.MissingRole):
            await ctx.send("Insufficient Permissions")
        elif isinstance(error, commands.CommandOnCooldown):
            await ctx.send(error)


def setup(bot):
    bot.add_cog(Raid(bot))
