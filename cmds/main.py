import discord
from discord.ext import commands
from discord.ext.commands.core import command
from core.classes import Cog_Extension
import datetime
import time

class Main(Cog_Extension):

    @commands.command()
    async def ping(self, ctx):
        pin = round( 1000 * self.bot.latency )
        await ctx.send(f'現在的延遲是{pin}ms左右')

    """@commands.command()
    async def em(self,ctx):
        embed=discord.Embed(title="About", url="https://www.youtube.com/watch?v=dQw4w9WgXcQ", description="沒梗了。", color=0xffff00, timestamp=datetime.datetime.now())
        embed.set_author(name="Cosmos", url="https://www.youtube.com/watch?v=dQw4w9WgXcQ", icon_url="https://imgur.com/BbEvSxv")
        embed.set_thumbnail(url="https://imgur.com/a/JfDv5KT")
        embed.add_field(name="1", value="沒東西", inline=True)
        embed.add_field(name="2", value="沒東西", inline=True)
        embed.add_field(name="3", value="沒東西", inline=True)
        embed.add_field(name="4", value="沒東西", inline=True)
        embed.set_footer(text=datetime.datetime.now().strftime('%Y %m %d %H %M'))
        await ctx.send(embed=embed)"""
    
    @commands.command()
    async def sayd(self, ctx, *, msg):
        await ctx.message.delete()
        await ctx.send(msg)

    @commands.command()
    async def clean(self, ctx, num : int, pswd):
        if pswd == 'conf1rm':
            await ctx.message.delete()
            await ctx.send('5秒後刪除訊息')
            time.sleep(5)
            await ctx.channel.purge(limit=num+1)
        else:
            await ctx.send('密碼不對')

def setup(bot):
    bot.add_cog(Main(bot))