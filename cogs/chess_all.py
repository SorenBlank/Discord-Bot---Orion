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
from chessdotcom.aio import Client as chessClient
from chessdotcom.aio import get_player_stats,get_player_profile
from asyncio import gather
chessClient.aio = True

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
    async def link(self,ctx,*,username):
        raw = chess_cur.find({})
        raw_info = []
        try:
            raw_info = [x for x in raw]
        except:
            pass

        exist = False
        for i in range(len(raw_info)):
            if raw_info[i]["dc_id"] == ctx.author.id:
                exist = True
                await ctx.send(f"{ctx.author.mention} Your account is already linked with a **chess.com** account.\nIf you want to unlink then type `.o chess unlink`")
        
        if exist == False:
            
            data = chessClient.loop.run_until_complete(gather(get_player_profile(username)))[0].json
            y = data["player"]

            try:
                if y["location"] == str(ctx.author):
                    up = {"_id":len(raw_info),"dc_id":ctx.author.id,"chess_user":username}
                    chess_cur.insert_one(up)
                    await ctx.send("You have successfully linked a **chess.com** account.")

                else:
                    embed = discord.Embed(title = ":vertical_traffic_light: Additional Verification Step :vertical_traffic_light:",description = f"In your chess.com profile, please paste your Discord tag ({ctx.author}) into the Location field temporarily to verify you have ownership of the account and re-run the command. After linking your account, you can revert your Location back to any value.\n\nYou can set your chess.com Location here:\nhttps://www.chess.com/settings")
                    embed.set_image(url = "https://i.imgur.com/IoAWrk4.png")
                    await ctx.send(embed = embed)
            except:
                embed = discord.Embed(title = ":vertical_traffic_light: Additional Verification Step :vertical_traffic_light:",description = f"In your chess.com profile, please paste your Discord tag ({ctx.author}) into the Location field temporarily to verify you have ownership of the account and re-run the command. After linking your account, you can revert your Location back to any value.\n\nYou can set your chess.com Location here:\nhttps://www.chess.com/settings")
                embed.set_image(url = "https://i.imgur.com/IoAWrk4.png")
                await ctx.send(embed = embed)

    @chess.command()
    async def unlink(self,ctx):
        raw = chess_cur.find_one({"dc_id": ctx.author.id})
        if raw != None:
            chess_cur.delete_many({"dc_id":ctx.author.id})
            await ctx.send("Your **chess.com** account has been unlinked.")
        elif raw == None:
            await ctx.send("Your are not linked with any **chess.com** account.")

    @chess.command()
    async def profile(self,ctx,*,name = None):
        if name:
            try:
                user = ctx.message.mentions[0]
            except IndexError:
                user = ctx.guild.get_member_named(name)
            if not user:
                user = ctx.guild.get_member(int(name))
            if not user:
                await ctx.send('Could not find user.')
                return
        else:
            user = ctx.message.author

        raw = chess_cur.find_one({"dc_id": user.id})

        if raw != None:
            #try:
            data = chessClient.loop.run_until_complete(gather(get_player_profile(raw["chess_user"])))[0].json
            data2 = chessClient.loop.run_until_complete(gather(get_player_stats(raw["chess_user"])))[0].json

            player = data["player"]
            stats = data2["stats"]

            profile_em = discord.Embed(title = "= = = = = |<:wk:820331572938539010> **Chess Profile** <:bk:820557586318360597>| = = = = =")
            try:
                profile_em.add_field(name = ':white_medium_square: NAME :',
                    value = f':white_small_square:`{player["name"]}`')
            except:
                profile_em.add_field(name = ':white_medium_square: NAME :',
                    value = ':white_small_square:`none`')

            profile_em.add_field(name = f':white_medium_square: USER_NAME :',
                value = f':white_small_square:`{player["username"]}`')

            try:
                profile_em.set_thumbnail(url = player["avatar"])
            except:
                pass

            profile_em.add_field(name = f':white_medium_square: PROFILE URL :',
                value = player["url"],
                inline = False)
            try:
                profile_em.add_field(name = "<:bulllet:820558290705580063>-BULLET",
                    value = stats["chess_bullet"]["last"]["rating"])
            except:
                profile_em.add_field(name = "<:bulllet:820558290705580063>-BULLET",
                    value = 0)

            try:
                profile_em.add_field(name = "<:blitz:820558071012786186>-BLITZ",
                    value = stats["chess_blitz"]["last"]["rating"])
            except:
                profile_em.add_field(name = "<:blitz:820558071012786186>-BLITZ",
                    value = 0)

            try:
                profile_em.add_field(name = "<:rapid:820557720645140480>-RAPID",
                    value = stats["chess_rapid"]["last"]["rating"])
            except:
                profile_em.add_field(name = "<:rapid:820557720645140480>-RAPID",
                    value = 0)

            await ctx.send(embed = profile_em)
            # except:
            #     await ctx.send("**Response ERROR!**\nPlease unlink and link your **chess.com** and try again.")
        elif raw == None:
            await ctx.send(f"`{user}` isn't linked with any **chess.com** account.")

def setup(client):
    client.add_cog(CHESS(client))