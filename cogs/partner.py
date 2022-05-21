import asyncio

import discord
from discord.ext import commands

taskforce = """
𝐖𝐞 𝐨𝐟𝐟𝐞𝐫:

➥ a friendly and helpful Hypixel Skyblock / Bedwars Community
➥ Giveaways worth at least 1 million sb coins
➥ a lot of Roles to collect
➥ purchasable Donator Ranks with many perks
➥ a place to advertise both Auctions and Trades
➥ a custom SB Server
➥ Voice Channels for Bed Wars Partys and Dungeon Team Ups 

All those things and much more is waiting for You! Join now!"""
TheSkyblockHub = """
Hey there,
I'm sure, you all know hundreds of Hypixel Skyblock Discord Servers, so why should you join another one?
The answer is simple, The Skyblock Hub is not just a Community Server like all the other servers, it's a tool, a tool to make your Skyblock adventures the best!

We've got a lot of features, like
checking Stats, Skills, Items and Entchantments,
lookup the Skyblock Events,
get notified with the Patchnotes,
participate at awesome Giveaways,
hear some Music,
read many available Guides,
do some Trades with other members,
ask for Crafts or advertise your Auctions,
and if you need help, just ask our Support.
All of this and much more, you'll find in our Server!"""
SkyblockCove = """A great growing community with great goals focusing all around Hypixel Skyblock!

Benefits of joining:
🎊 Biweekly Giveaways, ranging from 1m-10m!
🤑 Regular Events, including Puzzles and Riddles!
🎅 Amazing Staff Members who are Super Active!
🧑‍🤝‍🧑 Great Community with Friendly Users!
🤖 Channels and Bots"""
sfs = """
Welcome to Silent's Free Services!
---------------------------------------------------------------------------------------------------------------
What do we offer?
----------------------------------------------------------------------------------------------------------------
:pogchimp: FREE F1-F6 Dungeon Carries and FREE F7 AND MASTER MODE 1-3 COMPLETION
----------------------------------------------------------------------------------------------------------------
:Carpentry: FREE crafting services, with collateral as an option
----------------------------------------------------------------------------------------------------------------
🐲  FREE Summoning Eye placing, so you can get better drops from dragons
----------------------------------------------------------------------------------------------------------------
:tada: Giveaways at least once per week
----------------------------------------------------------------------------------------------------------------
"""
sfs2 = """:crossed_swords: FREE slayer carries! T5s might be tricky for one person, but why else do we have a community?
---------------------------------------------------------------------------------------------------------------
:wowfox: Contribution rewards for helping others. For the welfare of the community!
----------------------------------------------------------------------------------------------------------------
✨ Anyone can create a giveaway. Feel like it? Make a ticket and contribute to the community!
----------------------------------------------------------------------------------------------------------------
Want to join the server and getting offered FREE services? Then go join our Discord server!"""

paradise = """The Paradise Network is a Skyblock Discord with a focus on the community, Skyblock services and bringing a great experience to our members.  We offer one of the widest selections for services out of all SB servers, we offer great staff and moderation, and we consistently work to make your experience a great one!

Join us today to experience the Paradise difference!
"""

sbl = """WELCOME TO SBL

We have:

—> DAILY 1 MIL GIVEAWAYS
—> cool and active community based on Hypixel Skyblock
—> partnerships with low requirements
—> active and motivated staff team
—> cheap donator ranks with really cool perks
—> free steam games which would normally cost $2-$20
—> Dungeon Carry Services
—> proof channel to show we are going 100% legit
—> over 1/3 of a Billion coins given away
"""

larimar = """- Fun, non-toxic community!
- Giveaways(Hypixel SkyBlock)!
- Dungeons(Hypixel SkyBlock)!
- Dungeon Carries(Hypixel SkyBlock)!
- Gonna turn into a general Hypixel Server and Skyblock Server!
- Much more!"""

forumsweats = """The best Hypixel forums* server
Features:
- otty
- ratio
- epicduckiecousin
- ratio
- too much trolling
- sykese left
- sued by donpireso
- banned on forums
- among us
- rembutquaglet wrong clock formatting
- ratio
- clash of clans clan
- otty
- matdoesdev

*not actually allowed on forums"""

dragonsden = """Welcome to Dragon's Den.

Established in 2019, we started as a home for Hypixel Skyblock players to find new friends and groups to play video games with. Over the years, we are still committed to helping spread the joy of Skyblock to everyone, and have many community features to offer!

We feature giveaways, advice, trading, bot functions, events, and even feature a place for you to have fun on other video games when you need a break from Hypixel! 

See you there!"""

plun = """Hello! We are partnering with Aether Network, the new and improved SBL/ Carry Service. 

About Us

Aether Network is a Minecraft centred server based on SkyBlock, Hypixel game modes, and Minecraft gameplay. 

Originally as a Hypixel Skyblock server, we offer dungeon carry services and coin giveaways! After branching out, we offer a custom-coded SMP, guild events, pvp tournaments, and other sorts of nitro and prize giveaways!

Interested? Join Today!"""

stellular = """:tools: **Stellular **

**A little bit about us: ─━═༻ **
◈  Looking for a friendly discord server? Well, you're in great luck! Stellular is a discord server open to the community! 
◈ Stellular is a growing community and will be full of activities and events, and the community will be as nice as it can get.

**What we offer: ─━═༻**
◈ :moneybag: Weekly giveaways for prizes such as Skyblock coins, nitro, ranks, and cosmetics!
◈ :calendar: Regular events for a chance to win prizes! 
◈ :robot: Tons of popular Discord bots to use!
◈ :scream: A Hypixel guild with 50+ Levels 
◈ :smiley: Partnerships with other servers 
◈ :heart: An active non-toxic community! 

**Our details ─━═༻**
:flag_white: Banner: https://share.creavite.co/CBnEStefegN5hB8W.gif
:red_circle: Pings:"""


class Partner(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def partner(self, ctx):
        if ctx.message.author.id in [462940637595959296, 438529479355400194, 397389995113185293, 665885831856128001]:
            partnership = discord.Embed(
                title=f'Stellular',
                description='',
                colour=discord.Colour.dark_gray()
            )
            skykings = """
SkyKings is a guild networth of 9 guilds, with many activities!

:money_with_wings: Regular Giveaways!
:crossed_swords: Active Events!
:shield: 9 Guilds!
:robot: SkyKings Bots

Join today! """
            partnership.set_footer(text='SBU Partners')
            partnership.add_field(name="\u200b", value=f"{stellular}", inline=False)
            await ctx.send(embed=partnership)
            temp = f"Discord Invite: https://discord.gg/stellular"
            await ctx.send(temp)


def setup(bot):
    bot.add_cog(Partner(bot))
