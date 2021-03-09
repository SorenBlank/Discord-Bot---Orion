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

cluster = MongoClient(os.environ['DB'])
base = cluster["OrionDB"]

m1_cur = base["m1guilds"]
c1_cur = base["c1channels"]
anch_cur = base["anch"]
anc_cur = base["anc"]
fc_cur = base["fc"] #Formation = [Guild, Channel, Past_Number, Last_Number, Author]
tc_cur = base["tc"]
bc_cur = base["bc"]
ta_cur = base["ta"]
wc_cur = base["wc"]

class D_1(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        ("D1 is Loaded ----")

                                        ###########################
                                        ##      DEACTIVATOR      ##
                                        ###########################

    @commands.group(aliases = ["stop","eliminate","remove"],invoke_without_command = True,case_insensitive = True)
    async def deactivate(self,ctx):
        deactivator_embed = discord.Embed(title = "= = = = = = =| Help - [Deactivate] |= = = = = = =",description= "Aliases = `stop` , `eliminate`, `remove`\nFor more info: `.o help`\n-   -   -   -   -   -   -   -   -   -   -   -   -   -   -   -   -   -   -   -")
        

        deactivator_embed.add_field(name=":octagonal_sign: Deactivate Commands :octagonal_sign:",value="-:arrow_down: - -  :arrow_down: - -  :arrow_down: - -  :arrow_down: - -  :arrow_down:-\n\n:one: `.o deactivate m1`\nThis command will turn off **M1 protocol**.\n\n:two: `.o deactivate c1 (channel)` or `deactivate all c1`\nThis command will eliminate **C1 Protocol** from a specific channel or all channels.\n\n:three: `.o remove announce_ch`\nThis command removes **Announcement Command Channel**.\n\n:four: `.o remove announce (channel)`\nThis command removes bot **Announcement Channel**.\n\n:five: `.o deactivate fibo`\nThis command removes **Fibonacci Channel**.\n\n:six: `.o deactivate tictactoe`\nThis command removes **TicTacToe Channel**.\n\n:seven: `.o deactivate battleship`\nThis command removes **Battleship Channel**.\n\n:eight: `.o deactivate wiki`\nThis command removes **Wikipedia Channel**.")
        deactivator_embed.set_footer(icon_url=ctx.author.avatar_url,text=f"Requested by {ctx.author.name}")

        await ctx.send(embed = deactivator_embed)

    @deactivate.command()
    async def all(self,ctx,p = None):
        if p == "c1" or p == "C1":
            c1_cur.delete_many({"guild":ctx.guild.id})
            await ctx.send("C1 has been eliminated from all channels.")

    @deactivate.command(aliases = ["m1 protocol","m1 function"])
    async def m1(self,ctx):
        if ctx.author.guild_permissions.manage_channels and ctx.author.guild_permissions.manage_channels:
            id_guild = ctx.guild.id
            raw = m1_cur.find({})
            guilds = []
            try:
                x = [i for i in raw]
                guilds = [x[i]["guild"] for i in range(len(x))]
            except:
                pass
            if ctx.guild.id not in guilds:
                    await ctx.send(random.choice(["M1 is stop",
                                                  "M1 isn't running"]))
            
            if ctx.guild.id in guilds:
                m1_cur.delete_one({"guild":id_guild})
                await ctx.send(random.choice(["M1 Eliminated","M1 Stopped"]))
        
        else:
            await ctx.send("**Access Denied!** \nThis command requires `manage_channel` and `manage_messages` permission in order to execute.")

    @deactivate.command()
    async def c1(self,ctx,channel:discord.TextChannel=None):
        raw = c1_cur.find({})
        channels = [x["channel"] for x in raw]
        

        if ctx.author.guild_permissions.manage_channels:
            if channel == None:
                if ctx.channel.id in channels:
                    c1_cur.delete_one({"channel":ctx.channel.id})
                    await ctx.send(f"C1 has been eliminated from {ctx.channel.mention}")
                if ctx.channel.id not in channels:
                    await ctx.send(f"C1 is not running in {ctx.channel.mention}")
            
            if channel != None:
                try:
                    c1_cur.delete_one({"channel":channel.id})
                except:
                    await ctx.send(f"Argument ERROR.")
        else:
            await ctx.send("**Access Denied!**\nThis command requires `manage_channel` permission in order to execute.")


    @deactivate.command(aliases = ["fibo"])
    async def Fibonacci(self,ctx):
        raw = fc_cur.find({"guild":ctx.guild.id})
        guilds = []
        try:
            x = [i for i in raw]
            guilds = [x[i]["guild"] for i in range(len(x))]
        except:
            pass
        if ctx.author.guild_permissions.manage_channels:

            if ctx.guild.id in guilds:
                cooked = fc_cur.find_one({"guild":ctx.guild.id})
                ch = self.client.get_channel(cooked["channel"])
                fc_cur.delete_one({"guild":ctx.guild.id})
                await ctx.send(f"{ch.mention} is no longer a **Fibonacci** channel.")
            else:
                await ctx.send("No channel is set as **Fibonacci** channel.")

        else:
            await ctx.send("**Access Denied!**\nThis command requires `manage_channel` permission in order to execute.")

    @deactivate.command(aliases = ["tictactoe","tac"])
    async def Tic(self,ctx):
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
            if ctx.guild.id in guilds:
                cooked = tc_cur.find_one({"guild":ctx.guild.id})
                ch = self.client.get_channel(cooked["channel"])
                tc_cur.delete_one({"guild":ctx.guild.id})
                await ctx.send(f"{ch.mention} is no longer a **TicTacToe** channel.")
            else:
                await ctx.send("No channel is set as **TicTacToe** channel.")
        else:
            await ctx.send("**Access Denied!**\nThis command requires `manage_channel` permission in order to execute.")


    @deactivate.command()
    async def battleship(self,ctx):
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
            if ctx.guild.id in guilds:
                cooked = bc_cur.find_one({"guild":ctx.guild.id})
                ch = self.client.get_channel(cooked["channel"])
                bc_cur.delete_one({"guild":ctx.guild.id})
                await ctx.send(f"{ch.mention} is no longer a **Battleship** channel.")
            else:
                await ctx.send("No channel is set as **Battleship** channel.")
        else:
            await ctx.send("**Access Denied!**This command requires `manage_channel` permission in order to execute.")

    @deactivate.command(aliases= ["announcement_ch","ach"])
    async def Announce_ch(self,ctx):
        raw = anc_cur.find({})
        guilds = []
        try:
            x = [i for i in raw]
            guilds = [x[i]["guild"] for i in range(len(x))]
        except:
            pass

        cooked = bc_cur.find_one({"guild":ctx.guild.id})
        ch = self.client.get_channel(cooked["channel"])
        if ctx.author.guild_permissions.manage_channels:
            if ctx.guild.id in guilds:
                anc_cur.delete_one({"guild":ctx.guild.id})
                await ctx.send(f"{ch.mention} is no longer **Announcement Command Channel**.")
            else:
                await ctx.send("No channel is set as **Announcement Command Channel**.")
        else:
            await ctx.send("**Access Denied!**This command requires `manage_channel` permission in order to execute.")

    @deactivate.command(aliases=["an"])
    async def Announce(self,ctx,channel:discord.TextChannel = None):
        raw = anc_cur.find({})
        guilds = []
        channels = []
        try:
            x = [i for i in raw]
            guilds = [x[i]["guild"] for i in range(len(x))]
            channels = [x[i]["channel"] for i in range(len(x))]
        except:
            pass

        if ctx.author.guild_permissions.manage_channels:
            if ctx.channel.id in channels:
                au = ctx.author.id
                ch = ctx.channel.id
                raw2 = anch_cur.find({})
                guilds = []
                channels = []
                try:
                    x = [i for i in raw]
                    guilds = [x[i]["guild"] for i in range(len(x))]
                    channels = [x[i]["channel"] for i in range(len(x))]
                except:
                    pass

                if channel != None:
                    try:
                        if channel.id in channels:
                            anch_cur.delete_one({"channel":channel.id})
                            await ctx.send(f"{channel.mention} is no longer an **Announcement Channel**")
                        elif channel.id not in channels:
                            await ctx.send(f"**Access Denied!**\nNo channel of this server is set as **Announcement Channel**.")

                    except:
                        await ctx.send("Argument ERROR!")
                if channel == None:
                    try:
                        if ctx.channel.id in channels:
                            anch_cur.delete_one({"channel":ctx.channel.id})
                            await ctx.send(f"{ctx.channel.mention} is no longer an **Announcement Channel**")
                        elif channel.id not in channels:
                            await ctx.send(f"**Access Denied!**\nNo channel of this server is set as **Announcement Channel**.")

                    except:
                        await ctx.send("Argument ERROR!")

        else:
            await ctx.send("**Access Denied!**This command requires `manage_channel` permission in order to execute.")


    @deactivate.command(aliases = ["wiki"])
    async def WIKipedia(self,ctx):
        raw = wc_cur.find({})
        guilds = []
        channels = []
        try:
            x = [i for i in raw]
            guilds = [x[i]["guild"] for i in range(len(x))]
            channels = [x[i]["channel"] for i in range(len(x))]
        except:
            pass
        if ctx.author.guild_permissions.manage_channels:
            if ctx.guild.id in guilds:
                raw2 = wc_cur.find_one({"guild":ctx.guild.id})
                ch = raw2["channel"]
                wc_cur.delete_one({"guild":ctx.guild.id})

                channel = self.client.get_channel(ch)
                await ctx.send(f"{channel.mention} is no longer an **Wikipedia Channel**")
            else:
                await ctx.send("No channel of this server is set as **Wikipedia Channel**.")
        else:
            await ctx.send("**Access Denied!**This command requires `manage_channel` permission in order to execute.")

def setup(client):
    client.add_cog(D_1(client))