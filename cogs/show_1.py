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
fc_cur = base["fc"] #Formation = [Guild, Channel, Past_Number, Last_Number, Author]
tc_cur = base["tc"]
bc_cur = base["bc"]
ta_cur = base["ta"]
wc_cur = base["wc"]

class S_1(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print("S1 is Loaded ----")

    @commands.group(invoke_without_command = True,case_insensitive=True)
    async def show(self,ctx):
        show_embed = discord.Embed(title='= = = = = = = =| Help - [Show] |= = = = = = = =',description= "-------------------------------------------------------------")

        show_embed.set_footer(icon_url=ctx.author.avatar_url,text=f"Requested by {ctx.author.name}")
        await ctx.send(embed = show_embed)

    #This part sends the list of channels that are set as announcement channel 
    @show.command(aliases = ['announcement','announce'])
    async def announcements(self,ctx,msg):
        if msg.lower() == 'channels' or msg.lower() == 'channel':
            raw = anch_cur.find({})
            guilds = []
            all = []
            try:
                guilds = [x[i]["guild"] for i in range(len(x))]
                all = [x for x in raw]
            except:
                pass
            
            if ctx.guild.id in guilds:
                dic = {"0":":zero:","1":":one:","2":":two:","3":":three:","4":":four:","5":":five:","6":":six:","7":":seven:","8":":eight:","9":"nine","10":":one::zero:"}

                channels = ""

                num = 1

                for i in range(len(all)):
                    sym = dic[str(num)] if len(str(num)) > 1 else dic["0"]+dic[str(num)]
                    channel =  all[i]["channel"]
                    channels = channels + f"{sym} <#{channel}>\n "
                    num = num + 1

                if len(all) != 0:
                    embed = discord.Embed(title = "= = = =| All Announcement Channels |= = = =")
                    embed.add_field(name = "---------------- 📃 __Channels__ 📃 -----------------",value = channels, inline= True)
                    embed.set_footer(icon_url=ctx.author.avatar_url, text= f"Requested by {ctx.author.name}")
                    await ctx.send(embed = embed)
                    
            if ctx.guild.id not in guilds:
                await ctx.send("This server has no announcement channel set for me.")


def setup(client):
    client.add_cog(S_1(client))