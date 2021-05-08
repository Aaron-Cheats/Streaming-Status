import discord
from discord.ext import commands

token = "NTk1MDc4NTUzNzM3ODg3NzQ3.YI3MXA.xO0vRiaVGFVwcYoDi5tFF0blBKU"

bot = commands.Bot(command_prefix = "123456789")

print('Subscribe To Aaron')
status = input(' > ')

@bot.event
async def on_connect():
    stream = discord.Streaming(
        name = status,
        url = 'https://www.youtube.com/channel/UCs72eAh4HpsI6tsaQZ8B_Gw?sub_confirmation=1'
    )
    print('Streaming: ' + status)
    await bot.change_presence(activity=stream)

bot.run(token, bot=False)    
