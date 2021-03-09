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

class F_1(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print("F1 is Loaded ----")

    @commands.Cog.listener()
    async def on_message(self,message):
        #making the message.content lower case in order to make the commands case insensitive
        ex_1 = message.content.lower().replace(',','')
        ex_2 = ex_1.replace("?","")
        exact_txt = ex_2
        #splitting the exact_txt
        exact_txt_splitted = exact_txt.split(" ")
        raw = 0
        id = 0
        try:
            raw = fc_cur.find_one({"guild":message.guild.id})
        except:
            pass
        try:
            id = raw["channel"]
        except:
            pass
        r = 0
        
        try:
            r = eval(exact_txt_splitted[0])
        except:
            pass
        x = str(r)
        
        #try:     
        if message.channel.id == id:
            if r != 0 and x.isdigit():
                digit = r
                past_digit = raw["past"]
                last_digit = raw["last"]
                last_author = raw["author"]
                equal = past_digit + last_digit
                if past_digit == 0 and last_digit == 0:
                    if digit == 1:
                        fc_cur.update_one({"channel":message.channel.id},{"$set":{"last":digit,"author":message.author.id}})
                        await message.add_reaction("✅")

                elif digit == equal and last_author != message.author.id:
                    fc_cur.update_many({"channel":message.channel.id},{"$set":{"past":last_digit,"last":equal,"author":message.author.id}})
                    await message.add_reaction("✅")

                elif last_author == message.author.id:
                    await message.add_reaction("❎")
                    fc_cur.update_many({"channel":message.channel.id},{"$set":{"past":0,"last":0,"author":0}})
                    if message.author.id == 736818641907089520:
                        await message.channel.send(f"{message.author.mention} :pleading_face: Solly! You can not count 2 numbers in a row. :pleading_face: We will make it next time. ><")


                    else:
                        await message.channel.send(f"{message.author.mention} RUINED AT {equal}!! $#!%. You can not count 2 numbers in a row.")

                elif digit != equal:
                    fc_cur.update_many({"channel":message.channel.id},{"$set":{"past":0,"last":0,"author":0}})
                    await message.add_reaction("❎")
                    if message.author.id == 736818641907089520:
                        await message.channel.send(f"{message.author.mention} :pleading_face: It should be {equal}. :pleading_face: It's oki we will make it next time.")
                    else:
                        await message.channel.send(f"{message.author.mention} RUINED AT {equal}!! $#!%")
        #except:
            #pass

def setup(client):
    client.add_cog(F_1(client))