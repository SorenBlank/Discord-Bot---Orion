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
from PIL import Image
from io import BytesIO
import numpy as np
import re
from discord import ActivityType as AT
import pymongo
from pymongo import MongoClient

cluster = MongoClient("mongodb+srv://soren:cdD2_qWUYRk-d4G@orion.iztml.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
base = cluster["OrionDB"]

ign_cur = base["ign"]

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
                try:
                    user = ctx.guild.get_member(int(name))
                except:
                    pass
            if not user:
                await ctx.send('Could not find user.')
                return
        else:
            user = ctx.message.author


        if user.id != 777095257262522399:
            avi = user.avatar_url_as(static_format='png')
            if isinstance(user, discord.Member):
                roles = roles = [role for role in user.roles]
                for role in roles:
                    if role.name=="@everyone":
                        roles.remove(role)
                        break
            
            em = discord.Embed(color = 0x714ec4)
            em.set_author(name = "USER INFO", icon_url= self.client.user.avatar_url)
            em.add_field(name="USER NAME",value=f"```\n{user}```", inline=True)
            em.add_field(name = "USER ID",value = f"```\n{user.id}```",inline= True)
            
            if user.nick==None:
                nn=user.name
            else:
                nn=user.nick

            em.add_field(name='NICK NAME', value=f"```\n{nn}```", inline=False)
            
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

                elif playy.name == "Overwatch":
                    ACT.append(f"<:overwatch:814483380321910784> Playing **{playy.name}**")

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
            
            x = ign_cur.find_one({"dc_id":user.id})

            val_user_name = None
            chess_user_name = None

            if x != None:
                if 'val_user' in x.keys():
                    val_user_name = x["val_user"]
                if 'chess_user' in x.keys():
                    chess_user_name = x["chess_user"]
    
            if len(devices)>0:
                em.add_field(name='ACTIVE ON', value=", \n".join(devices) + "\n―", inline=True)

            elif len(devices)==0:
                em.add_field(name='ACTIVE ON', value="None\n―", inline=True)
            
            lists = []
            emo = {"val":"<:valorant:814455293328228394>", "chess":"<:chess:830030544661119056>"}

            if val_user_name != None:
                s = f"{emo['val']} - {val_user_name}"
                lists.append(s)
            if chess_user_name != None:
                j = f"{emo['chess']} - {chess_user_name}"
                lists.append(j)
            
            if len(lists) != 0:
                text = "\n".join(lists)
                em.add_field(name = "IGNS", value = text)
            else:
                em.add_field(name = "IGNS", value = "None")



            if len(roles)>0:
                em.add_field(name=f"ROLES ({len(roles)})", 
                            value=f"```\n{', '.join([role.name for role in roles])}```", inline=False)
            elif len(roles)==0:
                em.add_field(name=f"ROLES ({len(roles)})", 
                            value="```\nNone```", inline=False)

            form='%d/%m/%Y %H:%M:%S'
            em.add_field(name='ACCOUNT CREATED ON (D/M/Y)', 
                        value=f"```\n{user.created_at.__format__(form)}```",inline=False)
            em.add_field(name='JOINED SERVER ON (D/M/Y)', 
                        value=f"```\n{user.joined_at.__format__(form)}```",inline=False)
            nitro=user.premium_since
            if nitro != None:
                em.add_field(name='BOOST STATUS (D/M/Y)', 
                            value='None' if nitro==None else f"```\n{nitro.__format__(form)}```",inline=False)
            em.set_thumbnail(url=avi)
            av=ctx.author.avatar_url_as(static_format='png')
            await ctx.send(embed=em)

        else:
            avi = user.avatar_url_as(static_format='png')
            if isinstance(user, discord.Member):
                roles = roles = [role for role in user.roles]
                for role in roles:
                    if role.name=="@everyone":
                        roles.remove(role)
                        break
            
            em = discord.Embed(color = 0x714ec4)
            em.set_author(name = "USER INFO", icon_url= self.client.user.avatar_url)
            em.add_field(name="USER NAME",value=f"```\n{user}```", inline=True)
            em.add_field(name = "USER ID",value = f"```\n{user.id}```",inline= True)
            
            if user.nick==None:
                nn=user.name
            else:
                nn=user.nick

            em.add_field(name='NICK NAME', value=f"```\n{nn}```", inline=False)


            em.add_field(name='VERSION', value= "`V2.0`", inline=True)
            dic = {"0":":zero:","1":":one:","2":":two:","3":":three:","4":":four:","5":":five:","6":":six:","7":":seven:","8":":eight:","9":":nine:","10":":one::zero:"}
            num = str(len(self.client.guilds))
            if len(num) > 1:
                emo = ""
                for i in num:
                    emo = emo + dic[i]
            else:
                emo = dic[num]
            em.add_field(name='ACTIVE ON', value=f"{emo} servers", inline=True)


            mem1 = self.client.get_user(693375549686415381)

            mem2 = self.client.get_user(692066406384271451)

            mem3 = self.client.get_user(736818641907089520)

            # def underline(x):
            #     x = str(x)
            #     j = []

            #     for i in x:
            #         if i == "_":
            #             j = x.split("_")

            #     if len(j) > 1:
            #         j = "\_".join(j)
            #         return j
            #     else:
            #         return x


            em.add_field(name='DEVELOPER TEAM', value=f"```diff\n> {mem1} \n-worked on design and development.\n\n> {(mem2)}\n-worked on development.\n\n> {mem3}\n-helped with ideas and suggestions.```", inline=False)

            

            if len(roles)>0:
                em.add_field(name=f"ROLES ({len(roles)})", 
                            value=f"```\n{', '.join([role.name for role in roles])}```", inline=False)
            elif len(roles)==0:
                em.add_field(name=f"ROLES ({len(roles)})", 
                            value="```\nNone```", inline=False)

    

            form='%d/%m/%Y %H:%M:%S'
            em.add_field(name='ACCOUNT CREATED ON (D/M/Y)', 
                        value=f"```\n{user.created_at.__format__(form)}```",inline=False)
            em.add_field(name='JOINED SERVER ON (D/M/Y)', 
                        value=f"```\n{user.joined_at.__format__(form)}```",inline=False)

            em.set_thumbnail(url=avi)
            av=ctx.author.avatar_url_as(static_format='png')
            await ctx.send(embed=em)

    @commands.command()
    async def serverinfo(self, ctx, *, sname=""):
        if sname:
            server = None
            try:
                int(sname)
                server = self.client.get_guild(int(sname))
                if not server:
                    return await ctx.send('Server not found.')
            except:
                for i in self.client.guilds:
                    if i.name.lower() == sname.lower():
                        server = i
                        break
                if not server:
                    return await ctx.send('Could not find server.')
        else:
            server = ctx.message.guild

        textchannels = len(server.text_channels)
        voicechannels= len(server.voice_channels)
        total_channels=textchannels+voicechannels
        num_roles = len(server.roles)
        num_emojis= len(server.emojis)

        
        bots=0
        online, idle, dnd = 0,0,0
        for i in server.members:
            if i.bot:
                bots += 1
            if str(i.status) == 'online':
                online+=1
            elif str(i.status) == 'idle':
                idle+=1
            elif  str(i.status) == 'dnd':
                dnd+=1
        num_offline = server.member_count - online - idle - dnd
        humans = server.member_count - bots


        em = discord.Embed(color = 0x714ec4)
        em.add_field(name = "SERVER NAME", value = f"```\n{server.name}```",inline=True)
        em.add_field(name='SERVER OWNER', value=f"```\n{server.owner}```", inline=True)
        em.add_field(name=f'SERVER MEMBERS - {server.member_count}', value=f"```\nMembers: {humans} | Bots: {bots}```",inline=False)
        em.add_field(name='SERVER ID', value=f"```\n{server.id}```", inline=True)
        em.add_field(name='SERVER REGION', value=f"```\n{str(server.region).capitalize()}```",inline=True)
        
        
        em.add_field(name='SERVER CATEGORIES & CHANNELS', value=f"```\nCategories: {len(server.categories)} | Text: {textchannels} | Voice: {voicechannels}```",inline=False)
        em.add_field(name='SERVER VERIFICATION LEVEL', value=f"```\n{str(server.verification_level).capitalize()}```",inline=False)
        em.add_field(name = "SERVER BOOSTS", value = f"```\n{server.premium_subscription_count}```",inline=True)
        em.add_field(name='SERVER BOOST TIER', value=f"```\n{server.premium_tier}```",inline=True)

        form='%d/%m/%Y %H:%M:%S'
        em.add_field(name='SERVER CREATED ON (D/M/Y)', value=f"```\n{server.created_at.__format__(form)}```",inline=False)
        em.set_thumbnail(url=server.icon_url)
        em.set_author(name="SERVER INFO", icon_url=self.client.user.avatar_url)
        av=ctx.author.avatar_url_as(static_format='png')
        await ctx.send(embed=em)
    
    @commands.command()
    async def ign(self,ctx, *, name=""):
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


        if user.id != 777095257262522399:
            avi = user.avatar_url_as(static_format='png')
            if isinstance(user, discord.Member):
                roles = roles = [role for role in user.roles]
                for role in roles:
                    if role.name=="@everyone":
                        roles.remove(role)
                        break
        
        game = discord.Embed(color = 0x714ec4, title = user)
        game.set_author(name = "IGNS", icon_url= self.client.user.avatar_url)

        x = ign_cur.find_one({"dc_id":user.id})

        val_user_name = None
        chess_user_name = None

        if x != None:
            if 'val_user' in x.keys():
                val_user_name = x["val_user"]
            if 'chess_user' in x.keys():
                chess_user_name = x["chess_user"]

            if val_user_name != None:
                game.add_field(name = "<:valorant:814455293328228394> valorant", value = f"```\n{val_user_name}```", inline= False)
        
            if chess_user_name != None:
                game.add_field(name = "<:chess:830030544661119056> chess.com", value = f"```\n{chess_user_name}```", inline = False)


        if val_user_name == None and chess_user_name == None:
            temp = discord.Embed(title = user,description = "This account is not linked with any game", color = 0x714ec4)
            temp.set_author(name = "IGNS", icon_url= self.client.user.avatar_url)
            await ctx.send(embed = temp)
        else:
            await ctx.send(embed = game)



        


    @commands.command(aliases = ["avatar"])
    async def av(self,ctx, *, name=""):
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

        embed = discord.Embed(title=f"{user.name}",color = 0x714ec4)
        embed.set_image(url = avi)
        await ctx.send(embed = embed)

    

def setup(client):
    client.add_cog(U_1(client))