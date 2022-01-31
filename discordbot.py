from discord.ext import commands
from os import getenv
import traceback

bot = commands.Bot(command_prefix='/')


@bot.event
async def on_command_error(ctx, error):
    orig_error = getattr(error, "original", error)
    error_msg = ''.join(traceback.TracebackException.from_exception(orig_error).format())
    await ctx.send(error_msg)
    
async def on_command_error(ctx2, error):
    orig_error = getattr(error, "original", error)
    error_msg = ''.join(traceback.TracebackException.from_exception(orig_error).format())
    await ctx.send(error2_msg)
    
async def on_command_error(ctx3, error):
    orig_error = getattr(error, "original", error)
    error_msg = ''.join(traceback.TracebackException.from_exception(orig_error).format())
    await ctx.send(error2_msg)

@bot.command()
async def ping(ctx):
    await ctx.send('pong')
@bot.command()    
async def aaa(ctx2):
    await ctx2.send('https://livedoor.blogimg.jp/nim_2525/imgs/e/d/ed590862.jpg')

@bot.command()    
async def bbb(ctx3):
await ctx3.send('https://livedoor.blogimg.jp/nim_2525/imgs/e/d/ed590862.jpg') 

    





token = getenv('DISCORD_BOT_TOKEN')
bot.run(token)
