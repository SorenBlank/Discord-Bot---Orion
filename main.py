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


#database loads
base = sqlite3.connect("all.db")
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
                                                             name = '.o')
                                   )
    print("Bot is ready!")

#connecting cogs
client.load_extension('cogs.help_1')
client.load_extension('cogs.activate_1')
client.load_extension('cogs.deactivate_1')
client.load_extension('cogs.mod_1_protocol')
client.load_extension('cogs.chat_1_protocol')
client.load_extension('cogs.chat_1_2_protocol')
client.load_extension('cogs.announce_1')
client.load_extension('cogs.announce_timer_check_1')
client.load_extension('cogs.wiki_1_protocol')
client.load_extension('cogs.tic_1_protocol')
client.load_extension('cogs.bs_1_protocol')
client.load_extension('cogs.fibo_1_protocol')
client.load_extension('cogs.show_1')
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
async def userinfo(ctx, *, name=""):
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

    
    avi = user.avatar_url_as(static_format='png')
    if isinstance(user, discord.Member):
        roles = roles = [role for role in user.roles]
        for role in roles:
            if role.name=="@everyone":
                roles.remove(role)
                break
    
    em = discord.Embed(timestamp=ctx.message.created_at, title='= = = = = |:notepad_spiral: User Info :notepad_spiral:| = = = = =',description = "-----------------------------------------------")
    em.add_field(name="User Name:",value=user.name, inline=True)
    em.add_field(name="Discriminator:",value=user.discriminator, inline=True)
    
    if user.nick==None:
        nn=user.name
    else:
        nn=user.nick
    em.add_field(name='Nickname', value=nn, inline=True)
    dic={"online":"<:online:814161343426199622> ","dnd":"<:dnd:814161369892257842> ","offline":":black_circle: ","idle":"<:idle:814161403271184426> "}
    dic1={"online":"Online","dnd":"Do Not Disturb","offline":"Offline","idle":"Idle"}
    em.add_field(name='Presence', value=dic[str(user.status)] + dic1[str(user.status)], inline=True)
    
    st="None"
    activ=""
    listen,stream,playy,watch="","","",""
    ACT=[]
    vits=list(user.activities)
    for act in vits:
        if act.type==AT.custom:
            st=act
        elif act.type==AT.listening:
            listen=act
        elif act.type==AT.streaming:
            stream=act
        elif act.type==AT.playing:
            playy=act
        elif act.type==AT.watching:
            watch=act

    em.add_field(name='Status', value=st, inline=True)
    print(vits)
    for act in vits:
        print(act.type)
    if listen != "" and hasattr(listen,"title") and hasattr(listen,"artists"):
        ACT.append(f'<:spotify:814185511655964682> Listening to *{listen.title}*  by **{", ".join(listen.artists)}**') 
    if playy != "":
        ACT.append(f"Playing {playy.name}")
    if watch != "":
        ACT.append(f"Watching {watch.name}")
    if stream != "":
        ACT.append(f"Streaming {stream.name}")
    if ACT != []:
        activ=". \n".join(ACT)



    em.add_field(name='Activity', value=activ if activ!="" else "None", inline=False)
    devices=[]
    if str(user.desktop_status)!='offline':
        devices.append(":desktop: Desktop Client")
    if str(user.web_status)!='offline':
        devices.append(":spider_web: Web")
    if str(user.mobile_status)!='offline':
        devices.append(":mobile_phone: Mobile App")

    if len(devices)>0:
        em.add_field(name='Active on', value=", \n".join(devices), inline=True)

    elif len(devices)==0:
        em.add_field(name='Active on', value="None", inline=True)

    if len(roles)>0:
        em.add_field(name=f"Roles ({len(roles)})", 
                    value=" ,\n ".join([role.name for role in roles]), inline=True)
    elif len(roles)==0:
        em.add_field(name=f"Roles ({len(roles)})", 
                    value="No Roles", inline=True)

    form='*Date:* %A, %d %B %Y \n*Time:* %H:%M:%S'
    em.add_field(name='Account Created', 
                value=user.created_at.__format__(form),inline=True)
    em.add_field(name='Joined Server', 
                value=user.joined_at.__format__(form),inline=True)
    nitro=user.premium_since
    em.add_field(name='Boosted this server', 
                value='Hasn\'t boosted yet.' if nitro==None else nitro.__format__(form),inline=False)
    em.set_thumbnail(url=avi)
    av=ctx.author.avatar_url_as(static_format='png')
    em.set_author(name= "User Information", icon_url= client.user.avatar_url)
    em.set_footer(text=f"Requested by: {ctx.author}", icon_url=av)
    await ctx.send(embed=em)


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
    print(message.content)

#######################################################################################################
#######################################################################################################

#Token
client.run('Nzc3MDk1MjU3MjYyNTIyMzk5.X6-cWw.qo-kflaFk7S7eMvDM7EiD97Bzj8')