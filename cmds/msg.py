import discord,json,random,os
from discord.ext import commands
from core.classes import Cog_Extension

class Msg(Cog_Extension):

    @commands.command()
    async def Car(self, ctx):
        rand=str(random.randint(1,257))
        for i in range(3-len(rand)):
            rand='0'+rand
        path = jdata['Pic_Path']+rand+".jpg"
        if os.path.isfile(path):
            pic = discord.File(path)
        else:
            pic = discord.File(jdata['Pic_Path']+rand+".png")
        await ctx.send(file = pic)
    
    @commands.command()
    async def say(self, ctx):
        await ctx.send('我的開發者終於讓我說話了')

    @commands.command()
    async def yes(self, ctx):
        await ctx.send('Yes! Yes! Yes!')

def setup(bot):
    bot.add_cog(Msg(bot))