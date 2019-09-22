import discord,json,random,os
from discord.ext import commands
from core.classes import Cog_Extension

with open('setting.json','r',encoding='utf8') as jfile:
    jdata = json.load(jfile)

class Event(Cog_Extension):

    @commands.Cog.listener()
    async def on_member_join(self, member):
        channel = self.bot.get_channel(int(jdata['WELCOME_POST']))
        await channel.send(f'{member} welcome!')

    @commands.Cog.listener()
    async def on_member_remove(self, member):
        channel = self.bot.get_channel(int(jdata['WELCOME_POST']))
        await channel.send(f'{member} R.I.P.')

    @commands.Cog.listener()
    async def on_message(self, msg):
        if msg.content.endswith('w') and msg.author != self.bot.user:
            await msg.channel.send('wwwwwwww')
        elif msg.mentions:
            if msg.mentions[0] == self.bot.user:
                await msg.channel.send(random.choice(jdata['TAG_BOT']))


def setup(bot):
    bot.add_cog(Event(bot))