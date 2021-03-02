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

base = psycopg2.connect(user="yyflmbmssbqvcl",
                        password="f3f1c4a58fedf11450c7cf60d7a0e9d5564600cac78d867a3db59688f0bf88b6",
                        host="ec2-3-224-251-47.compute-1.amazonaws.com",
                        port="5432",
                        database="dda86padcqcfo8"
                        )
cur = base.cursor()

class D_1(commands.Cog):
	def __init__(self, client):
		self.client = client

	@commands.Cog.listener()
	async def on_ready(self):
		print("D1 is Loaded ----")

										###########################
										##      DEACTIVATOR      ##
										###########################

	@commands.group(aliases = ["stop","eliminate","remove"],invoke_without_command = True,case_insensitive = True)
	async def deactivate(self,ctx):
		deactivator_embed = discord.Embed(title = "= = = = = = =| Help - [Deactivate] |= = = = = = =",description= "Aliases = `stop` , `eliminate`, `remove`\nFor more info: `.o help`\n-   -   -   -   -   -   -   -   -   -   -   -   -   -   -   -   -   -   -   -")
		

		deactivator_embed.add_field(name=":octagonal_sign: Deactivate Commands :octagonal_sign:",value="-:arrow_down: - -  :arrow_down: - -  :arrow_down: - -  :arrow_down: - -  :arrow_down:-\n\n:one: `.o deactivate m1`\nThis command will turn off **M1 protocol**.\n\n:two: `.o deactivate c1 (channel)` or `deactivate all c1`\nThis command will eliminate **C1 Protocol** from a specific channel or all channels.\n\n:three: `.o remove announce_ch`\nThis command removes **Announcement Command Channel**.\n\n:four: `.o remove announce (channel)`\nThis command removes bot **Announcement Channel**.\n\n:five: `.o deactivate fibo`\nThis command removes **Fibonacci Channel**.\n\n:six: `.o deactivate tictactoe`\nThis command removes **TicTacToe Channel**.\n\n:seven: `.o deactivate battleship`\nThis command removes **Battleship Channel**.\n\n:eight: `.o deactivate wiki`\nThis command removes **Wikipedia Channel**.")
		deactivator_embed.set_footer(icon_url=ctx.author.avatar_url,text=f"Requested by {ctx.author.name}")

		await ctx.send(embed = deactivator_embed)

	@deactivate.command()
	async def all(self,ctx,p = None):
		if p == "c1" or p == "C1":
			cur.execute("DELETE FROM C1channels WHERE Guild = ?",(ctx.guild.id,))
			base.commit()
			await ctx.send("C1 has been eliminated from all channels.")



	@deactivate.command(aliases = ["m1 protocol","m1 function"])
	async def m1(self,ctx):
		if ctx.author.guild_permissions.manage_channels and ctx.author.guild_permissions.manage_channels:
			id_guild = ctx.guild.id
			cur.execute("SELECT*FROM M1guilds")
			raw_guilds = cur.fetchall()
			guilds = []
			for i in raw_guilds:
				guilds.append(i[0])
			
			if ctx.guild.id not in guilds:
					await ctx.send(random.choice(["M1 is stop",
												  "M1 isn't running"]))
			
			if ctx.guild.id in guilds:
				cur.execute("DELETE FROM M1guilds WHERE Guild = ?",(id_guild,))
				base.commit()
				await ctx.send(random.choice(["M1 Eliminated","M1 Stopped"]))
		else:
			await ctx.send("**Access Denied!** \nThis command requires `manage_channel` and `manage_messages` permission in order to execute.")

	@deactivate.command()
	async def c1(self,ctx,channel:discord.TextChannel=None):
		cur.execute("SELECT*FROM C1channels")
		raw_channels = cur.fetchall()
		channels = []
		for s in raw_channels:
			channels.append(s[1])

		if ctx.author.guild_permissions.manage_channels:
			if channel == None:
				if ctx.channel.id in channels:
					cur.execute("DELETE FROM C1channels Where Channel = ?",(ctx.channel.id,))
					base.commit()
					await ctx.send(f"C1 has been eliminated from {ctx.channel.mention}")
				if ctx.channel.id not in channels:
					await ctx.send(f"C1 is not running in {ctx.channel.mention}")
			
			if channel != None:
				try:
					cur.execute("DELETE FROM C1channels Where Channel = ?",(channel.id,))
					base.execute()
				except:
					await ctx.send(f"{ctx.author.mention}, please pass all required arguments.")
		else:
			await ctx.send("**Access Denied!**\nThis command requires `manage_channel` permission in order to execute.")


	@deactivate.command(aliases = ["fibo"])
	async def Fibonacci(self,ctx):
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

			if ctx.guild.id in guilds:
				x = [s for s in all if s[0] == ctx.guild.id]
				x_ch = self.client.get_channel(x[0][1])
				cur.execute("DELETE FROM FC WHERE Guild = ?",(ctx.guild.id,))
				base.commit()
				await ctx.send(f"{x_ch.mention} is no longer a **Fibonacci** channel.")
			else:
				await ctx.send("No channel is set as **Fibonacci** channel.")

		else:
			await ctx.send("**Access Denied!**\nThis command requires `manage_channel` permission in order to execute.")

	@deactivate.command(aliases = ["tictactoe","tac"])
	async def Tic(self,ctx):
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
			if ctx.guild.id in guilds:
				cur.execute("DELETE FROM TC WHERE Guild = ?",(ctx.guild.id))
				base.commit()
				await ctx.send("Command executed")

			else:
				await ctx.send("No channel is set as **TicTacToe** channel.")
		else:
			await ctx.send("**Access Denied!**\nThis command requires `manage_channel` permission in order to execute.")


	@deactivate.command()
	async def battleship(self,ctx):
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
			if ctx.guild.id in guilds:
				cur.execute("DELETE FROM BC WHERE Guild = ?",(ctx.guild.id))
				base.commit()
				await ctx.send("Command executed")
			else:
				await ctx.send("No channel is set as **Battleship** channel.")
		else:
			await ctx.send("**Access Denied!**This command requires `manage_channel` permission in order to execute.")

	@deactivate.command(aliases= ["announcement_ch","ach"])
	async def Announce_ch(self,ctx):
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
		if ctx.guild.id in guilds:
			cur.execute("DELETE FROM ANC WHERE Guild = ?",(ctx.guild.id,))
			base.commit()
			await ctx.send(f"{channel_set.mention} is no longer **Announcement Command Channel**.")
		else:
			await ctx.send("No channel is set as **Announcement Command Channel**.")

	@deactivate.command(aliases=["an"])
	async def Announce(self,ctx,channel:discord.TextChannel = None):
		cur.execute("SELECT*FROM ANC")
		all = cur.fetchall()
		channels = []
		guilds = []
		try:
			for i in all:
				channels.append(i[1])
				guilds.append(i[0])
		except:
			pass

		if ctx.channel.id in channels:
			au = ctx.author.id
			ch = ctx.channel.id
			cur.execute("SELECT*FROM Announce_ch")
			all = cur.fetchall()
			guilds = []
			channels = []

			for i in all:
				guilds.append(i[0])
				channels.append(i[1])

			if channel != None:
				try:
					if channel.id in channels:
						cur.execute("DELETE FROM Announce_ch WHERE Channel = ?",(channel.id,))
						base.commit()
						await ctx.send(f"{channel.mention} is no longer an **Announcement Channel**")
					elif channel.id not in channels:
						await ctx.send(f"**Access Denied!**\nNo channel of this server is set as **Announcement Channel**.")

				except:
					await ctx.send("Argument ERROR!")


	@deactivate.command(aliases = ["wiki"])
	async def WIKipedia(self,ctx):
		cur.execute("SELECT*FROM WC")
		all = cur.fetchall()
		channels = []
		guilds = []
		ch = 0
		try:
			for i in all:
				channels.append(i[1])
				guilds.append(i[0])
				if i[0] == ctx.guild.id:
					ch = i[1]
		except:
			pass

		if ctx.guild.id in guilds:
			cur.execute("DELETE FROM WC WHERE Guild = ?",(ctx.guild.id,))
			base.commit()
			channel = self.client.get_channel(ch)
			await ctx.send(f"{channel.mention} is no longer an **Wikipedia Channel**")
		else:
			await ctx.send("No channel of this server is set as **Wikipedia Channel**.")

def setup(client):
	client.add_cog(D_1(client))