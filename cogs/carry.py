import discord
from discord.ext import commands
import json


class Reputations(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def repgive(self, ctx, member: discord.Member, *, reason):
        if ctx.author.id == member.id:
            await ctx.send("You can't rep yourself.")
            return
        with open('reputation.json') as fp:
            listObj = json.load(fp)
        num1 = len(listObj) + 1
        count = 0

        for value in range(len(listObj)):
            if listObj[value]["repgiven"] == member.id:
                count = count + 1
        count = count + 1
        repembed = discord.Embed(
            title=f'Reputation Given',
            description=f'Reason: {reason}',
            colour=0x8F49EA
        )
        repembed.set_author(name=f'Reputation by {ctx.message.author}', icon_url=f'{ctx.author.avatar}')
        repembed.set_footer(text=f'Global reputation number {num1} | Reputation Number {count} for {member}')
        repembed.set_thumbnail(
            url="https://cdn.discordapp.com/avatars/937099605265485936/8a5d786e369fdda9f355f12eaf0487fb.png?size=4096")
        message = await ctx.send(embed=repembed)
        await ctx.send(f"Reputation added for {member}")
        data = {
            "number": num1,
            "messageid": message.id,
            "reason": reason,
            "authorid": ctx.author.id,
            "repgiven": member.id
        }
        listvar = list(listObj)
        listvar.append(data)

        with open('reputation.json', 'w') as json_file:
            json.dump(listvar, json_file,
                      indent=4,
                      separators=(',', ': '))

    @repgive.error
    async def repgive_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send("Incorrect format. Use `+repgive @mention Reason`")


def setup(bot):
    bot.add_cog(Reputations(bot))
