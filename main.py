import discord
import random
from discord.ext import commands

import os
import requests
from discord.ext import commands
intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command()
async def hello(ctx):
    """just say hello and name"""
    await ctx.send(f'Привет! Я бот который помогает в уборке мусора {bot.user}!')


    
@bot.command()
async def mem(ctx):
    images = os.listdir('images')
    img_name = random.choice(images)
    # А вот так можно подставить имя файла из переменной!
    with open(f'images/{img_name}', 'rb') as f:
            picture = discord.File(f)
    await ctx.send(file=picture)



@bot.command()
async def rubbish(ctx, city):
    if city == 'Moskva':
        with open(f'places/moskva.png', 'rb') as f:
                picture = discord.File(f)
    # Можем передавать файл как параметр!
        await ctx.send(file=picture)
    if city == 'SanktPeterburg':
        with open(f'places/sankt-peterburg.png', 'rb') as f:
                picture = discord.File(f)
    # Можем передавать файл как параметр!
        await ctx.send(file=picture)

    if city == 'YuzchnoSahalinsk':
        with open(f'places/yuzchno-sahalinsk.png', 'rb') as f:
                picture = discord.File(f)
    # Можем передавать файл как параметр!
        await ctx.send(file=picture)

    if city == 'Sochi':
        with open(f'places/sochi.png', 'rb') as f:
                picture = discord.File(f)
    # Можем передавать файл как параметр!
        await ctx.send(file=picture)

@bot.command()
async def url(ctx):
      await ctx.send('https://recyclemap.ru       давай спасай мир😉!')
@bot.command()
async def memAnimals(ctx):
    images2 = os.listdir('imagesanimal')
    img_name1 = random.choice(images2)
    # А вот так можно подставить имя файла из переменной!
    with open(f'imagesanimal/{img_name1}', 'rb') as f:
            picture = discord.File(f)
    await ctx.send(file=picture)

bot.run("")
