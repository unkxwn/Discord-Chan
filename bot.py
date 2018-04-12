# i need this stuff
import discord
from discord.ext import commands
from discord.ext.commands import Bot
import asyncio
import random
import datetime
import requests

bot = commands.Bot(command_prefix="?")
client = discord.Client

#config stuff

@bot.event
async def on_ready():
    print("I'm ready")
    print("My ID is: " + bot.user.id)
    print("Mah name is: " + bot.user.name)

@bot.event
async def on_ready():
    Game = discord.Game
    await bot.change_presence(game=Game(name="lmao"))


#commands

@bot.command(pass_context=True)
async def ping(ctx):
    await bot.say(":ping_pong: Pong!")

@bot.command(pass_context=True)
async def anime(ctx):
    animes = ["Zenkyou no Terror", "Another", "Blend S", "Corpse Party: Tortured Souls", "Sword Art Online", "Accel World", "High School DxD","Euphoria","Steins; Gate", "Higurashi no Naku Koro Ni", "Tokyo Ghoul", "Hinako Note", "Boku no Pico,"]
    await bot.say(random.choice(animes))

@bot.command(pass_context=True)
async def time(ctx):
    await bot.say("Date of year: " + datetime.date.today().strftime("%j"))

@bot.command(pass_context=True)
async def info(ctx, user: discord.Member):
    embed = discord.Embed(title="{}'s info".format(user.name), description="Here's what I could find.", color=0x00ff00)
    embed.add_field(name="Name", value=user.name, inline=True)
    embed.add_field(name="ID", value=user.id, inline=True)
    embed.add_field(name="Status", value=user.status, inline=True)
    embed.add_field(name="Joined", value=user.joined_at)
    embed.set_thumbnail(url=user.avatar_url)
    await bot.say(embed=embed)


@bot.command(pass_context=True)
async def serverinfo(ctx):
    embed = discord.Embed(title="{}'s info".format(ctx.message.server.name), description="Here's what I could find", color=0x00ff00)
    embed.add_field(name="Server's name", value=ctx.message.server.name, inline=True)
    embed.add_field(name="Server's ID", value=ctx.message.server.id, inline=True)
    embed.add_field(name="Server's roles", value=len(ctx.message.server.roles), inline=True)
    embed.add_field(name="Server's members", value=len(ctx.message.server.members))
    embed.set_thumbnail(url=ctx.message.server.icon_url)
    await bot.say(embed=embed)

@bot.command(pass_context=True)
@commands.has_role("Admin")
async def ban(ctx, user: discord.Member):
    await bot.say("{} sucessfully banned.".format(user.name))
    await bot.ban(user)
    if user == message.author:
        await bot.say("You can't ban yourself!")

@bot.command(pass_context=True)
@commands.has_role("Admin")
async def kick(ctx, user: discord.Member):
    await bot.say("{} sucessfully kicked.".format(user.name))
    await bot.kick(user)

@bot.command(pass_context=True)
async def bitcoin(ctx):
    url = "https://api.coindesk.com/v1/bpi/currentprice/BTC.json"
    request = requests.get(url)
    value = request.json() ["bpi"] ["USD"] ["rate"]
    await bot.say("Bitcoin value is: $" + value)

    
    
    
                  

    
bot.run("NDAxMDc1ODg2MjA1NDM1OTA0.Daqxzg.ax2KBNqlEBDpuW1ZHOrIsxliAKo")
