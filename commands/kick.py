import discord
from discord.ext import commands

bot = commands.Bot(command_prefix=".")

@bot.command(name="kick", description="Kicks the User", hidden=False)
async def kick(ctx, user:
discord.Member):
    await ctx.send(" {} Has been kicked!".format(user.mention))
    await user.send("You have been kicked from {}.".format(ctx.guild.name))
    await user.kick()
    
