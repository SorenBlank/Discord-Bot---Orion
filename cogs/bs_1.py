import discord
from discord.ext import commands
from discord import Intents
import asyncio
import random
import datetime
import math
import wikipedia
import re
from PIL import Image
from io import BytesIO
import os
import numpy as np
from threading import Thread
from multiprocessing import Process
import pymongo
from pymongo import MongoClient

cluster = MongoClient("mongodb+srv://soren:cdD2_qWUYRk-d4G@orion.iztml.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
base = cluster["OrionDB"]

bc_cur = base["bc"]

class Battleship(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print("Battleship is Loaded ----")
    
    @commands.command(aliases = ["bs"])
    async def battleship(self,ctx,member:discord.Member=None):
        raw = bc_cur.find({})
        guilds = []
        channels = []
        try:
            x = [i for i in raw]
            guilds = [x[i]["guild"] for i in range(len(x))]
            channels = [x[i]["channel"] for i in range(len(x))]
        except:
            pass

        if ctx.guild.id in guilds:
            if ctx.channel.id in channels:
                if member==None:
                    await ctx.send("You can\'t play alone bruh.")
                elif member==ctx.author:
                    await ctx.send("Are you serious?")
                elif member.bot:
                    await ctx.send("Come on! Go find a human to play Battleship with.")
                else:
                    await ctx.send(f"{member.mention}, you are being challenged on a game of **Battleship** by {ctx.author.mention}")
                    msg=await ctx.send("If you accept the challenge, respond by clicking on the :thumbsup: reaction. If you wanna decline the challenge click on the :thumbsdown: reaction. Do it, within a minute!")
                    reactions = ["👍", "👎"]
                    for r in reactions:
                        await msg.add_reaction(r)
                    def check(reaction, user):
                        return user == member and str(reaction.emoji) in reactions
                    try:
                        reaction, user = await self.client.wait_for('reaction_add', timeout=60, check=check)
                        if str(reaction.emoji)=="👎":
                            await ctx.send(f"{ctx.author.mention}, {member.mention} declined your challenge.")
                        else:
                            mes=await ctx.send(f"{member.mention} choose your color. react :blue_square: if you wanna play with blue, react :red_square: if you wanna play with red.")
                            col=["🟦","🟥"]
                            for c in col:
                                await mes.add_reaction(c)
                            def chec(reaction,user):
                                return user == member and str(reaction.emoji) in col
                            reac, user = await self.client.wait_for('reaction_add', check=chec)
                            if reac.emoji=="🟦":
                                coldict={member:"blue",ctx.author:"red"}
                                coll={"🟦":member, "🟥":ctx.author}
                                await ctx.send(f"So, {member.mention} is playing with 🟦, and {ctx.author.mention} is playing with 🟥")
                            elif reac.emoji=="🟥":
                                coldict={member:"red",ctx.author:"blue"}
                                coll={"🟦":ctx.author, "🟥":member}
                                await ctx.send(f"So, {member.mention} is playing with 🟥, and {ctx.author.mention} is playing with 🟦")

                            # def col2player(coll):
                            # 	for p,c in coldict.items():
                            # 		if c==coll:
                            # 			return p
                            players=[member,ctx.author]
                            await ctx.send(f"{ctx.author.mention}, {member.mention} check your DMs. Specify your ship position there.")
                            B=np.zeros((10,10))
                            R=np.zeros((10,10))
                            neel=Image.open('./Battleship/bs_blue.png')
                            laal=Image.open('./Battleship/bs_red.png')
                            im={"blue":neel, "red":laal}
                            mat={"blue":B, "red":R}

                            X=np.linspace(39,379,11)
                            Y=np.linspace(108,438,11)
                            X=[int(x) for x in X[:-1]]
                            Y=[int(y) for y in Y[:-1]]

                            letters=[chr(i) for i in range(97,107)]
                            numbers=[str(i) for i in range(1,11)]

                            

                            for player in players:
                                imm=im[coldict[player]]
                                matt=mat[coldict[player]]
                                blank1=Image.open('./Battleship/bs_template_new.png')
                                ch=await player.create_dm()
                                await ch.send(file=discord.File('./Battleship/bs_template_new.png'))
                                ships={'Carrier':5, 'Battleship':4, 'Cruiser':3, 'Submarine':3, 'Destroyer':2}
                                index={'Carrier':1, 'Battleship':2, 'Cruiser':3, 'Submarine':4, 'Destroyer':5}
                                indexinverse={1:'Carrier',2:'Battleship',3:'Cruiser',4:'Submarine',5:'Destroyer',}
                                

                                def chk(author):
                                    def inner_check(message):
                                        B1=len(message.content)==2 or len(message.content)==3
                                        M=message.content.lower()
                                        B2= M[0] in letters
                                        B3= M[1:] in numbers
                                        B4= message.channel == ch
                                        return B1 and B2 and B3 and B4
                                    return inner_check

                                for ship in ships:
                                    
                                    async def getend():
                                        await ch.send("Send me one endpoint of your {} ({} length ship)".format(ship,ships[ship]))
                                        mm=await self.client.wait_for('message', check=chk(player))
                                        M=mm.content.lower()
                                        x1=int(M[1:])-1
                                        y1=ord(M[0])-97
                                        await ch.send("Now send me the other endpoint of your {} ({} length ship)".format(ship,ships[ship]))
                                        mmm=await self.client.wait_for('message', check=chk(player))
                                        MM=mmm.content.lower()
                                        x2=int(MM[1:])-1
                                        y2=ord(MM[0])-97
                                        return x1,y1,x2,y2
                                    x1,y1,x2,y2=await getend()
                                    while x1==x2 and y1==y2:
                                        await ch.send("Two endpoints must be different. Start over.")
                                        x1,y1,x2,y2=await getend()
                                    while matt[x1][y1] !=0 or matt[x2][y2] != 0:
                                        await ch.send("Overlapping not allowed. Start over.")
                                        x1,y1,x2,y2=await getend()
                                    while x1 != x2 and y1 != y2:
                                        await ch.send("Ships must be vertical or horizontal. Start over.")
                                        x1,y1,x2,y2=await getend()
                                    bo1= x1==x2 and abs(y1-y2)!=ships[ship]-1
                                    bo2= y1==y2 and abs(x1-x2)!=ships[ship]-1
                                    if bo1 or bo2:
                                        await ch.send("Wrong ship length. Start over.")
                                        x1,y1,x2,y2=await getend()
                                    def overl(x1,y1,x2,y2):
                                        if x1==x2:
                                            L=max(y1,y2)
                                            l=min(y1,y2)
                                            if np.count_nonzero(matt[x1][l:L+1])>0:
                                                return True
                                            else:
                                                return False
                                        elif y1==y2:
                                            L=max(x1,x2)
                                            l=min(x1,x2)
                                            if np.count_nonzero(np.transpose(matt)[y1][l:L+1])>0:
                                                return True
                                            else:
                                                return False
                                    while overl(x1,y1,x2,y2):
                                        await ch.send("You can\'t overlap on your own ships. Start over.")
                                        x1,y1,x2,y2=await getend()
                                    
                                    if x1==x2:
                                        L=max(y1,y2)
                                        l=min(y1,y2)
                                        for y in np.arange(l,L+1):
                                            blank1.paste(imm, (X[x1],Y[y]))
                                            matt[x1][y]=index[ship]
                                    elif y1==y2:
                                        L=max(x1,x2)
                                        l=min(x1,x2)
                                        for x in np.arange(l,L+1):
                                            blank1.paste(imm, (X[x],Y[y1]))
                                            matt[x][y1]=index[ship]
                                    blank1.save('qwerty.png')
                                    await ch.send(file=discord.File("qwerty.png"))
                                    os.remove('qwerty.png')
                                    

                            #
                            await ctx.send("Alright! I got both your ship positions. Now we\'ll have a toss. Whoever wins, gets to start first.")
                            toss=random.choice(col)
                            await ctx.send(toss)
                            F=coll[toss]
                            await ctx.send(f"{F.mention}, you\'re gonna start first.")
                            col.remove(toss)
                            L=coll[col[0]]
                            move=F
                            noMove=L
                            game_ongoing=True

                            temred=Image.open('./Battleship/bs_template_red.png')
                            temblue=Image.open('./Battleship/bs_template_new.png')
                            hitblu=Image.open('./Battleship/bs_hit.png')
                            missblu=Image.open('./Battleship/bs_miss.png')
                            hitred=Image.open('./Battleship/bs_hit_red.png')
                            missred=Image.open('./Battleship/bs_miss_red.png')
                            
                            temdict={"blue":temblue,"red":temred}
                            hitdict={"blue":hitblu,"red":hitred}
                            misdict={"blue":missblu,"red":missred}

                            await ctx.send("Lemme clear something first. After a player\'s move, I will send a photo here. The photo will contain a :x: at the hit point, and a :heavy_multiplication_x: at the miss point. The grid color of the photo denotes the color of the player who just attempted a shot.")
                            
                            TH={member:6,ctx.author:6}
                            
                            def chck(author):
                                def inner_check(message):
                                    B1=len(message.content)==2 or len(message.content)==3
                                    M=message.content.lower()
                                    B2= M[0] in letters
                                    B3= M[1:] in numbers
                                    B4= message.channel == ctx.channel
                                    B5 = message.author == author
                                    return B1 and B2 and B3 and B4 and B5
                                return inner_check


                            while game_ongoing==True:
                                await ctx.send(f"{move.mention} It's your move now. Send me the point you wanna take a shot at.")
                                ms=await self.client.wait_for('message', check=chck(move))
                                msg=ms.content.lower()
                                x=int(msg[1:])-1
                                y=ord(msg[0])-97

                                matxx=mat[coldict[noMove]]
                                tem=temdict[coldict[move]]
                                hit=hitdict[coldict[move]]
                                miss=misdict[coldict[move]]

                                if matxx[x][y]==0:
                                    tem.paste(miss,(X[x],Y[y]))
                                    tem.save('qwerty.png')
                                    await ctx.send(file=discord.File("qwerty.png"))
                                    os.remove('qwerty.png')
                                    await ctx.send("It\'s a miss. Better luck next time.")
                                    
                                else:
                                    s=matxx[x][y]
                                    matxx[x][y]=0
                                    tem.paste(hit,(X[x],Y[y]))
                                    tem.save('qwerty.png')
                                    await ctx.send(file=discord.File("qwerty.png"))
                                    os.remove('qwerty.png')
                                    await ctx.send("It\'s a **HIT**.")
                                    if len(np.unique(matxx))<TH[move]:
                                        su=indexinverse[s]
                                        await ctx.send("Holy moly! It\'s a **SINK** also. You\'ve sunken your opponent\'s {}".format(su))
                                        TH[move]=len(np.unique(matxx))
                                    if TH[move]==1:
                                        await ctx.send(f"Congratulations! {move.mention}, you\'ve won!")
                                        game_ongoing=False

                                if move==F:
                                    move=L
                                    noMove=F
                                elif move==L:
                                    move=F
                                    noMove=L

                    except asyncio.TimeoutError:
                        await msg.clear_reactions()
                        await ctx.send(f"{member.mention} You took a long time to respond. The challenge is dismissed.")
                        return
            else:
                raw = bc_cur.find_one({"guild":ctx.guild.id})
                ch = raw["channel"]
                ch = self.client.get_channel(ch)
                await ctx.send(f"Please use this {ch.mention} channel.")

        else:
            if ctx.author.guild_permissions.manage_channels:
                await ctx.send("Set a channel first for playing Battleship!")
            else:
                await ctx.send("Ask one of your moderators to set a channel for Battleship.")

def setup(client):
    client.add_cog(Battleship(client))