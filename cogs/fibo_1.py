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
import psycopg2

base = psycopg2.connect(user="yyflmbmssbqvcl",
                        password="f3f1c4a58fedf11450c7cf60d7a0e9d5564600cac78d867a3db59688f0bf88b6",
                        host="ec2-3-224-251-47.compute-1.amazonaws.com",
                        port="5432",
                        database="dda86padcqcfo8"
                        )
cur = base.cursor()

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

        cur.execute("SELECT*FROM FC")
        all = cur.fetchall()
        channels = []
        
        try:
            for i in all:
                channels.append(i[1])
        except:
            pass
        
        r = 0
        
        try:
            r = eval(exact_txt_splitted[0])
        except:
            pass
        x = str(r)
        
        if message.channel.id in channels:
            if r != 0 and x.isdigit():
                digit = r
                cur.execute("SELECT*FROM FC WHERE Guild LIKE ?",(message.guild.id,))
                info = cur.fetchall()
                past_digit = info[0][2]
                last_digit = info[0][3]
                last_author = info[0][4]
                equal = past_digit + last_digit
                if past_digit == 0 and last_digit == 0:
                    if digit == 1:
                        cur.execute("UPDATE FC SET Last_Number = ? WHERE Channel = ?",(digit,message.channel.id))
                        cur.execute("UPDATE FC SET Author = ? WHERE Channel = ?",(message.author.id,message.channel.id))
                        base.commit()
                        await message.add_reaction("✅")

                elif digit == equal and last_author != message.author.id:
                    cur.execute("UPDATE FC SET Past_Number = ? WHERE Channel = ?",(last_digit,message.channel.id))
                    cur.execute("UPDATE FC SET Last_Number = ? WHERE Channel = ?",(equal,message.channel.id))
                    cur.execute("UPDATE FC SET Author = ? WHERE Channel = ?",(message.author.id,message.channel.id))
                    base.commit()
                    await message.add_reaction("✅")

                elif last_author == message.author.id:
                    await message.add_reaction("❎")
                    cur.execute("UPDATE FC SET Past_Number = ? WHERE Channel = ?",(0,message.channel.id))
                    cur.execute("UPDATE FC SET Last_Number = ? WHERE Channel = ?",(0,message.channel.id))
                    cur.execute("UPDATE FC SET Author = ? WHERE Channel = ?",(0,message.channel.id))
                    base.commit()
                    if message.author.id == 736818641907089520:
                        await message.channel.send(f"{message.author.mention} :pleading_face: Solly! You can not count 2 numbers in a row. :pleading_face: We will make it next time. ><")


                    else:
                        await message.channel.send(f"{message.author.mention} RUINED AT {equal}!! $#!%. You can not count 2 numbers in a row.")

                elif digit != equal:
                    cur.execute("UPDATE FC SET Past_Number = ? WHERE Channel = ?",(0,message.channel.id))
                    cur.execute("UPDATE FC SET Last_Number = ? WHERE Channel = ?",(0,message.channel.id))
                    cur.execute("UPDATE FC SET Author = ? WHERE Channel = ?",(0,message.channel.id))
                    base.commit()
                    await message.add_reaction("❎")
                    if message.author.id == 736818641907089520:
                        await message.channel.send(f"{message.author.mention} :pleading_face: It should be {equal}. :pleading_face: It's oki we will make it next time.")
                    else:
                        await message.channel.send(f"{message.author.mention} RUINED AT {equal}!! $#!%")



def setup(client):
    client.add_cog(F_1(client))