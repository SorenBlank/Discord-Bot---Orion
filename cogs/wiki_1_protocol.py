import discord
from discord import Intents
from discord.ext import commands
from discord.ext import commands, tasks
import random
import asyncio
import wikipedia as wiki
import math
import sqlite3

base = sqlite3.connect("all.db")
cur = base.cursor()

class W1(commands.Cog):

	def __init__(self, client):
		self.client = client
	
	@commands.Cog.listener()
	async def on_ready(self):
		print("W1 is Loaded ----")

	au = 0
	@commands.Cog.listener()
	async def on_message(self, message):

		#making the message.content lower case in order to make the commands case insensitive
		ex_1 = message.content.lower().replace(',','')
		ex_2 = ex_1.replace("?","")
		etxt = ex_2 
		
		#splitting the exact_txt
		exact_txt_splitted = etxt.split(" ")



										###########################
										##   Wikipedia Command   ##
										###########################
		if etxt.startswith(".o wiki") or etxt.startswith(".o wikipedia"):
			cur.execute("SELECT*FROM WC")
			all = cur.fetchall()

			guilds = []
			channels = []
			ch = 0
			for i in all:
				guilds.append(i[0])
				channels.append(i[1])
				if i[0] == message.guild.id:
					ch = i[1]

			if message.guild.id in guilds:
				if message.channel.id in channels:
					msg = message
					au = message.author.id
					x1 = etxt.split(" ")
					words = [".o","wiki","wikipedia"]
					xwords = [i for i in x1 if i not in words]
					joined = ' '.join(xwords)

					try:
						await msg.channel.send(wiki.summary(joined, sentences=5))
					except wiki.exceptions.DisambiguationError as e:
						m='Search item couldn\'t be distinguished. Here is a list of search results: '
						await msg.channel.send(m)
						items=20
						pages=math.ceil(len(e.options)/items)

						for page in range(pages):
							p=''
							start = (page) * items
							end = min(start + items , len(e.options))
							for i, opt in enumerate(e.options[start:end], start=start):
								p += '**{0}. {1}** \n'.format(i + 1, opt)
							await msg.channel.send(p)
						await msg.channel.send('Now choose the index of your desired search result.')
						msgg=await self.client.wait_for('message')
						while not (msgg.author.id == au and msgg.channel.id == ch):
							msgg=await self.client.wait_for('message')
							pass
						if msgg.author.id == au:
							try:
								msg1 = [words for words in msgg.content.lower().split(" ") if words.isnumeric()]
								ind = int(msg1[0])
								if 1<=ind and ind<=len(e.options):
									await msgg.channel.send(wiki.summary(e.options[ind-1], sentences=5))
								else :
									await msgg.channel.send('The index does not exist. Start over again.')
							except:
								await msgg.channel.send('This page cannot be shown for some unknown reason.')

				if message.channel.id not in channels:
					ch = self.client.get_channel(ch)
					await message.channel.send(f"Please use this {ch.mention} channel.")
			else:
				await message.channel.send("No channel of this server is set as **Wikipedia Channel**.\n Please set one using this command `.o set wiki (channel)`")

										###########################
										##  Wikipedia Search 2.0 ##
										###########################
		
		sq_1 = [["can", "ask", "question"],
			["something","to","ask"],
			["wanna","ask","something"]]
		
		x = 0
		for i in sq_1:
			for ii in i:
				if ii in exact_txt_splitted:
					x = x + 1
					if x == 3 :
						break
			if x == 3:
				break

		if (etxt.startswith("hey orion") or etxt.startswith("orion"))  and x == 3:
			cur.execute("SELECT*FROM WC")
			all = cur.fetchall()

			guilds = []
			channels = []
			ch = 0
			for i in all:
				guilds.append(i[0])
				channels.append(i[1])
				if i[0] == message.guild.id:
					ch = i[1]

			if message.guild.id in guilds:
				if message.channel.id in channels:
					au=message.author.id
					ch = message.channel.id
					await message.channel.send(random.choice(['Sure, why not?',
															"Sir just ask away",
															"Sure! Ask away."]))
					
					msg= await self.client.wait_for('message')
					while not (msg.author.id == au and msg.channel.id == ch):
						msg=await self.client.wait_for('message')
						pass

					ques=['hey','orion','what','is','are','a',"tell","me","who","about","would","you","mind","telling","where","what's"]
					if msg.author.id == au and msg.channel.id == ch:
						msg_words=msg.content.lower().replace('?','').split(" ")
						que_words=[word for word in msg_words if word not in ques]
						que=' '.join(que_words)
						print(que)
						try:
							await msg.channel.send(wiki.summary(que, sentences=5))
						except wiki.exceptions.DisambiguationError as e:
							m='Search item couldn\'t be distinguished. Here is a list of search results: '
							await msg.channel.send(m)
							items=20
							pages=math.ceil(len(e.options)/items)

							for page in range(pages):
								p=''
								start = (page) * items
								end = min(start + items , len(e.options))
								for i, opt in enumerate(e.options[start:end], start=start):
									p += '**{0}. {1}** \n'.format(i + 1, opt)
								await msg.channel.send(p)
							
							await msg.channel.send('Now choose the index of your desired search result.')
							msgg=await self.client.wait_for('message')
							while not (msgg.author.id == au and msgg.channel.id == ch):
								msgg=await self.client.wait_for('message')
								pass
							if msgg.author.id == au:
								try:
									msg1 = [words for words in msgg.content.lower().split(" ") if words.isnumeric()]
									ind = int(msg1[0])
									if 1<=ind and ind<=len(e.options):
										await msgg.channel.send(wiki.summary(e.options[ind-1], sentences=5))
									else :
										await msgg.channel.send('The index does not exist. Start over again.')
								except:
									await msgg.channel.send('This page cannot be shown for some unknown reason.')
				if message.channel.id not in channels:
					ch = self.client.get_channel(ch)
					await message.channel.send(f"Please use this {ch.mention} channel.")
			else:
				await message.channel.send("No channel of this server is set as **Wikipedia Channel**.\n Please set one using this command `.o set wiki (channel)`")
			
		

def setup(client):
	client.add_cog(W1(client))