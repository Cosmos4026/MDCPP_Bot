import discord
from discord.ext import commands
import json
import random
from dotenv import load_dotenv
import os
import keep_alive

load_dotenv('.env')

with open('setting.json', 'r', encoding='utf8') as jfile:
    jdata = json.load(jfile)

intents = discord.Intents.default()
intents.members = True

bot = commands.Bot(command_prefix='m!', intents = intents)

@bot.event
async def on_ready():
    print("M寶 一款真正人性化的智障語音")
    channel = bot.get_channel(int(jdata['bot_online']))
    await channel.send('bot is online :D')

@bot.command()
async def load(ctx, extension):
    bot.load_extension(f'cmds.{extension}')
    await ctx.send(f'{extension} successfully loaded')

@bot.command()
async def unload(ctx, extension):
    bot.unload_extension(f'cmds.{extension}')
    await ctx.send(f'{extension} successfully unloaded')

@bot.command()
async def reload(ctx, extension):
    bot.reload_extension(f'cmds.{extension}')
    await ctx.send(f'{extension} successfully reloaded')

for filename in os.listdir('./cmds'):
    if filename.endswith('.py'):
        bot.load_extension(f'cmds.{filename[:-3]}')



if __name__ == "__main__":
    #keep_alive.keep_alive()
    bot.run(os.getenv('BOT_TOKEN'))
