import discord
from discord.ext import commands

import random
import asyncio

import aiohttp
import json
import http

import time
import os

from discord import Game
from discord.ext.commands import Bot


bot = commands.Bot(command_prefix=".")

@bot.event
async def on_ready():
	print('Looged in', bot.user.name, bot.user.id, 'Powered by Team-NKVV.Coders')
	print('Hosted using Heroku')
	print('Aythor - PrabaRock7#3945')
	print('Version - 1.0.2')
	await bot.change_presence(status=discord.Status.online, activity=discord.Game(name="ProdigyBot on v1.0.2"))

async def on_member_join(self, member):
        guild = member.guild
        if guild.system_channel is not None:
            to_send = 'Welcome {0.mention} to {1.name}!'.format(member, guild)
            await guild.system_channel.send(to_send)
            
            
@bot.event
async def on_message(message):
 
    if message.content == ".botinfo":
        embed = discord.Embed(title="About ProdigyBot", description="Show info about bot")
        embed.set_thumbnail(url="https://i.imgur.com/Xq4QOU8.png")
        embed.set_author(name="PrabaRock7", url="https://i.imgur.com/nmnNL5c.png")
        embed.add_field(name="About Bot",
value="Hello, Im ProdigyBot, My Owner is PrabaRock7#3945, Support him on [Patreon](https://patreon.com/PrabaRock7) I can make you happy, kicks the bad user, bans the baddiest user, show info about you in discord, astrology")
        embed.add_field(name="Thanks to", value="**Team NKVV Coders for supporting me, Thank you my frnds AjProCoder, VickRock1py, DarshanCodingAlways**")
        embed.add_field(name="Author/Ceator", value="PrabaRock7#3945, AjProCoder, VickRock1py, DarshanCodingAlways")
        embed.add_field(name="Bot Links", value="[Patreon](https://patreon.com/PrabaRock7), [GitHub](https://github.com/b0tdev/ProdigyBot), [Support Server](https://discord.gg/V8RT3pp)")
        await message.channel.send(content=None, embed=embed)
            
@bot.command()
async def start(ctx):
	message = await ctx.send("Starting...")
	await message.edit(content='Started Prodigy Bot Successfully in your Server' + ", " + ctx.message.guild.name)

@bot.command()
async def ping(ctx, name="ping", description="Shows the Bot Latency m/s", hidden=False):
    start = time.perf_counter()
    message = await ctx.send("Ping...")
    end = time.perf_counter()
    duration = (end - start) * 1000
    await message.edit(content='Latency is! {:.2f}ms'.format(duration))
   
@bot.command()
async def kick(ctx, member:discord.User = None, reason = None):
    if member == None or member == ctx.message.author:
        await ctx.channel.send("You cannot kick yourself!")
        return
    if reason == None:
        reason = "No reason at all!"
    message = f"You have been kicked from {ctx.guild.name} for {reason}!"
    await member.send(message)
    await ctx.guild.kick(member)
    await ctx.channel.send(f"{member} is kicked!")

@bot.command()
async def ban(ctx, member:discord.User = None, reason = None):
    if member == None or member == ctx.message.author:
        await ctx.channel.send("You cannot ban yourself!")
        return
    if reason == None:
        reason = "No reason at all!"
    message = f"You have been banned from {ctx.guild.name} for {reason}!"
    await member.send(message)
    await ctx.guild.ban(member)
    await ctx.channel.send(f"{member} is banned!")
    
@bot.command(name="owncommand", description="Your Own Command", hidden=False) #set hidden to True to hide it in the help
async def owncommand(ctx, argument1, argument2):
    '''OwnCommamd is your own commamd
    
    Usage example:
    !owncommand hi 1
    '''
    await ctx.send(f"Got {argument1} and {argument2}")
    
@bot.command(name="hello", description="Returns hi", hidden=False)
async def hello(ctx):
	await ctx.send("Hi :wave:")
	
@bot.command()
async def invitelink(ctx):
	await ctx.send("https://discordapp.com/api/oauth2/authorize?client_id=599893675962531851&permissions=8&scope=bot")
	
@bot.command()
async def supportserver(ctx):
	await ctx.send("https://discordapp.com/invite/V8RT3pp")
	
@bot.command()
async def gitrepo(ctx):
	await ctx.send("**Note Please Dont use it as Self-Host Purpose. if we found using our bot instance we will take action on you.** Repo - https://github.com/b0tdev/ProdigyBot-Repo")
	
@bot.command()
async def premium(ctx):
	await ctx.send(":lock: Premium feature is not unlocked yet, but will")
	
@bot.command(hidden=True)
async def thanks(ctx):
	await ctx.send("Thanks To - discord.py API Refernce, Courtesy - AjCoder, Team - N.K.V.V.Coders, Aythor - PrabaRock7#3945, Version-1.0.0")

@bot.command()
async def iwanttodm(ctx):
	await ctx.send("Dm My Owner <@589647651939549206>")
	
@bot.command()
async def astrology(ctx):
	possible_responces = [
	       'You are good',
	       'You are Bad',
	       'You are Unlucky',
	       'You are Lucky',
	       'You soon have a crush :wink:',
	       'You are Beautiful',
	       'You are Adorable',
	       'You are Ghost',
	]
	await ctx.send(random.choice(possible_responces) + ", " + ctx.message.author.mention)
	
@bot.command()
async def square(ctx, number):
    squared_value = int(number) * int(number)
    await ctx.send(str(number) + " squared is " + str(squared_value))
    
@bot.command()
async def bitcoin(ctx):
    url = 'https://api.coindesk.com/v1/bpi/currentprice/BTC.json'
    async with aiohttp.ClientSession() as session:  # Async HTTP request
        raw_response = await session.get(url)
        response = await raw_response.text()
        response = json.loads(response)
        await ctx.send("Bitcoin price is: $" + response['bpi']['USD']['rate'])
        
@bot.command()
async def user(ctx, member:discord.User = None):
    if member == None:
        member = ctx.message.author
        pronoun = "Your"
    else:
        pronoun = "Their"
    name = f"{member.name}#{member.discriminator}"
    status = member.status
    joined = member.joined_at
    role = member.top_role
    await ctx.channel.send(f"{pronoun} name is {name}. {pronoun} status is {status}. They joined at {joined}. {pronoun} rank is {role}.")
    
bot.run(os.getenv("TOKEN"))
