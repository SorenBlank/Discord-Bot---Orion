import discord
from discord.ext import commands
import sqlite3
import pymongo
from pymongo import MongoClient

cluster = MongoClient("mongodb+srv://soren:cdD2_qWUYRk-d4G@orion.iztml.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
base = cluster["OrionDB"]

m1_cur = base["m1guilds"]


class M1(commands.Cog):

    def __init__(self, client):
        self.client = client
    
    @commands.Cog.listener()
    async def on_ready(self):
        print("M1 is Loaded ----")

    @commands.command()
    async def purge(self, ctx, number = 2, channel:discord.TextChannel=None):
        raw = m1_cur.find({})
        guilds = []
        try:
            x = [i for i in raw]
            guilds = [x[i]["guild"] for i in range(len(x))]
        except:
            pass

        if ctx.author.guild_permissions.administrator:
            if ctx.guild.id in guilds:
                if channel == None:
                    await ctx.channel.purge(limit = int(number)+1)

                if channel != None:
                    await channel.purge(limit= int(number) +1)
        else:
            await ctx.send("Access denied")


    #kick_command
    @commands.command()
    async def kick(self, ctx, member: discord.Member, reason = None):
        raw = m1_cur.find({})
        guilds = []
        channels = []
        try:
            x = [i for i in raw]
            guilds = [x[i]["guild"] for i in range(len(x))]
        except:
            pass
        

        if ctx.author.guild_permissions.kick_members:
            if ctx.guild.id in guilds:
                try:
                    await member.kick(reason=reason)
                    await ctx.send(f'{member.mention} is kicked')
                except:
                    await ctx.send(f"I dont have the power to kick {member.mention}")
        else:
            await ctx.send("You are not a valid user.")
    
    #ban_command
    @commands.command()
    async def ban(self, ctx, member: discord.Member, reason = None):
        raw = m1_cur.find({})
        guilds = []
        try:
            x = [i for i in raw]
            guilds = [x[i]["guild"] for i in range(len(x))]
        except:
            pass
        
        if ctx.author.guild_permissions.ban_members:
            if ctx.guild.id in guilds:
                await member.ban(reason=reason)
                if reason == None:
                    await ctx.send(f'{member.mention} has been banned by {ctx.author.mention}')
                else:
                    await ctx.send(f'{member.mention} has been banned by {ctx.author.mention}. Reason: {reason}')
            else:
                await ctx.send("M1 is deactivate")
        else:
            await ctx.channel.send("You are not a valid user.")
    
    #unban_command
    @commands.command()
    async def unban(self, ctx, *, member):
        raw = m1_cur.find({})
        guilds = []
        try:
            x = [i for i in raw]
            guilds = [x[i]["guild"] for i in range(len(x))]
        except:
            pass
        
        banned_entries = await ctx.guild.bans()
        member_name, member_tag = member.split("#")

        if ctx.author.guild_permissions.ban_members:
            if ctx.guild.id in guilds:
                for i in banned_entries:
                    user = i.user
                    if (user.name, user.discriminator) == (member_name,member_tag):
                        await ctx.guild.unban(user)
                        await ctx.send(f'User: {user.mention} is unbanned now.')
                        return
            else:
                ctx.send("M1 is deactivate.")
        else:
            await ctx.send("You are not a valid user of this command.")

    @commands.command()
    async def purge(self,ctx,number=None):
        if ctx.author.guild_permissions.manage_messages:
            if number != None:
                if number.isdigit():
                    await ctx.channel.purge(limit=int(number)+1)
            if number == None:
                await ctx.channel.purge(limit=2)
        else:
            await ctx.send("**Access Denied!** \nThis command requires `manage_messages` permission in order to execute.")

    @commands.command()
    async def chnick(self,ctx,member:discord.Member, nick):

        if ctx.author.guild_permissions.change_nickname:
            try:
                await member.edit(nick=nick)
                await ctx.send(f'Nickname was changed for {member.mention} ')
            except:
                await ctx.send(f"Access Denied!")


def setup(client):
    client.add_cog(M1(client))