import discord
from discord.ext import commands
import os
import random
import sys, traceback

class ModerationCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.Cog.listener()
    async def on_ready(self):
        print('The Moderation Specs for Jarvis is online')

    @commands.command()
    @commands.has_permissions(ban_members=True, kick_members=True)
    async def kick(self, ctx, member : discord.Member, *, reason=None, cog: str):
        await member.kick(reason=reason)
        await ctx.send('Failed to kick user')
        await ctx.send(f'{member} has been kicked and forced ejected back to the surface. Reason: {reason}')

    @kick.error
    async def kick_error(self, ctx, error):
        if isinstance(error, commands.BadArgument):
            await ctx.send('Failed to kick user. Make sure you mention them')

    @kick.error
    async def kick_error2(self, ctx, error):
        if isinstance(error, commands.MissingPermissions):
            await ctx.send('You do not have the power to ban users')

    @commands.command()
    @commands.has_permissions(ban_members=True, kick_members=True)
    async def ban(self, ctx, member : discord.Member, *, reason=None):    
        await member.send(f'You have been banned from ever returning to the Cave. Reason: {reason}. Maybe, just maybe, you can return at a later date.')
        await member.ban(reason=reason)
        await ctx.send(f'{member} has been banned from ever coming down to the Cave. Reason: {reason}')

    @ban.error
    async def ban_error(self, ctx, error):
        if isinstance(error, commands.BadArgument):
            await ctx.send('Failed to ban user')    

    @commands.command()
    @commands.has_permissions(ban_members=True, kick_members=True) 
    async def unban(self, ctx, *, member):
        banned_users = await ctx.guild.bans()
        member_name, member_discriminator = member.split('#')
        for ban_entry in banned_users:
            user = ban_entry.user
            if (user.name, user.discriminator) == (member_name, member_discriminator):
                await ctx.guild.unban(user)
                await ctx.send(f'{user.mention} has been allowed to come back to the Cave.')
                return
    
    @unban.error
    async def unban_error(self, ctx, error):
        await ctx.send(f'There was an error in your unbanning. Remember to use # to seperate the user and discriminator like so: user#discriminator.')

def setup(bot):
    bot.add_cog(ModerationCog(bot))