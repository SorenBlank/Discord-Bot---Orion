from discord.ext import commands
import datetime
import random
import sqlite3
import asyncio
import random
import pymongo
from pymongo import MongoClient

cluster = MongoClient("mongodb+srv://soren:cdD2_qWUYRk-d4G@orion.iztml.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
base = cluster["OrionDB"]

c1_cur = base["c1channels"]


class C1_2(commands.Cog):
    def __init__(self, client):
        self.client = client
    @commands.Cog.listener()
    async def on_ready(self):
        print("C1_2 is Loaded ----")
        while True:
            await asyncio.sleep(15.6)
            raw = c1_cur.find({})
            send_channels = [i for i in raw]
            if len(send_channels) != 0:
                for i in range(len(send_channels)):
                    channel_id = send_channels[i]["channel"]
                    channel_gap = send_channels[i]["timegap"]
                    #try:
                    channel = self.client.get_channel(channel_id)
                    msg = await channel.history(limit=10).flatten()
                    last_msg = msg[0]

                    if (channel_gap >= 1800) and (channel_gap <= 1850):
                        
                        if last_msg.author.id != 777095257262522399:

                            await channel.send(random.choice(["Hello. Anybody?",
                                                              "Anyone? '-'",
                                                              "Anybody up?",
                                                              "Hello! '-'"]))

                    if (channel_gap >= 3600) and (channel_gap <= 3650):
                        if last_msg.author.id == 777095257262522399:
                            await channel.send(random.choice(["Cool. Still nobody is online. Cool. Keep it up guys.",
                                                              "How could still nobody is talking!"]))
                    #except:
                        #c1_cur.delete_one({"_id":send_channels[i]["_id"]})

def setup(client):
    client.add_cog(C1_2(client))