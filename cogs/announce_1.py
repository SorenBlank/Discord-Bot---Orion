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

class AN_1(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print("AN1 is Loaded ----")

    @commands.command()
    async def announce(self,ctx, channel:discord.TextChannel, time = None):
        raw = ta_cur.find({})
        y = [x["guild"] for x in raw]

        au = ctx.author.id
        ch = ctx.channel.id

        await ctx.send("Recording your text. Please type down the announcement below -")
        text = await self.client.wait_for("message")

        while not (text.author.id == au and text.channel.id == ch):
            text = await self.client.wait_for("message")
            pass

        lower = text.content.lower()
        if lower != "eliminate":
            if text.author.id == au and text.channel.id ==ch:
                if time == None:
                    att=[]
                    if text.attachments != []:
                        if text.content != None:
                            await channel.send(text.content)
                            for a in text.attachments:
                                att.append(await a.to_file())
                            for at in att:
                                await channel.send(file=at)

                        if text.content == None:
                            for a in text.attachments:
                                att.append(await a.to_file())
                            for at in att:
                                await channel.send(file=at)
                    else:
                        await channel.send(text.content)
                if time != None:
                    if time.isdigit():
                        raw = ta_cur.find({})
                        all = [x for x in raw]
                        up = {"_id":len(all),
                              "guild":ctx.guild.id,
                              "channel":channel.id,
                              "time":time,
                              "announcement":text.content}
                        ta_cur.insert_one(up)
                        await ctx.send(f"Given input will be announced in {time} seconds.")
                    if time.isdigit() == False:
                        list_time = [i for i in time]
                        joined_time = ''.join(list_time[:-1])
                        actual_time = 0
                        try:
                            actual_time = int(joined_time)
                            x = list_time[len(list_time)-1]
                            if x.lower() == "s":
                                up = {"_id":len(y),
                                        "guild":ctx.guild.id,
                                        "channel":channel.id,
                                        "time":actual_time,
                                        "announcement":text.content}
                                ta_cur.insert_one(up)
                                if actual_time == 1:
                                    await ctx.send(f"Given input will be announced after {actual_time} second.")
                                else:
                                    await ctx.send(f"Given input will be announced after {actual_time} seconds.")
                            if x.lower() == "m":
                                m_time = actual_time*60
                                up = {"_id":len(y),
                                        "guild":ctx.guild.id,
                                        "channel":channel.id,
                                        "time":m_time,
                                        "announcement":text.content}
                                ta_cur.insert_one(up)
                                if actual_time == 1:
                                    await ctx.send(f"Given input will be announced after {actual_time} minute.")
                                else:
                                    await ctx.send(f"Given input will be announced after {actual_time} minute.")
                            if x.lower() == "h":
                                h_time = actual_time*3600
                                
                                up = {"_id":len(y),
                                        "guild":ctx.guild.id,
                                        "channel":channel.id,
                                        "time":h_time,
                                        "announcement":text.content}
                                ta_cur.insert_one(up)
                                if actual_time == 1:
                                    await ctx.send(f"Given input will be announced after {actual_time} hour.")
                                else:
                                    await ctx.send(f"Given input will be announced after {actual_time} hours.")
                        except:
                            await ctx.send("Argument Error!")

        if lower == "eliminate":
            await ctx.send("Command Dismissed")

        if channel == None:
            await ctx.send("Argument Error!")

def setup(client):
    client.add_cog(AN_1(client))