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
import re
import pymongo
from pymongo import MongoClient
from chessdotcom import get_player_profile, get_player_stats


cluster = MongoClient("mongodb+srv://soren:cdD2_qWUYRk-d4G@orion.iztml.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
base = cluster["OrionDB"]
chess_cur = base["chessaccount"]
def get_player(user):
        data = get_player_profile(user)
        return data

class CHESS(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print("CHESS is Loaded ----")

    




    @commands.group(invoke_without_command = True,case_insensitive=True)
    async def chess(self,ctx):
        pass


    @chess.command()
    async def link(self,ctx,username):
        raw = chess_cur.find({})
        raw_info = []
        try:
            raw_info = [x for i in raw]
        except:
            pass

        exist = False
        for i in range(len(raw_info)):
            if raw_info[i]["dc_id"] == ctx.author.id:
                exist = True
                await ctx.send(f"{ctx.author.mention} Your account is already linked with a **chess.com** account.\nIf you want to unlink then type `.o chess unlink`")
        if exist == False:
            
            x = get_player("Soren_Blank").json
            y = x["player"]

            if y["location"] == str(ctx.author):
                up = {"_id":len(raw_info),"dc_id":ctx.author.id,"chess_user":username}
                chess_cur.insert_one(up)

            else:
                embed = discord.Embed(title = ":vertical_traffic_light: Additional Verification Step :vertical_traffic_light:",description = f"In your chess.com profile, please paste your Discord tag ({ctx.author}) into the Location field temporarily to verify you have ownership of the account and re-run the command. After linking your account, you can revert your Location back to any value.\n\nYou can set your chess.com Location here:\nhttps://www.chess.com/settings")
                embed.set_image(url = "https://i.imgur.com/IoAWrk4.png")
                await ctx.send(embed = embed)


def setup(client):
    client.add_cog(CHESS(client))