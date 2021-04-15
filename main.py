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
from discord import ActivityType as AT
import urllib
import requests
import pymongo
from pymongo import MongoClient
from youtube_search import YoutubeSearch

cluster = MongoClient("mongodb+srv://soren:cdD2_qWUYRk-d4G@orion.iztml.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
base = cluster["OrionDB"]

fc_cur = base["fc"] #Formation = [_id, Guild, Channel, Past_Number, Last_Number, Author]
tc_cur = base["tc"] #Formation = [_id, Guild, Channel]
bc_cur = base["bc"] #Formation = [_id, Guild, Channel]
ta_cur = base["ta"] #Formation = [_id, Guild, Channel, time, announcement]
weclome_cur = base["welcome"] #Formation = [_id, Guild, Channel, Message]
bye_cur = base["bye"] #Formation = [_id, Guild, Channel, Message]

#set up of command prefix
client = commands.Bot(command_prefix = [".o ",".O "], case_insensitive=True, intents = Intents.all())
client.remove_command("help")

au = 0

#Bot's status
@client.event
async def on_ready():
    await client.change_presence(status=discord.Status.online, 
                                 activity = discord.Activity(type = discord.ActivityType.watching, 
                                                             name = '.o help')
                                   )
    print("Bot is ready!")


#connecting cogs
client.load_extension('cogs.help_1')
client.load_extension('cogs.activate_1')
client.load_extension('cogs.deactivate_1')
client.load_extension('cogs.mod_1')
client.load_extension('cogs.announce_1')
client.load_extension('cogs.announce_timer_check_1')
client.load_extension('cogs.philosophy_1')
client.load_extension('cogs.tic_1')
client.load_extension('cogs.bs_1')
client.load_extension('cogs.fibo_1')
client.load_extension('cogs.show_1')
client.load_extension('cogs.utility_1')
client.load_extension('cogs.chess_all')
client.load_extension('cogs.anime_1')
client.load_extension('cogs.google_1')
client.load_extension('cogs.countup_1')


@client.event
async def on_guild_remove(guild):

    #FC Removal
    fc_cur.delete_many({"guild":guild.id})

    #TC Removal
    tc_cur.delete_many({"guild":guild.id})

    #BC Removal
    bc_cur.delete_many({"guild":guild.id})

    #Timer Announce Removal
    ta_cur.delete_many({"guild":guild.id})

    #WELCOME Removal
    weclome_cur.delete_many({"guild":guild.id})

    #BYE Removal
    bye_cur.delete_many({"guild":guild.id})


@client.event
async def on_member_join(member):
    raw = weclome_cur.find({})
    guilds = []
    try:
        x = [i for i in raw]
        guilds = [x[i]["guild"] for i in range(len(x))]
    except:
        pass

    if member.guild.id in guilds:
        raw = weclome_cur.find_one({"guild":member.guild.id})
        channel = raw["channel"]
        channel = client.get_channel(channel)
        msg = raw["message"]
        testmsg = msg.replace("#member",member.mention)
        await channel.send(testmsg)

@client.event
async def on_member_remove(member):
    raw = bye_cur.find({})
    guilds = []
    try:
        x = [i for i in raw]
        guilds = [x[i]["guild"] for i in range(len(x))]
    except:
        pass

    if member.guild.id in guilds:
        raw = bye_cur.find_one({"guild":member.guild.id})

        channel = raw["channel"]
        channel = client.get_channel(channel)
        msg = raw["message"]
        testmsg = msg.replace("#member",member.mention)
        await channel.send(testmsg)

#sends you the latency
@client.command(aliases = ["ping","latency"])
async def lat(ctx):
    await ctx.send(f"Pong!{round(client.latency * 1000)} ms")

#8ball command
@client.command(aliases = ["ask", "8ball"])
async def _8ball(ctx, *, que):
    responses = ["It is certain.",
                "It is decidedly so.",
                "Without a doubt.",
                "Yes - definitely.",
                "You may rely on it.",
                "As I see it, yes.",
                "Most likely.",
                "Outlook good.",
                "Yes.",
                "Signs point to yes.",
                "Reply hazy, try again.",
                "Ask again later.",
                "Better not tell you now.",
                "Cannot predict now.",
                "Concentrate and ask again.",
                "Don't count on it.",
                "My reply is no.",
                "My sources say no.",
                "Outlook not so good.",
                "Very doubtful."]

    special_responses = ["Yes", "Definitely Yes"]
    if que == 'Do I love my Teddy?':
        await ctx.send(random.choice(special_responses))
    else:
        await ctx.send(random.choice(responses))


@client.command()
async def wanted(ctx, member : discord.Member = None):
    if member == None:
        member = ctx.author
    pic = Image.open("wanted.jpg")
    asset = member.avatar_url_as(size = 128)
    read = BytesIO(await asset.read())
    pfp = Image.open(read)
    pfp = pfp.resize((296,297))
    pic.paste(pfp,(86,222))
    pic.save("profile.jpg")
    await ctx.send(file = discord.File("profile.jpg"))

@client.command()
async def invite(ctx):
    embed = discord.Embed()
    embed.set_author(name = "INVITE",icon_url= client.user.avatar_url)
    embed.add_field(name="BOT INVITATION LINK",
                    value="[Click here](https://discord.com/api/oauth2/authorize?client_id=777095257262522399&permissions=8&scope=bot) to invite me in your server.\n឵឵",
                    inline = False)
    embed.add_field(name="SERVER INVITATION LINK",
                    value = ":small_blue_diamond: [Click here](https://discord.gg/JJtUtgMjBv) to join my creator's server.",
                    inline = False)
    embed.set_footer(icon_url=ctx.author.avatar_url,text=f"Thank you very much {ctx.author.name}")
    if isinstance(ctx.channel, discord.DMChannel):
        await ctx.author.send(embed = embed)
    else:
        await ctx.send(f"{ctx.author.mention} Please check your DM.")
        await ctx.author.send(embed = embed)

@client.command()
async def youtube(ctx, *, search):
    # query_string = urllib.parse.urlencode({'search_query': search})
    # html_content = urllib.request.urlopen('http://www.youtube.com/results?' + query_string)
    # search_content= html_content.read().decode()
    # search_results = re.findall(r'\/watch\?v=\w+', search_content)
    # link_msg = await ctx.send('https://www.youtube.com' + search_results[0])

    results = YoutubeSearch(search, max_results=15).to_json()
    results = json.loads(results)
    search_results = []
    number = len(results['videos'])
    for i in range(number):
        x = results['videos'][i]['url_suffix']
        search_results.append(x)

    link_msg = await ctx.send('https://www.youtube.com' + search_results[0])
    def react_check(reaction, user): #reaction check function
        emojis = ["🚫","➡️","⬅️"]
        return user.id == ctx.author.id and reaction.message.id == link_msg.id and str(reaction.emoji) in emojis
    
    page = 0
    pages = len(search_results)
    
    clean_emoji = True

    while True: # looping between pages
        if page == 0:
            if not clean_emoji:
                for i in emojis:
                    await link_msg.clear_reaction(i) # remove emoji if exists

            emojis = ["🚫","➡️"]
            for emoji in emojis:
                await link_msg.add_reaction(emoji) # add emoji to link_msg
        
            clean_emoji = True
            
        elif page == pages-1:
            if not clean_emoji:
                for i in emojis:
                    await link_msg.clear_reaction(i) # remove emoji if exists

            emojis = ["⬅️","🚫"]
            for emoji in emojis:
                await link_msg.add_reaction(emoji)
            
            clean_emoji = True
        else:
            if clean_emoji:
                for i in emojis:
                    await link_msg.clear_reaction(i) # remove emoji if exists

            emojis = ["⬅️","➡️"]
            for emoji in emojis:
                await link_msg.add_reaction(emoji)
        
            clean_emoji = False
        
        try: # to handle timeout error
            user_react,user = await client.wait_for("reaction_add", check = react_check, timeout=60)
            
            
            if user_react.emoji == "➡️" and page != pages-1:
                page += 1
                await link_msg.edit(content = 'https://www.youtube.com' + search_results[page])
                await link_msg.remove_reaction(user_react, user)
            
            if user_react.emoji == "⬅️" and page > 0:
                page -= 1
                await link_msg.edit(content = 'https://www.youtube.com' + search_results[page])
                await link_msg.remove_reaction(user_react, user)
            
            if user_react.emoji == "🚫":
                if react_check(user_react,user):
                    await link_msg.clear_reactions()
                    break

        except asyncio.TimeoutError:
            try:
                for emoji in link_msg.reactions:
                    await link_msg.clear_reaction(emoji)
                break
            except:
                pass

#######################################################################################################
                                    #ALL MESSAGE RELATED ACTIVITIES#
#######################################################################################################

@client.event
async def on_message(message):
    await client.process_commands(message)

    #making the message.content lower case in order to make the commands case insensitive
    ex_1 = message.content.lower().replace(',','')
    ex_2 = ex_1.replace("?","")
    exact_txt = ex_2 

    #splitting the exact_txt
    exact_txt_splitted = exact_txt.split(" ")
    exact_txt_spl = message.content.split(" ")

    if exact_txt == "i am sad":
            await message.channel.send(f"{message.author.mention} why? :pleading_face:")

    if isinstance(message.channel, discord.DMChannel):
        msg = message.content
        if message.author.id != 777095257262522399:
            print(f"{msg}  -- {message.author}")

    if message.author.id == 693375549686415381:
        
        if exact_txt_splitted[0] == "send_ch" and exact_txt_splitted[1].isdigit():
            ch = int(exact_txt_splitted[1])
            ch_o = client.get_channel(ch)
            await ch_o.send(" ".join(exact_txt_spl[2:]))

        if exact_txt_splitted[0] == "send_au" and exact_txt_splitted[1].isdigit():
            au = int(exact_txt_splitted[1])
            au_o = client.get_user(au)
            await au_o.send(" ".join(exact_txt_spl[2:]))


#######################################################################################################
#######################################################################################################

import nest_asyncio
nest_asyncio.apply()
#with open('token.txt','r') as f:
    #content = f.read()

#Token
#client.run(os.environ['TOKEN'])
#client.run("TOKEN")
client.run(str(os.environ.get('TOKEN')))
#client.run("ODE1OTA4MDk3Mjg4OTYyMDk5.YDzPoQ.t3z2n6e4ggEPYNlHUn1sKZLn0aQ")