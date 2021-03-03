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
            cur.execute("SELECT*FROM Announce_ch")
            all = cur.fetchall()
            an_guilds = []
            for i in all:
                an_guilds.append(i[0])
            
            if ctx.guild.id in an_guilds:
                cur.execute("SELECT*FROM Announce_ch WHERE Guild Like ?",(ctx.guild.id,))
                all = cur.fetchall()
                dic = {"0":":zero:","1":":one:","2":":two:","3":":three:","4":":four:","5":":five:","6":":six:","7":":seven:","8":":eight:","9":"nine","10":":one::zero:"}

                channels = ""

                num = 1

                for i in all:
                    sym = dic[str(num)] if len(str(num)) > 1 else dic["0"]+dic[str(num)]
                    channels = channels + f"{sym} <#{i[1]}>\n "
                    num = num + 1

                if len(all) != 0:
                    embed = discord.Embed(title = "= = = =| All Announcement Channels |= = = =")
                    embed.add_field(name = "---------------- 📃 __Channels__ 📃 -----------------",value = channels, inline= True)
                    embed.set_footer(icon_url=ctx.author.avatar_url, text= f"Requested by {ctx.author.name}")
                    await ctx.send(embed = embed)
                    
            if ctx.guild.id not in an_guilds:
                await ctx.send("This server has no announcement channel set for me.")


def setup(client):
    client.add_cog(S_1(client))