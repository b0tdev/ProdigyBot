import discord
from discord.ext import commands

bot = commands.Bot(command_prefix=".")

@bot.command()
async def ping(ctx, name="ping", description="Shows the Bot Latency m/s", hidden=False):
    start = time.perf_counter()
    message = await ctx.send("Ping...")
    end = time.perf_counter()
    duration = (end - start) * 1000
    await message.edit(content='Latency is! {:.2f}ms'.format(duration))
    
