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

class H_1(commands.Cog):
	def __init__(self, client):
		self.client = client

	@commands.Cog.listener()
	async def on_ready(self):
		print("H1 is Loaded ----")

	@commands.group(invoke_without_command = True,case_insensitive=True,aliases = ["h"])
	async def help(self,ctx):

		help_embed = discord.Embed(title='= = = = = = = |❗❕Help❕❗| = = = = = = =',description="Prefix = `.o`/`.O`\nInvite Link = `.o invite`\n-   -   -   -   -   -   -   -   -   -   -   -   -   -   -   -   -   -   -   -")
		
		help_embed.add_field(name=":gear:PROTOCOLS/SERVER UTILITIES:gear:",
							 value="--------------------- :arrow_down_small: ---------------------\n:white_small_square: This section includes all **Protocol** infos.\n**__Command:__** `.o help protocol`\n\n:white_small_square: This section includes all **Server Utility** infos.\n**__Command:__** `.o help server utility`\n ឵឵ \n ឵឵ ",
							 inline = False)

		help_embed.add_field(name=":card_box:UTILITIES:card_box:",
							 value="------- :arrow_down_small: -------\n:white_small_square: This section includes all **Utility** infos which are easily accessable to everyone.\n**__Command:__** `.o help utility`\n ឵឵ \n ឵឵",
							 inline=False)

		help_embed.add_field(name=":video_game:GAMES:video_game:",
							 value="------ :arrow_down_small: -----\n:white_small_square: This section includes all **Games** infos.\n**__Command:__** `.o help game`\n ឵឵ \n ឵឵",
							 inline=False)

		help_embed.add_field(name=":book:PHILOSOPHY:book:",
							 value="---------- :arrow_down_small: ---------\n:white_small_square: If you are not a nerd then this section is not for you.\n**__Command:__** `.o help philosophy`",
							 inline= False)
		help_embed.set_footer(icon_url=ctx.author.avatar_url,text=f"Requested by {ctx.author.name}")
		await ctx.send(embed = help_embed)

	@help.command(aliases=["games","g","tictactoe","tic","tac","fibo","Fibonacci"])
	async def game(self,ctx):
		game_embed = discord.Embed(title="= = = = = = = = |🎮 Game 🎮| = = = = = = = =",description="឵឵")
		game_embed.add_field(name=':1234: Fibonacci/Fibo :1234:',
							 value="This is a **Fibonacci Count Up** game. In mathematics, the Fibonacci numbers, commonly denoted `Fn`, form a sequence, called the Fibonacci sequence, such that each number is the sum of the two preceding ones, starting from `0` and `1`.\nSequence Example: `1, 1, 2, 3, 5, 8, 13, 21, 55........`. Just start the game by typing `1` in the Fibonacci channel.\n:notepad_spiral:__**Rules:**__:notepad_spiral:\n**1)** A channel has to be specified/set before playing **Fibonacci Countup**.\n__**Activation Command**__: `.o activate fibo (channel)`\n**2)** The count starts from 1.\n**3)** One player can not count twice on a row.",
							 inline=False)
		game_embed.add_field(name=" ឵឵ ",value=" ឵឵ ",inline=False)
		game_embed.add_field(name=":o: TicTacToe :x:",
							 value="This is a **TicTacToe** game. Tic-tac-toe (American English), noughts and crosses (Commonwealth English), or Xs and Os/“X’y O’sies” (Ireland), is a paper-and-pencil game for two players, X and O, who take turns marking the spaces in a 3×3 grid. The player who succeeds in placing three of their marks in a diagonal, horizontal, or vertical row is the winner. It is a solved game with a forced draw assuming best play from both players.\n __**Command:**__ `.o tic [player/opponent]`\n:notepad_spiral:__**Rules:**__:notepad_spiral:\n**1)** A channel has to be specified/set before playing **TicTacToe**\n**2)** You can not place your symbol twice on a row.\n**3)** You can not overlap.",
							 inline=False)
		game_embed.add_field(name=" ឵឵ ",value=" ឵឵ ",inline=False)
		game_embed.add_field(name=":ship: Battleship :ship:",
							 value="This is a **Battleship** game. Battleship (also Battleships or Sea Battle) is a strategy type guessing game for two players. It is played on ruled grids (paper or board) on which each player's fleet of ships (including battleships) are marked. The locations of the fleets are concealed from the other player.The objective of the game is to destroy the opposing player's fleet. You can check this [tutorial](https://www.youtube.com/watch?v=4gHJlYLomrs&ab_channel=GatherTogetherGames) or read this [article](https://www.thesprucecrafts.com/the-basic-rules-of-battleship-411069) or type `.o help battleship`.\n__**Command:**__ `.o battleship [player/opponent]`\n:notepad_spiral:__**Rules:**__:notepad_spiral:\n**1)** Each player places the 5 ships somewhere on their board.\n**2)** The ships can only be placed vertically or horizontally. Diagonal placement is not allowed.\n**3)** No part of a ship may hang off the edge of the board.\n**4)** Ships may not overlap each other.",
							 inline="False")
		game_embed.set_footer(icon_url=ctx.author.avatar_url,text=f"Requested by {ctx.author.name}")
		await ctx.send(embed = game_embed)

	@help.command(aliases=["bs"])
	async def battleship(self,ctx):
		bs_embed = discord.Embed(title="= = = = = = |:ship: Battleship :ship:| = = = = =",description="Aliases = `bs`\n__**Command:**__ `.o battleship (player/opponent)`\n-   -   -   -   -   -   -   -   -   -   -   -   -   -   -   -   -   -   -   -")
		bs_embed.add_field(name="=======:notepad_spiral:Rules for BattleShip:notepad_spiral:=======",
						   value="឵឵",
						   inline=False)
		bs_embed.add_field(name="Game Objective",
						   value="This is a **Battleship** game. Battleship (also Battleships or Sea Battle) is a strategy type guessing game for two players. It is played on ruled grids (paper or board) on which each player's fleet of ships (including battleships) are marked. The locations of the fleets are concealed from the other player. Players alternate turns calling \"shots\" at the other player's ships, and the objective of the game is to destroy the opposing player's fleet.",
						   inline=False)
		bs_embed.add_field(name="Starting a New Game",
						   value="Each player places the 5 ships somewhere on their board.  The ships can only be placed vertically or horizontally. Diagonal placement is not allowed. No part of a ship may hang off the edge of the board.  Ships may not overlap each other.  No ships may be placed on another ship.",
						   inline=False)
		bs_embed.add_field(name="Playing the Game",
						   value="The opponent responds with `hit` or `miss` as appropriate. Both players boards will be marked with `X`. `Red X` for hit, `White X` for miss. For example, if you call out F6 and your opponent does not have any ship located at F6, your opponent would respond with `miss`.  Your board will record the miss F6 by placing a `White X` of your board's F6. Your opponent records the miss by placing. You can check this [tutorial](https://www.youtube.com/watch?v=4gHJlYLomrs&ab_channel=GatherTogetherGames 'https://www.youtube.com/watch?v=4gHJlYLomrs&ab_channel=GatherTogetherGames') or read this [article](https://www.thesprucecrafts.com/the-basic-rules-of-battleship-411069 'https://www.thesprucecrafts.com/the-basic-rules-of-battleship-411069')",
						   inline=False)
		bs_embed.set_image(url="https://cdn.discordapp.com/attachments/753509805238517802/805099326317396037/bs2.jpg")
		bs_embed.set_footer(icon_url=ctx.author.avatar_url,text=f"Requested by {ctx.author.name}")
		await ctx.send(embed=bs_embed)

	@help.command(aliases=["p","c1","m1"])
	async def protocol(self,ctx):
		p_embed = discord.Embed(title="= = = = = = |:gear: Protocol :gear:| = = = = =",description="Aliases = `p`\n\n__**:warning:Disclaimer:warning:**__\n:white_small_square: The `[` and `]` around the argument mean it’s required.\n:white_small_square: The `(` and `)` around the argument mean it’s optional\n-   -   -   -   -   -   -   -   -   -   -   -   -   -   -   -   -   -   -   -")
		p_embed.add_field(name=":crossed_swords: M1 :crossed_swords:",
						  value=":small_orange_diamond: M1 Protocol includes moderation commands. After activating the **M1** you can use the following moderation commands-\n**1) **__Kick__\n__**Command:**__ `.o kick [member]`\n\n**2) **__Ban__\n__**Command:**__ `.o ban [member]`\n\n**3) **__Unban__\n__**Command:**__ `.o unabn [member]`",
						  inline=False)
		p_embed.add_field(name=" ឵឵ ",value=" ឵឵ ",inline=False)
		p_embed.add_field(name=":robot: C1 :robot:",
						  value=":small_blue_diamond: Just activate a channel using this command `.o activate c1 (channel)`. And rest of the job leave up to the bot.")
		p_embed.set_footer(icon_url=ctx.author.avatar_url,text=f"Requested by {ctx.author.name}")
		await ctx.send(embed=p_embed)

	@help.command(aliases = ["initiate","start","set","setup"])
	async def Activate(self,ctx):
		activator_embed = discord.Embed(title='= = = = = = =| Help - [Activate] |= = = = = = =',description='Aliases = `initiate`, `start`, `set`\nFor more info: `.o help`\n\n__**:warning:Disclaimer:warning:**__\n:white_small_square: The `[` and `]` around the argument mean it’s required.\n:white_small_square: The `(` and `)` around the argument mean it’s optional.\n-   -   -   -   -   -   -   -   -   -   -   -   -   -   -   -   -   -   -   -')


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
		activator_embed.add_field(name=":orange_book: Wikipedia",
								  value=":small_orange_diamond: This is wikipedia. Following command allows a specific channel to use **Wikipedia** commands. To know more about this in detail, type: `.o help philosophy` \n**__Command:__** `.o activate wiki (channel)`",
								  inline=False)


		activator_embed.set_footer(icon_url=ctx.author.avatar_url,text=f"Requested by {ctx.author.name}")

		await ctx.send(embed = activator_embed)

	@help.command(aliases = ["stop","eliminate","remove"])
	async def Deactivate(self,ctx):
		deactivator_embed = discord.Embed(title = "= = = = = = =| Help - [Deactivate] |= = = = = = =",description= "Aliases = `stop` , `eliminate`, `remove`\nFor more info: `.o help`\n-   -   -   -   -   -   -   -   -   -   -   -   -   -   -   -   -   -   -   -")

		deactivator_embed.add_field(name=":octagonal_sign: Deactivate Commands :octagonal_sign:",value="-:arrow_down: - -  :arrow_down: - -  :arrow_down: - -  :arrow_down: - -  :arrow_down:-\n\n:one: `.o deactivate m1`\nThis command will turn off **M1 protocol**.\n\n:two: `.o deactivate c1 (channel)` or `deactivate all c1`\nThis command will eliminate **C1 Protocol** from a specific channel or all channels.\n\n:three: `.o remove announce_ch`\nThis command removes **Announcement Command Channel**.\n\n:four: `.o remove announce (channel)`\nThis command removes bot **Announcement Channel**.\n\n:five: `.o deactivate fibo`\nThis command removes **Fibonacci Channel**.\n\n:six: `.o deactivate tictactoe`\nThis command removes **TicTacToe Channel**.\n\n:seven: `.o deactivate battleship`\nThis command removes **Battleship Channel**.\n\n:eight: `.o deactivate wiki`\nThis command removes **Wikipedia Channel**.")
		deactivator_embed.set_footer(icon_url=ctx.author.avatar_url,text=f"Requested by {ctx.author.name}")
		await ctx.send(embed = deactivator_embed)



	@help.command(aliases=["su","server","announce","announcement"])
	async def server_utilities(self,ctx,msg = None):
		try:
			if msg.lower() == "utility" or msg.lower() == "utilities" or msg.lower() == "u":
				su_embed = discord.Embed(title="= = = = = = |:card_box:Server Utilities :card_box:| = = = = =",description="Aliases = `su`,`server utility`,`server utilities`\nFor more info: `.o help`\n\n__**:warning:Disclaimer:warning:**__\n:white_small_square: The `[` and `]` around the argument mean it’s required.\n:white_small_square: The `(` and `)` around the argument mean it’s optional.\n-   -   -   -   -   -   -   -   -   -   -   -   -   -   -   -   -   -   -   -\n")

				su_embed.add_field(name="= = __:link:ACTIVATION / DEACTIVATION:link:__ = =",
									 value="- - - - - - - - - :arrow_down: - -  :arrow_down: - -  :arrow_down: - -  :arrow_down: - - - - - - - - -\n:white_small_square: **Activation/Deactivation** commands are the most important commands in order to use all features properly.",
									 inline=False)
				su_embed.add_field(name=":large_blue_diamond: Activation",
									 value=":small_blue_diamond: Thre are so many features in this bot which requires a specific channel for each where the features can Better used. Such as, a specific channel for **TicTacToe** game or **Battleship** game, one or two specific **Announcement** channel and a specific Announcement Command channel where you will tell the bot in which channel to announce. Here you will find all activation commands.\n**__Command:__** `.o help activate`\n឵឵",
									 inline=False)
				su_embed.add_field(name=":large_orange_diamond: Deactivation",
									 value=":small_orange_diamond: Sometimes you might need to deactivate a feature from a channel or change the channel. Here you will find all deactivation/update commands. \n**__Command:__** `.o help deactivate`\n- - - - - - - - - - - - - - - - - - - -",
									 inline=False)
				su_embed.add_field(name=" ឵឵ ",value=" ឵឵ ",inline=False)
				su_embed.add_field(name=":diamond_shape_with_a_dot_inside: ANNOUNCE",
								  value=":small_blue_diamond: You can announce announce with your bot now. You can also attach file with the announcement.\n__**Requirements:**__\n1) An *Announcement Command Channel*\n2) At least one *Announcement Channel* set for the bot.\n\nFirst execute the command written below in *Announcement Command Channel*. Then send your announcement in that same channel. You can also set a timer for when you want the bot to announce your announcement.\n__Example:__\nType `1s` at the place of `(time)` in order to announce after 1 second. In the same way, `1m` for after 1 minute, `1h` for after 1 hour.\n__**Command:**__ `.o announce [channel] (time)`\n឵឵",
								  inline=False)
				su_embed.add_field(name = ":crossed_swords: KICK",
								  value = ":small_orange_diamond: This command is used for kicking someone out of the server.\n__**Command:**__ `.o kick [member]`\n឵឵",
								  inline=False)
				su_embed.add_field(name = ":crossed_swords: BAN",
								  value = ":small_orange_diamond: This command is used for banning someone from the server.\n__**Command:**__ `.o ban [member]`\n឵឵")
				su_embed.add_field(name = ":crossed_swords: UNBAN",
								  value = ":small_orange_diamond: This command is used for unbanning someone.\n__**Command:**__ `.o unban [member]`\n឵឵")
				su_embed.add_field(name = ":crossed_swords: PURGE",
								  value = ":small_orange_diamond: This command is used for deleting messages of current channel.\n__**Command:**__ `.o purge [number of messages]`",
								  inline = False)
				su_embed.set_footer(icon_url=ctx.author.avatar_url,text=f"Requested by {ctx.author.name}")
				await ctx.send(embed= su_embed)
		except:
			su_embed = discord.Embed(title="= = = = = = |:card_box:Server Utilities :card_box:| = = = = =",description="Aliases = `su`,`server utility`,`server utilities`\nFor more info: `.o help`\n\n__**:warning:Disclaimer:warning:**__\n:white_small_square: The `[` and `]` around the argument mean it’s required.\n:white_small_square: The `(` and `)` around the argument mean it’s optional.\n-   -   -   -   -   -   -   -   -   -   -   -   -   -   -   -   -   -   -   -\n")
			
			su_embed.add_field(name="= = __:link:ACTIVATION / DEACTIVATION:link:__ = =",
								 value="- - - - - - - - - :arrow_down: - -  :arrow_down: - -  :arrow_down: - -  :arrow_down: - - - - - - - - -\n:white_small_square: **Activation/Deactivation** commands are the most important commands in order to use all features properly.",
								 inline=False)
			su_embed.add_field(name=":large_blue_diamond: Activation",
								 value=":small_blue_diamond: Thre are so many features in this bot which requires a specific channel for each where the features can Better used. Such as, a specific channel for **TicTacToe** game or **Battleship** game, one or two specific **Announcement** channel and a specific Announcement Command channel where you will tell the bot in which channel to announce. Here you will find all activation commands.\n**__Command:__** `.o help activate`\n឵឵",
								 inline=False)
			su_embed.add_field(name=":large_orange_diamond: Deactivation",
								 value=":small_orange_diamond: Sometimes you might need to deactivate a feature from a channel or change the channel. Here you will find all deactivation/update commands. \n**__Command:__** `.o help deactivate`\n- - - - - - - - - - - - - - - - - - - -",
								 inline=False)
			su_embed.add_field(name=" ឵឵ ",value=" ឵឵ ",inline=False)
			su_embed.add_field(name=":diamond_shape_with_a_dot_inside: ANNOUNCE",
							  value=":small_blue_diamond: You can announce announce with your bot now. You can also attach file with the announcement.\n__**Requirements:**__\n1) An *Announcement Command Channel*\n2) At least one *Announcement Channel* set for the bot.\n\nFirst execute the command written below in *Announcement Command Channel*. Then send your announcement in that same channel. You can also set a timer for when you want the bot to announce your announcement.\n__Example:__\nType `1s` at the place of `(time)` in order to announce after 1 second. In the same way, `1m` for after 1 minute, `1h` for after 1 hour.\n__**Command:**__ `.o announce [channel] (time)`\n឵឵",
							  inline=False)
			su_embed.add_field(name = ":crossed_swords: KICK",
							  value = ":small_orange_diamond: This command is used for kicking an account out of the server.\n__**Command:**__ `.o kick [member]`\n឵឵",
							  inline=False)
			su_embed.add_field(name = ":crossed_swords: BAN",
							  value = ":small_orange_diamond: This command is used for banning an account from the server.\n__**Command:**__ `.o ban [member]`\n឵឵")
			su_embed.add_field(name = ":crossed_swords: UNBAN",
							  value = ":small_orange_diamond: This command is used for unbanning an account.\n__**Command:**__ `.o unban [member]`\n឵឵")
			su_embed.add_field(name = ":crossed_swords: PURGE",
							  value = ":small_orange_diamond: This command is used for deleting messages of current channel.\n__**Command:**__ `.o purge [number of messages]`\n឵឵",
							  inline = False)
			su_embed.add_field(name = ":crossed_swords: CHANGE NICKNAME",
							   value = ":small_orange_diamond: This command is used to change nickname of a specific account.\n__**Command:**__ `.o chnick [user] [nickname]`\n឵឵",
							   inline = False)
			su_embed.set_footer(icon_url=ctx.author.avatar_url,text=f"Requested by {ctx.author.name}")
			await ctx.send(embed= su_embed)

	@help.command(aliases = ["utility","u"])
	async def utilities(self,ctx):
		u_embed = discord.Embed(title="= = = = = = |:card_box:Server Utilities :card_box:| = = = = =",description="Aliases = `u`,`utility`,`utilities`\nFor more info: `.o help`\n\n__**:warning:Disclaimer:warning:**__\n:white_small_square: The `[` and `]` around the argument mean it’s required.\n:white_small_square: The `(` and `)` around the argument mean it’s optional.\n-   -   -   -   -   -   -   -   -   -   -   -   -   -   -   -   -   -   -   -\n")
		
		u_embed.add_field(name=":large_blue_diamond: AVATAR",
						  value = ":small_blue_diamond: This command is used for seeing avatar of your account's or a specific account's.\n__**Command:**__ `.o avatar (member)` or `.o av (member)`\n឵឵",
						  inline = False)
		u_embed.add_field(name=":large_blue_diamond: USER INFO",
						   value= ":small_blue_diamond: This command is used for getting user info of your account's or a specific account's.\n__**Command:**__ `.o userinfo (member)`",
						   inline = False)
		u_embed.set_footer(icon_url=ctx.author.avatar_url,text=f"Requested by {ctx.author.name}")
		await ctx.send(embed= u_embed)


	@help.command(aliases=['philosophy','wiki','wikipedia'])
	async def philo(self,ctx):
		ph_embed = discord.Embed(title="= = = = = = |:card_box: Philosophy :card_box:| = = = = =",description="Aliases = `philo`\nFor more info: `.o help`\n\n__**:warning:Disclaimer:warning:**__\n:white_small_square: The `[` and `]` around the argument mean it’s required.\n:white_small_square: The `(` and `)` around the argument mean it’s optional.\n-   -   -   -   -   -   -   -   -   -   -   -   -   -   -   -   -   -   -   -\n")
	
		ph_embed.add_field(name=":notebook: WIKIPEDIA",value="Using Wikipedia command you can search for any thing's summary on Wikipedia.\n__**Command:**__ `.o wiki [subject]`",
							inline=False)
		ph_embed.set_footer(icon_url=ctx.author.avatar_url,text=f"Requested by {ctx.author.name}")
		await ctx.send(embed = ph_embed)

def setup(client):
	client.add_cog(H_1(client))