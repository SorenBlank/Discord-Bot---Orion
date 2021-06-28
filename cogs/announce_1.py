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

fc_cur = base["fc"]
tc_cur = base["tc"]
bc_cur = base["bc"]
tic_cur = base["tic"]
ta_cur = base["ta"]

class AN_1(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print("AN1 is Loaded ----")

    @commands.command()
    async def announce(self,ctx, channel:discord.TextChannel, time = None):
        if ctx.author.guild_permissions.manage_guild or ctx.author.guild_permissions.administration:
            raw = ta_cur.find({})
            y = [x["guild"] for x in raw]

            au = ctx.author.id
            ch = ctx.channel.id

            avi = self.client.user.avatar_url_as(static_format='png')

            permission = dict(ctx.me.permissions_in(channel))
            permission2 = dict(ctx.channel.permissions_for(ctx.me))
            permission_channel = permission["send_messages"]
            permission_current = permission2["manage_messages"]

            if permission_channel and permission_current:
                embed = discord.Embed(color = 0x5865F2, description = "Recording your text. Type down the announcement below -")
                main_embed = await ctx.send(embed = embed)
                text = await self.client.wait_for("message")

                while not (text.author.id == au and text.channel.id == ch):
                    text = await self.client.wait_for("message")
                    pass

                lower = text.content.lower()
                matches = ["eliminate","terminate","stop"]
                if lower not in matches:
                    if text.author.id == au and text.channel.id ==ch:
                        if time == None:
                            att=[]
                            names = ""
                            sort = 1
                            if text.attachments != []:
                                if text.content != None:
                                    for a in text.attachments:
                                        att.append(await a.to_file())
                                        names += f"{sort}|" +  f"{a.url}"
                                        sort += 1
                                        
                                    await channel.send(text.content, file=att[0])
                                    if len(att) > 0:
                                        att.pop(0)
                                        for i in att:
                                            await channel.send(file = i)

                                    await text.delete()
                                    embed = discord.Embed(color = 0x5865F2, description = f"**__CONTENT__:** ```\n{text.content}```")
                                    embed.set_author(name = "ANNOUNCEMENT LOG",icon_url = avi)
                                    embed.add_field(name = "____ATTACHMENTS____", value = f"```\n{names}```",inline=False)
                                    embed.add_field(name="__AUTHOR__", value = f"Mention: {ctx.author.mention}\nID: `{ctx.author.id}`",)
                                    embed.add_field(name = "__CHANNEL__", value = f"Mention: {channel.mention}\nID: `{channel.id}`")
                                    await main_embed.edit(embed = embed)

                                if text.content == None:
                                    for a in text.attachments:
                                        att.append(await a.to_file())
                                        names += f"{sort}|" +  f"{a.url}"
                                        sort += 1

                                    for at in att:
                                        await channel.send(file=at)
                                    await text.delete()
                                    embed = discord.Embed(color = 0x5865F2, description = f"**__ATTACHMENTS__:**\n```\n{names}```")
                                    embed.set_author(name = "ANNOUNCEMENT LOG",icon_url = avi)
                                    # embed.add_field(name = "__ATTACHMENTS__", value = f"{names}")
                                    embed.add_field(name="__AUTHOR__", value = f"Mention: {ctx.author.mention}\nID: `{ctx.author.id}`",)
                                    embed.add_field(name = "__CHANNEL__", value = f"Mention: {channel.mention}\nID: `{channel.id}`")
                                    await main_embed.edit(embed = embed)
                            else:
                                await channel.send(text.content)
                                await text.delete()
                                embed = discord.Embed(color = 0x5865F2, description = f"**__CONTENT__:** ```\n{text.content}```")
                                embed.set_author(name = "ANNOUNCEMENT LOG",icon_url = avi)

                                embed.add_field(name="__AUTHOR__", value = f"Mention: {ctx.author.mention}\nID: `{ctx.author.id}`",)
                                embed.add_field(name = "__CHANNEL__", value = f"Mention: {channel.mention}\nID: `{channel.id}`")
                                # embed.add_field(name= "__CONTENT__", value = f"```\n{text.content}```",inline=False)
                                await main_embed.edit(embed = embed)

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

                if lower in matches:
                    await ctx.send("Command Dismissed")
                    return

                if channel == None:
                    embed = discord.Embed(color = 0x5865F2, description = "Please provide required arguments.")
                    embed.set_author(name = "Argument EROOR",icon_url = self.client.user.avatar_url)
                    await ctx.send(embed = embed)
            else:
                embed = discord.Embed(color = 0x5865F2, description = f"For this command, bot requires `send_message` and `manage_messages` permission in order to execute.")
                embed.set_author(name = "Permission EROOR", icon_url = self.client.user.avatar_url)
                await ctx.send(embed = embed)
        else:
            embed = discord.Embed(color = 0x5865F2, description = f"This command requires `manage_guild` permission in order to execute.")
            embed.set_author(name = "Access Denied", icon_url = self.client.user.avatar_url)
            await ctx.send(embed = embed)

    @commands.command()
    async def edit(self,ctx,id:discord.Message=None):
        au = ctx.author.id
        ch = ctx.channel.id
        if id.author == self.client.user.id:
            avi = self.client.user.avatar_url_as(static_format='png')
            if ctx.author.guild_permissions.manage_guild or ctx.author.guild_permissions.administration:
                permission = dict(ctx.me.permissions_in(id.channel))
                permission2 = dict(ctx.channel.permissions_for(ctx.me))
                permission_channel = permission["send_messages"]
                permission_current = permission2["manage_messages"]
                if permission_channel and permission_current:
                    embed = discord.Embed(color = 0x5865F2, description = "Recording your text. Type down the edited message below -")
                    main_embed = await ctx.send(embed = embed)
                    text = await self.client.wait_for("message")

                    while not (text.author.id == au and text.channel.id == ch):
                        text = await self.client.wait_for("message")
                        pass

                    lower = text.content.lower()
                    matches = ["eliminate","terminate","stop"]
                    if lower not in matches:
                        if text.author.id == au and text.channel.id ==ch:
                            await id.edit(content = text.content)
        
                            await text.delete()
                            embed = discord.Embed(color = 0x5865F2, description = f"**__CONTENT__:** ```\n{text.content}```")
                            embed.set_author(name = "EDIT LOG",icon_url = avi)
                            embed.add_field(name="__AUTHOR__", value = f"Mention: {ctx.author.mention}\nID: `{ctx.author.id}`",)
                            embed.add_field(name = "__CHANNEL__", value = f"Mention: {id.channel.mention}\nID: `{id.id}`")
                            await main_embed.edit(embed = embed)
                    if lower in matches:
                        await ctx.send("Command Dismissed")
                
                else:
                    embed = discord.Embed(color = 0x5865F2, description = f"For this command, bot requires `send_message` and `manage_messages` permission in order to execute.")
                    embed.set_author(name = "Permission EROOR", icon_url = self.client.user.avatar_url)
                    await ctx.send(embed = embed)

            else:
                embed = discord.Embed(color = 0x5865F2, description = f"This command requires `manage_guild` permission in order to execute.")
                embed.set_author(name = "Access Denied", icon_url = self.client.user.avatar_url)
                await ctx.send(embed = embed)
        else:
            embed = discord.Embed(color = 0x5865F2, description = f"Can not edit a message authored by another user.")
            embed.set_author(name = "Permission EROOR", icon_url = self.client.user.avatar_url)
            await ctx.send(embed = embed)
    
    
def setup(client):
    client.add_cog(AN_1(client))