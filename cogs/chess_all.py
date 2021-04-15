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
from chessdotcom import Client as chessClient
from chessdotcom import get_player_stats,get_player_profile
from asyncio import gather
chessClient.aio = True

cluster = MongoClient("mongodb+srv://soren:cdD2_qWUYRk-d4G@orion.iztml.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
base = cluster["OrionDB"]
ign_cur = base["ign"]
chess_cur = base["chessaccount"]


class CHESS(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print("CHESS is Loaded ----")

    # @commands.group(invoke_without_command = True,case_insensitive=True)
    # async def chess(self,ctx):
    #     pass


    @commands.command()
    async def link(self,ctx,game,*,username):
        if game.lower() == "chess":
            raw = ign_cur.find_one({"dc_id":ctx.author.id})
            # raw_info = []
            # try:
            #     raw_info = [x for x in raw]
            # except:
            #     pass

            exist = False
            if raw != None:
                if "chess_user" in raw.keys():
                    exist = True
                    await ctx.send(f"{ctx.author.mention} Your account is already linked with a **chess.com** account.\nIf you want to unlink then type `.o chess unlink`")
            
            if exist == False:
                if raw == None:
                    data = chessClient.loop.run_until_complete(gather(get_player_profile(username)))[0].json
                    y = data["player"]

                    try:
                        if y["location"] == str(ctx.author):
                            up = {"dc_id":ctx.author.id,"chess_user":username}
                            ign_cur.insert_one(up)
                            await ctx.send("You have successfully linked a **chess.com** account.")

                        else:
                            embed = discord.Embed(title = ":vertical_traffic_light: Additional Verification Step :vertical_traffic_light:",description = f"In your chess.com profile, please paste your Discord tag ({ctx.author}) into the Location field temporarily to verify you have ownership of the account and re-run the command. After linking your account, you can revert your Location back to any value.\n\nYou can set your chess.com Location here:\nhttps://www.chess.com/settings")
                            embed.set_image(url = "https://i.imgur.com/IoAWrk4.png")
                            await ctx.send(embed = embed)
                    except:
                        embed = discord.Embed(title = ":vertical_traffic_light: Additional Verification Step :vertical_traffic_light:",description = f"In your chess.com profile, please paste your Discord tag ({ctx.author}) into the Location field temporarily to verify you have ownership of the account and re-run the command. After linking your account, you can revert your Location back to any value.\n\nYou can set your chess.com Location here:\nhttps://www.chess.com/settings")
                        embed.set_image(url = "https://i.imgur.com/IoAWrk4.png")
                        await ctx.send(embed = embed)
                if raw != None:
                    data = chessClient.loop.run_until_complete(gather(get_player_profile(username)))[0].json
                    y = data["player"]

                    try:
                        if y["location"] == str(ctx.author):
                            raw["chess_user"] = username
                            raw.pop("_id",None)
                            ign_cur.delete_many({"dc_id":ctx.author.id})
                            ign_cur.insert_one(raw)
                            await ctx.send("You have successfully linked a **chess.com** account.")

                        else:
                            embed = discord.Embed(title = ":vertical_traffic_light: Additional Verification Step :vertical_traffic_light:",description = f"In your chess.com profile, please paste your Discord tag ({ctx.author}) into the Location field temporarily to verify you have ownership of the account and re-run the command. After linking your account, you can revert your Location back to any value.\n\nYou can set your chess.com Location here:\nhttps://www.chess.com/settings")
                            embed.set_image(url = "https://i.imgur.com/IoAWrk4.png")
                            await ctx.send(embed = embed)
                    except:
                        embed = discord.Embed(title = ":vertical_traffic_light: Additional Verification Step :vertical_traffic_light:",description = f"In your chess.com profile, please paste your Discord tag ({ctx.author}) into the Location field temporarily to verify you have ownership of the account and re-run the command. After linking your account, you can revert your Location back to any value.\n\nYou can set your chess.com Location here:\nhttps://www.chess.com/settings")
                        embed.set_image(url = "https://i.imgur.com/IoAWrk4.png")
                        await ctx.send(embed = embed)


        if game.lower() == "valorant" or game.lower() == "val":
            raw = ign_cur.find_one({"dc_id":ctx.author.id})
            # try:
            #     raw_info = [x for x in raw]
            # except:
            #     pass

            exist = False

            if raw != None:
                if "val_user" in raw.keys():
                    exist = True
                    await ctx.send(f"{ctx.author.mention} Your account is already linked with a **valorant** account.\nIf you want to unlink then type `.o unlink val`")

            if exist == False:
                if raw == None:
                    up = {"dc_id":ctx.author.id,"val_user":username}
                    ign_cur.insert_one(up)
                    await ctx.send("You have successfully linked a **valorant** account.")
                
                if raw != None:
                    raw["val_user"] = username
                    ign_cur.delete_many({"dc_id": ctx.author.id})
                    ign_cur.insert_one(raw)
                    await ctx.send("You have successfully linked a **valorant** account.")

    @commands.command()
    async def unlink(self,ctx,game):
        if game.lower() == "chess":
            raw = ign_cur.find_one({"dc_id": ctx.author.id})
            if raw != None:
                if "chess_user" in raw.keys():
                    raw.pop("chess_user",None)
                    ign_cur.delete_many({"dc_id":ctx.author.id})
                    ign_cur.insert_one(raw)
                    await ctx.send("Your **chess.com** account has been unlinked.")
                else:
                    await ctx.send("Your are not linked with any **chess.com** account.")
            elif raw == None:
                await ctx.send("Your are not linked with any **chess.com** account.")
        
        if game.lower() == "val" or game.lower() == "valorant":
            raw = ign_cur.find_one({"dc_id": ctx.author.id})
            if raw != None:
                if "val_user" in raw.keys():
                    raw.pop("val_user",None)
                    ign_cur.delete_many({"dc_id":ctx.author.id})
                    ign_cur.insert_one(raw)
                    await ctx.send("Your **valorant** account has been unlinked.")
                else:
                    await ctx.send("Your are not linked with any **valorant** account.")
            elif raw == None:
                await ctx.send("Your are not linked with any **valorant** account.")
            

    @commands.command()
    async def profile(self,ctx,game,*,name = ""):
        if game.lower() == "chess":
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

            raw = ign_cur.find_one({"dc_id": user.id})

            if raw != None:
                if "chess_user" in raw.keys():
                    #try:
                    data = chessClient.loop.run_until_complete(gather(get_player_profile(raw["chess_user"])))[0].json
                    data2 = chessClient.loop.run_until_complete(gather(get_player_stats(raw["chess_user"])))[0].json

                    player = data["player"]
                    stats = data2["stats"]

                    profile_em = discord.Embed(color = 0x714ec4)
                    profile_em.set_author(name = "CHESS PROFILE",icon_url= self.client.user.avatar_url)
                    try:
                        profile_em.add_field(name = 'NAME',
                            value = f'```\n{player["name"]}```')
                    except:
                        profile_em.add_field(name = 'NAME :',
                            value = '```\nNone```')

                    profile_em.add_field(name = f'USER NAME',
                        value = f'```\n{player["username"]}```')

                    try:
                        profile_em.set_thumbnail(url = player["avatar"])
                    except:
                        pass

                    profile_em.add_field(name = f'PROFILE URL',
                        value = player["url"],
                        inline = False)
                    try:
                        profile_em.add_field(name = "<:bulllet:820558290705580063>-BULLET",
                            value = f"```\n{stats['chess_bullet']['last']['rating']}```")
                    except:
                        profile_em.add_field(name = "<:bulllet:820558290705580063>-BULLET",
                            value = f"```\n0```")

                    try:
                        profile_em.add_field(name = "<:blitz:820558071012786186>-BLITZ",
                            value = f"```\n{stats['chess_blitz']['last']['rating']}```")
                    except:
                        profile_em.add_field(name = "<:blitz:820558071012786186>-BLITZ",
                            value = f"```\n0```")

                    try:
                        profile_em.add_field(name = "<:rapid:820557720645140480>-RAPID",
                            value = f"```\n{stats['chess_rapid']['last']['rating']}```")
                    except:
                        profile_em.add_field(name = "<:rapid:820557720645140480>-RAPID",
                            value = f"```\n0```")

                    await ctx.send(embed = profile_em)
                    # except:
                    #     await ctx.send("**Response ERROR!**\nPlease unlink and link your **chess.com** and try again.")
                else:
                    await ctx.send(f"`{user}` isn't linked with any **chess.com** account.")
            elif raw == None:
                await ctx.send(f"`{user}` isn't linked with any **chess.com** account.")

    
def setup(client):
    client.add_cog(CHESS(client))
