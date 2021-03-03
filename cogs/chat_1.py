from discord.ext import commands
import datetime
import random
import sqlite3
import asyncio
import psycopg2
import os

base = psycopg2.connect(user="yyflmbmssbqvcl",
                        password="f3f1c4a58fedf11450c7cf60d7a0e9d5564600cac78d867a3db59688f0bf88b6",
                        host="ec2-3-224-251-47.compute-1.amazonaws.com",
                        port="5432",
                        database="dda86padcqcfo8"
                        )
cur = base.cursor()

class C1_1(commands.Cog):
    def __init__(self, client):
        self.client = client
    @commands.Cog.listener()
    async def on_ready(self):
        print("C1_1 is Loaded ----")
        while True:
            await asyncio.sleep(4)
            cur.execute("SELECT*FROM C1channels")
            loop_channels = cur.fetchall()
            if len(loop_channels) != 0:
                for i in loop_channels:
                    channel_id = i[1]
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
                        
                        cur.execute("UPDATE C1channels SET Timegap = ? WHERE Channel = ?",(timegap,channel_id))
                        cur.execute("UPDATE C1channels SET Createtime = ? WHERE Channel = ?",(createtime,channel_id))
                        
                        print(channel.name, i[3])
                        print()
                        base.commit()
                    except:
                        cur.execute("DELETE FROM C1channels WHERE Channel = ?",(channel_id,))
                        base.commit()


def setup(client):
    client.add_cog(C1_1(client))