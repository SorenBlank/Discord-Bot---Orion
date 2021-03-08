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
cluster = MongoClient("mongodb+srv://soren:cdD2_qWUYRk-d4G@orion.iztml.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
base = cluster["OrionDB"]

ta_cur = base["ta"]

class A_T_C_1(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
    	print("Timer Announce is Loaded ----")
    	while True:
    		await asyncio.sleep(1)
    		try:
	    		raw = ta_cur.find({})
	    		lists = [x for x in raw]
	    	except:
	    		pass

	    	for i in lists:
	    		if i["time"] <= 2:

	    			try:
	    				ch = self.client.get_channel(i["channel"])
	    				await ch.send(i["announcement"])
	    				ta_cur.delete_one({"_id":i["_id"]})

	    			except:
	    				pass

	    		elif i["time"] > 2:
	    			ta_cur.update_one({"_id":i["_id"]},{"$inc":{"time":-1}})

def setup(client):
    client.add_cog(A_T_C_1(client))