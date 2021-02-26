import discord
from discord import Intents
from discord.ext import commands
from discord.ext import commands, tasks
#importing other modules
import random
import os
import asyncio
import json
import datetime
import wikipedia as wiki
import math
import sqlite3
from PIL import Image
from io import BytesIO
import numpy as np
import re
from discord import ActivityType as AT

class U_1(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print("U1 is Loaded ----")

    @commands.command()
    async def userinfo(self,ctx, *, name=""):
        if name:
            try:
                user = ctx.message.mentions[0]
            except IndexError:
                user = ctx.guild.get_member_named(name)
            if not user:
                user = ctx.guild.get_member(int(name))
            if not user:
                await ctx.send('Could not find user.')
                return
        else:
            user = ctx.message.author

        
        avi = user.avatar_url_as(static_format='png')
        if isinstance(user, discord.Member):
            roles = roles = [role for role in user.roles]
            for role in roles:
                if role.name=="@everyone":
                    roles.remove(role)
                    break
        
        em = discord.Embed(title='= = = = = |:notepad_spiral: User Info :notepad_spiral:| = = = = =',description = "- - - - - - - - - - - - - - - - - - - - - - - - - - - -")
        em.add_field(name=":white_medium_small_square:USER_NAME:",value=f":white_small_square:`{user.name}`", inline=True)
        em.add_field(name=":white_medium_small_square:DISCRIMINATOR:",value=f":white_small_square:`{user.discriminator}`", inline=True)
        
        if user.nick==None:
            nn=user.name
        else:
            nn=user.nick
        em.add_field(name=':white_medium_small_square:NICK_NAME:', value=f":white_small_square:`{nn}`", inline=True)
        em.add_field(name=':white_medium_small_square:USER_ID:',value=f":white_small_square:`{user.id}`",inline = True)


        em.add_field(name=" ឵឵ ",value=" ឵឵ ",inline=False)

        dic={"online":"<:online:814161343426199622> ","dnd":"<:dnd:814161369892257842> ","offline":":black_circle: ","idle":"<:idle:814161403271184426> "}
        dic1={"online":"Online","dnd":"Do Not Disturb","offline":"Offline","idle":"Idle"}
        em.add_field(name='PRESENCE', value= f"{dic[str(user.status)] + dic1[str(user.status)]}\n―", inline=True)
        
        st="None"
        activ=""
        listen,stream,playy,watch="","","",""
        ACT=[]
        vits=list(user.activities)
        for act in vits:
            if act.type==AT.custom:
                st=act
            elif act.type==AT.listening:
                listen=act
            elif act.type==AT.streaming:
                stream=act
            elif act.type==AT.playing:
                playy=act
            elif act.type==AT.watching:
                watch=act

        em.add_field(name='STATUS', value=f"{st}\n―", inline=True)

        if listen != "" and hasattr(listen,"title") and hasattr(listen,"artists"):
            ACT.append(f'<:spotify:814185511655964682> Listening to `{listen.title}`  by **{", ".join(listen.artists)}**')
        if playy != "":
            if playy.name == "VALORANT":
                ACT.append(f"<:valorant:814455293328228394> Playing **{playy.name}**")
            elif playy.name == "Apex Legends":
                ACT.append(f"<:apex:814455315399442444> Playing **{playy.name}**")
            elif playy.name == "Minecraft":
                ACT.append(f"<:block:814428039206535180> Playing **{playy.name}**")
            elif playy.name == "Call of Duty®: Modern Warfare®":
                ACT.append(f"<:mw:814458659827744788> Playing **{playy.name}**")
            elif playy.name == "Fortnite":
                ACT.append(f"<:fortnite:814459933234954241> Playing **{playy.name}**")
            elif playy.name == "Tom Clancy's Rainbow Six Siege":
                ACT.append(f"<:rainbow:814460454260834306> Playing **{playy.name}**")
            elif playy.name == "Grand Theft Auto V":
                ACT.append(f"<:gtav:814461284636295218> Playing **{playy.name}**")
            elif playy.name == "BlueStacks":
                ACT.append(f"<:bs:814461697568800768> Playing **{playy.name}**")
            elif playy.name == "Genshin Impact":
                ACT.append(f"<:genshin:814462612346503188> Playing **{playy.name}**")
            elif playy.name == "Brawlhalla":
                ACT.append(f"<:brawlhalla:814463603745751050> Playing **{playy.name}**")

            elif playy.name == "osu!":
                ACT.append(f"<:osu:814465391077359666> Playing **{playy.name}**")

            elif playy.name == "ROBLOX":
                ACT.append(f"<:roblox:814466647128670240> Playing **{playy.name}**")

            elif playy.name == "VRChat":
                ACT.append(f"<:vrchat:814506984523038740> Playing **{playy.name}**")

            elif playy.name == "Counter-Strike: Global Offensive":
                ACT.append(f"<:csgo:814472867026567250> Playing **{playy.name}**")

            elif playy.name == "Sublime Text":
                ACT.append(f"<:sublime:814475264330694746> Playing **{playy.name}**")

            elif playy.name == "Dota 2":
                ACT.append(f"<:dota2:814477802204037130> Playing **{playy.name}**")

            elif playy.name == "Rocket League":
                ACT.append(f"<:RocketLeague:814483353091833908> Playing **{playy.name}**")

            elif playy.name == "Batman: Arkham Knight":
                ACT.append(f"<:batman:814492074106945616> Playing **{playy.name}**")

            elif playy.name == "Assassin's Creed Brotherhood":
                ACT.append(f"<:assasin:814494128506798200> Playing **{playy.name}**")

            elif playy.name == "Brawl Stars":
                ACT.append(f"<:brawlstars:814495602959450132> Playing **{playy.name}**")

            elif playy.name == "Visual Studio Code":
                ACT.append(f"<:vscode:814499769065799741> Playing **{playy.name}**")

            elif playy.name == "Dolphin Emulator":
                ACT.append(f"<:dolphinemu:814500628588003389> Playing **{playy.name}**")

            elif playy.name == "Citra":
                ACT.append(f"<:citra:814501683639353394> Playing **{playy.name}**")

            elif playy.name == "Cemu":
                ACT.append(f"<:Cemu:814502100288405555> Playing **{playy.name}**")

            elif playy.name == "League of Legends":
                ACT.append(f"<:lol:814619672975638559> Playing **{playy.name}**")


            else:
                ACT.append(f":grey_question: Playing **{playy.name}**")

        if watch != "":
            ACT.append(f"Watching {watch.name}")
        if stream != "":
            ACT.append(f"Streaming {stream.name}")
        if ACT != []:
            activ=" \n\n".join(ACT)


        em.add_field(name='ACTIVITY', value=f"{activ}\n―" if activ!="" else "None \n―", inline=False)
        devices=[]
        if str(user.desktop_status)!='offline':
            devices.append(":desktop: - Desktop Client")
        if str(user.web_status)!='offline':
            devices.append(":globe_with_meridians: - Web")
        if str(user.mobile_status)!='offline':
            devices.append(":mobile_phone: - Mobile App")

        if len(devices)>0:
            em.add_field(name='ACTIVE ON', value=", \n".join(devices) + "\n―", inline=True)

        elif len(devices)==0:
            em.add_field(name='ACTIVE ON', value="None\n―", inline=True)

        if len(roles)>0:
            em.add_field(name=f"ROLES ({len(roles)})", 
                        value=" ,\n".join([role.mention for role in roles]), inline=True)
        elif len(roles)==0:
            em.add_field(name=f"ROLES ({len(roles)})", 
                        value="No Roles", inline=True)

        em.add_field(name=" ឵឵ ",value=" ឵឵ ",inline=False)

        form=':calendar_spiral: __**Date:**__\n%d %B %Y\n:clock1: __**Time:**__\n%H:%M:%S'
        em.add_field(name=':pencil: ACCOUNT CREATED', 
                    value=f"{user.created_at.__format__(form)}\n―",inline=True)
        em.add_field(name=':pencil: JOINED SERVER', 
                    value=user.joined_at.__format__(form),inline=True)
        nitro=user.premium_since
        if nitro != None:
            em.add_field(name='BOOST STATUS', 
                        value='❎ No Boost' if nitro==None else nitro.__format__(form),inline=False)
        em.set_thumbnail(url=avi)
        av=ctx.author.avatar_url_as(static_format='png')

        em.set_footer(text=f"Requested by {ctx.author.name}", icon_url=av)
        await ctx.send(embed=em)


    @commands.command(aliases = ["avatar"])
    async def av(self,ctx,user:discord.Member = None):
        if user == None:
            user = ctx.author
        embed = discord.Embed(title=f"{user.name}")
        embed.set_image(url = user.avatar_url)
        embed.set_footer(text=f"Requested by {ctx.author.name}", icon_url=ctx.author.avatar_url)
        await ctx.send(embed = embed)


def setup(client):
    client.add_cog(U_1(client))