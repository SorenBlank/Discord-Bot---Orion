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
import pymongo
from pymongo import MongoClient

cluster = MongoClient("mongodb+srv://soren:cdD2_qWUYRk-d4G@orion.iztml.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
base = cluster["OrionDB"]

m1_cur = base["m1guilds"]
c1_cur = base["c1channels"]
anch_cur = base["anch"]
anc_cur = base["anc"]
fc_cur = base["fc"]
tc_cur = base["tc"]
bc_cur = base["bc"]
tic_cur = base["tic"]
ta_cur = base["ta"]
wc_cur = base["wc"]

class A_1(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print("A1 is Loaded ----")


                                    ###########################
                                    ##        ACTIVATOR      ##
                                    ###########################

    @commands.group(invoke_without_command = True,aliases = ["initiate","start","set","setup"],case_insensitive=True)
    async def activate(self,ctx):
        activator_embed = discord.Embed(title='\
= = = = = = =| Help - [Activate] |= = = = = = =',description="Aliases = `initiate`, `start`, `set`\nFor more info: `.o help`\n\n\
__**:warning:Disclaimer:warning:**__\n\
:white_small_square: The `[` and `]` around the argument mean it’s required.\n\
:white_small_square: The `(` and `)` around the argument mean it’s optional.\n\
-   -   -   -   -   -   -   -   -   -   -   -   -   -   -   -   -   -   -   -")



        #FIRST FIELD
        activator_embed.add_field(name=":gear:PROTOCOLS:gear:",
                                  value='‎‎--------- :arrow_down_small: ---------',
                                  inline=False)
        activator_embed.add_field(name=":large_orange_diamond: M1",
                                  value=":small_orange_diamond:Activating M1 will allow the mods to use **Moderation Commands**.\n**__Command:__** `.o activate m1`",
                                  inline=False)
        activator_embed.add_field(name=":large_orange_diamond: C1 (BETA)",
                                  value=":small_orange_diamond:Activating C1 on a specific channel will allow the bot to use it's chat functionality.\n**__Command:__** `.o activate c1 (channel)`",
                                  inline=False)

        activator_embed.add_field(name=" ឵឵ ",value=" ឵឵ ",inline=False)

        #SECOND FIELD
        activator_embed.add_field(name=":card_box:SERVER UTILITIES:card_box:",
                                  value = "------------ :arrow_down_small: ------------\nThis section includes all **server utility activation** commands.\n ឵឵ ",
                                  inline= False)

        activator_embed.add_field(name=":hammer_pick: Announcement Command Channel",
                                  value=":small_orange_diamond: You can announce anything in your server using **Announcement Commands**. In order to use these commands you need to set a specific channel which is not visible to all members beside the server admins and moderators, where you will execute these commands.\n**__Command:__** `.o set announce_ch (channel)`",
                                  inline=False)


        activator_embed.add_field(name=":hammer_pick: Announcement Channel",
                                  value=":small_orange_diamond: After setting up **Announcement Command Channel**, you need to set your announcement channels where you will announce stuffs. You can set up to 2 channels as **Announcement Channels**. After you set a channel, you will be able to use `.o announce` command for announcing with the bot.\n**__Command:__** `.o set announce (channel)`",
                                  inline=False)

        activator_embed.add_field(name=" ឵឵ ",value=" ឵឵ ",inline=False)


        #THIRD FIELD
        activator_embed.add_field(name=":video_game:GAMES:video_game:",
                                  value="------ :arrow_down_small: -----",
                                  inline=False)
        activator_embed.add_field(name=":large_blue_diamond: Fibonacci/Fibo",
                                  value=":small_blue_diamond: This is a Fibonacci Count Up game. Following command allows a specific channel to run this game. To know more about this in detail, type: `.o help game`\n**__Command:__** `.o activate fibo (channel)`",inline=False)
        activator_embed.add_field(name=":large_blue_diamond: TicTacToe",
                                  value=":small_blue_diamond: No need to tell about this game I suppose. Following command allows a specific channel to run this game. In case you don't know what this game is ( xD ) please do not hesitate to type this `.o help game`\n**__Command:__** `.o activate tic (channel)`",
                                  inline=False)
        activator_embed.add_field(name=":large_blue_diamond: Battleship (BETA)",
                                  value=':small_blue_diamond: This is a Battleship game. Following command allows a specific channel to run this game. You can [click here](https://en.wikipedia.org/wiki/Battleship_game "https://en.wikipedia.org/wiki/Battleship_game") or type `.o help game` or more specifically type `.o help battleship` in order to know about this game. \n**__Command:__** `.o activate battleship (channel)`',
                                  inline = False)
        
        activator_embed.add_field(name=" ឵឵ ",value=" ឵឵ ",inline=False)


        activator_embed.add_field(name=":book:PHILOSOPHY:book:",
                                  value="---------- :arrow_down_small: ---------",
                                  inline=False)
        activator_embed.add_field(name=":notebook: Wikipedia",
                                  value=":small_orange_diamond: This is wikipedia. Following command allows a specific channel to use **Wikipedia** commands. To know more about this in detail, type: `.o help philosophy` \n**__Command:__** `.o activate wiki (channel)`",
                                  inline=False)


        activator_embed.set_footer(icon_url=ctx.author.avatar_url,text=f"Requested by {ctx.author.name}")

        await ctx.send(embed = activator_embed)

    @activate.command()
    async def M1(self,ctx):
        if ctx.author.guild_permissions.manage_channels and ctx.author.guild_permissions.manage_messages:
            id_guild = ctx.guild.id
            
            raw = m1_cur.find({"guild":id_guild})
            guilds = []
            try:
                x = [i for i in raw]
                guilds = [x[i]["guild"] for i in range(len(x))]
            except:
                pass
            
            if ctx.guild.id in guilds:
                    await ctx.send(random.choice(["M1 is running",
                                                  "M1 is active"]))

            if ctx.guild.id not in guilds:

                up = {"_id":len(guilds),"guild":id_guild}
                m1_cur.insert_one(up)

                await ctx.send("M1 Activated\nModeration Commands has been unlocked!")
        else:
            await ctx.send("**Access Denied!** This command requires `manage_channel` and `manage_messages` permission in order to execute.")


    @activate.command()
    async def C1(self,ctx,channel:discord.TextChannel = None):
        #This checks if the user has manage channels permission
        if ctx.author.guild_permissions.manage_channels:
            
            #This makes the bot acts as if the a specific channel has been provided
            if channel != None:
                try:
                    id_channel = channel.id
                    raw_channels = c1_cur.find({"channel":channel.id})
                    channels = [i["channel"] for i in raw_channels ]
                    
                    if id_channel not in channels:
                        up = {"_id":len(channels),
                              "guild":ctx.guild.id,
                              "channel":id_channel,
                              "createtime":"",
                              "timegap":0}
                        c1_cur.insert_one(up)
                        await ctx.send(f"C1 has been activated in {channel.mention}")
                    else:
                        await ctx.send(f"C1 is already running in {channel.mention}")
                except:
                    await ctx.send(f"{ctx.author.mention}, please pass all required arguments.")

            #This makes the bot acts as if no channel was specified
            elif channel == None:
                try:
                    id_channel = ctx.channel.id
                    raw_channels = c1_cur.find({})
                    x = [i for i in raw_channels]
                    channels = [x[i]["channel"] for i in range(len(x))]
                    
                    if id_channel not in channels:
                        up = {"_id":len(channels),
                              "guild":ctx.guild.id,
                              "channel":id_channel,
                              "createtime":"",
                              "timegap":0}

                        c1_cur.insert_one(up)
                        
                        await ctx.send(f"C1 has been activated in {ctx.channel.mention}")

                    else:
                        await ctx.send(f"C1 is already running in {ctx.channel.mention}")
                except:
                    pass

        else:
            await ctx.send(f"**Access Denied!** \nThis command requires `manage_channel` permission in order to execute.")


    #set a channel where you are gonna give your announcement commands
    @activate.command(aliases = ["announce_ch","ach"])
    async def Announcement_ch(self,ctx, channel:discord.TextChannel = None):
        au = ctx.author.id
        ch = ctx.channel.id

        raw = anc_cur.find({})
        guilds = []
        channels = []
        try:
            x = [i for i in raw]
            guilds = [x[i]["guild"] for i in range(len(x))]
            channels = [x[i]["channel"] for i in range(len(x))]
        except:
            pass

        print(guilds)
        if ctx.guild.id in guilds:

            channel_id = anc_cur.find_one({"guild":ctx.guild.id})
            channel = self.client.get_channel(channel_id["channel"])
            
            await ctx.send(f"{channel.mention} is already set as the **Announcement Command Channel**. Would you like to change it? (Type: Y/N)")
            
            text = await self.client.wait_for("message")
            while text.author.id != au:
                text = await self.client.wait_for("message")
                pass

            if text.author.id == au and text.channel.id ==ch:
                answer = text.content.lower()
                y_matches = ["yes","y"]
                n_matches = ["no","n"]
                m = ["yes","y","no","n"]

                if answer in y_matches:
                    await ctx.send("Please mention the channel below_")
                    mention = await self.client.wait_for("message")
                    while not (text.author.id == au and text.channel.id == ch):
                        mention = await self.client.wait_for("message")
                        pass

                    ch1 = mention.content.split("#")
                    print(ch1)
                    ch2 = ch1[1].split(">")
                    ch3 = int(ch2[0])
                    lower = mention.content.lower()

                    if lower != "eliminate":
                        try:
                            channel1 = self.client.get_channel(ch3)
                            anc_cur.update_one({"guild":ctx.guild.id},{"$set":{"channel":ch3}})
                            await ctx.send(f"**Announcement Command Channel** has been updated to {channel1.mention}.")
                        except:
                            await ctx.send("Argument ERROR!")

                if answer in n_matches:
                    await ctx.send("Granted!")

                if answer not in m:
                    await ctx.send("Input ERROR")

        if ctx.guild.id not in guilds:
            if channel == None:
                raw = anc_cur.find({})
                leng = [x for x in raw]
                anc_cur.insert_one({"_id": len(leng),
                                    "guild":ctx.guild.id,
                                    "channel": ctx.channel.id}) 
                await ctx.send(f"{ctx.channel.mention} has been set as an **Announcement Command Channel**")

            if channel != None:
                raw = anc_cur.find({})
                leng = [x for x in raw]
                anc_cur.insert_one({"_id": len(leng),
                                    "guild":ctx.guild.id,
                                    "channel": channel.id})
                await ctx.send(f"{channel.mention} has been set as an **Announcement Command Channel**")

    #this is the command using which you are going to set the announcement channel
    @activate.command(aliases = ["announce","announcement_channel"])
    async def announcement(self,ctx,channel:discord.TextChannel = None):

        raw = anch_cur.find({})

        channels = []
        try:
            x = [i for i in raw]
            channels = [x[i]["channel"] for i in range(len(x))]
        except:
            pass

        raw = anc_cur.find({})
        anc = [x for x in raw]
        x = [anc[i]["guild"] for i in range(len(anc))]

        if ctx.author.guild_permissions.administrator or ctx.author.guild_permissions.manage_channels:
            if ctx.guild.id in x:

                if channel.id in channels:
                    await ctx.send(f"{channel.mention} is already set as an **Announcement Channel**.")

                else:
                    channel_id = channel.id
                    guild_id = ctx.guild.id

                    ctx_channel = self.client.get_channel(ctx.channel.id)
                    text = await ctx_channel.history(limit = 2).flatten()
                    raw = anch_cur.find({})
                    x = [i for i in raw]
                    a_channels = [x[i]["channel"] for i in range(len(x))]
                    print(a_channels)
                    if len(channels) <10:
                        if channel_id not in a_channels:
                            raw = anch_cur.find({})
                            raw_count = [i for i in raw]

                            up = {"_id":len(raw_count),
                                  "guild":ctx.guild.id,
                                  "channel":channel_id}
                            anch_cur.insert_one(up)
                            await text[0].add_reaction("✅") 
                            await ctx.send("Channel Added!")

                    if channel_id in a_channels:
                        await text[0].add_reaction("❎")
                        await ctx.send(f"{channel.mention} is already set as an announcement channel.")

                    if len(a_channels) == 10:
                        await ctx.send("You can have up to 10 announcement channels.")
                
            elif ctx.guild.id not in x:
                raw = anc_cur.find_one({"guild":ctx.guild.id})
                m_ch = raw["channel"]
                
                if len(m_ch) > 1:
                    ch = client.get_channel(m_ch[0])
                    ch2 = client.get_channel(m_ch[1])
                    await ctx.send(f"You are giving command on wrong channel. Please type command here, {ch.mention} or {ch2.mention}")
                
                if len(m_ch) == 1:
                    ch = self.client.get_channel(m_ch[0])
                    await ctx.send(f"You are giving command on wrong channel. Please type command here, {ch.mention}")
            
            elif ctx.guild.id not in guilds:
                await ctx.send("No channel of this server is set as **Announcement Command Channel**.\nPlease set one using this command `.o set announce_ch 'channel mention'`")

        else:
            await ctx.send(f"**Access Denied!** \nThis command requires `manage_channel` permission in order to execute.")


    @activate.command(aliases = ["fibo"])
    async def fibonacci(self,ctx, channel:discord.TextChannel = None):
        raw = fc_cur.find({})

        
        guilds = []
        channels = []
        try:
            x = [i for i in raw]
            guilds = [x[i]["guild"] for i in range(len(x))]
            channels = [x[i]["channel"] for i in range(len(x))]
        except:
            pass

        print(guilds)
        print(channels)
        if ctx.author.guild_permissions.manage_channels:
            if channel == None:
                id_channel = ctx.channel.id
                if ctx.guild.id not in guilds:
                    up = {"_id":len(guilds),
                          "guild":ctx.guild.id,
                          "channel":id_channel,
                          "past":0,
                          "last":0,
                          "author":0}
                    fc_cur.insert_one(up)
                    await ctx.send(f"Fibonacci Counting channel has been updated to {ctx.channel.mention}")
                
                if ctx.guild.id in guilds and id_channel in channels:
                    await ctx.send("This channel is already set as Fibonacci Counting channel.")
                
                if ctx.guild.id in guilds and id_channel not in channels:
                    up = {"_id":len(guilds),
                          "guild":ctx.guild.id,
                          "channel":id_channel,
                          "past":0,
                          "last":0,
                          "author":0}
                    fc_cur.insert_one(up)
                    await ctx.send(f"Fibonacci Counting channel has been update to {ctx.channel.mention}")

            if channel != None:
                try:
                    id_channel = channel.id
                    if ctx.guild.id not in guilds:
                        up = {"_id":len(guilds),
                          "guild":ctx.guild.id,
                          "channel":id_channel,
                          "past":0,
                          "last":0,
                          "author":0}
                        fc_cur.insert_one(up)
                        await ctx.send(f"Fibonacci Counting channel has been updated to {ctx.channel.mention}")
                    
                    if ctx.guild.id in guilds and id_channel in channels:
                        await ctx.send("This channel is already set as Fibonacci Counting channel.")
                    
                    if ctx.guild.id in guilds and id_channel not in channels:
                        fc_cur.update_one({"guild":ctx.guild.id}, {"$set":{"channel":id_channel}})
                        await ctx.send(f"Fibonacci Counting channel has been update to {channel.mention}")
                except:
                    await ctx.send(f"Argument ERROR!")

        else:
            await ctx.send("**Access Denied!** \nThis command requires `manage_channel` permission in order to execute.")


    @activate.command(aliases = ["tictac","tictactoe"])
    async def tic(self,ctx, channel: discord.TextChannel = None):
        raw = tc_cur.find({})
        guilds = []
        channels = []
        try:
            x = [i for i in raw]
            guilds = [x[i]["guild"] for i in range(len(x))]
            channels = [x[i]["channel"] for i in range(len(x))]
        except:
            pass

        if ctx.author.guild_permissions.manage_channels:
            if channel == None:
                    if ctx.guild.id not in guilds:
                        up = {"_id":len(guilds),
                              "guild":ctx.guild.id,
                              "channel":ctx.channel.id}
                        tc_cur.insert_one(up)
                        await ctx.send(f"**TicTacToe** channel has been updated to {ctx.channel.mention}")

                    if ctx.guild.id in guilds and ctx.channel.id in channels:
                        await ctx.send("This channel is already set as **TicTacToe** channel.")
            
                    if ctx.guild.id in guilds and ctx.channel.id not in channels:
                        tc_cur.update_one({"guild":ctx.guild.id}, {"$set":{"channel":ctx.channel.id}})                    
                        await ctx.send(f" TicTacToe channel has been updated to {ctx.channel.mention}")
                    
            elif channel != None:
                try:
                    if ctx.guild.id not in guilds:
                        up = [{"_id":len(guilds),
                              "guild":ctx.guild.id,
                              "channel":channel.id}]
                        tc_cur.insert_one(up)

                        await ctx.send(f"**TicTacToe** channel has been updated to {channel.mention}")
                    
                    if ctx.guild.id in guilds and channel.id in channels:
                        await ctx.send("This channel is already set as **TicTacToe** channel.")
                    
                    if ctx.guild.id in guilds and ctx.channel.id not in channels:
                        tc_cur.update_one({"guild":ctx.guild.id}, {"$set":{"channel":channel.id}})
                        await ctx.send(f" TicTacToe channel has been updated to {channel.mention}")
                
                except:
                    await ctx.send(f"Argument ERROR!")
                
        else:
            await ctx.send("**Access Denied!** \nThis command requires `manage_channel` permission in order to execute.")

    @activate.command(aliases = ["battleship"])
    async def bs(self,ctx, channel: discord.TextChannel = None):
        raw = bc_cur.find({})
        guilds = []
        channels = []
        try:
            x = [i for i in raw]
            guilds = [x[i]["guild"] for i in range(len(x))]
            channels = [x[i]["channel"] for i in range(len(x))]
        except:
            pass

        if ctx.author.guild_permissions.manage_channels:
            if channel != None:
                try:
                    if ctx.guild.id not in guilds:
                        up = {"_id":len(guilds),
                              "guild":ctx.guild.id,
                              "channel":channel.id}
                        bc_cur.insert_one(up)
                        await ctx.send(f"**Battleship** channel has been updated to {channel.mention}")

                    if ctx.guild.id in guilds and channel.id in channels:
                        await ctx.send("This channel is already set as **Battleship** channel.")
                    
                    if ctx.guild.id in guilds and channel.id not in channels:
                        bc_cur.update_one({"guild":ctx.guild.id}, {"$set":{"channel":channel.id}})
                        await ctx.send(f" **Battleship** channel has been updated to {channel.mention}")

                except:
                    await ctx.send(f"Argument ERROR!")


            if channel == None:
                if ctx.guild.id not in guilds:
                    up = {"_id":len(guilds),
                              "guild":ctx.guild.id,
                              "channel":ctx.channel.id}
                    bc_cur.insert_one(up)
                    await ctx.send(f"**Battleship** channel has been updated to {ctx.channel.mention}")

                if ctx.guild.id in guilds and ctx.channel.id in channels:
                    await ctx.send("This channel is already set as **Battleship** channel.")

                if ctx.guild.id in guilds and ctx.channel.id not in channels:
                    bc_cur.update_one({"guild":ctx.guild.id}, {"$set":{"channel":ctx.channel.id}})
                    await ctx.send(f" **Battleship** channel has been updated to {ctx.channel.mention}")

        else:
            await ctx.send("**Access Denied!** \nThis command requires `manage_channel` permission in order to execute.")

    @activate.command(aliases = ["wiki"])
    async def Wikipedia(self,ctx,channel:discord.TextChannel = None):
        raw = wc_cur.find({})
        guilds = []
        channels = []
        try:
            x = [i for i in raw]
            guilds = [x[i]["guild"] for i in range(len(x))]
            channels = [x[i]["channel"] for i in range(len(x))]
        except:
            pass

        if channel == None:
            try:
                if ctx.guild.id not in guilds:
                        up = {"_id":len(guilds),
                              "guild":ctx.guild.id,
                              "channel":ctx.channel.id}
                        wc_cur.insert_one(up)
                        await ctx.send(f"**Wikipedia** channel has been updated to {ctx.channel.mention}.")

                if ctx.guild.id in guilds and ctx.channel.id in channels:
                    await ctx.send("This channel is already set as **Wikipedia** channel.")

                if ctx.guild.id in guilds and ctx.channel.id not in channels:
                        wc_cur.update_one({"guild":ctx.guild.id}, {"$set":{"channel":ctx.channel.id}})
                        await ctx.send(f"**Wikipedia** channel has been updated to {ctx.channel.mention}.")
            except:
                ctx.send("Argument ERROR!")

        if channel != None:
            try:
                if ctx.guild.id not in guilds:
                        up = {"_id":len(guilds),
                              "guild":ctx.guild.id,
                              "channel":channel.id}
                        wc_cur.insert_one(up)
                        await ctx.send(f"**Wikipedia** channel has been updated to {channel.mention}.")

                if ctx.guild.id in guilds and channel.id in channels:
                    await ctx.send("This channel is already set as **Wikipedia** channel.")

                if ctx.guild.id in guilds and channel.id not in channels:
                        wc_cur.update_one({"guild":ctx.guild.id}, {"$set":{"channel":channel.id}})
                        await ctx.send(f"**Wikipedia** channel has been updated to {channel.mention}.")
                        
            except:
                ctx.send("Argument ERROR!")

def setup(client):
    client.add_cog(A_1(client))