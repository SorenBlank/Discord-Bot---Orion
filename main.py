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
from discord import ActivityType as AT
import psycopg2

#database loads
base = psycopg2.connect(os.environ['DATABASE_URL'])
cur = base.cursor()

cur.execute("CREATE TABLE IF NOT EXISTS M1guilds (Guild INTEGER)")
cur.execute("CREATE TABLE IF NOT EXISTS C1channels (Guild INTEGER,Channel INTEGER, Createtime TEXT, Timegap INTEGER)")
cur.execute("CREATE TABLE IF NOT EXISTS Announce_ch (Guild INTEGER, Channel INTEGER)")
cur.execute("CREATE TABLE IF NOT EXISTS ANC (Guild INTEGER, Channel INTEGER)")
cur.execute("CREATE TABLE IF NOT EXISTS FC (Guild INTEGER, Channel INTEGER, Past_Number INTEGER, Last_Number INTEGER, Author INTEGER)")
cur.execute("CREATE TABLE IF NOT EXISTS TC (Guild INTEGER, Channel INTEGER)")
cur.execute("CREATE TABLE IF NOT EXISTS BC (Guild INTEGER, Channel INTEGER)")
cur.execute("CREATE TABLE IF NOT EXISTS Tic (User INTEGER, Wins INTEGER, Loses INTEGER, Draws INTEGER)")
cur.execute("CREATE TABLE IF NOT EXISTS TimerAnnounce (Guild INTEGER,Channel INTEGER, TimeLeft INTEGER, Announcement TEXT)")
cur.execute("CREATE TABLE IF NOT EXISTS WC (Guild INTEGER, Channel INTEGER)")


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
    async for guild in client.fetch_guilds(limit=150):
        print(guild.name)

#connecting cogs
client.load_extension('cogs.help_1')
client.load_extension('cogs.activate_1')
client.load_extension('cogs.deactivate_1')
client.load_extension('cogs.mod_1')
client.load_extension('cogs.chat_1')
client.load_extension('cogs.chat_1_2')
client.load_extension('cogs.announce_1')
client.load_extension('cogs.announce_timer_check_1')
client.load_extension('cogs.philosophy_1')
client.load_extension('cogs.tic_1')
client.load_extension('cogs.bs_1')
client.load_extension('cogs.fibo_1')
client.load_extension('cogs.show_1')
client.load_extension('cogs.utility_1')

#Texts you in the terminal if somebody enters
@client.event
async def on_member_join(member):
    print(f"{member} has joined to our server")


@client.event
async def on_guild_remove(guild):
    #m1_removal
    cur.execute("SELECT*FROM M1guilds")
    m1_guilds = cur.fetchall()
    m_g = []
    for i in m1_guilds:
        m_g.append(i[0])

    if guild.id in m_g:
        cur.execute("DELETE FROM M1guilds WHERE Guild = ?",(guild.id,))
        base.commit()

    #c1removal
    cur.execute("SELECT*FROM C1channels")
    c1_guilds = cur.fetchall()
    c1_g = []
    for i in c1_guilds:
        c1_g.append(i[0])
    if guild.id in c1_g:
        cur.execute("DELETE FROM C1channels WHERE Guild = ?",(guild.id,))
        base.commit()
    
    #Announce_chremoval
    cur.execute("SELECT*FROM Announce_ch")
    an_guilds = cur.fetchall()
    an_g = []
    for i in an_guilds:
        an_g.append(i[0])
    if guild.id in an_g:
        cur.execute("DELETE FROM Announce_ch WHERE Guild = ?",(guild.id,))
        base.commit()

    #ANCremoval
    cur.execute("SELECT*FROM ANC")
    anc_guids = cur.fetchall()
    anc_g = []
    for i in anc_guids:
        anc_g.append(i[0])
    if guild.id in anc_g:
        cur.execute("DELETE FROM ANC WHERE Guild = ?",(guild.id,))
        base.commit()

    #FC Removal
    cur.execute("SELECT*FROM FC")
    fc_guilds = cur.fetchall()
    fc_g = []
    for i in fc_guilds:
        fc_g.append(i[0])
    if guild.id in fc_g:
        cur.execute("DELETE FROM FC WHERE Guild = ?",(guild.id,))
        base.commit()

    #TC Removal
    cur.execute("SELECT*FROM TC")
    tc_guilds = cur.fetchall()
    tc_g = []
    for i in tc_guilds:
        tc_g.append(i[0])
    if guild.id in tc_g:
        cur.execute("DELETE FROM TC WHERE Guild = ?",(guild.id,))
        base.commit()

    #BC Removal
    cur.execute("SELECT*FROM BC")
    bc_guilds = cur.fetchall()
    bc_g = []
    for i in bc_guilds:
        bc_g.append(i[0])
    if guild.id in bc_g:
        cur.execute("DELETE FROM BC WHERE Guild = ?",(guild.id,))
        base.commit()

    #Timer Announce Removal
    cur.execute("SELECT*FROM TimerAnnounce")
    ta_guilds = cur.fetchall()
    ta_g = []
    for i in ta_guilds:
        ta_g.append(i[0])
    if guild.id in ta_g:
        cur.execute("DELETE FROM TimerAnnounce WHERE Guild = ?",(guild.id,))
        base.commit()

    #WC
    cur.execute("SELECT*FROM WC")
    wc_guilds = cur.fetchall()
    wc_g = []
    for i in wc_guilds:
        wc_g.append(i[0])
    if guild.id in wc_g:
        cur.execute("DELETE FROM WC WHERE Guild = ?",(guild.id,))


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

########################################################## ANNOUNCE PART ##########################################################

##################################################################################################################################

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
    embed = discord.Embed(title= "= = = = = = = =| :mailbox_with_mail: Invite :mailbox_with_mail:  |= = = = = = = =")
    embed.add_field(name=":large_blue_diamond: BOT INVITATION LINK",
                    value=":small_blue_diamond: [Click here](https://discord.com/api/oauth2/authorize?client_id=777095257262522399&permissions=8&scope=bot) to invite me in your server.\n឵឵",
                    inline = False)
    embed.add_field(name=":large_blue_diamond: SERVER INVITATION LINK",
                    value = ":small_blue_diamond: [Click here](https://discord.gg/JJtUtgMjBv) to join my creator's server.",
                    inline = False)
    embed.set_footer(icon_url=ctx.author.avatar_url,text=f"Thank you very much {ctx.author.name}")
    if isinstance(ctx.channel, discord.DMChannel):
        await ctx.author.send(embed = embed)
    else:
        await ctx.send(f"{ctx.author.mention} Please check your DM.")
        await ctx.author.send(embed = embed)

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

#with open('token.txt','r') as f:
    #content = f.read()

#Token
client.run(os.environ['TOKEN'])