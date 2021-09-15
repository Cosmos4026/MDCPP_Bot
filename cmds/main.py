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

    @commands.command()
    async def sayd(self, ctx, *, msg):
        await ctx.message.delete()
        await ctx.send(msg)

def setup(bot):
    bot.add_cog(Main(bot))
