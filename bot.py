#!/usr/bin/env python -W ignore::DeprecationWarning
#-*- coding: utf-8 -*-
#################################################
#### created the 16/08/2018 14:48 by Frayal #####
#################################################
'''
/!| WIP /!| A NE PAS UTILISER. A MODIFIER. A TESTER.
En cours de test alors on se calme svp!
'''

'''
Améliorations possibles:

'''
import warnings
warnings.filterwarnings('ignore')
#################################################
###########        Imports      #################
#################################################
import sys
import os
import numpy as np
import datetime
import time
from subprocess import Popen
import discord
from discord.ext import commands
#################################################
########### Global variables ####################
#################################################

#################################################
########## Important functions ##################
bot = commands.Bot(command_prefix='$')

@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')

@bot.command()
async def add(ctx, a: int, b: int):
    await ctx.send(a+b)

@bot.command()
async def multiply(ctx, a: int, b: int):
    await ctx.send(a*b)

@bot.command()
async def greet(ctx):
    await ctx.send(":smiley: :wave: Hello, there!")

@bot.command()
async def cat(ctx):
    await ctx.send("https://media.giphy.com/media/JIX9t2j0ZTN9S/giphy.gif")

#Personal messages
@bot.command()
async def Karde(ctx):
    await ctx.send("Karde est un noob!")

@bot.command()
async def Frayal(ctx):
    await ctx.send("Frayal est un Dieu Vivant! Prosternez-vous devant lui! (bien tenté Karde)")
    
@bot.command()
async def Zeus(ctx):
    await ctx.send("Le pro des explosifs. Teamkill ne fait pas partie de son vocabulaire.")

@bot.command()
async def info(ctx):
    embed = discord.Embed(title="nice bot", description="Nicest bot there is ever.", color=0xeee657)

    # give info about you here
    embed.add_field(name="Author", value="Frayal")

    # Shows the number of servers the bot is member of.
    embed.add_field(name="Server count", value=f"{len(bot.guilds)}")

    # give users a link to invite this bot to their server
    embed.add_field(name="Invite", value="https://discordapp.com/api/oauth2/authorize?client_id=487559807046516737&permissions=1280822336&scope=bot")

    await ctx.send(embed=embed)

bot.remove_command('help')

@bot.command()
async def help(ctx):
    embed = discord.Embed(title="nice bot", description="A Very Nice bot. List of commands are:", color=0xeee657)

    embed.add_field(name="$add X Y", value="Gives the addition of **X** and **Y**", inline=False)
    embed.add_field(name="$multiply X Y", value="Gives the multiplication of **X** and **Y**", inline=False)
    embed.add_field(name="$greet", value="Gives a nice greet message", inline=False)
    embed.add_field(name="$cat", value="Gives a cute cat gif to lighten up the mood.", inline=False)
    embed.add_field(name="$info", value="Gives a little info about the bot", inline=False)
    embed.add_field(name="$help", value="Gives this message", inline=False)

    await ctx.send(embed=embed)

bot.run('NDg3NTU5ODA3MDQ2NTE2NzM3.DnPyAw.9wsGmUvoPQTREeETN8qFunoL8-s')
