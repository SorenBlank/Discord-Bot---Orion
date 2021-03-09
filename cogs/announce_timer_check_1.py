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
from PIL import Image
from io import BytesIO
import numpy as np
import re
import pymongo
from pymongo import MongoClient

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
    		raw = ta_cur.find({})
    		lists = []

    		try:
	    		lists = [x for x in raw]
	    	except:
	    		pass

	    	for i in range(len(lists)):

	    		if int(lists[i]["time"]) <= 2:

	    			try:
	    				ch = self.client.get_channel(lists[i]["channel"])
	    				await ch.send(lists[i]["announcement"])
	    				ta_cur.delete_one({"_id":lists[i]["_id"]})

	    			except:
	    				pass

	    		elif int(lists[i]["time"]) > 2:
	    			ta_cur.update_one({"_id":lists[i]["_id"]},{"$inc":{"time":-1}})

def setup(client):
    client.add_cog(A_T_C_1(client))