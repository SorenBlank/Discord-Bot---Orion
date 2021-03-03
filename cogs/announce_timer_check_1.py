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
import psycopg2

base = sqlite3.connect("all.db")
cur = base.cursor()

class A_T_C_1(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
    	print("Timer Announce is Loaded ----")
    	while True:
    		await asyncio.sleep(1)
    		try:
	    		cur.execute("SELECT*FROM TimerAnnounce")
	    		channels = cur.fetchall()
	    	except:
	    		pass

	    	for i in channels:
	    		if i[2] <= 2:

	    			try:
	    				ch = self.client.get_channel(i[1])
	    				await ch.send(i[3])
	    				cur.execute("DELETE FROM TimerAnnounce WHERE Announcement = ?",(i[3],))
	    				base.commit()

	    			except:
	    				pass

	    		elif i[2] > 2:
	    			time_left = i[2] - 1
	    			cur.execute("UPDATE TimerAnnounce SET TimeLeft = ? WHERE Channel = ?",(time_left,i[1]))
	    			base.commit()

def setup(client):
    client.add_cog(A_T_C_1(client))