import discord
from discord.ext import commands
import random
import asyncio
import time

bot = commands.Bot(command_prefix='.')

@bot.event
async def on_ready():
	print('Looged in', bot.user.name, bot.user.id, 'Powered by Team-NKVV.Coders')
	print('Hosted using Heroku')
	print('Aythor - PrabaRock7#3945')
	print('Version - 1.0.0')
	
async def on_member_join(self, member):
        guild = member.guild
        if guild.system_channel is not None:
            to_send = 'Welcome {0.mention} to {1.name}!'.format(member, guild)
            await guild.system_channel.send(to_send)
            
@bot.command()
async def start(ctx):
	message = await ctx.send("Starting...")
	await message.edit(content='Started Prodigy Bot Successfully.')

@bot.command()
async def ping(ctx, name="ping", description="Shows the Bot Latency m/s", hidden=False):
    start = time.perf_counter()
    message = await ctx.send("Ping...")
    end = time.perf_counter()
    duration = (end - start) * 1000
    await message.edit(content='Latency is! {:.2f}ms'.format(duration))
    
@bot.command(name="kick", description="Kicks the User", hidden=False)
async def kick(ctx, user:
discord.Member):
    await ctx.send(" {} Has been kicked!".format(user.mention))
    await user.send("You have been kicked from {}.".format(ctx.guild.name))
    await user.kick()
    
@bot.command()
async def ban(ctx, user:
discord.Member):
	await ctx.send("{} Has Been Banned!".format(user.mention))
	await user.send("You Have been Banned from {}.".format(ctx.guild.name))
	await user.ban()
	
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
async def wtf(ctx):
	await ctx.send("shhh! No bad words.Strictly")
	
@bot.command()
async def funnyimage(ctx):
	await ctx.send("https://imgur.com/VlHE2nl")
	
@bot.command()
async def ownerinfo(ctx):
	await ctx.send("**About Me, Im PrabaRock7#3945(aka :- b0tdev#3945)basically im a Python Basic Coder. I love discord and making discord bots. I made this bot under supersitions :wink:. Support Me on : [Patreon](https://www.patreon.com/PrabaRock7). (c)PrabaRock7**")
	
@bot.command()
async def invitelink(ctx):
	await ctx.send("https://discordapp.com/api/oauth2/authorize?client_id=599893675962531851&permissions=8&scope=bot")
	
@bot.command()
async def patreon(ctx):
	await ctx.send("https://www.patreon.com/PrabaRock7")
	
@bot.command()
async def supportserver(ctx):
	await ctx.send("https://discord.gg/Me3bmNc")
	
@bot.command()
async def botlogo(ctx):
	await ctx.send("https://i.imgur.com/6fslp74.png")
	
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
    
bot.run('TOKEN') #TODO : INSERT TOKEN
