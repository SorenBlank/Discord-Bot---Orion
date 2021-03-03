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

class AN_1(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print("AN1 is Loaded ----")

    @commands.command()
    async def announce(self,ctx, channel:discord.TextChannel = None, time = None):
        if channel != None:
            try:
                cur.execute("SELECT*FROM ANC")
                all = cur.fetchall()
                channels = []
                guilds = []
                try:
                    for i in all:
                        channels.append(i[1])
                        guilds.append(i[0])
                except:
                    pass

                if ctx.channel.id in channels:
                    au = ctx.author.id
                    ch = ctx.channel.id
                    cur.execute("SELECT*FROM Announce_ch")
                    all = cur.fetchall()
                    guilds = []
                    channels = []

                    for i in all:
                        guilds.append(i[0])
                        channels.append(i[1])

                    if ctx.guild.id in guilds:
                        if channel.id in channels:
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

                                    if time.isdigit():
                                        cur.execute("INSERT INTO TimerAnnounce (Guild, Channel, TimeLeft, Announcement) VALUES (?,?,?,?)",(ctx.guild.id,channel.id,time,text.content))
                                        base.commit()
                                        await ctx.send(f"Given input will be announced in {time} seconds.")
                                    if time.isdigit() == False:
                                        list_time = [i for i in time]
                                        joined_time = ''.join(list_time[:-1])
                                        actual_time = 0
                                        try:
                                            actual_time = int(joined_time)
                                            print(actual_time)
                                            x = list_time[len(list_time)-1]
                                            if x.lower() == "s":
                                                cur.execute("INSERT INTO TimerAnnounce (Guild, Channel, TimeLeft, Announcement) VALUES (?,?,?,?)",
                                                    (ctx.guild.id,channel.id,actual_time,text.content))
                                                base.commit()
                                                if actual_time == 1:
                                                    await ctx.send(f"Given input will be announced after {actual_time} second.")
                                                else:
                                                    await ctx.send(f"Given input will be announced after {actual_time} seconds.")
                                            if x.lower() == "m":
                                                m_time = actual_time*60
                                                cur.execute("INSERT INTO TimerAnnounce (Guild, Channel, TimeLeft, Announcement) VALUES (?,?,?,?)",(ctx.guild.id,channel.id,m_time,text.content))
                                                base.commit()
                                                if actual_time == 1:
                                                    await ctx.send(f"Given input will be announced after {actual_time} minute.")
                                                else:
                                                    await ctx.send(f"Given input will be announced after {actual_time} minute.")
                                            if x.lower() == "h":
                                                h_time = actual_time*3600
                                                cur.execute("INSERT INTO TimerAnnounce (Guild, Channel, TimeLeft, Announcement) VALUES (?,?,?,?)",(ctx.guild.id,channel.id,h_time,text.content))
                                                base.commit()
                                                if actual_time == 1:
                                                    await ctx.send(f"Given input will be announced after {actual_time} hour.")
                                                else:
                                                    await ctx.send(f"Given input will be announced after {actual_time} hours.")
                                        except:
                                            await ctx.send("Argument Error!")

                                    
                            if lower == "eliminate":
                                await ctx.send("Command Dismissed")

                        if channel.id not in channels:
                            await ctx.send(f"{channel.mention} is not set as an announcement channel of this server.")

                    if ctx.guild.id not in guilds:
                        await ctx.send(f"{channel.mention} is not set as an announcement channel.")

                cur.execute("SELECT*FROM ANC")
                all = cur.fetchall()
                channels = []
                guilds = []
                
                try:
                    for i in all:
                        channels.append(i[1])
                        guilds.append(i[0])
                except:
                    pass
                
                if ctx.guild.id not in guilds:
                    await ctx.send("No channel of this server is set as **Announcement Command Channel**.\n Please set one using this command `.o set announce_ch (channel)`")
            except:
                pass
        if channel == None:
            await ctx.send("Argument Error!")

def setup(client):
    client.add_cog(AN_1(client))