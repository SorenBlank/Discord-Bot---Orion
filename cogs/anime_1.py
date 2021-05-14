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
import requests
import json
import re


class ANIME(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print("ANIME is Loaded ----")

    @commands.command()
    async def anime(self,ctx,*,name):
        url = f"https://api.jikan.moe/v3/search/anime?q={name}"
        req = requests.get(url)
        big_data = req.json()
        result_list = big_data["results"]
        result = result_list[0]
        id = result["mal_id"]
        all_data = requests.get(f"https://api.jikan.moe/v3/anime/{id}").json()
        title = all_data['title']
        url = all_data['url']
        des = all_data['synopsis']

        x = des.split(" ")
        d = des.split(".")
        if x[0] == "Final":
            des = d[0] + "."

        anime_em = discord.Embed(title = title,url = url, description = des,color = 0x5865F2)
        
        anime_em.set_thumbnail(url = all_data['image_url'])

        if all_data['type'] != "Movie":
            air_from = all_data['aired']['from'][:10]
            air_to = all_data['aired']['to'][:10] if all_data['aired']['to'] != None else "unknown"
            anime_em.add_field(name = ":calendar_spiral: AIRED",
                value = f"**FROM:** `{air_from}`\n**TO:** `{air_to}`",
                inline = True)
        else:
            air_from = all_data['aired']['from'][:10]
            anime_em.add_field(name = ":calendar_spiral: AIRED",
                value = f"**Released:** `{air_from}`")

        status = "Completed" if all_data['airing'] == False else "Airing"
        anime_em.add_field(name = ":page_facing_up: STATUS",
            value = f"{status}")

        anime_em.add_field(name = ":bookmark_tabs: TYPE",
            value = all_data['type'])

        if all_data['episodes'] != None:
            anime_em.add_field(name = ":cd: EPISODES",
            value = f"{all_data['episodes']} eps")
        else:
            anime_em.add_field(name = ":cd: EPISODES",
            value = "0 eps")

        anime_em.add_field(name = ":stopwatch: DURATION",
            value = f"{all_data['duration']}")

        anime_em.add_field(name = ":bar_chart: SCORE",
            value = f"**{all_data['score']} / 10 **")
        n = []
        for i in all_data["genres"]:
            n.append(i["name"])

        n = ", ".join(n)

        anime_em.add_field(name = ":scroll: GENRES",
            value = n,
            inline = False)

        await ctx.send(embed = anime_em)
    
    @commands.command()
    async def manga(self,ctx,*,name):
        url = f"https://api.jikan.moe/v3/search/manga?q={name}"
        req = requests.get(url)
        big_data = req.json()
        result_list = big_data["results"]
        result = result_list[0]
        id = result["mal_id"]
        all_data = requests.get(f"https://api.jikan.moe/v3/manga/{id}").json()
        title = all_data['title']
        url = all_data['url']
        des = all_data['synopsis']

        x = des.split(" ")
        d = des.split(".")
        if x[0] == "Final":
            des = d[0] + "."

        manga_em = discord.Embed(color = 0x5865F2,title = title,url = url, description = des)
        
        manga_em.set_thumbnail(url = all_data['image_url'])

        air_from = all_data['published']['from'][:10]
        air_to = all_data['published']['to'][:10] if all_data['published']['to'] != None else "unknown"
        manga_em.add_field(name = ":calendar_spiral: PUBLISHED",
            value = f"**FROM:** `{air_from}`\n**TO:** `{air_to}`",
            inline = True)
        

        manga_em.add_field(name = ":page_facing_up: STATUS",
            value = all_data["status"])

        manga_em.add_field(name = ":bookmark_tabs: TYPE",
            value = all_data['type'])

        manga_em.add_field(name = ":book: LENGTH",
        value = f"**chapters:** {all_data['chapters']}\n**volumes:** {all_data['volumes']}")

        manga_em.add_field(name = ":chart_with_upwards_trend: RANK",
            value = f"TOP {all_data['rank']}")
        manga_em.add_field(name = ":bar_chart: SCORE",
            value = f"**{all_data['score']} / 10 **")
        n = []
        for i in all_data["genres"]:
            n.append(i["name"])

        n = ", ".join(n)

        manga_em.add_field(name = ":scroll: GENRES",
            value = n,
            inline = False)

        await ctx.send(embed = manga_em)


def setup(client):
    client.add_cog(ANIME(client))