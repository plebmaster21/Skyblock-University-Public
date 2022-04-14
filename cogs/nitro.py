import discord
from discord.ext import commands
from discord import utils
import os
import asyncio
import aiohttp


class NQNcog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def nqn(self, ctx):
        await ctx.send('Pong!')

    async def getemote(self, arg):
        emoji = utils.get(self.bot.emojis, name=arg.strip(":"))
        if emoji is None:
            return
        if emoji.animated:
            add = "a"
        else:
            add = ""
        return f"<{add}:{emoji.name}:{emoji.id}>"

    async def getinstr(self, content):
        ret = []

        spc = content.split(" ")
        cnt = content.split(":")
        if len(cnt) > 1:
            for item in spc:
                if item.count(":") > 1:
                    wr = ""
                    if item.startswith("<") and item.endswith(">"):
                        ret.append(item)
                    else:
                        cnt = 0
                        for i in item:
                            if cnt == 2:
                                aaa = wr.replace(" ", "")
                                ret.append(aaa)
                                wr = ""
                                cnt = 0
                            if i != ":":
                                wr += i
                            else:
                                if wr == "" or cnt == 1:
                                    wr += " : "
                                    cnt += 1
                                else:
                                    aaa = wr.replace(" ", "")
                                    wr = ":"
                                    cnt = 1
                        aaa = wr.replace(" ", "")
                        ret.append(aaa)
                else:
                    ret.append(item)
        else:
            return content
        return ret

    @commands.Cog.listener()
    async def on_message(self, message):
        role = discord.utils.get(message.guild.roles, name="Active")
        if role in message.author.roles:
            pass
        else:
            return
        if message.channel.id != 765420497747050506:
            return
        if message.author.bot:
            return
        if ":" in message.content:
            msg = await self.getinstr(message.content)
            ret = " "
            em = False
            smth = message.content.split(":")
            if len(smth) > 1:
                for word in msg:
                    if word.startswith(":") and word.endswith(":"):
                        emoji = await self.getemote(word)
                        if emoji is not None:
                            em = True
                            ret += f" {emoji}"
                        else:
                            ret += f" {word}"
                    else:
                        ret += f" {word}"
            else:
                ret += msg

            if em:
                channel = message.channel
                webhooks = await message.channel.webhooks()
                webhook = utils.get(webhooks, name="NQN")
                if webhook is None:
                    webhook = await channel.create_webhook(name="NQN")

                if message.reference is not None:
                    message2 = await channel.fetch_message(
                        message.reference.message_id)
                    embed = discord.Embed(
                        description=
                        f'**[Reply to:]({message2.jump_url}) {message2.content}**',
                        colour=0x00FF6600)
                    embed.set_footer(text=f'ID: {message2.author.id}')

                    embed.set_author(name=f"{message2.author.name}",
                                     )
                    await webhook.send(ret,
                                       username=message.author.display_name,
                                       avatar_url=message.author.avatar,
                                       embed=embed)
                else:
                    await webhook.send(ret,
                                       username=message.author.display_name,
                                       avatar_url=message.author.avatar
                                       )
                await message.delete()


def setup(bot):
    bot.add_cog(NQNcog(bot))
