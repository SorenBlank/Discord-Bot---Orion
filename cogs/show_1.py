                                ###################
                                #importing modules#
                                ###################

#importing discord modules
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

base = sqlite3.connect("all.db")
cur = base.cursor()

class S_1(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print("S1 is Loaded ----")

    @commands.group(invoke_without_command = True,case_insensitive=True)
    async def show(self,ctx):
        show_embed = discord.Embed(title='= = = = = = = =| Help - [Show] |= = = = = = = =',description= "-------------------------------------------------------------")
        show_embed.set_author(name='Show Commands',icon_url=f'{self.client.user.avatar_url}')




        show_embed.set_footer(icon_url=ctx.author.avatar_url,text=f"Requested by {ctx.author.name}")
        await ctx.send(embed = show_embed)

    #This part sends the list of channels that are set as announcement channel 
    @show.command(aliases = ['announcement','announce'])
    async def announcements(self,ctx,msg):
        if msg.lower() == 'channels' or msg.lower() == 'channel':

                cur.execute("SELECT*FROM ANC")
                all = cur.fetchall()
                channels = []
                try:
                    for i in all:
                        channels.append(i[1])
                except:
                    pass

                guilds = []
                try:
                    for i in all:
                        guilds.append(i[0])
                except:
                    pass

                if ctx.channel.id in channels:
                    cur.execute("SELECT*FROM Announce_ch")
                    all = cur.fetchall()
                    an_guilds = []
                    for i in all:
                        an_guilds.append(i[0])
                    
                    if ctx.guild.id in an_guilds:
                        cur.execute("SELECT*FROM Announce_ch WHERE Guild Like ?",(ctx.guild.id,))
                        all = cur.fetchall()

                        channels = ""
                        num = 1
                        for i in all:
                            channels = channels + f"0{num}| <#{i[1]}>\n "
                            num = num + 1

                        if len(all) != 0:
                            embed = discord.Embed(title = "= = = = =| All Announcement Channels |= = = = =")
                            embed.set_author(name='Announcement Channels',icon_url=f'{self.client.user.avatar_url}')
                            embed.add_field(name = "------------------ 📃 __Channels__ 📃 -------------------",value = channels, inline= True)
                            embed.set_footer(icon_url=ctx.author.avatar_url, text= f"Requested by {ctx.author.name}")
                            await ctx.send(embed = embed)
                            
                    if ctx.guild.id not in an_guilds:
                        await ctx.send("This server has no announcement channel set for me.")
                
                cur.execute("SELECT*FROM ANC")
                all = cur.fetchall()
                channels = []
                try:
                    for i in all:
                        channels.append(i[1])
                except:
                    pass

                if ctx.channel.id not in channels:
                    m_ch = []
                    for i in all:
                        if i[0] == ctx.guild.id:
                            m_ch.append(i[1])
                    
                    if len(m_ch) > 1:
                        ch = client.get_channel(m_ch[0])
                        ch2 = client.get_channel(m_ch[1])
                        await ctx.send(f"You are giving command on wrong channel. Please type command here, {ch.mention} or {ch2.mention}")
                    
                    if len(m_ch) == 1:
                        ch = client.get_channel(m_ch[0])
                        await ctx.send(f"You are giving command on wrong channel. Please type command here, {ch.mention}")

                if ctx.guild.id not in guilds:
                    await ctx.send("No channel of this server is set as **Announcement Command Channel**.\n Please set one using this command `.o set announce_ch (channel)`")



@client.command()
async def userinfo(ctx, *, name=""):
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
    voice_state = None if not user.voice else user.voice.channel
    em = discord.Embed(timestamp=ctx.message.created_at, colour=user.top_role.color)
    em.add_field(name='ID', value=user.id, inline=True)
    em.add_field(name="Discriminator:",value=user.discriminator, inline=True)
    em.add_field(name="User Name:",value=user.name, inline=True)
    if user.nick==None:
        nn=user.name
    else:
        nn=user.nick
    em.add_field(name='Nickname', value=nn, inline=True)
    dic={"online":":green_circle: ","dnd":":red_circle: ","offline":":black_circle: ","idle":":yellow_circle: "}
    dic1={"online":"Online","dnd":"Do Not Disturb","offline":"Offline","idle":"Idle"}
    em.add_field(name='Presence', value=dic[str(user.status)]+dic1[str(user.status)], inline=True)
    
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

    em.add_field(name='Status', value=st, inline=True)
    print(vits)
    for act in vits:
        print(act.type)
    if listen != "" and hasattr(listen,"title") and hasattr(listen,"artists"):
        ACT.append(f'Listening to *{listen.title}*  by **{", ".join(listen.artists)}**') 
    if playy != "":
        ACT.append(f"Playing {playy.name}")
    if watch != "":
        ACT.append(f"Watching {watch.name}")
    if stream != "":
        ACT.append(f"Streaming {stream.name}")
    if ACT != []:
        activ=". \n".join(ACT)





    em.add_field(name='Activity', value=activ if activ!="" else "None", inline=False)
    devices=[]
    if str(user.desktop_status)!='offline':
        devices.append(":desktop: Desktop Client")
    if str(user.web_status)!='offline':
        devices.append(":spider_web: Web")
    if str(user.mobile_status)!='offline':
        devices.append(":mobile_phone: Mobile App")
    if len(devices)>0:
        em.add_field(name='Active on', value=", \n".join(devices), inline=True)
    elif len(devices)==0:
        em.add_field(name='Active on', value="None", inline=True)
    em.add_field(name='Voice Channel', value=voice_state, inline=True)
    if len(roles)>0:
        em.add_field(name=f"Roles ({len(roles)})", 
                    value=" ,\n ".join([role.name for role in roles]), inline=True)
    elif len(roles)==0:
        em.add_field(name=f"Roles ({len(roles)})", 
                    value="No Roles", inline=True)
    form='*Date:* %A, %d %B %Y \n*Time:* %H:%M:%S'
    em.add_field(name='Account Created', 
                value=user.created_at.__format__(form),inline=True)
    em.add_field(name='Joined Server', 
                value=user.joined_at.__format__(form),inline=True)
    nitro=user.premium_since
    em.add_field(name='Boosted this server', 
                value='Hasn\'t boosted yet.' if nitro==None else nitro.__format__(form),inline=False)
    em.set_thumbnail(url=avi)
    av=ctx.author.avatar_url_as(static_format='png')
    em.set_author(name=user, icon_url=avi)
    em.set_footer(text=f"Requested by: {ctx.author}", icon_url=av)
    await ctx.send(embed=em)


def setup(client):
    client.add_cog(S_1(client))