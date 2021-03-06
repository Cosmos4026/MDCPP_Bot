import discord
from discord.ext import commands
from core.classes import Cog_Extension
import json

with open('setting.json', 'r', encoding='utf8') as jfile:
    jdata = json.load(jfile)


class Roles(Cog_Extension):
    @commands.Cog.listener()
    async def on_member_join(self, member):
        channel = self.bot.get_channel(int(jdata['join_ch']))
        await channel.send(f'{member} 偷偷溜進來了')


    @commands.Cog.listener()
    async def on_member_remove(self, member):
        channel = self.bot.get_channel(int(jdata['leave_ch']))
        await channel.send(f'{member} 打開門走出去了')
        
    @commands.Cog.listener()
    async def on_reaction_add(self, reaction, user):
        print(reaction)

    @commands.Cog.listener()
    async def on_raw_reaction_add(self, data):
        
        if data.channel_id == int(jdata['role_ch']):
            if str(data.emoji) == '<:cat_A:885532118300639284>':
                guild = self.bot.get_guild(data.guild_id)
                role = guild.get_role(int(jdata['roleA_ID']))
                await data.member.add_roles(role)

            if str(data.emoji) == '<:cat_B:885532165419442247>':
                guild = self.bot.get_guild(data.guild_id)
                role = guild.get_role(int(jdata['roleB_ID']))
                await data.member.add_roles(role)

            if str(data.emoji) == '<:cat_C:885532297779085372>':
                guild = self.bot.get_guild(data.guild_id)
                role = guild.get_role(int(jdata['roleC_ID']))
                await data.member.add_roles(role)

            if str(data.emoji) == '<:doge:885532360324558868>':
                guild = self.bot.get_guild(data.guild_id)
                role = guild.get_role(int(jdata['roleD_ID']))
                await data.member.add_roles(role)

    @commands.Cog.listener()
    async def on_raw_reaction_remove(self, data):
        if data.channel_id == int(jdata['role_ch']):
            if str(data.emoji) == '<:cat_A:885532118300639284>':
                guild = self.bot.get_guild(data.guild_id)
                user = guild.get_member(data.user_id)
                role = guild.get_role(int(jdata['roleA_ID']))
                await user.remove_roles(role)

            if str(data.emoji) == '<:cat_B:885532165419442247>':
                guild = self.bot.get_guild(data.guild_id)
                user = guild.get_member(data.user_id)
                role = guild.get_role(int(jdata['roleB_ID']))
                await user.remove_roles(role)
            
            if str(data.emoji) == '<:cat_C:885532297779085372>':
                guild = self.bot.get_guild(data.guild_id)
                user = guild.get_member(data.user_id)
                role = guild.get_role(int(jdata['roleC_ID']))
                await user.remove_roles(role)

            if str(data.emoji) == '<:doge:885532360324558868>':
                guild = self.bot.get_guild(data.guild_id)
                user = guild.get_member(data.user_id)
                role = guild.get_role(int(jdata['roleD_ID']))
                await user.remove_roles(role)


def setup(bot):
    bot.add_cog(Roles(bot))
