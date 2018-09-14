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
import discord
from discord.ext import commands
#################################################
########### Global variables ####################
#################################################

#################################################
########## Important functions ##################
bot = commands.Bot(command_prefix='$')
messages = ['Whaoooou....même Zeus fait moi de TK que toi',"j'ai pas d'idée d'insultes merci à la DT De m'envoyer les messages qu'il veulent afficher"]

@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')

@bot.command()
async def admins(ctx):
    await ctx.send("les admins sont Zeus, Frayal, Courgette, Zippo, Keyser et Karde.")

@bot.command()
async def rules(ctx):
    embed = discord.Embed(title="Règles", description="", color=0xe8192e)
    await ctx.send("""Conduite à tenir :
                    \nLes joueurs de la team doivent être identifiable en plaçant le Tag [DT] apres leur pseudo:triangular_flag_on_post: 
                    \nUn accès prioritaire est attribué aux joueurs de la team 
                    \nQuand on se connecte c'est pour passer du bon temps, on joue , on se marre et on prépare les grandes batailles! Dans toutes circonstances, sachez garder votre calme. 
                    \nRappelez vous que vous avez un tag et que ceci n'est qu'un jeux
                    \nNe pas recourir aux insultes ni de rager pour rien.
                    \nSoyez respectueux sur le serveur ainsi que sur le discord , envers les utilisateurs et le staff. 'Bonjour', 'Au-revoir' n'ont jamais tué personne aussi bien sur le serveur afin de donner une bonne image;) 
                    \nSi vous avez un soucis avec un membre, discutez en dans un Canal dédié, le dialogue entre gentleman/ personne civilisée trouve souvent une solution. 
                    \nUn membre [DT] surpris avec un cheat sera banni automatiquement , que ce soit sur notre serveur ou un serveur de la communauté RS2 ! 
                    \nMerci de bien regler votre micro quand on joue sur le discord certaine personne sont plus sensible que d'autres  c est comme le language fleuri.
                    """)

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

@bot.command()
async def Karde(ctx):
    await ctx.send("Karde est un noob!")

@bot.command()
async def Zeus(ctx):
    await ctx.send("Zeus! Oh mon Zeus! (please send nudes)")

@bot.command()
async def Frayal(ctx):
    await ctx.send("Frayal est un Dieu Vivant! Prosternez-vous devant lui!")

@bot.command()
async def info(ctx):
    embed = discord.Embed(title="nice bot", description="Nicest bot there is ever.", color=0xeee657)

    # give info about you here
    embed.add_field(name="Author", value="Frayal")

    # Shows the number of servers the bot is member of.
    embed.add_field(name="Server count", value={len(bot.guilds)})

    # give users a link to invite this bot to their server
    embed.add_field(name="Invite", value="plouf")

    await ctx.send(embed=embed)

@bot.command(pass_context = True)
async def say(ctx,*,message : str):
    #228803118635155456
    if ctx.message.author.id == 228803118635155456:
        await ctx.send(":microphone2: " + message + " :microphone2:")
        return
    else:
        await ctx.send(":warning: " + ctx.message.author.mention + " : Tu n'as pas le droit de faire la commande $say "+":warning:")
        return

@bot.command(pass_context = True)
async def make_fun(ctx, member : discord.Member = None):
    if member is None:
        await ctx.send("Eh tu dois me dire qui insulter :o")
        return
    elif member.id == (228803118635155456):
        await ctx.send("Mais WTF gros! J'insulte pas Frayal! J'ai beaucoup trop peur")
        return
    elif member.id == ctx.message.author.id:
        await ctx.send("T'es sur que tu veux t'insulter toi même? En tout cas moi je ne te ferai pas ce plaisir...")
        return
    else:
        nombre = np.random.randint(0, len(messages))
        text = messages[nombre].format(member.mention)
        await ctx.send(":picke: " + text + " :picke:")
        return
