import discord
from discord.ext import commands

bot = commands.Bot(command_prefix=".")

@bot.command()
async def ban(ctx, user:
discord.Member):
	await ctx.send("{} Has Been Banned!".format(user.mention))
	await user.send("You Have been Banned from {}.".format(ctx.guild.name))
	await user.ban()
	
