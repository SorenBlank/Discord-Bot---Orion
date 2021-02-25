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

base = sqlite3.connect("all.db")
cur = base.cursor()

class A_1(commands.Cog):
	def __init__(self, client):
		self.client = client

	@commands.Cog.listener()
	async def on_ready(self):
		print("A1 is Loaded ----")


									###########################
									##        ACTIVATOR      ##
									###########################

	@commands.group(invoke_without_command = True,aliases = ["initiate","start","set","setup"],case_insensitive=True)
	async def activate(self,ctx):
		activator_embed = discord.Embed(title='= = = = = = =| Help - [Activate] |= = = = = = =',description='Aliases = `initiate`, `start`, `set`\nFor more info: `.o help`\n\n__**:warning:Disclaimer:warning:**__\n:white_small_square: The `[` and `]` around the argument mean it’s required.\n:white_small_square: The `(` and `)` around the argument mean it’s optional.\n-   -   -   -   -   -   -   -   -   -   -   -   -   -   -   -   -   -   -   -')
		activator_embed.set_author(name='Activate Commands',icon_url=f'{self.client.user.avatar_url}')


		#FIRST FIELD
		activator_embed.add_field(name=":gear:PROTOCOLS:gear:",
								  value='‎‎--------- :arrow_down_small: ---------',
								  inline=False)
		activator_embed.add_field(name=":large_orange_diamond: M1",
								  value=":small_orange_diamond:Activating M1 will allow the mods to use **Moderation Commands**.\n**__Command:__** `.o activate m1`",
								  inline=False)
		activator_embed.add_field(name=":large_orange_diamond: C1 (BETA)",
								  value=":small_orange_diamond:Activating C1 on a specific channel will allow the bot to use it's chat functionality.\n**__Command:__** `.o activate c1 (channel)`",
								  inline=False)

		activator_embed.add_field(name=" ឵឵ ",value=" ឵឵ ",inline=False)

		#SECOND FIELD
		activator_embed.add_field(name=":card_box:SERVER UTILITIES:card_box:",
								  value = "------------ :arrow_down_small: ------------\nThis section includes all **server utility activation** commands.\n ឵឵ ",
								  inline= False)

		activator_embed.add_field(name=":hammer_pick: Announcement Command Channel",
								  value=":small_orange_diamond: You can announce anything in your server using **Announcement Commands**. In order to use these commands you need to set a specific channel which is not visible to all members beside the server admins and moderators, where you will execute these commands.\n**__Command:__** `.o set announce_ch (channel)`",
								  inline=False)


		activator_embed.add_field(name=":hammer_pick: Announcement Channel",
								  value=":small_orange_diamond: After setting up **Announcement Command Channel**, you need to set your announcement channels where you will announce stuffs. You can set up to 2 channels as **Announcement Channels**. After you set a channel, you will be able to use `.o announce` command for announcing with the bot.\n**__Command:__** `.o set announce (channel)`",
								  inline=False)

		activator_embed.add_field(name=" ឵឵ ",value=" ឵឵ ",inline=False)


		#THIRD FIELD
		activator_embed.add_field(name=":video_game:GAMES:video_game:",
								  value="------ :arrow_down_small: -----",
								  inline=False)
		activator_embed.add_field(name=":large_blue_diamond: Fibonacci/Fibo",
								  value=":small_blue_diamond: This is a Fibonacci Count Up game. Following command allows a specific channel to run this game. To know more about this in detail, type: `.o help game`\n**__Command:__** `.o activate fibo (channel)`",inline=False)
		activator_embed.add_field(name=":large_blue_diamond: TicTacToe",
								  value=":small_blue_diamond: No need to tell about this game I suppose. Following command allows a specific channel to run this game. In case you don't know what this game is ( xD ) please do not hesitate to type this `.o help game`\n**__Command:__** `.o activate tic (channel)`",
								  inline=False)
		activator_embed.add_field(name=":large_blue_diamond: Battleship (BETA)",
								  value=':small_blue_diamond: This is a Battleship game. Following command allows a specific channel to run this game. You can [click here](https://en.wikipedia.org/wiki/Battleship_game "https://en.wikipedia.org/wiki/Battleship_game") or type `.o help game` or more specifically type `.o help battleship` in order to know about this game. \n**__Command:__** `.o activate battleship (channel)`',
								  inline = False)
		
		activator_embed.add_field(name=" ឵឵ ",value=" ឵឵ ",inline=False)


		activator_embed.add_field(name=":book:PHILOSOPHY:book:",
								  value="---------- :arrow_down_small: ---------",
								  inline=False)
		activator_embed.add_field(name=":notebook: Wikipedia",
								  value=":small_orange_diamond: This is wikipedia. Following command allows a specific channel to use **Wikipedia** commands. To know more about this in detail, type: `.o help philosophy` \n**__Command:__** `.o activate wiki (channel)`",
								  inline=False)


		activator_embed.set_footer(icon_url=ctx.author.avatar_url,text=f"Requested by {ctx.author.name}")

		await ctx.send(embed = activator_embed)

	@activate.command()
	async def M1(self,ctx):
		if ctx.author.guild_permissions.manage_channels and ctx.author.guild_permissions.manage_messages:
			id_guild = ctx.guild.id
			cur.execute("SELECT*FROM M1guilds")
			raw_guilds = cur.fetchall()
			guilds = []
			for i in raw_guilds:
				guilds.append(i[0])

			if ctx.guild.id in guilds:
					await ctx.send(random.choice(["M1 is running",
												  "M1 is active"]))

			if ctx.guild.id not in guilds:
				cur.execute("INSERT INTO M1guilds (Guild) VALUES (?)",(id_guild,))
				base.commit()
				cur.execute("SELECT*FROM M1guilds")
				raw_guilds = cur.fetchall()
				guilds = []
				for i in raw_guilds:
					guilds.append(i[0])
				if ctx.guild.id in guilds:
					await ctx.send("M1 Activated\nModeration Commands has been unlocked!")
		else:
			await ctx.send("**Access Denied!** This command requires `manage_channel` and `manage_messages` permission in order to execute.")

	@activate.command()
	async def C1(self,ctx,channel:discord.TextChannel = None):

		#This checks if the user has manage channels permission
		if ctx.author.guild_permissions.manage_channels:
			
			#This makes the bot acts as if the a specific channel has been provided
			if channel != None:
				try:
					id_channel = channel.id
					cur.execute("SELECT*FROM C1channels")
					raw_channels = cur.fetchall()
					channels = []
					for s in raw_channels:
						channels.append(s[1])
					if id_channel not in channels:
						cur.execute("INSERT INTO C1channels (Guild,Channel,Createtime,Timegap) VALUES (?,?,?,?)",(ctx.guild.id,id_channel,"",0))
						base.commit()
						await ctx.send(f"C1 has been activated in {channel.mention}")
					else:
						await ctx.send(f"C1 is already running in {channel.mention}")
				except:
					await ctx.send(f"{ctx.author.mention}, please pass all required arguments.")

			#This makes the bot acts as if no channel was specified
			elif channel == None:
				id_channel = ctx.channel.id
				cur.execute("SELECT*FROM C1channels")
				raw_channels = cur.fetchall()
				channels = []
				for s in raw_channels:
					channels.append(s[1])
				if id_channel not in channels:
					cur.execute("INSERT INTO C1channels (Guild,Channel,Createtime,Timegap) VALUES (?,?,?,?)",(ctx.guild.id,id_channel,"",0))
					base.commit()
					await ctx.send(f"C1 has been activated in {ctx.channel.mention}")
				else:
					await ctx.send(f"C1 is already running in {ctx.channel.mention}")

		else:
			await ctx.send(f"**Access Denied!** \nThis command requires `manage_channel` permission in order to execute.")


	#set a channel where you are gonna give your announcement commands
	@activate.command(aliases = ["announce_ch","ach"])
	async def Announcement_ch(self,ctx, channel:discord.TextChannel = None):
	    au = ctx.author.id
	    ch = ctx.channel.id
	    cur.execute("SELECT*FROM ANC")
	    all = cur.fetchall()
	    guilds = []

	    try:
	        for i in all:
	            guilds.append(i[0])
	    except:
	        pass
	    
	    channel_id = 0
	    if ctx.guild.id in guilds:
	        for i in all:
	            if i[0] == ctx.guild.id:
	                channel_id = i[1]

	        channel_set = self.client.get_channel(channel_id)
	        await ctx.send(f"{channel_set.mention} is already set as the **Announcement Command Channel**. Would you like to change it? (Type: Y/N)")
	        text = await self.client.wait_for("message")
	        while text.author.id != au:
	            text = await self.client.wait_for("message")
	            pass

	        if text.author.id == au and text.channel.id ==ch:
	            answer = text.content.lower()
	            y_matches = ["yes","y"]
	            n_matches = ["no","n"]
	            m = ["yes","y","no","n"]

	            if answer in y_matches:
	                await ctx.send("Please mention the channel below_")
	                mention = await self.client.wait_for("message")
	                while not (text.author.id == au and text.channel.id == ch):
	                    mention = await self.client.wait_for("message")
	                    pass

	                ch1 = mention.content.split("#")
	                print(ch1)
	                ch2 = ch1[1].split(">")
	                ch3 = int(ch2[0])
	                print(ch3)
	                lower = mention.content.lower()

	                if lower != "eliminate":
	                    try:
	                        channel1 = self.client.get_channel(ch3)
	                        cur.execute("UPDATE ANC SET Channel = ? WHERE Guild = ?",(channel1.id,ctx.guild.id))
	                        base.commit()
	                        await ctx.send(f"**Announcement Command Channel** has been updated to {channel1.mention}.")
	                    except:
	                        await ctx.send("Argument ERROR!")

	            if answer in n_matches:
	            	await ctx.send("Granted!")

	            if answer not in m:
	            	await ctx.send("Input ERROR")

	    if ctx.guild.id not in guilds:
	    	if channel == None:
	    		cur.execute("INSERT INTO ANC (Guild,Channel) VALUES(?,?)",(ctx.guild.id,ctx.channel.id))
	    		base.commit()
	    		await ctx.send(f"{ctx.channel.mention} has been set as an **Announcement Command Channel**")

	    	if channel != None:
	        	cur.execute("INSERT INTO ANC (Guild,Channel) VALUES(?,?)",(ctx.guild.id,channel.id))
	        	base.commit()
	        	await ctx.send(f"{channel.mention} has been set as an **Announcement Command Channel**")

	#this is the command using which you are going to set the announcement channel
	@activate.command(aliases = ["announce"])
	async def announcement(self,ctx,channel:discord.TextChannel = None):
		cur.execute("SELECT*FROM ANC")
		all = cur.fetchall()
		guilds = []
		channels = []
		try:
			for i in all:
				guilds.append(i[0])
			for i in all:
				channels.append(i[1])
		except:
			pass

		if ctx.author.guild_permissions.administrator or ctx.author.guild_permissions.manage_channels:

			if channel.id in channels:
				await ctx.send(f"{channel.mention} is set as an **Announcement Command Channel**.")

			else:
				if ctx.channel.id in channels:
					channel_id = channel.id
					guild_id = ctx.guild.id
					ctx_channel = self.client.get_channel(ctx.channel.id)
					text = await ctx_channel.history(limit = 2).flatten()
					cur.execute("SELECT*FROM Announce_ch WHERE Guild Like ?",(ctx.guild.id,))
					all = cur.fetchall()
					a_channels = []

					try:
						for i in all:
							a_channels.append(i[1])
					except:
						pass
					
					if len(a_channels) <10:
						if channel_id not in a_channels:
							cur.execute("INSERT INTO Announce_ch (Guild, Channel) VALUES(?,?)",(guild_id,channel_id))
							base.commit()
							await text[0].add_reaction("✅")
							await ctx.send("Channel Added!")

					if channel_id in a_channels:
						await text[0].add_reaction("❎")
						await ctx.send(f"{channel.mention} is already set as an announcement channel.")

					if len(a_channels) == 10:
						await ctx.send("You can only have 10 announcement channels.")
				
				elif ctx.guild.id in guilds:
					m_ch = []
					for i in all:
						if i[0] == ctx.guild.id:
							m_ch.append(i[1])
					
					if len(m_ch) > 1:
						ch = client.get_channel(m_ch[0])
						ch2 = client.get_channel(m_ch[1])
						await ctx.send(f"You are giving command on wrong channel. Please type command here, {ch.mention} or {ch2.mention}")
					
					if len(m_ch) == 1:
						ch = self.client.get_channel(m_ch[0])
						await ctx.send(f"You are giving command on wrong channel. Please type command here, {ch.mention}")
				
				elif ctx.guild.id not in guilds:
					await ctx.send("No channel of this server is set as **Announcement Command Channel**.\nPlease set one using this command `.o set announce_ch 'channel mention'`")


	@activate.command(aliases = ["fibo"])
	async def fibonacci(self,ctx, channel:discord.TextChannel = None):
		cur.execute("SELECT*FROM FC")
		all = cur.fetchall()
		guilds = []
		channels = []
		try:
			for i in all:
				guilds.append(i[0])
			for i in all:
				channels.append(i[1])
		except:
			pass

		if ctx.author.guild_permissions.manage_channels:
			if channel == None:
				id_channel = ctx.channel.id
				if ctx.guild.id not in guilds:
					cur.execute("INSERT INTO FC (Guild, Channel, Past_Number, Last_Number, Author) VALUES (?,?,?,?,?)",(ctx.guild.id,id_channel,0,0,0))
					base.commit()
					await ctx.send(f"Fibonacci Counting channel has been updated to {ctx.channel.mention}")
				
				if ctx.guild.id in guilds and id_channel in channels:
					await ctx.send("This channel is already set as Fibonacci Counting channel.")
				
				if ctx.guild.id in guilds and id_channel not in channels:
					cur.execute("UPDATE FC SET Channel = ? WHERE Guild = ?",(id_channel,ctx.guild.id))
					base.commit()
					await ctx.send(f"Fibonacci Counting channel has been update to {ctx.channel.mention}")

			else:
				try:
					id_channel = channel.id
					if ctx.guild.id not in guilds:
						cur.execute("INSERT INTO FC (Guild, Channel, Past_Number, Last_Number, Author) VALUES (?,?,?,?,?)",(ctx.guild.id,id_channel,0,0,0))
						base.commit()
						await ctx.send(f"Fibonacci Counting channel has been updated to {ctx.channel.mention}")
					
					if ctx.guild.id in guilds and id_channel in channels:
						await ctx.send("This channel is already set as Fibonacci Counting channel.")
					
					if ctx.guild.id in guilds and id_channel not in channels:
						cur.execute("UPDATE FC SET Channel = ? WHERE Guild = ?",(id_channel,ctx.guild.id))
						base.commit()
						await ctx.send(f"Fibonacci Counting channel has been update to {channel.mention}")
				except:
					await ctx.send(f"Argument ERROR!")

		else:
			await ctx.send("**Access Denied!** \nThis command requires `manage_channel` permission in order to execute.")


	@activate.command(aliases = ["tictac","tictactoe"])
	async def tic(self,ctx, channel: discord.TextChannel = None):
		cur.execute("SELECT*FROM TC")
		all = cur.fetchall()
		guilds = []
		channels = []
		try:
			for i in all:
				guilds.append(i[0])
			for i in all:
				channels.append(i[1])
		except:
			pass

		if ctx.author.guild_permissions.manage_channels:
			if channel == None:
					if ctx.guild.id not in guilds:
						cur.execute("INSERT INTO TC (Guild, Channel) VALUES (?,?)",(ctx.guild.id,ctx.channel.id))
						base.commit()
						await ctx.send(f"**TicTacToe** channel has been updated to {ctx.channel.mention}")

					if ctx.guild.id in guilds and ctx.channel.id in channels:
						await ctx.send("This channel is already set as **TicTacToe** channel.")
			
					if ctx.guild.id in guilds and ctx.channel.id not in channels:
						cur.execute("UPDATE TC SET Channel = ? WHERE Guild = ?",(ctx.channel.id,ctx.guild.id))
						base.commit()
						await ctx.send(f" TicTacToe channel has been updated to {ctx.channel.mention}")
					
			elif channel != None:
				try:
					if ctx.guild.id not in guilds:
						cur.execute("INSERT INTO TC (Guild, Channel) VALUES (?,?)",(ctx.guild.id,channel.id))
						base.commit()
						await ctx.send(f"**TicTacToe** channel has been updated to {channel.mention}")
					
					if ctx.guild.id in guilds and channel.id in channels:
						await ctx.send("This channel is already set as **TicTacToe** channel.")
					
					if ctx.guild.id in guilds and ctx.channel.id not in channels:
						cur.execute("UPDATE TC SET Channel = ? WHERE Guild = ?",(channel.id,ctx.guild.id))
						base.commit()
						await ctx.send(f" TicTacToe channel has been updated to {channel.mention}")
				
				except:
					await ctx.send(f"Argument ERROR!")
				
		else:
			await ctx.send("**Access Denied!** \nThis command requires `manage_channel` permission in order to execute.")

	@activate.command(aliases = ["battleship"])
	async def bs(self,ctx, channel: discord.TextChannel = None):
		cur.execute("SELECT*FROM BC")
		all = cur.fetchall()
		guilds = []
		channels = []
		try:
			for i in all:
				guilds.append(i[0])
			for i in all:
				channels.append(i[1])
		except:
			pass

		if ctx.author.guild_permissions.manage_channels:
			if channel != None:
				try:
					if ctx.guild.id not in guilds:
						cur.execute("INSERT INTO BC (Guild, Channel) VALUES (?,?)",(ctx.guild.id,channel.id))
						base.commit()
						await ctx.send(f"**Battleship** channel has been updated to {channel.mention}")

					if ctx.guild.id in guilds and channel.id in channels:
						await ctx.send("This channel is already set as **Battleship** channel.")
					
					if ctx.guild.id in guilds and channel.id not in channels:
						cur.execute("UPDATE BC SET Channel = ? WHERE Guild = ?",(channel.id,ctx.guild.id))
						base.commit()
						await ctx.send(f" **Battleship** channel has been updated to {channel.mention}")

				except:
					await ctx.send(f"Argument ERROR!")


			if channel == None:
				if ctx.guild.id not in guilds:
					cur.execute("INSERT INTO BC (Guild, Channel) VALUES (?,?)",(ctx.guild.id,ctx.channel.id))
					base.commit()
					await ctx.send(f"**Battleship** channel has been updated to {ctx.channel.mention}")

				if ctx.guild.id in guilds and ctx.channel.id in channels:
					await ctx.send("This channel is already set as **Battleship** channel.")

				if ctx.guild.id in guilds and ctx.channel.id not in channels:
					cur.execute("UPDATE BC SET Channel = ? WHERE Guild = ?",(ctx.channel.id,ctx.guild.id))
					base.commit()
					await ctx.send(f" **Battleship** channel has been updated to {ctx.channel.mention}")

		else:
			await ctx.send("**Access Denied!** \nThis command requires `manage_channel` permission in order to execute.")

	@activate.command(aliases = ["wiki"])
	async def Wikipedia(self,ctx,channel:discord.TextChannel = None):
		cur.execute("SELECT*FROM WC")
		all = cur.fetchall()
		guilds = []
		channels = []
		for i in all:
			guilds.append(i[0])
			channels.append(i[1])

		if channel != None:
			try:
				if ctx.guild.id not in guilds:
					if channel.id not in channels:
						cur.execute("INSERT INTO WC (Guild, Channel) VALUES (?,?)",(ctx.guild.id,channel.id))
						base.commit()
						await ctx.send(f"**Wikipedia** channel has been updated to {channel.mention}.")

				if ctx.guild.id in guilds:
					if channel.id not in channels:
						cur.execute("UPDATE WC SET Channel = ? WHERE Guild = ?",(channel.id,guild.id))
						base.commit()
						await ctx.send(f"**Wikipedia** channel has been updated to {channel.mention}.")
			except:
				ctx.send("Argument ERROR!")
		if channel == None:
			if ctx.guild.id not in guilds:
				if ctx.channel.id not in channels:
					cur.execute("INSERT INTO WC (Guild, Channel) VALUES (?,?)",(ctx.guild.id,ctx.channel.id))
					base.commit()
					await ctx.send(f"**Wikipedia** channel has been updated to {ctx.channel.mention}.")

			if ctx.guild.id in guilds:
				if ctx.channel.id not in channels:
					cur.execute("UPDATE WC SET Channel = ? WHERE Guild = ?",(ctx.channel.id,ctx.guild.id))
					base.commit()
					await ctx.send(f"**Wikipedia** channel has been updated to {ctx.channel.mention}.")

def setup(client):
	client.add_cog(A_1(client))