import discord
from discord.ext import commands

bot = commands.Bot(command_prefix=".")

@bot.command()
async def start(ctx):
	message = await ctx.send("Starting...")
	await message.edit(content='Started Prodigy Bot Successfully.')
