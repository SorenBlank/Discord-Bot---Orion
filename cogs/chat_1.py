from discord.ext import commands
import datetime
import random
import sqlite3
import asyncio
import os
import pymongo
from pymongo import MongoClient

cluster = MongoClient("mongodb+srv://soren:cdD2_qWUYRk-d4G@orion.iztml.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
base = cluster["OrionDB"]

c1_cur = base["c1channels"]

class C1_1(commands.Cog):
    def __init__(self, client):
        self.client = client
    @commands.Cog.listener()
    async def on_ready(self):
        print("C1_1 is Loaded ----")
        while True:
            await asyncio.sleep(4)
            raw = c1_cur.find({})
            loop_channels = [x for x in raw]
            if len(loop_channels) != 0:
                for i in range(len(loop_channels)):
                    channel_id = loop_channels[i]["channel"]
                    try:  
                        channel = self.client.get_channel(channel_id)
                        msg = await channel.history(limit=2).flatten()
                        gmt6 = datetime.timedelta(hours=6)
                        createtime = msg[0].created_at + gmt6
                        nowtime = datetime.datetime.now()
                        gap = nowtime-createtime
                        timegap = (gap.seconds)
                        if timegap >= 86390 and timegap <=86400:
                            timegap = 0
                        
                        c1_cur.update_one({"_id":loop_channels[i]["_id"]},{"$set":{"timegap":timegap}})
                        c1_cur.update_one({"_id":loop_channels[i]["_id"]},{"$set":{"createtime":createtime}})
                    except:
                        c1_cur.delete_one({"_id":loop_channels[i]["_id"]})


def setup(client):
    client.add_cog(C1_1(client))