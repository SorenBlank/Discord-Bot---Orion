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
import urllib

class H_1(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print("H1 is Loaded ----")

    @commands.group(invoke_without_command = True,case_insensitive=True,aliases = ["h"])
    async def help(self,ctx):

        help_embed = discord.Embed()
        help_embed.set_author(name = "HELP COMMANDS",icon_url = self.client.user.avatar_url)
        help_embed.set_thumbnail(url= self.client.user.avatar_url)
        
        help_embed.add_field(name="Server Utilities",
                             value="```\n.o help server utility```",
                             inline = True)

        help_embed.add_field(name="Utilities",
                             value="```\n.o help utility```",
                             inline=False)

        help_embed.add_field(name="Games",
                             value="```\n.o help game```",
                             inline=True)

        help_embed.add_field(name="Activities",
                             value="```\n.o help activity```",
                             inline= True)

        help_embed.add_field(name = "Links",
                             value = "**[Invite link](https://discord.com/api/oauth2/authorize?client_id=777095257262522399&permissions=8&scope=bot) | [Official server](https://discord.gg/JJtUtgMjBv) | [Vote](https://top.gg/bot/777095257262522399/vote/)**",
                             inline = False)
        
        await ctx.send(embed = help_embed)

    @help.command(aliases=["games","g","tictactoe","tic","tac","fibo","Fibonacci"])
    async def game(self,ctx):
        game_embed = discord.Embed()
        game_embed.set_author(name = "GAME COMMANDS",icon_url = self.client.user.avatar_url)
        game_embed.add_field(name=':1234: Fibonacci Countup',
                             value="`.o set fibo (channel)`")
        game_embed.add_field(name=":o: TicTacToe",
                             value="`.o tic [player]`")
        game_embed.add_field(name=":ship: Battleship",
                             value="`.o bs [player]`")

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

    @help.command(aliases = ["initiate","start","set","setup","activation"])
    async def Activate(self,ctx):
        activator_embed = discord.Embed()
        activator_embed.set_author(name = "ACTIVATE COMMANDS", icon_url=self.client.user.avatar_url)

        #SECOND FIELD
        activator_embed.add_field(name=":card_box:SERVER UTILITIES:card_box:",
                                  value = "Use the command `!set [option] (channel)` to set channels.",
                                  inline= False)


        activator_embed.add_field(name = ":hammer_pick: Welcome/Bye Message",
                                  value = "```py\n.o set welcome [channel] [message] \n# to set a greeting channel & message\n\n.o set bye [channel] [message] \n# to set a farewell channel & message```Use `#member` keyword to mention the member.\n\n ឵឵ ",
                                  inline = False)

        #THIRD FIELD
        activator_embed.add_field(name=":video_game:GAMES:video_game:",
                                  value="Use the command `!set [option] (channel)` to set channels for games.",
                                  inline=False)
        activator_embed.add_field(name=":1234: Fibonacci Countup",
                                  value="`.o set fibo (channel)`")
        activator_embed.add_field(name=":bangbang:  TicTacToe",
                                  value="`.o set tic (channel)`")
        activator_embed.add_field(name=":ship: Battleship (BETA)",
                                  value='`.o set bs (channel)`')

        activator_embed.set_footer(icon_url=ctx.author.avatar_url,text="Pro tip: The ( and ) around the argument mean it’s optional.")

        await ctx.send(embed = activator_embed)

    @help.command(aliases = ["stop","eliminate","remove","deactivation"])
    async def Deactivate(self,ctx):
        deactivator_embed = discord.Embed(description = ":one: `.o deactivate fibo`\nThis command removes **Fibonacci Channel**.\n\n:two: `.o deactivate tictactoe`\nThis command removes **TicTacToe Channel**.\n\n:three: `.o deactivate battleship`\nThis command removes **Battleship Channel**.\n\n:nine: `.o deactivate welcome`\nThis command removes  **Welcome Channel**.\n\n:keycap_ten: `.o deactivate bye`\nThis command removes  **Bye Channel**.")
        deactivator_embed.set_author(name = "DEACTIVATE COMMANDS", icon_url= self.client.user.avatar_url)
        await ctx.send(embed = deactivator_embed)

    @help.command(aliases=["su","server","announce","announcement"])
    async def server_utilities(self,ctx,msg = None):
        try:
            if msg.lower() == "utility" or msg.lower() == "utilities" or msg.lower() == "u":
                su_embed = discord.Embed(description = "Use the command `.o help <option>` to view more info.")
                su_embed.set_author(name = "SERVER UTILITY COMMANDS",icon_url = self.client.user.avatar_url)
                su_embed.add_field(name=":white_check_mark: Activation",
                                     value="`.o help activate`",
                                     inline=True)
                su_embed.add_field(name=":negative_squared_cross_mark: Deactivation",
                                     value="`.o help deactivate`",
                                     inline=True)
                su_embed.add_field(name="-\n:bell: Announce",
                                  value="`.o announce [channel] (time)`\nTime Plugin Example: `1s`, `1m`, `1h`\n**-**",
                                  inline=False)
                su_embed.add_field(name = ":crossed_swords: Kick",
                                    value = "`.o kick [member]`")
                su_embed.add_field(name = ":crossed_swords: Ban",
                                    value = "`.o ban [member]`")
            
                su_embed.add_field(name = ":crossed_swords: Unban",
                                    value = "`.o unban [member]`")
                su_embed.add_field(name = ":crossed_swords: Purge",
                                    value = "`.o purge [number]`឵឵")
                su_embed.add_field(name = ":crossed_swords: Change Nickname",
                                value = "`.o chnick [user] [nickname]`")
                su_embed.set_footer(text= "Pro tip: The ( and ) around the argument mean it’s optional.", icon_url= ctx.author.avatar_url)

                await ctx.send(embed= su_embed)
        except:
            su_embed = discord.Embed(description = "Use the command `.o help <option>` to view more info.")
            su_embed.set_author(name = "SERVER UTILITY COMMANDS",icon_url = self.client.user.avatar_url)
            su_embed.add_field(name=":white_check_mark: Activation",
                                    value="`.o help activate`",
                                    inline=True)
            su_embed.add_field(name=":negative_squared_cross_mark: Deactivation",
                                    value="`.o help deactivate`",
                                    inline=True)
            su_embed.add_field(name="-\n:bell: Announce",
                                value="```\n.o announce [channel] (time)```Time Plugin Example: `1s`, `1m`, `1h`\n**-**",
                                inline=False)
            su_embed.add_field(name = ":crossed_swords: Kick",
                                value = "`.o kick [member]`")
            su_embed.add_field(name = ":crossed_swords: Ban",
                                value = "`.o ban [member]`")
        
            su_embed.add_field(name = ":crossed_swords: Unban",
                                value = "`.o unban [member]`")
            su_embed.add_field(name = ":crossed_swords: Purge",
                                value = "`.o purge [number]`឵឵")
            su_embed.add_field(name = ":crossed_swords: Change Nickname",
                            value = "`.o chnick [user] [nickname]`")
            su_embed.set_footer(text= "Pro tip: The ( and ) around the argument mean it’s optional.", icon_url= ctx.author.avatar_url)

            await ctx.send(embed= su_embed)

    @help.command(aliases = ["utility","u"])
    async def utilities(self,ctx):
        u_embed = discord.Embed()
        u_embed.set_author(name = "UTILITY COMMANDS",icon_url = self.client.user.avatar_url)
        u_embed.add_field(name=":frame_photo: Avatar",
                          value = "`.o av (member)`")
        u_embed.add_field(name=":card_index: User Info",
                           value= "`.o userinfo (member)`")
        u_embed.set_footer(text= "Pro tip: The ( and ) around the argument mean it’s optional.", icon_url= ctx.author.avatar_url)
        await ctx.send(embed= u_embed)


    @help.command(aliases=['activity','wiki','wikipedia','act'])
    async def activities(self,ctx):
        ph_embed = discord.Embed()
        ph_embed.set_author(name = "ACTIVITY COMMANDS",icon_url = self.client.user.avatar_url)
        ph_embed.add_field(name=":mag: SEARCH",value="Use the command `.o <platform> <search>` to search.", inline= False)
        ph_embed.add_field(name = ":notebook: Wikipedia",value = "`.o wiki [search]`")
        ph_embed.add_field(name = ":flag_jp: Anime", value = "`.o anime [search]`")
        ph_embed.add_field(name = ":flag_jp: Manga", value = "`.o manga [search]`")
        ph_embed.add_field(name = "<:google:829098461306683443> Google", value = "`.o google [search]`")
        ph_embed.add_field(name = "<:youtube:829099216944758857> YouTube", value = "`.o youtube [search]`")
        ph_embed.add_field(name = " ឵឵ \n📚 RESOURCES",
                      value = "Use the command `.o re <option>` to view all resource.",
                      inline= False)
        ph_embed.add_field(name = "<:python:814811189241970718> Python ",
                     value= "`.o re python`")
        ph_embed.add_field(name = "<:html:815225352958771210> Web Dev",
                     value = "`.o re web`")
        ph_embed.add_field(name = ":gear: Machine Learning",
                     value = "`.o re ml`")
        ph_embed.add_field(name = "<:android:814849449570205736> Android Dev",
                     value = "`.o re android`")

        ph_embed.add_field(name = "<:iOS:814846523128676372> iOS Dev",
                     value = "`.o re ios`")

        ph_embed.add_field(name = ":keyboard: Programming",
                     value = "`.o re programming`")

        ph_embed.add_field(name = "<:linux:814863906756624384> Linux Guide",
                     value = "`.o re linux`")
        await ctx.send(embed = ph_embed)

def setup(client):
    client.add_cog(H_1(client))