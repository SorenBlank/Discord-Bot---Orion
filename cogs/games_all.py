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
import requests
from bs4 import BeautifulSoup
import lichess.api

chessClient.aio = True

cluster = MongoClient("mongodb+srv://soren:cdD2_qWUYRk-d4G@orion.iztml.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
base = cluster["OrionDB"]
ign_cur = base["ign"]


class GAMES(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print("GAMES is Loaded ----")

    # @commands.group(invoke_without_command = True,case_insensitive=True)
    # async def chess(self,ctx):
    #     pass


    @commands.group(invoke_without_command = True,case_insensitive=True)
    async def link(self,ctx):
        return
    
    @link.command()
    async def chess(self, ctx,*,username = ""):

        if username:
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
                    
                    embed = discord.Embed(color = 0x714ec4,description = "Overwrite ERROR!\n\nA linked `chess` account already exists. Type `.o unlink chess` to unlink.")
                    embed.set_author(name = "ERROR", icon_url = self.client.user.avatar_url)
                    await ctx.send(embed = embed)

            if exist == False:
                if raw == None:
                    data = chessClient.loop.run_until_complete(gather(get_player_profile(username)))[0].json
                    y = data["player"]

                    try:
                        if y["location"] == str(ctx.author):
                            up = {"dc_id":ctx.author.id,"chess_user":username}
                            ign_cur.insert_one(up)
                            embed = discord.Embed(color = 0x714ec4,description = "You have successfully linked a `chess.com` account.")
                            embed.set_author(name = "Linked Successful!", icon_url= self.client.user.avatar_url)
                            await ctx.send(embed = embed)

                        else:
                            embed = discord.Embed(color = 0x714ec4,title = ":vertical_traffic_light: Additional Verification Step :vertical_traffic_light:",description = f"In your chess.com profile, please paste your Discord tag ({ctx.author}) into the Location field temporarily to verify you have ownership of the account and re-run the command. After linking your account, you can revert your Location back to any value.\n\nYou can set your chess.com Location here:\nhttps://www.chess.com/settings")
                            embed.set_image(url = "https://i.imgur.com/IoAWrk4.png")
                            await ctx.send(embed = embed)
                    except:
                        embed = discord.Embed(color = 0x714ec4,title = ":vertical_traffic_light: Additional Verification Step :vertical_traffic_light:",description = f"In your chess.com profile, please paste your Discord tag ({ctx.author}) into the Location field temporarily to verify you have ownership of the account and re-run the command. After linking your account, you can revert your Location back to any value.\n\nYou can set your chess.com Location here:\nhttps://www.chess.com/settings")
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
                            embed = discord.Embed(color = 0x714ec4,description = "You have successfully linked a `chess.com` account.")
                            embed.set_author(name = "Linked Successful!", icon_url= self.client.user.avatar_url)
                            await ctx.send(embed = embed)

                        else:
                            embed = discord.Embed(color = 0x714ec4, title = ":vertical_traffic_light: Additional Verification Step :vertical_traffic_light:",description = f"In your chess.com profile, please paste your Discord tag ({ctx.author}) into the Location field temporarily to verify you have ownership of the account and re-run the command. After linking your account, you can revert your Location back to any value.\n\nYou can set your chess.com Location here:\nhttps://www.chess.com/settings")
                            embed.set_image(url = "https://i.imgur.com/IoAWrk4.png")
                            await ctx.send(embed = embed)
                    except:
                        embed = discord.Embed(title = ":vertical_traffic_light: Additional Verification Step :vertical_traffic_light:",description = f"In your chess.com profile, please paste your Discord tag ({ctx.author}) into the Location field temporarily to verify you have ownership of the account and re-run the command. After linking your account, you can revert your Location back to any value.\n\nYou can set your chess.com Location here:\nhttps://www.chess.com/settings")
                        embed.set_image(url = "https://i.imgur.com/IoAWrk4.png")
                        await ctx.send(embed = embed)
        else:
            embed = discord.Embed(color = 0x714ec4,description = "Argument ERROR!")
            embed.set_author(name = "ERROR", icon_url= self.client.user.avatar_url)
            await ctx.send(embed = embed)

    @link.command()
    async def lichess(self, ctx,*,username = ""):

        if username:
            raw = ign_cur.find_one({"dc_id":ctx.author.id})
            exist = False

            if raw != None:
                if "lichess_user" in raw.keys():
                    exist = True
                    embed = discord.Embed(color = 0x714ec4,description = "Overwrite ERROR!\n\nA linked `lichess` account already exists. Type `.o unlink lichess` to unlink.")
                    embed.set_author(name = "ERROR", icon_url= self.client.user.avatar_url)
                    await ctx.send(embed = embed)

            if exist == False:
                if raw == None:
                    user = lichess.api.user(username)
                    try:
                        if user["profile"]["location"] == str(ctx.author):
                            up = {"dc_id":ctx.author.id,"lichess_user":username}
                            ign_cur.insert_one(up)
                            embed = discord.Embed(color = 0x714ec4,description = "You have successfully linked a `lichess` account.")
                            embed.set_author(name = "Linked Successful!", icon_url= self.client.user.avatar_url)
                            await ctx.send(embed = embed)
                        else:
                            embed = discord.Embed(color = 0x714ec4,title = ":vertical_traffic_light: Additional Verification Step :vertical_traffic_light:",description = f"In your lichess profile, please paste your Discord tag ({ctx.author}) into the Location field temporarily to verify you have ownership of the account and re-run the command. After linking your account, you can revert your Location back to any value.\n\nYou can set your lichess Location here:\nhttps://lichess.org/account/profile")
                            embed.set_image(url = "https://i.imgur.com/kWaOcfT.png")
                            await ctx.send(embed = embed)
                    except:
                        embed = discord.Embed(color = 0x714ec4,title = ":vertical_traffic_light: Additional Verification Step :vertical_traffic_light:",description = f"In your lichess profile, please paste your Discord tag ({ctx.author}) into the Location field temporarily to verify you have ownership of the account and re-run the command. After linking your account, you can revert your Location back to any value.\n\nYou can set your lichess Location here:\nhttps://lichess.org/account/profile")
                        embed.set_image(url = "https://i.imgur.com/kWaOcfT.png")
                        await ctx.send(embed = embed)

                if raw != None:
                    user = lichess.api.user(username)
                    try:
                        if user["profile"]["location"] == str(ctx.author):
                            raw["lichess_user"] = username
                            ign_cur.delete_many({"dc_id":ctx.author.id})
                            ign_cur.insert_one(raw)
                            embed = discord.Embed(color = 0x714ec4,description = "You have successfully linked a `lichess` account.")
                            embed.set_author(name = "Linked Successful!", icon_url= self.client.user.avatar_url)
                            await ctx.send(embed = embed)
                        else:
                            embed = discord.Embed(color = 0x714ec4,title = ":vertical_traffic_light: Additional Verification Step :vertical_traffic_light:",description = f"In your lichess profile, please paste your Discord tag ({ctx.message.author}) into the Location field temporarily to verify you have ownership of the account and re-run the command. After linking your account, you can revert your Location back to any value.\n\nYou can set your lichess Location here:\nhttps://lichess.org/account/profile")
                            embed.set_image(url = "https://i.imgur.com/kWaOcfT.png")
                            await ctx.send(embed = embed)

                    except:
                        embed = discord.Embed(color = 0x714ec4,title = ":vertical_traffic_light: Additional Verification Step :vertical_traffic_light:",description = f"In your lichess profile, please paste your Discord tag ({ctx.author}) into the Location field temporarily to verify you have ownership of the account and re-run the command. After linking your account, you can revert your Location back to any value.\n\nYou can set your lichess Location here:\nhttps://lichess.org/account/profile")
                        embed.set_image(url = "https://i.imgur.com/kWaOcfT.png")
                        await ctx.send(embed = embed)
        else:
            embed = discord.Embed(color = 0x714ec4,description = "Argument ERROR!")
            embed.set_author(name = "ERROR", icon_url= self.client.user.avatar_url)
            await ctx.send(embed = embed)
        

    @link.command(aliases = ["val"])
    async def valorant(self,ctx,*,username = ""):

        if username:
            raw = ign_cur.find_one({"dc_id":ctx.author.id})
            # try:
            #     raw_info = [x for x in raw]
            # except:
            #     pass

            exist = False

            if raw != None:
                if "val_user" in raw.keys():
                    exist = True
                    embed = discord.Embed(color = 0x714ec4,description = "Overwrite ERROR!\n\nA linked `valorant` account already exists. Type `.o unlink val` to unlink.")
                    embed.set_author(name = "ERROR", icon_url= self.client.user.avatar_url)
                    await ctx.send(embed = embed)

            if exist == False:
                embed = discord.Embed(color = 0x714ec4, description = "`📡 verifying data......`")
                link_msg = await ctx.send(embed = embed)
                if raw == None:
                    try:
                        splited = username.split("#")
                    except:
                        temp = discord.Embed(title = ctx.author.name,description = "`Valorant` Account not found.", color = 0x714ec4)
                        await link_msg.edit(embed = temp)
                        return
                    
                    name = splited[0].replace(" ","%20")
                    try:
                        tag = splited[1]
                    except:
                        temp = discord.Embed(title = ctx.author.name,description = "Invalid `valorant` IGN.\n\nPlease make sure you provided your tag along with the username.\nExample: `.o link val SorenBlank#1570`", color = 0x714ec4)
                        temp.set_author(name = "VALORANT PROFILE", icon_url= self.client.user.avatar_url)
                        await link_msg.edit(embed = temp)
                        return

                    url = f"https://tracker.gg/valorant/profile/riot/{name}%23{tag}/overview"
                    req = requests.get(url)

                    if str(req) == "<Response [200]>" or str(req) == "<Response [451]>":

                        up = {"dc_id":ctx.author.id,"val_user":username}
                        ign_cur.insert_one(up)
                        embed = discord.Embed(color = 0x714ec4,description = "You have successfully linked a `valorant` account.")
                        embed.set_author(name = "Linked Successful!", icon_url= self.client.user.avatar_url)
                        await link_msg.edit(embed = embed)
                    else:
                        temp = discord.Embed(title = ctx.author.name,description = "`Valorant` Account not found.", color = 0x714ec4)
                        await link_msg.edit(embed = temp)
                        return
                
                if raw != None:
                    try:
                        splited = username.split("#")
                    except:
                        temp = discord.Embed(title = ctx.author.name,description = "`Valorant` Account not found.", color = 0x714ec4)
                        await link_msg.edit(embed = temp)
                        return
                    
                    name = splited[0].replace(" ","%20")
                    try:
                        tag = splited[1]
                    except:
                        temp = discord.Embed(title = ctx.author.name,description = "Invalid `valorant` IGN.\n\nPlease make sure you provided your tag along with the username.\nExample: `.o link val SorenBlank#1570`", color = 0x714ec4)
                        temp.set_author(name = "VALORANT PROFILE", icon_url= self.client.user.avatar_url)
                        await link_msg.edit(embed = temp)
                        return


                    url = f"https://tracker.gg/valorant/profile/riot/{name}%23{tag}/overview"
                    req = requests.get(url)

                    if str(req) == "<Response [200]>" or str(req) == "<Response [451]>":
                        raw["val_user"] = username
                        ign_cur.delete_many({"dc_id": ctx.author.id})
                        ign_cur.insert_one(raw)
                        embed = discord.Embed(color = 0x714ec4,description = "You have successfully linked a `valorant` account.")
                        embed.set_author(name = "Linked Successful!", icon_url= self.client.user.avatar_url)
                        await link_msg.edit(embed = embed)
                    else: 
                        temp = discord.Embed(title = ctx.author.name,description = "`Valorant` Account not found.", color = 0x714ec4)
                        await link_msg.edit(embed = temp)
                        return
        else:
            embed = discord.Embed(color = 0x714ec4, description = "Argument ERROR!")
            embed.set_author(name = "ERROR", icon_url= self.client.user.avatar_url)
            await ctx.send(embed = embed)

    @commands.group(invoke_without_command = True,case_insensitive=True)
    async def unlink(self,ctx,game):
        return
    

    @unlink.command()
    async def Chess(self,ctx):
        raw = ign_cur.find_one({"dc_id": ctx.author.id})
        if raw != None:
            if "chess_user" in raw.keys():
                raw.pop("chess_user",None)
                ign_cur.delete_many({"dc_id":ctx.author.id})
                ign_cur.insert_one(raw)
                embed = discord.Embed(color = 0x714ec4,description = "You have successfully unlinked `chess.com` account.")
                embed.set_author(name = "Unlinked Successful!", icon_url= self.client.user.avatar_url)
                await ctx.send(embed = embed)
            else:
                embed = discord.Embed(color = 0x714ec4,description = "Overwrite ERROR!\n\nThis account is not linked with any `chess.com` account.")
                embed.set_author(name = "ERROR", icon_url= self.client.user.avatar_url)
                await ctx.send(embed = embed)
        elif raw == None:
            embed = discord.Embed(color = 0x714ec4,description = "Overwrite ERROR!\n\nThis account is not linked with any `chess.com` account.")
            embed.set_author(name = "ERROR", icon_url= self.client.user.avatar_url)
            await ctx.send(embed = embed)
    
    @unlink.command(aliases = ["valorant"])
    async def val(self,ctx):
        raw = ign_cur.find_one({"dc_id": ctx.author.id})
        if raw != None:
            if "val_user" in raw.keys():
                raw.pop("val_user",None)
                ign_cur.delete_many({"dc_id":ctx.author.id})
                ign_cur.insert_one(raw)
                embed = discord.Embed(color = 0x714ec4,description = "You have successfully unlinked `valorant` account.")
                embed.set_author(name = "Unlinked Successful!", icon_url= self.client.user.avatar_url)
                await ctx.send(embed = embed)
            else:
                embed = discord.Embed(color = 0x714ec4,description = "Overwrite ERROR!\n\nThis account is not linked with any `valorant` account.")
                embed.set_author(name = "ERROR", icon_url= self.client.user.avatar_url)
                await ctx.send(embed = embed)
        elif raw == None:
            embed = discord.Embed(color = 0x714ec4,description = "Overwrite ERROR!\n\nThis account is not linked with any `valorant` account.")
            embed.set_author(name = "ERROR", icon_url= self.client.user.avatar_url)
            await ctx.send(embed = embed)
    
    @unlink.command()
    async def lIchess(self,ctx):
        raw = ign_cur.find_one({"dc_id": ctx.author.id})
        if raw != None:
            if "lichess_user" in raw.keys():
                raw.pop("lichess_user",None)
                ign_cur.delete_many({"dc_id":ctx.author.id})
                ign_cur.insert_one(raw)
                embed = discord.Embed(color = 0x714ec4,description = "You have successfully unlinked `lichess` account.")
                embed.set_author(name = "Unlinked Successful!", icon_url= self.client.user.avatar_url)
                await ctx.send(embed = embed)
            else:
                embed = discord.Embed(color = 0x714ec4,description = "Overwrite ERROR!\n\nThis account is not linked with any `lichess` account.")
                embed.set_author(name = "ERROR", icon_url= self.client.user.avatar_url)
                await ctx.send(embed = embed)
        elif raw == None:
            embed = discord.Embed(color = 0x714ec4,description = "Overwrite ERROR!\n\nThis account is not linked with any `lichess` account.")
            embed.set_author(name = "ERROR", icon_url= self.client.user.avatar_url)
            await ctx.send(embed = embed)


    @commands.group(invoke_without_command = True,case_insensitive=True)
    async def profile(self,ctx):
        return
    
    @profile.command()
    async def CHess(self,ctx,*,name = ""):
        if name:
            try:
                user = ctx.message.mentions[0]
            except IndexError:
                user = ctx.guild.get_member_named(name)
            if not user:
                try:
                    user = ctx.guild.get_member(int(name))
                except:
                    pass
            if not user:
                embed = discord.Embed(color = 0x714ec4,description = "Index ERROR!")
                embed.set_author(name = "ERROR", icon_url= self.client.user.avatar_url)
                await ctx.send(embed = embed)
                return
        else:
            user = ctx.message.author

        raw = ign_cur.find_one({"dc_id": user.id})

        if raw != None:
            embed = discord.Embed(color = 0x714ec4, description = "`📡 fetching data......`") 
            link_msg = await ctx.send(embed = embed)
            if "chess_user" in raw.keys():
                # try:
                data = chessClient.loop.run_until_complete(gather(get_player_profile(raw["chess_user"])))[0].json
                data2 = chessClient.loop.run_until_complete(gather(get_player_stats(raw["chess_user"])))[0].json

                player = data["player"]
                stats = data2["stats"]

                profile_em = discord.Embed(color = 0x714ec4)
                profile_em.set_author(name = "CHESS PROFILE",icon_url= self.client.user.avatar_url, url = player["url"])
                try:
                    profile_em.add_field(name = 'NAME',
                        value = f'```\n{player["name"]}```')
                except:
                    profile_em.add_field(name = 'NAME :',
                        value = '```\nNone```')

                profile_em.add_field(name = f'USER NAME',
                    value = f'```\n{player["username"]}```')
                
                profile_em.add_field(name = "PROFILE URL",
                    value= f'```\n{player["url"]}```',
                    inline= False)
                
                # total_chess_bullet = stats['chess_bullet']['record']['draw'] + stats['chess_bullet']['record']['loss'] + stats['chess_bullet']['record']['win']
                # total_chess_blitz  = stats['chess_blitz']['record']['draw'] + stats['chess_blitz']['record']['loss'] + stats['chess_blitz']['record']['win']
                # total_chess_rapid = stats['chess_rapid']['record']['draw'] +  stats['chess_rapid']['record']['loss'] + stats['chess_rapid']['record']['win']            
                
                try:
                    total_chess_bullet = stats['chess_bullet']['record']['draw'] + stats['chess_bullet']['record']['loss'] + stats['chess_bullet']['record']['win']
                    profile_em.add_field(name = "<:bulllet:837074565331025920> BULLET",
                        value = f"```py\nGames  - {total_chess_bullet}\nRating - {stats['chess_bullet']['last']['rating']}```")
                except:
                    profile_em.add_field(name = "<:bulllet:837074565331025920> BULLET",
                        value = f"```py\nGames  - 0\nRating - 0```")

                try:
                    total_chess_blitz  = stats['chess_blitz']['record']['draw'] + stats['chess_blitz']['record']['loss'] + stats['chess_blitz']['record']['win']
                    profile_em.add_field(name = "<:blitz:837074538151804978> BLITZ",
                        value = f"```py\nGames  - {total_chess_blitz}\nRating - {stats['chess_blitz']['last']['rating']}```")
                except:
                    profile_em.add_field(name = "<:blitz:837074538151804978> BLITZ",
                        value = f"```py\nGames  - 0\nRating - 0```")

                try:
                    total_chess_rapid = stats['chess_rapid']['record']['draw'] +  stats['chess_rapid']['record']['loss'] + stats['chess_rapid']['record']['win']
                    profile_em.add_field(name = "<:rapid:837074588419489802> RAPID",
                        value = f"```py\nGames  - {total_chess_rapid}\nRating - {stats['chess_rapid']['last']['rating']}```")
                except:
                    profile_em.add_field(name = "<:rapid:837074588419489802> RAPID",
                        value = f"```py\nGames  - 0\nRating - 0```")

                await link_msg.edit(embed = profile_em)
                # except:
                #     temp = discord.Embed(title = user.name,description = "chess.com Account not found.\n\nPlease unlink and link your account and try again.", color = 0x714ec4)
                #     temp.set_author(name = "CHESS PROFILE", icon_url= self.client.user.avatar_url)
                #     await link_msg.edit(embed = temp)
            else:
                temp = discord.Embed(title = user.name,description = "This account is not linked with any chess.com account.", color = 0x714ec4)
                temp.set_author(name = "CHESS PROFILE", icon_url= self.client.user.avatar_url)
                await link_msg.edit(embed = temp)
        elif raw == None:
            temp = discord.Embed(title = user.name,description = "This account is not linked with any chess.com account.", color = 0x714ec4)
            temp.set_author(name = "CHESS PROFILE", icon_url= self.client.user.avatar_url)
            await link_msg.edit(embed = temp)

    @profile.command()
    async def Lichess(self,ctx,*,name =""):
        if name:
            try:
                user = ctx.message.mentions[0]
            except IndexError:
                user = ctx.guild.get_member_named(name)
            if not user:
                try:
                    user = ctx.guild.get_member(int(name))
                except:
                    pass
            if not user:
                embed = discord.Embed(color = 0x714ec4,description = "Index ERROR!")
                embed.set_author(name = "ERROR", icon_url= self.client.user.avatar_url)
                await ctx.send(embed = embed)
                return
        else:
            user = ctx.message.author

        raw = ign_cur.find_one({"dc_id": user.id})

        if raw != None:
            embed = discord.Embed(color = 0x714ec4, description = "`📡 fetching data......`") 
            link_msg = await ctx.send(embed = embed)
            if "lichess_user" in raw.keys():
                try:
                    user = lichess.api.user(raw["lichess_user"])
                    user_profile = user["profile"]
                    username = user["username"]
                    profile_em = discord.Embed(color = 0x714ec4)
                    profile_em.set_author(name = "LICHESS PROFILE",icon_url= self.client.user.avatar_url, url = user["url"])
                    firstname = ""
                    lastname = ""
                    fullname = ""
                    if "firstName" in user_profile.keys():
                        firstname = user_profile["firstName"]
                    
                    if "lastName" in user_profile.keys():
                        lastname = user_profile["lastName"]
                    
                    if firstname:
                        fullname = firstname
                    
                    if lastname:
                        fullname = fullname + " " + lastname

                    if fullname:
                        profile_em.add_field(name = "NAME", value= f"```\n{fullname}```")
                    else:
                        profile_em.add_field(name = "NAME",value= f"```\n{username}```")
                    
                    profile_em.add_field(name = "USER NAME", value = f"```\n{username}```")
                    profile_em.add_field(name = "PROFILE URL", value = f"```\n{user['url']}```", inline = False)

                    profile_em.add_field(name = "<:bulllet:837074565331025920> BULLET",
                    value= f'```py\nGames  - {user["perfs"]["bullet"]["games"]}\nRating - {user["perfs"]["bullet"]["rating"]}```')

                    profile_em.add_field(name = "<:blitz:837074538151804978> BLITZ",
                    value= f'```py\nGames  - {user["perfs"]["blitz"]["games"]}\nRating - {user["perfs"]["blitz"]["rating"]}```')

                    profile_em.add_field(name = "<:rapid:837074588419489802> RAPID",
                    value = f'```py\nGames  - {user["perfs"]["rapid"]["games"]}\nRating - {user["perfs"]["rapid"]["rating"]}```')

                    await link_msg.edit(embed = profile_em)
                except:
                    temp = discord.Embed(title = user.name,description = "Lichess Account not found.\n\nPlease unlink and link your account and try again.", color = 0x714ec4)
                    temp.set_author(name = "LICHESS PROFILE", icon_url= self.client.user.avatar_url)
                    await link_msg.edit(embed = temp)
            else:
                temp = discord.Embed(title = user.name,description = "This account is not linked with any chess.com account.", color = 0x714ec4)
                temp.set_author(name = "LICHESS PROFILE", icon_url= self.client.user.avatar_url)
                await link_msg.edit(embed = temp)
        elif raw == None:
            temp = discord.Embed(title = user.name,description = "This account is not linked with any lichess account.", color = 0x714ec4)
            temp.set_author(name = "LICHESS PROFILE", icon_url= self.client.user.avatar_url)
            await link_msg.edit(embed = temp)


    @profile.command(aliases = ["val"])
    async def VAlorant(self,ctx,*,name=""):
        if name:
            try:
                user = ctx.message.mentions[0]
            except IndexError:
                user = ctx.guild.get_member_named(name)
            if not user:
                try:
                    user = ctx.guild.get_member(int(name))
                except:
                    pass
            if not user:
                embed = discord.Embed(color = 0x714ec4,description = "Index ERROR!")
                embed.set_author(name = "ERROR", icon_url= self.client.user.avatar_url)
                await ctx.send(embed = embed)
                return
        else:
            user = ctx.message.author

        raw = ign_cur.find_one({"dc_id": user.id})

        if raw != None:
            embed = discord.Embed(color = 0x714ec4, description = "`📡 fetching data......`") 
            link_msg = await ctx.send(embed = embed)
            if 'val_user' in raw.keys():
                try:
                    splited = raw['val_user'].split("#")
                except:
                    temp = discord.Embed(title = user.name,description = "`Valorant` Account not found.", color = 0x714ec4)
                    temp.set_author(name = "VALORANT PROFILE", icon_url= self.client.user.avatar_url)
                    await link_msg.edit(embed = temp)
                    return

                name = splited[0].replace(" ","%20")
                try:
                    tag = splited[1]
                except:
                    temp = discord.Embed(title = user.name,description = "Invalid `valorant` IGN.\n\nPlease make sure you provided your tag along with the username.\nExample: `.o link val SorenBlank#1570`", color = 0x714ec4)
                    temp.set_author(name = "VALORANT PROFILE", icon_url= self.client.user.avatar_url)
                    await link_msg.edit(embed = temp)
                    return

                url = f"https://tracker.gg/valorant/profile/riot/{name}%23{tag}/overview"
                req = requests.get(url)
                if str(req) == "<Response [200]>":
                    try:
                        def fill_space(number, spaces):
                            x = number
                            if len(number) < spaces:
                                num_of_spaces = spaces - len(number)
                                x = x + (num_of_spaces*" ")
                                return x
                            else:
                                return number
                        
                        req = req.text
                        soup = BeautifulSoup(req, 'html.parser')
                        title = soup.find('div',class_ = "segment-stats main-stats card bordered header-bordered responsive").find('h2').text

                        title = title.split(" ")[0]
                        
                        weapon = soup.find_all('div', class_ = 'weapon')
                        playtime = soup.find('span', class_ = 'playtime').text[11:-19]
                        matches = soup.find('span', class_ = 'matches').text.split(" ")[10]

                        data_raw = soup.find_all('div', class_ = 'main')
                        data_raw_2 = data_raw[0].find_all('span','value')
                        wins = data_raw_2[0].text.replace(",","")
                        kills = data_raw_2[1].text.replace(",","")
                        headshots = data_raw_2[2].text.replace(",","")
                        deaths = data_raw_2[3].text.replace(",","")
                        assists = data_raw_2[4].text.replace(",","")
                        clutches = data_raw_2[7].text.replace(",","")

                        # for i in find:
                        #     weapon = i.find('div','weapon__name').text
                        #     kills = i.find('span','value').text
                        #     x = x + f"{weapon} - {kills}\n"

                        if title != "Deathmatch":
                            accuracy_stats_raw = (soup.find('table', class_ = "accuracy__stats")).find_all('tr')

                            head_per = accuracy_stats_raw[0].find_all("span",class_ = "stat__value")[0].text
                            head_hit = accuracy_stats_raw[0].find_all("span",class_ = "stat__value")[1].text.replace(",","")

                            body_per = accuracy_stats_raw[1].find_all("span",class_ = "stat__value")[0].text
                            body_hit = accuracy_stats_raw[1].find_all("span",class_ = "stat__value")[1].text.replace(",","")

                            leg_per = accuracy_stats_raw[2].find_all("span",class_ = "stat__value")[0].text
                            leg_hit = accuracy_stats_raw[2].find_all("span",class_ = "stat__value")[1].text.replace(",","")
                        
                        weapons = find = soup.find_all('div', class_ = 'weapon')

                        weapon1 = weapons[0].find('div','weapon__name').text
                        kill1 = weapons[0].find('span','value').text.replace(",","")

                        weapon2 = weapons[1].find('div','weapon__name').text
                        kill2 = weapons[1].find('span','value').text.replace(",","")
                        
                        weapon3 = weapons[2].find('div','weapon__name').text
                        kill3 = weapons[2].find('span','value').text.replace(",","")


                        val = discord.Embed(color = 0x714ec4)
                        val.set_author(name = "VALORANT PROFILE",icon_url= self.client.user.avatar_url,url= url)
                        val.add_field(name = f"<:overview:836858315664261121> {title} | <:clockval:837391041123975219> {playtime} | {matches} Matches", 
                        value= f"```py\nWins     -  {fill_space(str(wins),5)} |  Assists   -   {assists}\nKills    -  {fill_space(str(kills),5)} |  Deaths    -   {deaths}\nCluthes  -  {fill_space(str(clutches),5)} |  Headshots -   {headshots}```", inline= False)
                        
                        if title == "Competitive":
                            img = soup.find('div', class_ = 'valorant-highlighted-content__stats').find_all('img')[0].attrs['src']
                            val.set_thumbnail(url = img)
                        
                        # val.add_field(name = f"<:matches:836871938927886366> Last 5 Matches",
                        # value= "```diff\n   MAP    -  SCORE  -   K/D/A\n ——————————————————————————————\n+ Split   -  12/05  -  08/14/13\n+ Bind    -  13/00  -  02/01/00\n- Icebox  -  09/13  -  19/17/07\n+ Ascent  -  13/11  -  21/18/05```",inline = False)
                        
                        if title != "Deathmatch":
                            val.add_field(name = f"<:accuracy:836866509061226526> Accuracy",
                            value= f"```py\nHead - {fill_space(head_hit,3)} ({head_per})\nBody - {fill_space(body_hit,3)} ({body_per})\nLegs - {fill_space(leg_hit,3)} ({leg_per})```")

                        val.add_field(name = f"<:weapon:836861817170952255> Top Weapons",
                        value = f"```py\n{fill_space(weapon1, 8)} -  {kill1}\n{fill_space(weapon2, 8)} -  {kill2}\n{fill_space(weapon3, 8)} -  {kill3}```")

                        await link_msg.edit(embed = val)
                    except:
                        temp = discord.Embed(title = user.name,description = "No matches found for the specified mode.", color = 0x714ec4)
                        temp.set_author(name = "VALORANT PROFILE", icon_url= self.client.user.avatar_url)
                        await link_msg.edit(embed = temp)
                        return
                if str(req) == "<Response [404]>":
                    temp = discord.Embed(title = user.name,description = "`Valorant` Account not found.", color = 0x714ec4)
                    temp.set_author(name = "VALORANT PROFILE", icon_url= self.client.user.avatar_url)
                    await link_msg.edit(embed = temp)
                
                if str(req) == "<Response [451]>":
                    temp = discord.Embed(title = user.name,description = f"Please sign up on [tracker.gg]({url}) with your Riot account to view your stats.", color = 0x714ec4)
                    temp.set_author(name = "VALORANT PROFILE", icon_url= self.client.user.avatar_url)
                    await link_msg.edit(embed = temp)
            else:
                temp = discord.Embed(title = user.name,description = "This account is not linked with any `valorant` account.", color = 0x714ec4)
                temp.set_author(name = "VALORANT PROFILE", icon_url= self.client.user.avatar_url)
                await link_msg.edit(embed = temp)
        
    
    @profile.command(aliases = ["competitive"])
    async def comp(self,ctx,game,*,name=""):
        if game:
            if game.lower() == "val" or game.lower() == "valorant":
                if name:
                    try:
                        user = ctx.message.mentions[0]
                    except IndexError:
                        user = ctx.guild.get_member_named(name)
                    if not user:
                        try:
                            user = ctx.guild.get_member(int(name))
                        except:
                            pass
                    if not user:
                        embed = discord.Embed(color = 0x714ec4,description = "Index ERROR!")
                        embed.set_author(name = "ERROR", icon_url= self.client.user.avatar_url)
                        await ctx.send(embed = embed)
                        return
                else:
                    user = ctx.message.author

                raw = ign_cur.find_one({"dc_id": user.id})

                if raw != None:
                    embed = discord.Embed(color = 0x714ec4, description = "`📡 fetching data......`") 
                    link_msg = await ctx.send(embed = embed)
                    if 'val_user' in raw.keys():

                        try:
                            splited = raw['val_user'].split("#")
                        except:
                            temp = discord.Embed(title = user.name,description = "`Valorant` Account not found.", color = 0x714ec4)
                            temp.set_author(name = "VALORANT PROFILE", icon_url= self.client.user.avatar_url)
                            await link_msg.edit(embed = temp)
                            return

                        name = splited[0].replace(" ","%20")
                        try:
                            tag = splited[1]
                        except:
                            temp = discord.Embed(title = user.name,description = "Invalid valorant IGN.\n\nPlease make sure you provided your tag along with the username.\nExample: `.o link val SorenBlank#1570`", color = 0x714ec4)
                            temp.set_author(name = "VALORANT PROFILE", icon_url= self.client.user.avatar_url)
                            await link_msg.edit(embed = temp)
                            return

                        url = f"https://tracker.gg/valorant/profile/riot/{name}%23{tag}/overview?playlist=competitive"
                        req = requests.get(url)
                        if str(req) == "<Response [200]>":
                            try:

                                def fill_space(number, spaces):
                                    x = number
                                    if len(number) < spaces:
                                        num_of_spaces = spaces - len(number)
                                        x = x + (num_of_spaces*" ")
                                        return x
                                    else:
                                        return number
                                
                                req = req.text
                                soup = BeautifulSoup(req, 'html.parser')
                                title = soup.find('div',class_ = "segment-stats main-stats card bordered header-bordered responsive").find('h2').text

                                title = title.split(" ")[0]
                                
                                weapon = soup.find_all('div', class_ = 'weapon')
                                playtime = soup.find('span', class_ = 'playtime').text[11:-19]
                                matches = soup.find('span', class_ = 'matches').text.split(" ")[10]

                                data_raw = soup.find_all('div', class_ = 'main')
                                data_raw_2 = data_raw[0].find_all('span','value')
                                wins = data_raw_2[0].text.replace(",","")
                                kills = data_raw_2[1].text.replace(",","")
                                headshots = data_raw_2[2].text.replace(",","")
                                deaths = data_raw_2[3].text.replace(",","")
                                assists = data_raw_2[4].text.replace(",","")
                                clutches = data_raw_2[7].text.replace(",","")

                                # for i in find:
                                #     weapon = i.find('div','weapon__name').text
                                #     kills = i.find('span','value').text
                                #     x = x + f"{weapon} - {kills}\n"

                                if title != "Deathmatch":
                                    accuracy_stats_raw = (soup.find('table', class_ = "accuracy__stats")).find_all('tr')

                                    head_per = accuracy_stats_raw[0].find_all("span",class_ = "stat__value")[0].text
                                    head_hit = accuracy_stats_raw[0].find_all("span",class_ = "stat__value")[1].text.replace(",","")

                                    body_per = accuracy_stats_raw[1].find_all("span",class_ = "stat__value")[0].text
                                    body_hit = accuracy_stats_raw[1].find_all("span",class_ = "stat__value")[1].text.replace(",","")

                                    leg_per = accuracy_stats_raw[2].find_all("span",class_ = "stat__value")[0].text
                                    leg_hit = accuracy_stats_raw[2].find_all("span",class_ = "stat__value")[1].text.replace(",","")
                                
                                weapons = find = soup.find_all('div', class_ = 'weapon')

                                weapon1 = weapons[0].find('div','weapon__name').text
                                kill1 = weapons[0].find('span','value').text.replace(",","")

                                weapon2 = weapons[1].find('div','weapon__name').text
                                kill2 = weapons[1].find('span','value').text.replace(",","")
                                
                                weapon3 = weapons[2].find('div','weapon__name').text
                                kill3 = weapons[2].find('span','value').text.replace(",","")

                                val = discord.Embed(color = 0x714ec4)
                                val.set_author(name = "VALORANT PROFILE",icon_url= self.client.user.avatar_url,url= url)
                                val.add_field(name = f"<:overview:836858315664261121> {title} | <:clockval:837391041123975219> {playtime} | {matches} Matches", 
                                value= f"```py\nWins     -  {fill_space(str(wins),5)} |  Assists   -   {assists}\nKills    -  {fill_space(str(kills),5)} |  Deaths    -   {deaths}\nCluthes  -  {fill_space(str(clutches),5)} |  Headshots -   {headshots}```", inline= False)
                                
                                
                                # val.add_field(name = f"<:matches:836871938927886366> Last 5 Matches",
                                # value= "```diff\n   MAP    -  SCORE  -   K/D/A\n ——————————————————————————————\n+ Split   -  12/05  -  08/14/13\n+ Bind    -  13/00  -  02/01/00\n- Icebox  -  09/13  -  19/17/07\n+ Ascent  -  13/11  -  21/18/05```",inline = False)
                                
                                if title != "Deathmatch":
                                    val.add_field(name = f"<:accuracy:836866509061226526> Accuracy",
                                    value= f"```py\nHead - {fill_space(head_hit,3)} ({head_per})\nBody - {fill_space(body_hit,3)} ({body_per})\nLegs - {fill_space(leg_hit,3)} ({leg_per})```")

                                val.add_field(name = f"<:weapon:836861817170952255> Top Weapons",
                                value = f"```py\n{fill_space(weapon1, 8)} -  {kill1}\n{fill_space(weapon2, 8)} -  {kill2}\n{fill_space(weapon3, 8)} -  {kill3}```")

                                img = soup.find('div', class_ = 'valorant-highlighted-content__stats').find_all('img')[0].attrs['src']

                                val.set_thumbnail(url = img)

                                await link_msg.edit(embed = val)
                            except:
                                temp = discord.Embed(title = user.name,description = "No matches found for the specified mode.", color = 0x714ec4)
                                temp.set_author(name = "VALORANT PROFILE", icon_url= self.client.user.avatar_url)
                                await link_msg.edit(embed = temp)
                                return
                        if str(req) == "<Response [404]>":
                            temp = discord.Embed(title = user.name,description = "`Valorant` Account not found.", color = 0x714ec4)
                            temp.set_author(name = "VALORANT PROFILE", icon_url= self.client.user.avatar_url)
                            await link_msg.edit(embed = temp)
                        
                        if str(req) == "<Response [451]>":
                            temp = discord.Embed(title = user.name,description = f"Please sign up on [tracker.gg]({url}) with your Riot account to view your stats.", color = 0x714ec4)
                            temp.set_author(name = "VALORANT PROFILE", icon_url= self.client.user.avatar_url)
                            await link_msg.edit(embed = temp)
                    else:
                        temp = discord.Embed(title = user.name,description = "This account is not linked with any `valorant` account.", color = 0x714ec4)
                        temp.set_author(name = "VALORANT PROFILE", icon_url= self.client.user.avatar_url)
                        await link_msg.edit(embed = temp)
    
    
    @profile.command(aliases = ["ur"])
    async def unrated(self,ctx,game,*,name=""):
        if game:
            if game.lower() == "val" or game.lower() == "valorant":
                if name:
                    try:
                        user = ctx.message.mentions[0]
                    except IndexError:
                        user = ctx.guild.get_member_named(name)
                    if not user:
                        try:
                            user = ctx.guild.get_member(int(name))
                        except:
                            pass
                    if not user:
                        embed = discord.Embed(color = 0x714ec4,description = "Index ERROR!")
                        embed.set_author(name = "ERROR", icon_url= self.client.user.avatar_url)
                        await ctx.send(embed = embed)
                        return
                else:
                    user = ctx.message.author

                raw = ign_cur.find_one({"dc_id": user.id})

                if raw != None:
                    embed = discord.Embed(color = 0x714ec4, description = "`📡 fetching data......`") 
                    link_msg = await ctx.send(embed = embed)
                    if 'val_user' in raw.keys():

                        try:
                            splited = raw['val_user'].split("#")
                        except:
                            temp = discord.Embed(title = user.name,description = "`Valorant` Account not found.", color = 0x714ec4)
                            temp.set_author(name = "VALORANT PROFILE", icon_url= self.client.user.avatar_url)
                            await link_msg.edit(embed = temp)
                            return

                        name = splited[0].replace(" ","%20")
                        try:
                            tag = splited[1]
                        except:
                            temp = discord.Embed(title = user.name,description = "Invalid `valorant` IGN.\n\nPlease make sure you provided your tag along with the username.\nExample: `.o link val SorenBlank#1570`", color = 0x714ec4)
                            temp.set_author(name = "VALORANT PROFILE", icon_url= self.client.user.avatar_url)
                            await link_msg.edit(embed = temp)
                            return

                        url = f"https://tracker.gg/valorant/profile/riot/{name}%23{tag}/overview?playlist=unrated"
                        req = requests.get(url)
                        if str(req) == "<Response [200]>":
                            try:

                                def fill_space(number, spaces):
                                    x = number
                                    if len(number) < spaces:
                                        num_of_spaces = spaces - len(number)
                                        x = x + (num_of_spaces*" ")
                                        return x
                                    else:
                                        return number
                                
                                req = req.text
                                soup = BeautifulSoup(req, 'html.parser')
                                title = soup.find('div',class_ = "segment-stats main-stats card bordered header-bordered responsive").find('h2').text

                                title = title.split(" ")[0]
                                
                                weapon = soup.find_all('div', class_ = 'weapon')
                                playtime = soup.find('span', class_ = 'playtime').text[11:-19]
                                matches = soup.find('span', class_ = 'matches').text.split(" ")[10]

                                data_raw = soup.find_all('div', class_ = 'main')
                                data_raw_2 = data_raw[0].find_all('span','value')
                                wins = data_raw_2[0].text.replace(",","")
                                kills = data_raw_2[1].text.replace(",","")
                                headshots = data_raw_2[2].text.replace(",","")
                                deaths = data_raw_2[3].text.replace(",","")
                                assists = data_raw_2[4].text.replace(",","")
                                clutches = data_raw_2[7].text.replace(",","")

                                # for i in find:
                                #     weapon = i.find('div','weapon__name').text
                                #     kills = i.find('span','value').text
                                #     x = x + f"{weapon} - {kills}\n"

                                if title != "Deathmatch":
                                    accuracy_stats_raw = (soup.find('table', class_ = "accuracy__stats")).find_all('tr')

                                    head_per = accuracy_stats_raw[0].find_all("span",class_ = "stat__value")[0].text
                                    head_hit = accuracy_stats_raw[0].find_all("span",class_ = "stat__value")[1].text.replace(",","")

                                    body_per = accuracy_stats_raw[1].find_all("span",class_ = "stat__value")[0].text
                                    body_hit = accuracy_stats_raw[1].find_all("span",class_ = "stat__value")[1].text.replace(",","")

                                    leg_per = accuracy_stats_raw[2].find_all("span",class_ = "stat__value")[0].text
                                    leg_hit = accuracy_stats_raw[2].find_all("span",class_ = "stat__value")[1].text.replace(",","")
                                
                                weapons = find = soup.find_all('div', class_ = 'weapon')

                                weapon1 = weapons[0].find('div','weapon__name').text
                                kill1 = weapons[0].find('span','value').text.replace(",","")

                                weapon2 = weapons[1].find('div','weapon__name').text
                                kill2 = weapons[1].find('span','value').text.replace(",","")
                                
                                weapon3 = weapons[2].find('div','weapon__name').text
                                kill3 = weapons[2].find('span','value').text.replace(",","")


                                val = discord.Embed(color = 0x714ec4)
                                val.set_author(name = "VALORANT PROFILE",icon_url= self.client.user.avatar_url,url= url)
                                val.add_field(name = f"<:overview:836858315664261121> {title} | <:clockval:837391041123975219> {playtime} | {matches} Matches", 
                                value= f"```py\nWins     -  {fill_space(str(wins),5)} |  Assists   -   {assists}\nKills    -  {fill_space(str(kills),5)} |  Deaths    -   {deaths}\nCluthes  -  {fill_space(str(clutches),5)} |  Headshots -   {headshots}```", inline= False)
                                
                                
                                # val.add_field(name = f"<:matches:836871938927886366> Last 5 Matches",
                                # value= "```diff\n   MAP    -  SCORE  -   K/D/A\n ——————————————————————————————\n+ Split   -  12/05  -  08/14/13\n+ Bind    -  13/00  -  02/01/00\n- Icebox  -  09/13  -  19/17/07\n+ Ascent  -  13/11  -  21/18/05```",inline = False)
                                
                                if title != "Deathmatch":
                                    val.add_field(name = f"<:accuracy:836866509061226526> Accuracy",
                                    value= f"```py\nHead - {fill_space(head_hit,3)} ({head_per})\nBody - {fill_space(body_hit,3)} ({body_per})\nLegs - {fill_space(leg_hit,3)} ({leg_per})```")

                                val.add_field(name = f"<:weapon:836861817170952255> Top Weapons",
                                value = f"```py\n{fill_space(weapon1, 8)} -  {kill1}\n{fill_space(weapon2, 8)} -  {kill2}\n{fill_space(weapon3, 8)} -  {kill3}```")

                                await link_msg.edit(embed = val)
                            except:
                                temp = discord.Embed(title = user.name,description = "No matches found for the specified mode.", color = 0x714ec4)
                                temp.set_author(name = "VALORANT PROFILE", icon_url= self.client.user.avatar_url)
                                await link_msg.edit(embed = temp)
                                return
                            
                        if str(req) == "<Response [404]>":
                            temp = discord.Embed(title = user.name,description = "`Valorant` Account not found.", color = 0x714ec4)
                            temp.set_author(name = "VALORANT PROFILE", icon_url= self.client.user.avatar_url)
                            await link_msg.edit(embed = temp)
                        
                        if str(req) == "<Response [451]>":
                            temp = discord.Embed(title = user.name,description = f"Please sign up on [tracker.gg]({url}) with your Riot account to view your stats.", color = 0x714ec4)
                            temp.set_author(name = "VALORANT PROFILE", icon_url= self.client.user.avatar_url)
                            await link_msg.edit(embed = temp)
                    else:
                        temp = discord.Embed(title = user.name,description = "This account is not linked with any `valorant` account.", color = 0x714ec4)
                        temp.set_author(name = "VALORANT PROFILE", icon_url= self.client.user.avatar_url)
                        await link_msg.edit(embed = temp)

    @profile.command(aliases = ["spikerush", "rush"])
    async def spike(self,ctx,game,*,name=""):
        if game:
            if game.lower() == "val" or game.lower() == "valorant":
                if name:
                    try:
                        user = ctx.message.mentions[0]
                    except IndexError:
                        user = ctx.guild.get_member_named(name)
                    if not user:
                        try:
                            user = ctx.guild.get_member(int(name))
                        except:
                            pass
                    if not user:
                        embed = discord.Embed(color = 0x714ec4,description = "Index ERROR!")
                        embed.set_author(name = "ERROR", icon_url= self.client.user.avatar_url)
                        await ctx.send(embed = embed)
                        return
                else:
                    user = ctx.message.author

                raw = ign_cur.find_one({"dc_id": user.id})

                if raw != None:
                    embed = discord.Embed(color = 0x714ec4, description = "`📡 fetching data......`") 
                    link_msg = await ctx.send(embed = embed)
                    if 'val_user' in raw.keys():

                        try:
                            splited = raw['val_user'].split("#")
                        except:
                            temp = discord.Embed(title = user.name,description = "`Valorant` Account not found.", color = 0x714ec4)
                            temp.set_author(name = "VALORANT PROFILE", icon_url= self.client.user.avatar_url)
                            await link_msg.edit(embed = temp)
                            return

                        name = splited[0].replace(" ","%20")
                        try:
                            tag = splited[1]
                        except:
                            temp = discord.Embed(title = user.name,description = "Invalid `valorant` IGN.\n\nPlease make sure you provided your tag along with the username.\nExample: `.o link val SorenBlank#1570`", color = 0x714ec4)
                            temp.set_author(name = "VALORANT PROFILE", icon_url= self.client.user.avatar_url)
                            await link_msg.edit(embed = temp)
                            return
                        
                        url = f"https://tracker.gg/valorant/profile/riot/{name}%23{tag}/overview?playlist=spikerush"
                        req = requests.get(url)
                        if str(req) == "<Response [200]>":
                            try:

                                def fill_space(number, spaces):
                                    x = number
                                    if len(number) < spaces:
                                        num_of_spaces = spaces - len(number)
                                        x = x + (num_of_spaces*" ")
                                        return x
                                    else:
                                        return number
                                
                                req = req.text
                                soup = BeautifulSoup(req, 'html.parser')
                                title = soup.find('div',class_ = "segment-stats main-stats card bordered header-bordered responsive").find('h2').text

                                title = title.split(" ")[0] + " " + title.split(" ")[1]
                                
                                weapon = soup.find_all('div', class_ = 'weapon')
                                playtime = soup.find('span', class_ = 'playtime').text[11:-19]
                                matches = soup.find('span', class_ = 'matches').text.split(" ")[10]

                                data_raw = soup.find_all('div', class_ = 'main')
                                data_raw_2 = data_raw[0].find_all('span','value')
                                wins = data_raw_2[0].text.replace(",","")
                                kills = data_raw_2[1].text.replace(",","")
                                headshots = data_raw_2[2].text.replace(",","")
                                deaths = data_raw_2[3].text.replace(",","")
                                assists = data_raw_2[4].text.replace(",","")
                                clutches = data_raw_2[7].text.replace(",","")

                                # for i in find:
                                #     weapon = i.find('div','weapon__name').text
                                #     kills = i.find('span','value').text
                                #     x = x + f"{weapon} - {kills}\n"

                                if title != "Deathmatch":
                                    accuracy_stats_raw = (soup.find('table', class_ = "accuracy__stats")).find_all('tr')

                                    head_per = accuracy_stats_raw[0].find_all("span",class_ = "stat__value")[0].text
                                    head_hit = accuracy_stats_raw[0].find_all("span",class_ = "stat__value")[1].text.replace(",","")

                                    body_per = accuracy_stats_raw[1].find_all("span",class_ = "stat__value")[0].text
                                    body_hit = accuracy_stats_raw[1].find_all("span",class_ = "stat__value")[1].text.replace(",","")

                                    leg_per = accuracy_stats_raw[2].find_all("span",class_ = "stat__value")[0].text
                                    leg_hit = accuracy_stats_raw[2].find_all("span",class_ = "stat__value")[1].text.replace(",","")
                                
                                weapons = find = soup.find_all('div', class_ = 'weapon')

                                weapon1 = weapons[0].find('div','weapon__name').text
                                kill1 = weapons[0].find('span','value').text.replace(",","")

                                weapon2 = weapons[1].find('div','weapon__name').text.replace(",","")
                                kill2 = weapons[1].find('span','value').text
                                
                                weapon3 = weapons[2].find('div','weapon__name').text
                                kill3 = weapons[2].find('span','value').text.replace(",","")


                                val = discord.Embed(color = 0x714ec4)
                                val.set_author(name = "VALORANT PROFILE",icon_url= self.client.user.avatar_url,url= url)
                                val.add_field(name = f"<:overview:836858315664261121> {title} | <:clockval:837391041123975219> {playtime} | {matches} Matches", 
                                value= f"```py\nWins     -  {fill_space(str(wins),5)} |  Assists   -   {assists}\nKills    -  {fill_space(str(kills),5)} |  Deaths    -   {deaths}\nCluthes  -  {fill_space(str(clutches),5)} |  Headshots -   {headshots}```", inline= False)
                                
                                
                                # val.add_field(name = f"<:matches:836871938927886366> Last 5 Matches",
                                # value= "```diff\n   MAP    -  SCORE  -   K/D/A\n ——————————————————————————————\n+ Split   -  12/05  -  08/14/13\n+ Bind    -  13/00  -  02/01/00\n- Icebox  -  09/13  -  19/17/07\n+ Ascent  -  13/11  -  21/18/05```",inline = False)
                                
                                if title != "Deathmatch":
                                    val.add_field(name = f"<:accuracy:836866509061226526> Accuracy",
                                    value= f"```py\nHead - {fill_space(head_hit,3)} ({head_per})\nBody - {fill_space(body_hit,3)} ({body_per})\nLegs - {fill_space(leg_hit,3)} ({leg_per})```")

                                val.add_field(name = f"<:weapon:836861817170952255> Top Weapons",
                                value = f"```py\n{fill_space(weapon1, 8)} -  {kill1}\n{fill_space(weapon2, 8)} -  {kill2}\n{fill_space(weapon3, 8)} -  {kill3}```")

                                await link_msg.edit(embed = val)
                            except:
                                temp = discord.Embed(title = user.name,description = "No matches found for the specified mode.", color = 0x714ec4)
                                temp.set_author(name = "VALORANT PROFILE", icon_url= self.client.user.avatar_url)
                                await link_msg.edit(embed = temp)
                                return
                            
                        if str(req) == "<Response [404]>":
                            temp = discord.Embed(title = user.name,description = "`Valorant` Account not found.", color = 0x714ec4)
                            temp.set_author(name = "VALORANT PROFILE", icon_url= self.client.user.avatar_url)
                            await link_msg.edit(embed = temp)
                        
                        if str(req) == "<Response [451]>":
                            temp = discord.Embed(title = user.name,description = f"Please sign up on [tracker.gg]({url}) with your Riot account to view your stats.", color = 0x714ec4)
                            temp.set_author(name = "VALORANT PROFILE", icon_url= self.client.user.avatar_url)
                            await link_msg.edit(embed = temp)
                    else:
                        temp = discord.Embed(title = user.name,description = "This account is not linked with any `valorant` account.", color = 0x714ec4)
                        temp.set_author(name = "VALORANT PROFILE", icon_url= self.client.user.avatar_url)
                        await link_msg.edit(embed = temp)
        
    @profile.command()
    async def deathmatch(self,ctx,game,*,name=""):
        if game:
            if game.lower() == "val" or game.lower() == "valorant":
                if name:
                    try:
                        user = ctx.message.mentions[0]
                    except IndexError:
                        user = ctx.guild.get_member_named(name)
                    if not user:
                        try:
                            user = ctx.guild.get_member(int(name))
                        except:
                            pass
                    if not user:
                        embed = discord.Embed(color = 0x714ec4,description = "Index ERROR!")
                        embed.set_author(name = "ERROR", icon_url= self.client.user.avatar_url)
                        await ctx.send(embed = embed)
                        return
                else:
                    user = ctx.message.author

                raw = ign_cur.find_one({"dc_id": user.id})

                if raw != None:
                    embed = discord.Embed(color = 0x714ec4, description = "`📡 fetching data......`") 
                    link_msg = await ctx.send(embed = embed)
                    if 'val_user' in raw.keys():

                        try:
                            splited = raw['val_user'].split("#")
                        except:
                            temp = discord.Embed(title = user.name,description = "`Valorant` Account not found.", color = 0x714ec4)
                            temp.set_author(name = "VALORANT PROFILE", icon_url= self.client.user.avatar_url)
                            await link_msg.edit(embed = temp)
                            return

                        name = splited[0].replace(" ","%20")
                        try:
                            tag = splited[1]
                        except:
                            temp = discord.Embed(title = user.name,description = "Invalid `valorant` IGN.\n\nPlease make sure you provided your tag along with the username.\nExample: `.o link val SorenBlank#1570`", color = 0x714ec4)
                            temp.set_author(name = "VALORANT PROFILE", icon_url= self.client.user.avatar_url)
                            await link_msg.edit(embed = temp)
                            return

                        url = f"https://tracker.gg/valorant/profile/riot/{name}%23{tag}/overview?playlist=deathmatch"
                        req = requests.get(url)
                        if str(req) == "<Response [200]>":
                            try:

                                def fill_space(number, spaces):
                                    x = number
                                    if len(number) < spaces:
                                        num_of_spaces = spaces - len(number)
                                        x = x + (num_of_spaces*" ")
                                        return x
                                    else:
                                        return number
                                
                                req = req.text
                                soup = BeautifulSoup(req, 'html.parser')
                                title = soup.find('div',class_ = "segment-stats main-stats card bordered header-bordered responsive").find('h2').text

                                title = title.split(" ")[0]
                                
                                weapon = soup.find_all('div', class_ = 'weapon')
                                playtime = soup.find('span', class_ = 'playtime').text[11:-19]
                                matches = soup.find('span', class_ = 'matches').text.split(" ")[10]

                                data_raw = soup.find_all('div', class_ = 'main')
                                data_raw_2 = data_raw[0].find_all('span','value')
                                wins = data_raw_2[0].text.replace(",","")
                                kills = data_raw_2[1].text.replace(",","")
                                headshots = data_raw_2[2].text.replace(",","")
                                deaths = data_raw_2[3].text.replace(",","")
                                assists = data_raw_2[4].text.replace(",","")
                                clutches = data_raw_2[7].text.replace(",","")

                                # for i in find:
                                #     weapon = i.find('div','weapon__name').text
                                #     kills = i.find('span','value').text
                                #     x = x + f"{weapon} - {kills}\n"

                                if title != "Deathmatch":
                                    accuracy_stats_raw = (soup.find('table', class_ = "accuracy__stats")).find_all('tr')

                                    head_per = accuracy_stats_raw[0].find_all("span",class_ = "stat__value")[0].text
                                    head_hit = accuracy_stats_raw[0].find_all("span",class_ = "stat__value")[1].text.replace(",","")

                                    body_per = accuracy_stats_raw[1].find_all("span",class_ = "stat__value")[0].text
                                    body_hit = accuracy_stats_raw[1].find_all("span",class_ = "stat__value")[1].text.replace(",","")

                                    leg_per = accuracy_stats_raw[2].find_all("span",class_ = "stat__value")[0].text
                                    leg_hit = accuracy_stats_raw[2].find_all("span",class_ = "stat__value")[1].text.replace(",","")
                                
                                weapons = find = soup.find_all('div', class_ = 'weapon')

                                weapon1 = weapons[0].find('div','weapon__name').text
                                kill1 = weapons[0].find('span','value').text.replace(",","")

                                weapon2 = weapons[1].find('div','weapon__name').text
                                kill2 = weapons[1].find('span','value').text.replace(",","")
                                
                                weapon3 = weapons[2].find('div','weapon__name').text
                                kill3 = weapons[2].find('span','value').text.replace(",","")


                                val = discord.Embed(color = 0x714ec4)
                                val.set_author(name = "VALORANT PROFILE",icon_url= self.client.user.avatar_url,url= url)
                                val.add_field(name = f"<:overview:836858315664261121> {title} | <:clockval:837391041123975219> {playtime} | {matches} Matches", 
                                value= f"```py\nWins     -  {fill_space(str(wins),5)} |  Assists   -   {assists}\nKills    -  {fill_space(str(kills),5)} |  Deaths    -   {deaths}\nCluthes  -  {fill_space(str(clutches),5)} |  Headshots -   {headshots}```", inline= False)
                                
                                
                                # val.add_field(name = f"<:matches:836871938927886366> Last 5 Matches",
                                # value= "```diff\n   MAP    -  SCORE  -   K/D/A\n ——————————————————————————————\n+ Split   -  12/05  -  08/14/13\n+ Bind    -  13/00  -  02/01/00\n- Icebox  -  09/13  -  19/17/07\n+ Ascent  -  13/11  -  21/18/05```",inline = False)
                                
                                if title != "Deathmatch":
                                    val.add_field(name = f"<:accuracy:836866509061226526> Accuracy",
                                    value= f"```py\nHead - {fill_space(head_hit,3)} ({head_per})\nBody - {fill_space(body_hit,3)} ({body_per})\nLegs - {fill_space(leg_hit,3)} ({leg_per})```")

                                val.add_field(name = f"<:weapon:836861817170952255> Top Weapons",
                                value = f"```py\n{fill_space(weapon1, 8)} -  {kill1}\n{fill_space(weapon2, 8)} -  {kill2}\n{fill_space(weapon3, 8)} -  {kill3}```")

                                await link_msg.edit(embed = val)
                            except:
                                temp = discord.Embed(title = user.name,description = "No matches found for the specified mode.", color = 0x714ec4)
                                temp.set_author(name = "VALORANT PROFILE", icon_url= self.client.user.avatar_url)
                                await link_msg.edit(embed = temp)
                                return
                            
                        if str(req) == "<Response [404]>":
                            temp = discord.Embed(title = user.name,description = "`Valorant` Account not found.", color = 0x714ec4)
                            temp.set_author(name = "VALORANT PROFILE", icon_url= self.client.user.avatar_url)
                            await link_msg.edit(embed = temp)
                        
                        if str(req) == "<Response [451]>":
                            temp = discord.Embed(title = user.name,description = f"Please sign up on [tracker.gg]({url}) with your Riot account to view your stats.", color = 0x714ec4)
                            temp.set_author(name = "VALORANT PROFILE", icon_url= self.client.user.avatar_url)
                            await link_msg.edit(embed = temp)
                    else:
                        temp = discord.Embed(title = user.name,description = "This account is not linked with any `valorant` account.", color = 0x714ec4)
                        temp.set_author(name = "VALORANT PROFILE", icon_url= self.client.user.avatar_url)
                        await link_msg.edit(embed = temp)

def setup(client):
    client.add_cog(GAMES(client))