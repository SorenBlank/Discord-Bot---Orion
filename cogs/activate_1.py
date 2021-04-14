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
from PIL import Image
from io import BytesIO
import numpy as np
import re
import pymongo
from pymongo import MongoClient

cluster = MongoClient("mongodb+srv://soren:cdD2_qWUYRk-d4G@orion.iztml.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
base = cluster["OrionDB"]

fc_cur = base["fc"]
tc_cur = base["tc"]
bc_cur = base["bc"]
tic_cur = base["tic"]
ta_cur = base["ta"]
weclome_cur = base["welcome"]
bye_cur = base["bye"]
c_cur = base["c"] #Formation = [Guild, Channel, Past_Number, Last_Number, Author]

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
= = = = = = =| Help - [Activate] |= = = = = = =',description="\
:white_small_square: The `[` and `]` around the argument mean it’s required.\n\
:white_small_square: The `(` and `)` around the argument mean it’s optional.\n\
-   -   -   -   -   -   -   -   -   -   -   -   -   -   -   -   -   -   -   -")


        #SECOND FIELD
        activator_embed.add_field(name=":card_box:SERVER UTILITIES:card_box:",
                                  value = "------------ :arrow_down_small: ------------",
                                  inline= False)

        activator_embed.add_field(name = ":hammer_pick: Welcome Message",
                                  value = ":small_orange_diamond: A channel and message where Orion will welcome new comers.\nType '#member' inside the message in order to mention the member.\n**__Command:__** `.o set welcome [channel] [message]`",
                                  inline = False)

        activator_embed.add_field(name=":hammer_pick: Bye Message",
                                  value = ":small_orange_diamond: A channel and message where Orion will send bye message.\nType '#member' inside the message in order to mention the member.\n**__Command:__** `.o set bye [channel] [message]`",
                                  inline = False)

        activator_embed.add_field(name=" ឵឵ ",value=" ឵឵ ",inline=False)


        #THIRD FIELD
        activator_embed.add_field(name=":video_game:GAMES:video_game:",
                                  value="------ :arrow_down_small: -----",
                                  inline=False)
        activator_embed.add_field(name=":large_blue_diamond: Fibonacci/Fibo",
                                  value=":small_blue_diamond: A channel where you can count up but in Fibonacci series.\n**__Command:__** `.o activate fibo (channel)`",inline=False)
        activator_embed.add_field(name=":large_blue_diamond: TicTacToe",
                                  value=":small_blue_diamond: A channel for playing tictactoe.\n**__Command:__** `.o activate tic (channel)`",
                                  inline=False)
        activator_embed.add_field(name=":large_blue_diamond: Battleship (BETA)",
                                  value=':small_blue_diamond: A channel for playing battleship.\n**__Command:__** `.o activate battleship (channel)`',
                                  inline = False)
        
        activator_embed.add_field(name=" ឵឵ ",value=" ឵឵ ",inline=False)


        activator_embed.add_field(name=":book:PHILOSOPHY:book:",
                                  value="---------- :arrow_down_small: ---------",
                                  inline=False)
        activator_embed.add_field(name=":orange_book: Wikipedia",
                                  value=":small_orange_diamond: A channel for wikipedia search.\n**__Command:__** `.o activate wiki (channel)`",
                                  inline=False)

        await ctx.send(embed = activator_embed)


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

    @activate.command(aliases = ["count"])
    async def countup(self,ctx,channel:discord.TextChannel = None):
        raw = c_cur.find({})
        
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
                id_channel = ctx.channel.id
                if ctx.guild.id not in guilds:
                    up = {"_id":len(guilds),
                          "guild":ctx.guild.id,
                          "channel":id_channel,
                          "last":0,
                          "highest":0,
                          "author":0}
                    c_cur.insert_one(up)
                    await ctx.send(f"Countup channel has been updated to {ctx.channel.mention}")
                
                if ctx.guild.id in guilds and id_channel in channels:
                    await ctx.send("This channel is already set as Countup channel.")
                
                if ctx.guild.id in guilds and id_channel not in channels:
                    c_cur.update_one({"guild":ctx.guild.id},{"$set":{"channel":ctx.channel.id}})
                    await ctx.send(f"Countup channel has been update to {ctx.channel.mention}")

            if channel != None:
                try:
                    id_channel = channel.id
                    if ctx.guild.id not in guilds:
                        up = {"_id":len(guilds),
                          "guild":ctx.guild.id,
                          "channel":id_channel,
                          "last":0,
                          "highest":0,
                          "author":0}
                        c_cur.insert_one(up)
                        await ctx.send(f"Countup channel has been updated to {ctx.channel.mention}")
                    
                    if ctx.guild.id in guilds and id_channel in channels:
                        await ctx.send("This channel is already set as Countup channel.")
                    
                    if ctx.guild.id in guilds and id_channel not in channels:
                        c_cur.update_one({"guild":ctx.guild.id}, {"$set":{"channel":id_channel}})
                        await ctx.send(f"Countup channel has been update to {channel.mention}")
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

    @activate.command()
    async def welcome(self,ctx,channel:discord.TextChannel = None,*,message):
        raw = weclome_cur.find({})
        guilds = []
        channels = []
        try:
            x = [i for i in raw]
            guilds = [x[i]["guild"] for i in range(len(x))]
            channels = [x[i]["channel"] for i in range(len(x))]
        except:
            pass

        if ctx.author.guild_permissions.manage_guild:
            try:
                if ctx.guild.id not in guilds:
                        up = {"_id":len(guilds),
                              "guild":ctx.guild.id,
                              "channel":channel.id,
                              "message":message}
                        weclome_cur.insert_one(up)
                        await ctx.send(f"**WELCOME** channel has been set to {channel.mention}.\n**WELCOME** message is ```{message}```")

                if ctx.guild.id in guilds and channel.id in channels:
                    weclome_cur.update_one({"guild":ctx.guild.id}, {"$set":{"message":message}})
                    await ctx.send(f"**WELCOME** message is ```{message}```")

                if ctx.guild.id in guilds and channel.id not in channels:
                        weclome_cur.update_one({"guild":ctx.guild.id}, {"$set":{"channel":channel.id}})
                        weclome_cur.update_one({"guild":ctx.guild.id}, {"$set":{"message":message}})
                        await ctx.send(f"**WELCOME** channel has been updated to {channel.mention}.\n**WELCOME** message is ```{message}```")
            except:
                ctx.send("Argument ERROR!")
        else:
            await ctx.send("**Access Denied!** \nThis command requires `manage_guild` permission in order to execute.")


    @activate.command()
    async def bye(self,ctx,channel:discord.TextChannel = None,*,message):
        raw = bye_cur.find({})
        guilds = []
        channels = []

        try:
            x = [i for i in raw]
            guilds = [x[i]["guild"] for i in range(len(x))]
            channels = [x[i]["channel"] for i in range(len(x))]
        except:
            pass

        if ctx.author.guild_permissions.manage_guild:
            try:
                if ctx.guild.id not in guilds:
                        up = {"_id":len(guilds),
                              "guild":ctx.guild.id,
                              "channel":channel.id,
                              "message":message}
                        bye_cur.insert_one(up)
                        await ctx.send(f"**BYE** channel has been set to {channel.mention}.\n**BYE** message is ```{message}```")

                if ctx.guild.id in guilds and channel.id in channels:
                    bye_cur.update_one({"guild":ctx.guild.id}, {"$set":{"message":message}})
                    await ctx.send(f"**BYE** message is ```{message}```")

                if ctx.guild.id in guilds and channel.id not in channels:
                        bye_cur.update_one({"guild":ctx.guild.id}, {"$set":{"channel":channel.id}})
                        bye_cur.update_one({"guild":ctx.guild.id}, {"$set":{"message":message}})
                        await ctx.send(f"**BYE** channel has been updated to {channel.mention}.\n**BYE** message is ```{message}```")
            except:
                ctx.send("Argument ERROR!")
        else:
            await ctx.send("**Access Denied!** \nThis command requires `manage_guild` permission in order to execute.")

def setup(client):
    client.add_cog(A_1(client))