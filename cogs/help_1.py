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

        help_embed = discord.Embed(color = 0x714ec4)
        avi = self.client.user.avatar_url_as(static_format='png')
        help_embed.set_author(name = "HELP COMMANDS",icon_url = avi)
        help_embed.set_thumbnail(url= avi)
        
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
                             value = "**[Invite link](https://discord.com/api/oauth2/authorize?client_id=777095257262522399&permissions=3691506935&scope=bot) | [Official server](https://discord.gg/JJtUtgMjBv) | [Vote](https://top.gg/bot/777095257262522399/vote/)**",
                             inline = False)
        
        await ctx.send(embed = help_embed)

    @help.command(aliases=["games","g","tictactoe","tic","tac","fibo","Fibonacci"])
    async def game(self,ctx):
        game_embed = discord.Embed(color = 0x714ec4)
        game_embed.set_author(name = "GAME COMMANDS",icon_url = self.client.user.avatar_url)
        game_embed.add_field(name=':1234: Countup',
                             value="`.o set countup (channel)`")
                             
        game_embed.add_field(name=':1234: Fibonacci Countup',
                             value="`.o set fibo (channel)`")
        
        game_embed.add_field(name=":o: TicTacToe",
                             value="`.o tic [player]`")
        game_embed.add_field(name=":ship: Battleship",
                             value="`.o bs [player]`", inline= False)

        game_embed.add_field(name = "-\nIGNS", value = "`.o ign (member)`",inline= True)
        game_embed.add_field(name = "-\nCHESS PROFILE", value = "`.o profile chess (member)`",inline= True)
        game_embed.add_field(name = "-\nLINK", value = "Your IGN will be shown on your userinfo.",inline= False)
        game_embed.add_field(name = "<:valorant:814455293328228394> - valorant",value = "`.o link val [username]`",inline=True)
        game_embed.add_field(name = "<:chess:830030544661119056> - chess.com",value = "`.o link chess [username]`",inline=True)
        game_embed.set_footer(text= "Pro tip: The ( and ) around the argument mean it’s optional.", icon_url= ctx.author.avatar_url)

        await ctx.send(embed = game_embed)

    @help.command(aliases = ["initiate","start","set","setup","activation"])
    async def Activate(self,ctx):
        activator_embed = discord.Embed(color = 0x714ec4)
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
        deactivator_embed = discord.Embed(color = 0x714ec4,description = ":one: `.o deactivate countup`\nThis command removes **Countup Channel**.\n\n :two: `.o deactivate fibo`\nThis command removes **Fibonacci Channel**.\n\n:three: `.o deactivate tictactoe`\nThis command removes **TicTacToe Channel**.\n\n:four: `.o deactivate battleship`\nThis command removes **Battleship Channel**.\n\n:five: `.o deactivate welcome`\nThis command removes  **Welcome Channel**.\n\n:six: `.o deactivate bye`\nThis command removes  **Bye Channel**.")
        deactivator_embed.set_author(name = "DEACTIVATE COMMANDS", icon_url= self.client.user.avatar_url)
        await ctx.send(embed = deactivator_embed)

    @help.command(aliases=["su","server","announce","announcement"])
    async def server_utilities(self,ctx,msg = None):
        try:
            if msg.lower() == "utility" or msg.lower() == "utilities" or msg.lower() == "u":
                su_embed = discord.Embed(color = 0x714ec4,description = "Use the command `.o help <option>` to view more info.")
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
            su_embed = discord.Embed(color = 0x714ec4,description = "Use the command `.o help <option>` to view more info.")
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
        u_embed = discord.Embed(color = 0x714ec4)
        u_embed.set_author(name = "UTILITY COMMANDS",icon_url = self.client.user.avatar_url)
        u_embed.add_field(name=":frame_photo: Avatar",
                          value = "`.o av (member)`")
        u_embed.add_field(name=":card_index: User Info",
                           value= "`.o userinfo (member)`")
        u_embed.add_field(name = ":card_index: Server Info",
                           value = "`.o serverinfo`")
        u_embed.add_field(name = ":card_index: In Game Name", value = "`.o ign (member)`")
        u_embed.add_field(name = "-\n:link: LINK", value = "Your IGN will be shown on your userinfo.",inline= False)
        u_embed.add_field(name = "<:valorant:814455293328228394> - valorant",value = "`.o link val [username]`",inline=True)
        u_embed.add_field(name = "<:chess:830030544661119056> - chess.com",value = "`.o link chess [username]`")
        u_embed.set_footer(text= "Pro tip: The ( and ) around the argument mean it’s optional.", icon_url= ctx.author.avatar_url)
        await ctx.send(embed= u_embed)


    @help.command(aliases=['activity','wiki','wikipedia','act'])
    async def activities(self,ctx):
        act_embed = discord.Embed(color = 0x714ec4)
        act_embed.set_author(name = "ACTIVITY COMMANDS",icon_url = self.client.user.avatar_url)
        act_embed.add_field(name=":mag: SEARCH",value="Use the command `.o <platform> <search>` to search.", inline= False)
        act_embed.add_field(name = "<:google:829098461306683443> Google", value = "`.o google [search]`")
        act_embed.add_field(name = "<:youtube:829099216944758857> YouTube", value = "`.o youtube [search]`")
        act_embed.add_field(name = ":notebook: Wikipedia",value = "`.o wiki [search]`")
        act_embed.add_field(name = ":flag_jp: Anime", value = "`.o anime [search]`")
        act_embed.add_field(name = ":flag_jp: Manga", value = "`.o manga [search]`")
        act_embed.add_field(name = " ឵឵ \n😆 FUN",
                      value = "`kiss` `hug` `cry` `pat` `tickle` `lick`",
                      inline= False)
        act_embed.add_field(name = " ឵឵ \n📚 RESOURCES",
                      value = "Use the command `.o re` or `.o re <option>` for resources.\n`programming` `python` `webdev` `androiddev` `iosdev` `ml` `linux`",
                      inline= False)
        await ctx.send(embed = act_embed)

def setup(client):
    client.add_cog(H_1(client))