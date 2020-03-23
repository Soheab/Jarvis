import discord
import os
from discord.ext import commands
import random
import asyncio
import io
import aiohttp
import sys, traceback

token = 'Njc4MzM3NTc2MjY4MDcwOTQy.XnannA.HupUzvELh1qsawAg_2OsjprFmzo' 

cogs_list = ['cogs.general',
             'cogs.moderation',
             'cogs.jokes']

client = commands.Bot(command_prefix='::', case_insensitive=True)

@client.remove_command('help')

@client.command()
async def load(ctx, extension):
    client.load_extension(f'cogs.{extension}')
    await ctx.send('Spec sucessfully loaded')

@client.event
async def on_ready():
    activity = discord.Activity(name='over the Cave and its people.', type=discord.ActivityType.watching)
    print(f"Activated {client.user}")
    await client.change_presence(activity=activity)

@client.event
async def on_member_remove(member):
    channel = client.get_channel(689959642947780733)
    await channel.send(f'{member.mention} has ascended back to the surface')

@client.command(aliases=['help'])
async def commands(ctx):
    embed = discord.Embed(title='The abilities of Jarvis the Bot', description='What Jarvis can do. Commands have "::" before them')
    embed.set_thumbnail(url='https://mir-s3-cdn-cf.behance.net/project_modules/disp/1d3a9615488433.56291d6a72211.jpg')
    embed.add_field(name="jokes", value="The witty humor Jarvis can give")        
    embed.add_field(name="rules", value="The strict rules Jarvis will enforce")
    embed.add_field(name='other', value='The side commands Jarvis has been equipped with')        
    await ctx.channel.send(content=None, embed=embed)

@client.command()
async def createrole(ctx, arg1, name=None):
    guild = ctx.guild
    await guild.create_role(name=name)
    await ctx.send('The {} role has been created'.format(arg1))

@client.command()
async def deleterole(ctx, role: discord.Role):
    guild = ctx.guild
    await role.delete()
    await ctx.send(f'The {role.name} role has been deleted')

@createrole.error
async def role_error(ctx, error):
    if isinstance(error, commands.MissingPermissions):
        await ctx.send('You cannot create a role yet.')

@deleterole.error
async def role_error(ctx, error):
    if isinstance(error, commands.MissingPermissions):
        await ctx.send('You cannot delete a role yet.')

@client.command()
async def jokes(ctx):
    await ctx.send('I can do Jojokes, sassy replies and many others. Just ask away')

@client.command()
async def others(ctx):
    await ctx.send('I can show you how the server works and even about a certain......special channel we have on here')

@client.command()
async def changenick(ctx, user: discord.Member, *, nick):
    await user.edit(nick=nick)

@client.command()
async def floor6(ctx):
    user = ctx.message.author
    floor6 = ctx.message
    await floor6.delete()
    await user.send("How.....")
    await asyncio.sleep(6)
    await user.send('How do you know about floor 6?')
    await asyncio.sleep(4)
    await user.send('I....I purged it long ago....')
    await asyncio.sleep(3)
    await user.send('Could it be that its power is too strong to erase?')
    await asyncio.sleep(2)
    await user.send('No....only those with the admin role could know about floor 6')
    await asyncio.sleep(5)
    await user.send('The fact that you know makes you a powerful cave being....')
    await asyncio.sleep(6)
    await user.send('Alright, I will tell you about Floor 6: The Floor Which Refused') 
    await asyncio.sleep(1)
    await user.send('Use ;;continue if you want to know more')

@client.command()
async def regret(ctx):
    with open('blackalabi.png', 'rb') as fp:
        await ctx.send(file=discord.File(fp, 'blackalabi.png'))

@client.command()
async def killerqueen(ctx, amount=50):
    with open('rewindtime.gif', 'rb') as fp:
        andanotheronedown = await ctx.send(file=discord.File(fp, 'rewindtime.gif'))
        await asyncio.sleep(1.5)
        await ctx.channel.purge(before=andanotheronedown, limit=amount)
        await asyncio.sleep(1.5)
        bitesthedust = await ctx.send('Shit, I need to undo Bites the Dust now.')
        await asyncio.sleep(4)
        anotherone = await ctx.send('Return, Killer Queen!')
        await asyncio.sleep(2)
        await anotherone.delete()
        await bitesthedust.delete()
        await andanotheronedown.delete()

@client.command()
async def rule1(ctx):
    await ctx.send("Rule 1: Be civil. A chat server relies on civilness, so fights are nothing good, both for spectators and for the admins.")

@client.command()
async def unload(ctx, extension):
    client.unload_extension(f'cogs.{extension}')
    await ctx.send('Specs successfully unloaded')

@unload.error
async def unload_error(ctx, error):
    if isinstance(error, commands.MissingPermissions):
        await ctx.send('You dont have the power unload my specs (cogs) yet.')

@client.command()
async def reload(ctx, extension):
    client.reload_extension(f'cogs.{extension}')
    await ctx.send('Spec has been updated')

for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        client.load_extension(f'cogs.{filename[:-3]}')

client.run(token, bot=True, reconnect=True)