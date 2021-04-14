                                ###################
                                #importing modules#
                                ###################

#importing discord modules
import discord
from discord import Intents
from discord.ext import commands
from discord.ext import commands, tasks
#importing other modules
from io import BytesIO
import re
import pymongo
from pymongo import MongoClient

cluster = MongoClient("mongodb+srv://soren:cdD2_qWUYRk-d4G@orion.iztml.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
base = cluster["OrionDB"]

c_cur = base["c"] #Formation = [Guild, Channel, Past_Number, Last_Number, Author]

class C_1(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print("C1 is Loaded ----")
    
    @commands.Cog.listener()
    async def on_message(self,message):
        #making the message.content lower case in order to make the commands case insensitive
        
        raw = 0
        id = 0
        try:
            raw = c_cur.find_one({"guild":message.guild.id})
        except:
            pass
        try:
            id = raw["channel"]
        except:
            pass

        #try:     
        if message.channel.id == id:
            ex_1 = message.content.lower().replace(',','')
            ex_2 = ex_1.replace("?","")
            exact_txt = ex_2
            #splitting the exact_txt
            exact_txt_splitted = exact_txt.split(" ")
            r = 0
            try:
                r = eval(exact_txt_splitted[0])
            except:
                pass
            x = str(r)
            if r != 0 and x.isdigit():
                digit = r
                last_digit = raw["last"]
                last_author = raw["author"]
                highest = raw["highest"]
                equal = last_digit + 1
                if last_digit == 0:
                    if digit == 1:
                        if digit > highest:
                            c_cur.update_many({"channel":message.channel.id},{"$set":{"last":digit,"author":message.author.id,"highest":digit}})
                            await message.add_reaction("☑")
                        else:
                            c_cur.update_many({"channel":message.channel.id},{"$set":{"last":digit,"author":message.author.id}})
                            await message.add_reaction("✅")

                elif digit == equal and last_author != message.author.id:
                    if digit > highest:
                        c_cur.update_many({"channel":message.channel.id},{"$set":{"last":equal,"author":message.author.id,"highest":equal}})
                        await message.add_reaction("☑")
                    else:
                        c_cur.update_many({"channel":message.channel.id},{"$set":{"last":equal,"author":message.author.id}})
                        await message.add_reaction("✅")

                elif last_author == message.author.id:
                    await message.add_reaction("❎")
                    c_cur.update_many({"channel":message.channel.id},{"$set":{"last":0,"author":0}})
                    if message.author.id == 736818641907089520:
                        await message.channel.send(f"{message.author.mention} :pleading_face: Solly! You can not count 2 numbers in a row. :pleading_face: We will make it next time. ><")

                    else:
                        await message.channel.send(f"{message.author.mention} RUINED AT {equal}!! $#!%. You can not count 2 numbers in a row.")

                elif digit != equal:
                    c_cur.update_many({"channel":message.channel.id},{"$set":{"last":0,"author":0}})
                    await message.add_reaction("❎")
                    if message.author.id == 736818641907089520:
                        await message.channel.send(f"{message.author.mention} :pleading_face: It should be {equal}. :pleading_face: It's oki we will make it next time.")
                    else:
                        await message.channel.send(f"{message.author.mention} RUINED AT {equal}!! $#!%")
        #except:
            #pass

def setup(client):
    client.add_cog(C_1(client))