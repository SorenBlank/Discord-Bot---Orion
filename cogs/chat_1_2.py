from discord.ext import commands
import datetime
import random
import sqlite3
import asyncio
import random

base = psycopg2.connect(user="yyflmbmssbqvcl",
                        password="f3f1c4a58fedf11450c7cf60d7a0e9d5564600cac78d867a3db59688f0bf88b6",
                        host="ec2-3-224-251-47.compute-1.amazonaws.com",
                        port="5432",
                        database="dda86padcqcfo8"
                        )
cur = base.cursor()

class C1_2(commands.Cog):
    def __init__(self, client):
        self.client = client
    @commands.Cog.listener()
    async def on_ready(self):
        print("C1_2 is Loaded ----")
        while True:
            await asyncio.sleep(15.6)
            cur.execute("SELECT*FROM C1channels")
            send_channels = cur.fetchall()
            if len(send_channels) != 0:
                for i in send_channels:
                    channel_id = i[1]
                    channel_gap = i[3]
                    try:
                        channel = self.client.get_channel(channel_id)
                        msg = await channel.history(limit=10).flatten()
                        last_msg = msg[0]

                        if (channel_gap >= 1800) and (channel_gap <= 1850):
                            
                            x = 0
                            for i in msg:
                                if i != 777095257262522399:
                                    x = i
                                    break
                            
                            if last_msg.author.id == 777095257262522399:

                                await channel.send(random.choice(["Hello. Anybody?",
                                                                  "Anyone? '-'",
                                                                  "Anybody up?",
                                                                  "Hello! '-'"]))

                        if (channel_gap >= 3600) and (channel_gap <= 3650):
                            if last_msg.author.id == 777095257262522399:
                                await channel.send(random.choice(["Cool. Still nobody is online. Cool. Keep it up guys.",
                                                                  "How could still nobody is talking!"]))
                    except:
                        cur.execute("DELETE FROM C1channels WHERE Channel = ?",(channel_id,))
                        base.commit()
                         
def setup(client):
    client.add_cog(C1_2(client))