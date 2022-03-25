                                ###################
                                #importing modules#
                                ###################

#importing discord modules
from threading import active_count
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
import urllib
import requests
import pymongo
from pymongo import MongoClient
from youtube_search import YoutubeSearch
import cv2 as cv
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from PIL import Image
from io import BytesIO
import imageio

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
banner_cur = base["banner"] #Formation = [Guild, Banner Byte]

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
        return

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
                    up = {"_id":len(guilds)+1,
                          "guild":ctx.guild.id,
                          "channel":id_channel,
                          "past":0,
                          "last":0,
                          "author":0}
                    fc_cur.insert_one(up)
                    embed = discord.Embed(color = 0x5865F2, description = f"Fibonacci Countup channel has been updated to: {ctx.channel.mention}.")
                    embed.set_author(name = "Set Successful!", icon_url = self.client.user.avatar_url)
                    await ctx.send(embed = embed)
                
                if ctx.guild.id in guilds and id_channel in channels:
                    embed = discord.Embed(color = 0x5865F2,description = f"{ctx.channel.mention} is already set as `fibonacci countup` channel.")
                    embed.set_author(name = "Overwrite ERROR", icon_url= self.client.user.avatar_url)
                    await ctx.send(embed = embed)

                if ctx.guild.id in guilds and id_channel not in channels:
                    up = {"_id":len(guilds)+1,
                          "guild":ctx.guild.id,
                          "channel":id_channel,
                          "past":0,
                          "last":0,
                          "author":0}
                    fc_cur.insert_one(up)
                    embed = discord.Embed(color = 0x5865F2, description = f"Fibonacci Countup channel has been updated to: {ctx.channel.mention}.")
                    embed.set_author(name = "Update Successful!", icon_url = self.client.user.avatar_url)
                    await ctx.send(embed = embed)

            if channel != None:
                try:
                    id_channel = channel.id
                    if ctx.guild.id not in guilds:
                        up = {"_id":len(guilds)+1,
                          "guild":ctx.guild.id,
                          "channel":id_channel,
                          "past":0,
                          "last":0,
                          "author":0}
                        fc_cur.insert_one(up)
                        embed = discord.Embed(color = 0x5865F2, description = f"Fibonacci Countup channel has been updated to: {channel.mention}.")
                        embed.set_author(name = "Set Successful!", icon_url = self.client.user.avatar_url)
                        await ctx.send(embed = embed)

                    if ctx.guild.id in guilds and id_channel in channels:
                        embed = discord.Embed(color = 0x5865F2,description = f"{channel.mention} is already set as `fibonacci countup` channel.")
                        embed.set_author(name = "Overwrite ERROR", icon_url= self.client.user.avatar_url)
                        await ctx.send(embed = embed)

                    if ctx.guild.id in guilds and id_channel not in channels:
                        fc_cur.update_one({"guild":ctx.guild.id}, {"$set":{"channel":id_channel}})
                        embed = discord.Embed(color = 0x5865F2, description = f"Fibonacci Countup channel has been updated to: {channel.mention}.")
                        embed.set_author(name = "Update Successful!", icon_url = self.client.user.avatar_url)
                        await ctx.send(embed = embed)

                except:
                    embed = discord.Embed(color = 0x5865F2, description = "Please provide required arguments.")
                    embed.set_author(name = "Argument EROOR",icon_url = self.client.user.avatar_url)
                    await ctx.send(embed = embed)

        else:
            embed = discord.Embed(color = 0x5865F2, description = f"This command requires `manage_channel` permission in order to execute.")
            embed.set_author(name = "Access Denied", icon_url = self.client.user.avatar_url)
            await ctx.send(embed = embed)

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
                    up = {"_id":len(guilds)+1,
                          "guild":ctx.guild.id,
                          "channel":id_channel,
                          "last":0,
                          "highest":0,
                          "author":0}
                    c_cur.insert_one(up)
                    embed = discord.Embed(color = 0x5865F2, description = f"Countup channel has been updated to: {ctx.channel.mention}.")
                    embed.set_author(name = "Set Successful!", icon_url = self.client.user.avatar_url)
                    await ctx.send(embed = embed)
                
                if ctx.guild.id in guilds and id_channel in channels:
                    embed = discord.Embed(color = 0x5865F2,description = f"{ctx.channel.mention} is already set as `countup` channel.")
                    embed.set_author(name = "Overwrite ERROR", icon_url= self.client.user.avatar_url)
                    await ctx.send(embed = embed)
                
                if ctx.guild.id in guilds and id_channel not in channels:
                    c_cur.update_one({"guild":ctx.guild.id},{"$set":{"channel":ctx.channel.id}})
                    embed = discord.Embed(color = 0x5865F2, description = f"Countup channel has been updated to: {ctx.channel.mention}.")
                    embed.set_author(name = "Update Successful!", icon_url = self.client.user.avatar_url)
                    await ctx.send(embed = embed)

            if channel != None:
                try:
                    id_channel = channel.id
                    if ctx.guild.id not in guilds:
                        up = {"_id":len(guilds)+1,
                          "guild":ctx.guild.id,
                          "channel":id_channel,
                          "last":0,
                          "highest":0,
                          "author":0}
                        c_cur.insert_one(up)
                        embed = discord.Embed(color = 0x5865F2, description = f"Countup channel has been updated to: {ctx.channel.mention}.")
                        embed.set_author(name = "Set Successful!", icon_url = self.client.user.avatar_url)
                        await ctx.send(embed = embed)

                    if ctx.guild.id in guilds and id_channel in channels:
                        embed = discord.Embed(color = 0x5865F2,description = f"{ctx.channel.mention} is already set as `countup` channel.")
                        embed.set_author(name = "Overwrite ERROR", icon_url= self.client.user.avatar_url)
                        await ctx.send(embed = embed)
                    
                    if ctx.guild.id in guilds and id_channel not in channels:
                        c_cur.update_one({"guild":ctx.guild.id}, {"$set":{"channel":id_channel}})
                        embed = discord.Embed(color = 0x5865F2, description = f"Countup channel has been updated to: {channel.mention}.")
                        embed.set_author(name = "Update Successful!", icon_url = self.client.user.avatar_url)
                        await ctx.send(embed = embed)
                except:
                    embed = discord.Embed(color = 0x5865F2, description = "Please provide required arguments.")
                    embed.set_author(name = "Argument EROOR",icon_url = self.client.user.avatar_url)
                    await ctx.send(embed = embed)

        else:
            embed = discord.Embed(color = 0x5865F2, description = f"This command requires `manage_channel` permission in order to execute.")
            embed.set_author(name = "Access Denied", icon_url = self.client.user.avatar_url)
            await ctx.send(embed = embed)


    # @activate.command(aliases = ["tictac","tictactoe"])
    # async def tic(self,ctx, channel: discord.TextChannel = None):
    #     raw = tc_cur.find({})
    #     guilds = []
    #     channels = []
    #     try:
    #         x = [i for i in raw]
    #         guilds = [x[i]["guild"] for i in range(len(x))]
    #         channels = [x[i]["channel"] for i in range(len(x))]
    #     except:
    #         pass

    #     if ctx.author.guild_permissions.manage_channels:
    #         if channel == None:
    #                 if ctx.guild.id not in guilds:
    #                     up = {"_id":len(guilds),
    #                           "guild":ctx.guild.id,
    #                           "channel":ctx.channel.id}
    #                     tc_cur.insert_one(up)
    #                     await ctx.send(f"**TicTacToe** channel has been updated to {ctx.channel.mention}")

    #                 if ctx.guild.id in guilds and ctx.channel.id in channels:
    #                     await ctx.send("This channel is already set as **TicTacToe** channel.")
            
    #                 if ctx.guild.id in guilds and ctx.channel.id not in channels:
    #                     tc_cur.update_one({"guild":ctx.guild.id}, {"$set":{"channel":ctx.channel.id}})                    
    #                     await ctx.send(f" TicTacToe channel has been updated to {ctx.channel.mention}")
                    
    #         elif channel != None:
    #             try:
    #                 if ctx.guild.id not in guilds:
    #                     up = [{"_id":len(guilds),
    #                           "guild":ctx.guild.id,
    #                           "channel":channel.id}]
    #                     tc_cur.insert_one(up)

    #                     await ctx.send(f"**TicTacToe** channel has been updated to {channel.mention}")
                    
    #                 if ctx.guild.id in guilds and channel.id in channels:
    #                     await ctx.send("This channel is already set as **TicTacToe** channel.")
                    
    #                 if ctx.guild.id in guilds and ctx.channel.id not in channels:
    #                     tc_cur.update_one({"guild":ctx.guild.id}, {"$set":{"channel":channel.id}})
    #                     await ctx.send(f" TicTacToe channel has been updated to {channel.mention}")
                
    #             except:
    #                 await ctx.send(f"Argument ERROR!")
                
    #     else:
    #         await ctx.send("**Access Denied!** \nThis command requires `manage_channel` permission in order to execute.")

    # @activate.command(aliases = ["battleship"])
    # async def bs(self,ctx, channel: discord.TextChannel = None):
    #     raw = bc_cur.find({})
    #     guilds = []
    #     channels = []
    #     try:
    #         x = [i for i in raw]
    #         guilds = [x[i]["guild"] for i in range(len(x))]
    #         channels = [x[i]["channel"] for i in range(len(x))]
    #     except:
    #         pass

    #     if ctx.author.guild_permissions.manage_channels:
    #         if channel != None:
    #             try:
    #                 if ctx.guild.id not in guilds:
    #                     up = {"_id":len(guilds),
    #                           "guild":ctx.guild.id,
    #                           "channel":channel.id}
    #                     bc_cur.insert_one(up)
    #                     await ctx.send(f"**Battleship** channel has been updated to {channel.mention}")

    #                 if ctx.guild.id in guilds and channel.id in channels:
    #                     await ctx.send("This channel is already set as **Battleship** channel.")
                    
    #                 if ctx.guild.id in guilds and channel.id not in channels:
    #                     bc_cur.update_one({"guild":ctx.guild.id}, {"$set":{"channel":channel.id}})
    #                     await ctx.send(f" **Battleship** channel has been updated to {channel.mention}")

    #             except:
    #                 await ctx.send(f"Argument ERROR!")


    #         if channel == None:
    #             if ctx.guild.id not in guilds:
    #                 up = {"_id":len(guilds),
    #                           "guild":ctx.guild.id,
    #                           "channel":ctx.channel.id}
    #                 bc_cur.insert_one(up)
    #                 await ctx.send(f"**Battleship** channel has been updated to {ctx.channel.mention}")

    #             if ctx.guild.id in guilds and ctx.channel.id in channels:
    #                 await ctx.send("This channel is already set as **Battleship** channel.")

    #             if ctx.guild.id in guilds and ctx.channel.id not in channels:
    #                 bc_cur.update_one({"guild":ctx.guild.id}, {"$set":{"channel":ctx.channel.id}})
    #                 await ctx.send(f" **Battleship** channel has been updated to {ctx.channel.mention}")

    #     else:
    #         await ctx.send("**Access Denied!** \nThis command requires `manage_channel` permission in order to execute.")

    @activate.command()
    async def welcome(self,ctx,channel:discord.TextChannel = None,*,message = None):
        raw = weclome_cur.find({})
        guilds = []
        channels = []
        try:
            x = [i for i in raw]
            guilds = [x[i]["guild"] for i in range(len(x))]
            channels = [x[i]["channel"] for i in range(len(x))]
        except:
            pass

        if ctx.author.guild_permissions.manage_guild or ctx.author.guild_permissions.administrator:
            # try:
            if ctx.guild.id not in guilds:
                up = {"guild":ctx.guild.id,
                      "channel":channel.id,
                      "message":message}
                weclome_cur.insert_one(up)
                embed = discord.Embed(color = 0x5865F2, description = f"__Welcome channel:__ {channel.mention}.\n__Welcome message:__ ```\n{message}```")
                embed.set_author(name = "Set Successful!", icon_url = self.client.user.avatar_url)
                await ctx.send(embed = embed)

            if ctx.guild.id in guilds and channel.id in channels:
                weclome_cur.update_one({"guild":ctx.guild.id}, {"$set":{"message":message}})
                embed = discord.Embed(color = 0x5865F2, description = f"__Welcome message:__ ```\n{message}```")
                embed.set_author(name = "Update Successful!", icon_url = self.client.user.avatar_url)
                await ctx.send(embed = embed)

            if ctx.guild.id in guilds and channel.id not in channels:
                weclome_cur.update_one({"guild":ctx.guild.id}, {"$set":{"channel":channel.id}})
                weclome_cur.update_one({"guild":ctx.guild.id}, {"$set":{"message":message}})
                embed = discord.Embed(color = 0x5865F2, description = f"__Welcome channel:__ {channel.mention}.\n__Welcome message:__ ```\n{message}```")
                embed.set_author(name = "Update Successful!", icon_url = self.client.user.avatar_url)
                await ctx.send(embed = embed)
            # except:
            #     await ctx.send("Argument ERROR!")
        else:
            embed = discord.Embed(color = 0x5865F2, description = f"This command requires `manage_guild` permission in order to execute.")
            embed.set_author(name = "Access Denied", icon_url = self.client.user.avatar_url)
            await ctx.send(embed = embed)


    @activate.command()
    async def bye(self,ctx,channel:discord.TextChannel = None,*,message = None):
        raw = bye_cur.find({})
        guilds = []
        channels = []

        try:
            x = [i for i in raw]
            guilds = [x[i]["guild"] for i in range(len(x))]
            channels = [x[i]["channel"] for i in range(len(x))]
        except:
            pass

        if ctx.author.guild_permissions.manage_guild or ctx.author.guild_permissions.administrator:
            try:
                if ctx.guild.id not in guilds:
                    up = {"guild":ctx.guild.id,
                          "channel":channel.id,
                          "message":message}
                    bye_cur.insert_one(up)
                    embed = discord.Embed(color = 0x5865F2, description = f"__Bye channel:__ {channel.mention}.\n__Bye message:__ ```\n{message}```")
                    embed.set_author(name = "Set Successful!", icon_url = self.client.user.avatar_url)
                    await ctx.send(embed = embed)

                if ctx.guild.id in guilds and channel.id in channels:
                    bye_cur.update_one({"guild":ctx.guild.id}, {"$set":{"message":message}})
                    embed = discord.Embed(color = 0x5865F2, description = f"__Bye message:__ ```\n{message}```")
                    embed.set_author(name = "Update Successful!", icon_url = self.client.user.avatar_url)
                    await ctx.send(embed = embed)

                if ctx.guild.id in guilds and channel.id not in channels:
                    bye_cur.update_one({"guild":ctx.guild.id}, {"$set":{"channel":channel.id}})
                    bye_cur.update_one({"guild":ctx.guild.id}, {"$set":{"message":message}})
                    embed = discord.Embed(color = 0x5865F2, description = f"__Bye channel:__ {channel.mention}.\n__Bye message:__ ```\n{message}```")
                    embed.set_author(name = "Update Successful!", icon_url = self.client.user.avatar_url)
                    await ctx.send(embed = embed)
            except:
                embed = discord.Embed(color = 0x5865F2, description = "Please provide required arguments.")
                embed.set_author(name = "Argument EROOR",icon_url = self.client.user.avatar_url)
                await ctx.send(embed = embed)
        else:
            embed = discord.Embed(color = 0x5865F2, description = f"This command requires `manage_guild` permission in order to execute.")
            embed.set_author(name = "Access Denied", icon_url = self.client.user.avatar_url)
            await ctx.send(embed = embed)


    @activate.command()
    async def banner(self,ctx,link = ""):
        if ctx.author.guild_permissions.manage_guild or ctx.author.guild_permissions.administrator:
            exist = banner_cur.find_one({"guild":ctx.guild.id})
            if exist == None:
                colors = ["blurple","red","green","yellow","fuchsia","black","white","cyan","cyan1","cyan2"]
                if link:
                    try:
                        response = requests.get(link)
                        up = {"guild":ctx.guild.id,
                            "circle_color" : "white",
                            "welcome_color": "white",
                            "name_color": "white",
                            "banner": response.content}
                        banner_cur.insert_one(up)
                        embed = discord.Embed(color = 0x5865F2, description = f"`welcome banner` has been set successfully.")
                        embed.set_author(name = "Set Successful!", icon_url = self.client.user.avatar_url)
                        await ctx.send(embed = embed)

                    except:
                        embed = discord.Embed(color = 0x5865F2,description = "Failed to fetch the image. Please make sure the link is valid.")
                        embed.set_author(name = "INDEX ERROR", icon_url = self.client.user.avatar_url)
                        await ctx.send(embed = embed)
                        return
                else:
                    embed = discord.Embed(color = 0x5865F2, description = "Please provide required arguments.")
                    embed.set_author(name = "Argument EROOR",icon_url = self.client.user.avatar_url)
                    await ctx.send(embed = embed)

            if exist != None:
                colors = ["blurple","red","green","yellow","fuchsia","black","white","cyan","cyan1","cyan2"]
                if link:
                    try:
                        response = requests.get(link)
                        banner_cur.update_one({"guild":ctx.guild.id}, {"$set":{"banner":response.content}})
                        embed = discord.Embed(color = 0x5865F2, description = f"`welcome banner` has been updated successfully.")
                        embed.set_author(name = "Updated Successfully!", icon_url = self.client.user.avatar_url)
                        await ctx.send(embed = embed)
                    except:
                        embed = discord.Embed(color = 0x5865F2,description = "Failed to fetch the image. Please make sure the link is valid.")
                        embed.set_author(name = "INDEX ERROR", icon_url = self.client.user.avatar_url)
                        await ctx.send(embed = embed)
                else:
                    embed = discord.Embed(color = 0x5865F2, description = "Please provide required arguments.")
                    embed.set_author(name = "Argument EROOR",icon_url = self.client.user.avatar_url)
                    await ctx.send(embed = embed)
        else:
            embed = discord.Embed(color = 0x5865F2, description = f"This command requires `manage_guild` permission in order to execute.")
            embed.set_author(name = "Access Denied", icon_url = self.client.user.avatar_url)
            await ctx.send(embed = embed)

    @activate.command()
    async def ringcolor(self, ctx, color):
        if ctx.author.guild_permissions.manage_guild or ctx.author.guild_permissions.administrator:
            exist = banner_cur.find_one({"guild":ctx.guild.id})
            if exist == None:
                embed = discord.Embed(color = 0x5865F2,description = "Banner not found.")
                embed.set_author(name = "Index ERROR", icon_url= self.client.user.avatar_url)
                await ctx.send(embed = embed)
                return
            else:
                colors = ["blurple","blurple-old","blurpleold","red","green","yellow","fuchsia","black","white","cyan","cyan1","cyan2"]
                if color.lower() in colors:
                    banner_cur.update_one({"guild":ctx.guild.id}, {"$set":{"circle_color":color.lower()}})
                    embed = discord.Embed(color = 0x5865F2, description = f"`ringcolor` has been updated successfully.")
                    embed.set_author(name = "Updated Successfully!", icon_url = self.client.user.avatar_url)
                    await ctx.send(embed = embed)

                elif color.lower() not in colors:
                    embed = discord.Embed(color = 0x5865F2,description = "Please pick any color from `blurple` `blurple-old` `red` `green` `yellow` `fuchsia` `black` `white` `cyan`.")
                    embed.set_author(name = "Index ERROR", icon_url= self.client.user.avatar_url)
                    await ctx.send(embed = embed)
                    return
        else:
            embed = discord.Embed(color = 0x5865F2, description = f"This command requires `manage_guild` permission in order to execute.")
            embed.set_author(name = "Access Denied", icon_url = self.client.user.avatar_url)
            await ctx.send(embed = embed)

    @activate.command()
    async def welcomecolor(self,ctx,color):
        if ctx.author.guild_permissions.manage_guild or ctx.author.guild_permissions.administrator:
            exist = banner_cur.find_one({"guild":ctx.guild.id})
            if exist == None:
                embed = discord.Embed(color = 0x5865F2,description = "Banner not found.")
                embed.set_author(name = "Index ERROR", icon_url= self.client.user.avatar_url)
                await ctx.send(embed = embed)
                return
            else:
                colors = ["blurple","blurple-old","blurpleold","red","green","yellow","fuchsia","black","white","cyan","cyan1","cyan2"]
                if color.lower() in colors:
                    banner_cur.update_one({"guild":ctx.guild.id}, {"$set":{"welcome_color":color.lower()}})
                    embed = discord.Embed(color = 0x5865F2, description = f"`welcomecolor` has been updated successfully.")
                    embed.set_author(name = "Updated Successfully!", icon_url = self.client.user.avatar_url)
                    await ctx.send(embed = embed)

                elif color.lower() not in colors:
                    embed = discord.Embed(color = 0x5865F2,description = "Please pick any color from `blurple` `blurple-old` `red` `green` `yellow` `fuchsia` `black` `white` `cyan`.")
                    embed.set_author(name = "Index ERROR", icon_url= self.client.user.avatar_url)
                    await ctx.send(embed = embed)
                    return
        else:
            embed = discord.Embed(color = 0x5865F2, description = f"This command requires `manage_guild` permission in order to execute.")
            embed.set_author(name = "Access Denied", icon_url = self.client.user.avatar_url)
            await ctx.send(embed = embed)
    
    @activate.command()
    async def namecolor(self,ctx,color):
        if ctx.author.guild_permissions.manage_guild or ctx.author.guild_permissions.administrator:
            exist = banner_cur.find_one({"guild":ctx.guild.id})
            if exist == None:
                embed = discord.Embed(color = 0x5865F2,description = "Banner not found.")
                embed.set_author(name = "Index ERROR", icon_url= self.client.user.avatar_url)
                await ctx.send(embed = embed)
                return
            else:
                colors = ["blurple","blurple-old","blurpleold","red","green","yellow","fuchsia","black","white","cyan","cyan1","cyan2"]
                if color.lower() in colors:
                    banner_cur.update_one({"guild":ctx.guild.id}, {"$set":{"name_color":color.lower()}})
                    embed = discord.Embed(color = 0x5865F2, description = f"`namecolor` has been updated successfully.")
                    embed.set_author(name = "Updated Successfully!", icon_url = self.client.user.avatar_url)
                    await ctx.send(embed = embed)

                elif color.lower() not in colors:
                    embed = discord.Embed(color = 0x5865F2,description = "Please pick any color from `blurple` `blurple-old` `red` `green` `yellow` `fuchsia` `black` `white` `cyan`.")
                    embed.set_author(name = "Index ERROR", icon_url= self.client.user.avatar_url)
                    await ctx.send(embed = embed)
                    return
        else:
            embed = discord.Embed(color = 0x5865F2, description = f"This command requires `manage_guild` permission in order to execute.")
            embed.set_author(name = "Access Denied", icon_url = self.client.user.avatar_url)
            await ctx.send(embed = embed)

    @commands.group(invoke_without_command = True,case_insensitive=True)
    async def preview(self,ctx):
        raw = weclome_cur.find_one({"guild":ctx.author.guild.id})
        raw1 = bye_cur.find_one({"guild":ctx.author.guild.id})
        raw2 = banner_cur.find_one({"guild":ctx.author.guild.id})
        embed = discord.Embed(color = 0x5865F2)
        if raw != None:
            channel = raw["channel"]
            channel = self.client.get_channel(channel)
            message = raw["message"]
            embed.add_field(name= "__Welcome Message__", value= f"Channel: {channel.mention}\nMessage:```\n{message}```", inline= False)

        if raw1 != None:
            channel = raw1["channel"]
            channel = self.client.get_channel(channel)
            message = raw1["message"]
            embed.add_field(name= "__Farewell Message__", value= f"__Channel:__ {channel.mention}\n__Message:__```\n{message}```", inline= False)
        
        if raw2!= None:
            banner = BytesIO(raw2["banner"])
            circle_color = raw2["circle_color"]
            welcome_color = raw2["welcome_color"]
            name_color = raw2["name_color"]

            hmm = np.asarray(bytearray(banner.read()), dtype=np.uint8)

            img = cv.imdecode(hmm, cv.IMREAD_COLOR)

            pfp_url = str(ctx.author.avatar_url_as(static_format='png'))
            response = requests.get(pfp_url)

            if ".gif" in pfp_url:
                imdata = response.content
                fname = "tmp.gif"
                imbytes = bytearray(imdata)
                open(fname,"wb+").write(imdata)

                gif = imageio.mimread(fname)

                pfp = cv.cvtColor(gif[0], cv.COLOR_RGB2BGR)
                os.remove(fname)

            if ".gif" not in pfp_url:
                bruh = BytesIO(response.content)
                hmm = np.asarray(bytearray(bruh.read()), dtype=np.uint8)
                pfp = cv.imdecode(hmm, cv.IMREAD_COLOR)

            colors = {"blurple":(242,101,88),
                        "blurpleold":(218,137,114),
                        "blurple-old":(218,137,114),
                        "green":(135,242,87),
                        "red":(69,66,237),
                        "yellow":(92,231,254),
                        "fuchsia":(158,69,235),
                        "white":(255,255,255),
                        "black":(42,39,35),
                        "cyan1":(227,255,37),
                        "cyan":(227,255,37),
                        "cyan2":(255,252,159)}

            # bg_image_path = r"P:\Projects\Jobs\Discord-Bot-XEN\bg.jpg"
            # bg = cv.imread(bg_image_path)

            RATIO = (1024 + 1) / (500 + 1) # width/height

            def crop(img, ratio):
                height, width = img.shape[0:2]
                if width / height == ratio:
                    return img
                new_height, new_width = 0, 0
                if width / height > ratio:
                    new_width = int(ratio * height)
                    new_height = height
                elif width / height < ratio:
                    new_height = int(ratio * width)
                    new_width = width
                top = int((height - new_height)/2)
                left = int((width - new_width)/2)
                return img[top : top + new_height, left : left + new_width]

            bg_crop = crop(img, ratio = RATIO)

            # show(bg_crop)

            bg_crop.shape

            bg_resize = cv.resize(bg_crop, (1024 + 1, 500 + 1))

            # show(bg_resize, showTicks = True)

            height, width = bg_resize.shape[0:2]
            center_coord = (width // 2, height // 3)
            radius = height // 3 - 20

            def transparent_circle(img):
                height, width = img.shape[:2]
                height = int(height)
                width = int(width)

                circ = np.zeros((height, width, 1), np.uint8)
                circ = cv.circle(circ, (width // 2, height // 2), min(height, width) // 2, (1), -1, lineType = cv.LINE_AA)

                result = np.zeros((height, width, 4), np.uint8)

                result[:, :, 0] = np.multiply(img[:, :, 0], circ[:, :, 0])
                result[:, :, 1] = np.multiply(img[:, :, 1], circ[:, :, 0])
                result[:, :, 2] = np.multiply(img[:, :, 2], circ[:, :, 0])

                circ[circ == 1] = 255
                result[:, :, 3] = circ[:, :, 0]

                return result

            # pfp_path = "P:\Projects\Jobs\Discord-Bot-XEN\pfp.jpg"
            # pfp = cv.imread(pfp_path)
            
            pfp_resize = cv.resize(pfp, (radius * 2, radius * 2))


            pfp_png = transparent_circle(pfp_resize)

            #
            # show(bg_resize)
            #
            # pfp_png[0][0]
            # 


            def copyTransparent(mainImage, transparentImage, x, y):
                y1, y2 = y, y + transparentImage.shape[0]
                x1, x2 = x, x + transparentImage.shape[1]

                alpha_s = transparentImage[:, :, 3] / 255.0
                alpha_l = 1.0 - alpha_s

                for c in range(0, 3):
                    mainImage[y1:y2, x1:x2, c] = (alpha_s * transparentImage[:, :, c] + alpha_l * mainImage[y1:y2, x1:x2, c])

                return mainImage

            xc = center_coord[0] - radius
            yc = center_coord[1] - radius
            transparent_copied = copyTransparent(bg_resize.copy(), pfp_png, xc, yc)

            # show(transparent_copied)

            # circle_border_color = (0,0,255) # in BGR
            cv.circle(transparent_copied, center_coord, radius, colors[circle_color], 5,lineType = cv.LINE_AA)
            # show(transparent_copied)

            from PIL import Image, ImageFont, ImageDraw


            def customTextCenter(img, string, fontPath, textSize, fontColor, h):
                font = ImageFont.truetype(fontPath, textSize)

                img_pil = Image.fromarray(img)
                im_width, im_height = img_pil.size

                draw = ImageDraw.Draw(img_pil)

                text_width = draw.textsize(string, font = font)[0]
                textCoord = ((im_width - text_width)/2, h)

                draw.text(textCoord, string, font = font, fill = fontColor)
                return np.array(img_pil)

            #

            FONT_PATH = "./Uni Sans Heavy.ttf"

            # member_name = "atonu_#1514"
            # server_name = "Atonu and Comrades"
            # member_count = str(69)

            hello_string = f"WELCOME"
            welcome_string = f"{ctx.author}"
            # count_string = f"You are the {member_count}-th member of this server."

            after_hello = customTextCenter(transparent_copied, hello_string, FONT_PATH, 90, colors[welcome_color], 2 * (height // 3) - 5)
            # show(after_hello)

            after_welcome = customTextCenter(after_hello, welcome_string, FONT_PATH, 50, colors[name_color], 2 * (height // 3) + 80)
            # show(after_welcome)

            # after_count = customTextCenter(after_welcome, count_string, FONT_PATH, 30, text_col, 2 * (height // 3) + 115)
            # show(after_count)
            cv.imwrite('qwerty.png',after_welcome)
            f = discord.File("./qwerty.png", filename="image.png")
            embed.add_field(name = "__Welcome Banner__", value= f"Ring Color: `{circle_color}`\nWelcome Color: `{welcome_color}`\nName Color: `{name_color}`",inline=False)
            embed.set_image(url = "attachment://image.png") 

        embed.set_author(name = "PREVIEW", icon_url = self.client.user.avatar_url)

        if raw == None and raw1 == None and raw2 == None:
            embed = discord.Embed(color = 0x5865F2, description = "`welcome message`, `farewell message`, `welcome banner` not found.")
            embed.set_author(name = "PREVIEW", icon_url = self.client.user.avatar_url)

        if raw2 == None:
            await ctx.send(embed = embed)
        if raw2 != None:
            await ctx.send(embed = embed, file = f)
            os.remove('qwerty.png')
        else:
            pass
        return



def setup(client):
    client.add_cog(A_1(client))