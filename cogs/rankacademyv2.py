import discord
from discord.ext import commands
from discord.utils import get
from discord.ui import Button, View

class RAV2(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
        
    @commands.command()
    async def rank(self, ctx):
        button = Button(
            label='Click Me!',
            style=discord.ButtonStyle.green,
            emoji='<:thonk:810579524735205377>'
        )
        embed = discord.Embed(
            title=f'Rank Academy',
            description=f'Thank you for creating a Rank Academy Ticket! \n I am SBU bot and I will be your guide today. \n Click the button to get started',
            timestamp=ctx.message.created_at,
            colour=0x8F49EA
        )
        embed.set_footer(text=f'Skyblock University Rank Academy')
        embed.set_thumbnail(
            url="https://cdn.discordapp.com/avatars/937099605265485936/8a5d786e369fdda9f355f12eaf0487fb.png?size=4096")
        
        async def endingcallback(interaction):
            await ctx.send('<@&801634222577156097>')
            await interaction.respond('Begining Testing Now')
        
        async def kindnesscallback(interaction):
            button = Button(
            label='Click Me!',
            style=discord.ButtonStyle.green,
            emoji='<:thonk:810579524735205377>'
            )
            kindness = """This academy is an incredibly important piece to how we survive as a guild and server. Our staff need to also be helpful and kind. People that are found being catty or otherwise rude will be stripped of their ranks and reduced to Freshmen moving forward.

We aren't here to berate confused newcomers into submission by calling them worthless nons and promoting how big and strong we are. The sole purpose of our server and guilds are to help new and mid-game players learn how to play skyblock. Holding yourself above another player due to how much weight, networth, etc you have has absolutely no place here. The idea that you treat others this way needs to be smashed from here on if you wish to have a rank in this server.

If you would consider our guild like a college campus, our general chat being our open area where people can congregate, our help channels are like our classrooms, and our tutoring sessions are just that. We are a school here, and where we absolutely do like to have fun, there is still a bit of professionalism that we need to show to the new and confused members of our community. With new members we need to remember that we were new too at one point in time and didn't have all the information or know where to go. We must put ourselves back in their shoes to treat them with kindness and respect all humans deserve.

If you feel yourself getting short with someone, irritated or angry - don't fret! We have plenty of other people who would love to help and take your place. Just step back for a minute and let someone else take over.

If you are helping someone that is just asking for free things from you over and over again, please be sure to report beggars to our mod team, so we may handle these situations individually.
"""
            embed = discord.Embed(
                title=f'Example 4',
                description=kindness,
                timestamp=ctx.message.created_at,
                colour=0x8F49EA
            )
            embed.set_footer(text=f'Skyblock University Rank Academy')
            embed.set_thumbnail(
            url="https://cdn.discordapp.com/avatars/937099605265485936/8a5d786e369fdda9f355f12eaf0487fb.png?size=4096")
            view = View()
            view.add_item(button)
            button.callback=endingcallback
            await interaction.response.send_message(embed=embed, view=view)
        
        async def example4callback(interaction):
            button = Button(
            label='Click Me!',
            style=discord.ButtonStyle.green,
            emoji='<:thonk:810579524735205377>'
            )
            example ="""
Sopheee is upset you “told on” her by reporting her to staff. She's DMing you telling you how horrible you are for ruining their fun.

This is plain harassment and is not tolerated. Please let us know if you're every harassed publicly or privately by another member in our server or guilds and we will be sure to handle them immediately. We want everyone to feel safe on our server. You will need to take and submit screenshots with your report.
"""
            embed = discord.Embed(
                title=f'Example 4',
                description=example,
                timestamp=ctx.message.created_at,
                colour=0x8F49EA
            )
            embed.set_footer(text=f'Skyblock University Rank Academy')
            embed.set_thumbnail(
            url="https://cdn.discordapp.com/avatars/937099605265485936/8a5d786e369fdda9f355f12eaf0487fb.png?size=4096")
            view = View()
            view.add_item(button)
            button.callback=kindnesscallback
            await interaction.response.send_message(embed=embed, view=view)
        
        async def example3callback(interaction):
            button = Button(
            label='Click Me!',
            style=discord.ButtonStyle.green,
            emoji='<:thonk:810579524735205377>'
            )
            example ="""Sopheee, Randy67, and Bobby555 are all getting a bit rowdy. They start to turn to making “deez nuts” jokes to each other. Sopheee sets all the jokes up, and Bobby555 is saying the punchline to each joke.

We don't allow “deez nuts” jokes in our guilds or on our discord. Usually these jokes are harmful to the welcoming environment that we're trying to create, plus they're considered “Not Safe for Work” or NSFW and therefore not allowed. Everyone involved in making the jokes and egging others on to make these actions would warrant needing to be reported. You will need to take and submit screenshots with your report.
"""
            embed = discord.Embed(
                title=f'Example 3',
                description=example,
                timestamp=ctx.message.created_at,
                colour=0x8F49EA
            )
            embed.set_footer(text=f'Skyblock University Rank Academy')
            embed.set_thumbnail(
            url="https://cdn.discordapp.com/avatars/937099605265485936/8a5d786e369fdda9f355f12eaf0487fb.png?size=4096")
            view = View()
            view.add_item(button)
            button.callback=example4callback
            await interaction.response.send_message(embed=embed, view=view)
            
        async def example2callback(interaction):
            button = Button(
            label='Click Me!',
            style=discord.ButtonStyle.green,
            emoji='<:thonk:810579524735205377>'
            )
            example ="""Georgina32 and Bobby555 have been talking about drugs for a few minutes, both of them are just simply naming drugs one after another. This started because Bobby555 said he needed more drugs for his dungeon runs(referring to Potions).

Because Mojang's ToS states the game is for ages 10 and above, we don't allow talk of illicit substances or likewise, due to the player base being so young. These actions would warrant a report, even if Georgina32 and Bobby555 have already stopped talking about drugs. You will need to take and submit screenshots with your report.
"""
            embed = discord.Embed(
                title=f'Example 2',
                description=example,
                timestamp=ctx.message.created_at,
                colour=0x8F49EA
            )
            embed.set_footer(text=f'Skyblock University Rank Academy')
            embed.set_thumbnail(
            url="https://cdn.discordapp.com/avatars/937099605265485936/8a5d786e369fdda9f355f12eaf0487fb.png?size=4096")
            view = View()
            view.add_item(button)
            button.callback=example3callback
            await interaction.response.send_message(embed=embed, view=view)
            
        async def example1callback(interaction):
            button = Button(
            label='Click Me!',
            style=discord.ButtonStyle.green,
            emoji='<:thonk:810579524735205377>'
            )
            example ="""
Bobby531 recently joined the guild and is asking for a Hyperion for free, then saying they're just kidding right afterwards. They have repeated this behavior a few times in the past.

It's never fun to be nagged by guild members for free things. We have “No Begging” in our rules and believe everyone should know that they can be in our guild without 10 people harassing them, asking for free things. Regardless if someone says “just kidding” right after, it's still annoying to have to deal with on a regular basis, and we don't want to have to force our members ignore these issues or /ignore add the beggar. Handling them right away by reporting them is the best and fastest way to get someone to stop doing an undesirable behavior."""
            embed = discord.Embed(
                title=f'Example 1',
                description=example,
                timestamp=ctx.message.created_at,
                colour=0x8F49EA
            )
            embed.set_footer(text=f'Skyblock University Rank Academy')
            embed.set_thumbnail(
            url="https://cdn.discordapp.com/avatars/937099605265485936/8a5d786e369fdda9f355f12eaf0487fb.png?size=4096")
            view = View()
            view.add_item(button)
            button.callback=example2callback
            await interaction.response.send_message(embed=embed, view=view)
        
        async def reportcallback(interaction):
            button = Button(
            label='Click Me!',
            style=discord.ButtonStyle.green,
            emoji='<:thonk:810579524735205377>'
            )
            report = """
                Here at Skyblock University, we believe each and every person deserves to feel comfortable in our guild. However, this does not mean that we allow individuals to bully or treat others poorly in our guilds and server. Unfortunately, our moderation team cannot be everywhere at once, so we need to rely on our Seniors and Instructors to tell us when someone has taken an action that has disturbed them or otherwise made them uncomfortable.
                Here's a few examples of potential rule breaking that's reportable:
                ```Begging  \nTalking about drugs   \nTalking about sexually related things (including "deez nuts" jokes)   \nSpamming chat with caps, or fast messages with little in it \nPromoting rule breaking or leading people to break rules \nHacking```
                This list is not exhaustive, but should give you an idea of some of the things that we don't allow. You can find a full list of our rules in rules \nIf you find someone doing these actions in game you can report them to our moderation team by opening a “report a user” ticket in <#765927458314387498>. Please be sure to include screenshots of everything you are reporting. \nOur lack of knowledge of these situations happening may turn into people thinking we tolerate bad behavior. This is not our intention or what we wish to show new members. The more people report, the more aware we are of people who make everyone else unhappy, the faster we can remove excessively disruptive people and make our guilds and server more comfortable for everyone. You will be our front line in making our server safe for both current and new members.
                """
            embed = discord.Embed(
                title=f'How to Report',
                description=report,
                timestamp=ctx.message.created_at,
                colour=0x8F49EA
            )
            embed.set_footer(text=f'Skyblock University Rank Academy')
            embed.set_thumbnail(
            url="https://cdn.discordapp.com/avatars/937099605265485936/8a5d786e369fdda9f355f12eaf0487fb.png?size=4096")
            view = View()
            view.add_item(button)
            button.callback=example1callback
            await interaction.response.send_message(embed=embed, view=view)
        
        async def seniorcallback(interaction):
            button = Button(
            label='Click Me!',
            style=discord.ButtonStyle.green,
            emoji='<:thonk:810579524735205377>'
            )
            senior = """
                Seniors are required to have 350+ weight. Use the bot command `/weight` to show you have enough weight for this rank before continuing, if you haven't already.

                This rank requires you to:
                Report disruptive people
                Understand when to report
                Be generally helpful, kind, and welcoming to all

                This Academy has two sections.
                **Report Guide** - How and when to report someone to our staff that is breaking our rules
                **Kindness Academy** - How to be generally helpful, kind, and welcoming to all
                """
            view = View()
            view.add_item(button)
            button.callback=reportcallback
            embed = discord.Embed(
                title=f'Rank Academy Senior',
                description=senior,
                timestamp=ctx.message.created_at,
                colour=0x8F49EA
            )
            embed.set_footer(text=f'Skyblock University Rank Academy')
            embed.set_thumbnail(
            url="https://cdn.discordapp.com/avatars/937099605265485936/8a5d786e369fdda9f355f12eaf0487fb.png?size=4096")
            await interaction.response.send_message(embed=embed, view=view)

        async def instrcallback(interaction):
            instrplus = """
                `Instructors, Professors, Deans and Provost` are required to have 700+, 2100+, 4200+ and 8400+  weight respectively.
                > Report disruptive people
                > Understand when to report 
                > Check people as they request to join our guild
                > Be available to answer questions in tutoring tickets
                > Be generally helpful, kind, and welcoming to all.

                **This Academy has four sections.**
                **Report Guide** - How and when to report someone to our staff that is breaking our rules
                **Kindness Academy** - How to be generally helpful, kind, and welcoming to all
                **Guild Checking Academy** - How to check if people are on our <#830188559964307526> or on a scammer list
                **Tutoring Academy** - What tutoring tickets are and how to act in them

                After you are done reading, you will be tested with several open answer questions to make sure you understand what was covered. You may ask questions before testing.
            """
            embed = discord.Embed(
            title=f'Rank Academy Instructor+',
            description=instrplus,
            timestamp=ctx.message.created_at,
            colour=0x8F49EA
            )
            embed.set_footer(text=f'Skyblock University Rank Academy')
            embed.set_thumbnail(
            url="https://cdn.discordapp.com/avatars/937099605265485936/8a5d786e369fdda9f355f12eaf0487fb.png?size=4096")
            view = View()
            view.add_item(button)
            button.callback=reportcallback
            await interaction.response.send_message(embed=embed, view=view)
            
        async def button_callback(interaction):
            button = Button(
            label='Senior',
            style=discord.ButtonStyle.green
            )
            button1 = Button(
            label='Instructor',
            style=discord.ButtonStyle.blurple
            )
            view = View()
            view.add_item(button)
            view.add_item(button1)
            button.callback = seniorcallback
            button1.callback = instrcallback
            embed = discord.Embed(
            title=f'Rank Academy',
            description=f'Please run /weight. \nIf you have 350 weight or less click on senior. \nIf you have 700 weight or more click on Instructor.',
            timestamp=ctx.message.created_at,
            colour=0x8F49EA
            )
            embed.set_footer(text=f'Skyblock University Rank Academy')
            embed.set_thumbnail(
            url="https://cdn.discordapp.com/avatars/937099605265485936/8a5d786e369fdda9f355f12eaf0487fb.png?size=4096")
            await interaction.response.send_message(embed=embed, view=view)
        button.callback = button_callback
        view = View()
        view.add_item(button)
        await ctx.send(embed=embed, view=view)


        
def setup(bot):
    bot.add_cog(RAV2(bot))
