from discord.ext import commands
from os import getenv
import traceback



bot = commands.Bot(command_prefix='/')


@bot.event
async def on_command_error(ctx, error):
    orig_error = getattr(error, "original", error)
    error_msg = ''.join(traceback.TracebackException.from_exception(orig_error).format())
    await ctx.send(error_msg)

@bot.event    
async def on_command_error(ctx2, error):
    orig_error = getattr(error2, "original", error)
    error_msg = ''.join(traceback.TracebackException.from_exception(orig_error).format())
    await ctx2.send(error2_msg)
    
@bot.event
async def on_command_error(ctx3, error):
    orig_error = getattr(error3, "original", error)
    error_msg = ''.join(traceback.TracebackException.from_exception(orig_error).format())
    await ctx3.send(error2_msg)

@bot.event
async def on_command_error(ctx4, error):
    orig_error = getattr(error4, "original", error)
    error_msg = ''.join(traceback.TracebackException.from_exception(orig_error).format())
    await ctx4.send(error2_msg)

@bot.event
async def on_command_error(ctx5, error):
    orig_error = getattr(erro5r, "original", error)
    error_msg = ''.join(traceback.TracebackException.from_exception(orig_error).format())
       await ctx5.send(error5_msg)



    

@bot.command()
async def ping(ctx):
    await ctx.send('pong')
    
@bot.command()    
async def mks(ctx2):
    await ctx2.send('https://livedoor.blogimg.jp/nim_2525/imgs/e/d/ed590862.jpg')

@bot.command()    
async def wp(ctx3):
    await ctx3.send('https://livedoor.blogimg.jp/nim_2525/imgs/6/a/6a33f204.jpg')

@bot.command()    
async def ssc(ctx4):
    await ctx4.send('https://livedoor.blogimg.jp/nim_2525/imgs/7/2/72fd79db.jpg')

@bot.command()    
async def tr(ctx5):
    await ctx5.send('https://livedoor.blogimg.jp/nim_2525/imgs/1/5/15f34362.jpg')




    





token = getenv('DISCORD_BOT_TOKEN')
bot.run(token)
