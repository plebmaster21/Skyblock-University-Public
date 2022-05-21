import discord
import discord.utils
import os
import random
from discord.ext import commands
from dotenv import load_dotenv
import aiohttp
import asyncio

# noinspection SpellCheckingInspection
intents = discord.Intents.all()
bot = commands.Bot(command_prefix="-", intents=intents)
bot.remove_command('help')


@bot.event
async def on_ready():
    print(f"{bot.user} is ready")


@bot.command()
async def load(ctx, extension):
    if ctx.message.author.id in [462940637595959296, 438529479355400194, 397389995113185293, 665885831856128001]:
        bot.load_extension(f'cogs.{extension}')
        await ctx.reply("Loaded")
    else:
        await ctx.send("Insufficient permissions, only bot owners can run this command")


@bot.command()
@commands.has_permissions(ban_members=True)
async def unload(ctx, extension):
    if ctx.message.author.id in [462940637595959296, 438529479355400194, 397389995113185293, 665885831856128001]:
        bot.unload_extension(f'cogs.{extension}')
        await ctx.reply("Unloaded")
    else:
        await ctx.send("Insufficient permissions, only bot owners can run this command")


for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        bot.load_extension(f'cogs.{filename[:-3]}')


@bot.command()
async def reload(ctx):
    if ctx.message.author.id in [462940637595959296, 438529479355400194, 397389995113185293, 665885831856128001]:
        for filename1 in os.listdir('./cogs'):
            if filename1.endswith('.py'):
                bot.unload_extension(f'cogs.{filename1[:-3]}')

        for filename1 in os.listdir('./cogs'):
            if filename1.endswith('.py'):
                bot.load_extension(f'cogs.{filename1[:-3]}')
        await ctx.reply("All cogs reloaded")
    else:
        await ctx.send("Insufficient permissions, only bot owners can run this command")


# noinspection SpellCheckingInspection
@bot.command()
async def ping(ctx):
    await ctx.send(f'Pong! {round(bot.latency * 1000)} ms')


@bot.command()
async def help(ctx):
    embed = discord.Embed(
        title='Help',
        description='All the help commands are listed below',
        colour=discord.Colour.red()
    )
    embed.set_footer(text='SBU Custom Bot')
    embed.add_field(name="ping", value="Pong!", inline=False)
    embed.add_field(name="verify", value="Link your discord and hypixel accounts", inline=False)
    embed.add_field(name="unverify", value="UnLink your discord and hypixel accounts", inline=False)
    embed.add_field(name="hypixel", value="Lists hypixel stats", inline=False)
    embed.add_field(name="checkreq", value="Check if you meet reqs for SB Masters \n `+checkreq IGN`", inline=False)
    embed.add_field(name="repgive", value="Give a reputation for a carry \n `+repgive @mention Reason`", inline=False)
    embed.add_field(name="suggest", value="Suggest something \n `+suggest Suggestion`", inline=False)
    await ctx.send(embed=embed)


@bot.command()
@commands.has_role("Junior Moderator")
async def modhelp(ctx):
    embed = discord.Embed(
        title='Moderation Commands',
        description='All the moderation commands are listed below',
        colour=discord.Colour.red()
    )
    embed.set_footer(text='SBU Custom Bot')
    embed.add_field(name="ban", value="`+ban User Reason`", inline=False)
    embed.add_field(name="mute", value="`+mute User Time Reason`", inline=False)
    embed.add_field(name="unmute", value="`+unmute User Reason`", inline=False)
    embed.add_field(name="Lookup section for Rank Academy ", value="`+lookupsection`", inline=False)
    embed.add_field(name="Shortened questions for promo for Instr and higher", value="`+ras`", inline=False)
    embed.add_field(name="Add a banned member to banned list", value="`+banlist IGN`", inline=False)
    embed.add_field(name="Activate SBU's Crisis Mode", value="`+crisis`", inline=False)
    embed.add_field(name="Deactivate SBU's Crisis Mode", value="`+crisisend`", inline=False)

    await ctx.send(embed=embed)


@bot.command()
async def dm(ctx, member: discord.Member, *, message: str):
    if ctx.message.author.id in [462940637595959296, 438529479355400194, 397389995113185293, 665885831856128001]:
        await member.send(message)
        await ctx.send("User Dmed")
    else:
        await ctx.send("Insufficient permissions, only bot owners can run this command")


@bot.event
async def on_message(message):
    if message.content.upper() == "MEOW":
        if message.author.id in [397389995113185293, 462940637595959296, 438529479355400194]:
            await message.reply("Meow")
    elif message.content.upper() == "MEOWO":
        if message.author.id in [397389995113185293, 462940637595959296]:
            await message.reply("UwU meow")
    elif message.content.upper() == "FLOP":
        if message.author.id in [615987518890049555, 462940637595959296]:
            list = ["<:turtlefire:945023173353697320>", "Fleee", "All hail King Flop"]
            randommessage = random.sample(range(0, len(list)), 1)
            await message.reply(list[randommessage[0]])
    elif message.content.upper() == "PINGU":
        if message.author.id in [381494697073573899, 462940637595959296]:
            list = ["<:poguin:933279319579561986>", "<a:pingupat:932962348908560417>", "UwU"]
            randommessage = random.sample(range(0, len(list)), 1)
            await message.reply(list[randommessage[0]])
    elif message.content.upper() == "MELON":
        if message.author.id in [438529479355400194, 798500372993933332]:
            await message.reply("ily ash (wyvtrusty best)")
    elif message.content.upper() == "JACK":
        if message.author.id in [358670711109320705, 462940637595959296, 397389995113185293, 438529479355400194]:
            await message.reply("Go play <@909802667495268372> in <#910961553480765440>")
    elif message.content.upper() == "NEO":
        if message.author.id in [566329261535920175]:
            await message.reply("op")
    elif message.content.upper() == "OBBY":
        if message.author.id in [699769343344377916]:
            await message.reply(
                "https://cdn.discordapp.com/attachments/910303971187507210/954606327970295828/unknown.png")
    elif message.content.upper() == "WYVTRUSTY":
        if message.author.id in [699769343344377916, 462940637595959296]:
            list = ["https://cdn.discordapp.com/attachments/910303971187507210/954606120255758386/unknown.png",
                    "https://cdn.discordapp.com/attachments/910303971187507210/954606120528408616/unknown.png",
                    "https://cdn.discordapp.com/attachments/910303971187507210/954606120876523520/unknown.png",
                    "https://cdn.discordapp.com/attachments/910303971187507210/954606121157529610/unknown.png",
                    "https://cdn.discordapp.com/attachments/910303971187507210/954606121467932712/unknown.png",
                    "https://cdn.discordapp.com/attachments/910303971187507210/954606121761521714/unknown.png",
                    "https://cdn.discordapp.com/attachments/910303971187507210/954606121971224646/unknown.png",
                    "https://cdn.discordapp.com/attachments/910303971187507210/954606122172579870/unknown.png",
                    "https://cdn.discordapp.com/attachments/910303971187507210/954606122390679602/unknown.png",
                    "https://cdn.discordapp.com/attachments/910303971187507210/954606122575212554/unknown.png",
                    "https://cdn.discordapp.com/attachments/910303971187507210/954606208453574686/unknown.png",
                    "https://cdn.discordapp.com/attachments/910303971187507210/954606208713633802/unknown.png",
                    "https://cdn.discordapp.com/attachments/910303971187507210/954606208894001162/unknown.png",
                    "https://cdn.discordapp.com/attachments/910303971187507210/954606209237917696/unknown.png",
                    "https://cdn.discordapp.com/attachments/910303971187507210/954606209535721492/unknown.png",
                    "https://cdn.discordapp.com/attachments/910303971187507210/954606209929982002/unknown.png",
                    "https://cdn.discordapp.com/attachments/910303971187507210/954606210269741066/unknown.png"]
            randommessage = random.sample(range(0, len(list)), 1)
            await message.reply(list[randommessage[0]])
    elif message.content.upper() == "SLOGO":
        if message.author.id in [354741702004703242]:
            await message.reply("Op Ironman")
    elif message.content.upper() == "WINDOW":
        if message.author.id in [797274543042986024]:
            await message.reply("Door")
    elif message.content.upper() == "PLEB":
        if message.author.id in [519985798393626634, 462940637595959296]:
            await message.reply("shitting on the bw gamers.")
    elif message.content.upper() == "FOOD":
        if message.author.id in [606917358438580224]:
            await message.reply("no")
            await message.delete()
    elif message.content.upper() == "THUNDXR":
        if message.author.id in [694604709591384226]:
            list = ["huh?",
                    "stop annoying me smh",
                    "bad at coding",
                    "good at coding",
                    "edited me",
                    "hacks ppl hehe",
                    "stop looking at me",
                    "is hot",
                    "is nice",
                    "what?",
                    "ITHUNDXR!!!!!",
                    "IThundxr",
                    "why?",
                    "Grinds alot",
                    "where?",
                    "HOW?",
                    "no",
                    "no.",
                    "NO",
                    "No.",
                    "shut up",
                    "codes alot",
                    "Minecraft.",
                    "oooh you found the special response that does legit nothing. cool?",
                    "wow",
                    "is ~~kinda~~ very mean",
                    "lol"]
            randommessage = random.sample(range(0, len(list)), 1)
            await message.reply(list[randommessage[0]])
    await bot.process_commands(message)


"""@bot.event
async def updatemember():
    await bot.wait_until_ready()

    while not bot.is_closed():
        vc = [945493379599446056,945493468539654205,945493492434604072,945493508398153808
                  ,945493526047776889,945493540748791899,945493556909473812,945493573263040522]
        guilds = ["6111fcb48ea8c95240436c57", "604a765e8ea8c962f2bb3b7a",
                  "607a0d7c8ea8c9c0ff983976", "608d91e98ea8c9925cdb91b7",
                "60a16b088ea8c9bb7f6d9052", "60b923478ea8c9a3aefbf3dd", "6125800e8ea8c92e1833e851",
                  "570940fb0cf2d37483e106b3"]
        total_members = 0
        for i in range(len(guilds)):
            async with aiohttp.ClientSession() as session:
                async with session.get(f'https://api.slothpixel.me/api/guilds/id/{guilds[i]}') as resp:
                    guildrename = await resp.json()
            rename = guildrename["name"] + ": " + str(len(guildrename["members"]))
            total_members = total_members + int(len(guildrename["members"]))
            vc1 = bot.get_channel(vc[i])
            await vc1.edit(name=rename)
        vc2 = bot.get_channel(890288776302190602)
        rename1 = "Guild members: " + str(total_members)
        await vc2.edit(name=rename1)
        channel = bot.get_channel(946591422616838264)
        await channel.send(f"Guild Stats VC Updated")
        print("Updated")
        await asyncio.sleep(1800)

bot.loop.create_task(updatemember())"""
# noinspection SpellCheckingInspection

load_dotenv()
bot.run(os.getenv("TOKEN"))
