import aiohttp
import asyncio
import discord
import io
import os
import random
import sys
import traceback
from discord.ext import commands

token = 'lol no token 4 you'

cogs = [
    'cogs.general',
    'cogs.moderation',
    'cogs.jokes'
]

bot = commands.Bot(command_prefix='::', case_insensitive=True, help_command=None)


@bot.event
async def on_ready():
    activity = discord.Activity(name='over the Cave and its people.', type=discord.ActivityType.watching)
    print(f"Activated {bot.user}")
    await bot.change_presence(activity=activity)


@bot.command()
async def load(ctx, extension):
    try:
        bot.load_extension(f'cogs.{extension}')
        await ctx.send(f'Successfully loaded {extension}')
    except Exception as e:
        return await ctx.send(e)


@bot.event
async def on_member_remove(member):
    channel = bot.get_channel(689959642947780733)
    await channel.send(f'{member.mention} has ascended back to the surface')


@bot.command(aliases=['help'])
async def commands(ctx):
    embed = discord.Embed(
        title='The abilities of Jarvis the Bot',
        description='What Jarvis can do. Commands have "::" before them')
    embed.set_thumbnail(url='https://mir-s3-cdn-cf.behance.net/project_modules/disp/1d3a9615488433.56291d6a72211.jpg')
    embed.add_field(name="jokes", value="The witty humor Jarvis can give")
    embed.add_field(name="rules", value="The strict rules Jarvis will enforce")
    embed.add_field(name='other', value='The side commands Jarvis has been equipped with')
    await ctx.channel.send(embed=embed)


@bot.command()
async def createrole(ctx, name):
    await ctx.guild.create_role(name=name)
    await ctx.send(f'The {name} role has been created')


@bot.command()
async def deleterole(ctx, role: discord.Role):
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


@bot.command()
async def jokes(ctx):
    await ctx.send('I can do Jojokes, sassy replies and many others. Just ask away')


@bot.command()
async def others(ctx):
    await ctx.send('I can show you how the server works and even about '
                   'a certain......special channel we have on here')


@bot.command()
async def changenick(ctx, user: discord.Member, *, nick):
    await user.edit(nick=nick)


@bot.command()
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


@bot.command()
async def regret(ctx):
    with open('blackalabi.png', 'rb') as fp:
        await ctx.send(file=discord.File(fp, 'blackalabi.png'))


@bot.command()
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


@bot.command()
async def rule1(ctx):
    await ctx.send(
        "Rule 1: Be civil. A chat server relies on civilness, "
        "so fights are nothing good, both for spectators and for the admins.")


@bot.command()
async def unload(ctx, extension):
    try:
        bot.unload_extension(f'cogs.{extension}')
        await ctx.send(f'Successfully unloaded {extension}')
    except Exception as e:
        return await ctx.send(e)


@unload.error
async def unload_error(ctx, error):
    if isinstance(error, commands.MissingPermissions):
        await ctx.send('You dont have the power unload my specs (cogs) yet.')


@bot.command()
async def reload(ctx, extension):
    try:
        bot.reload_extension(f'cogs.{extension}')
        await ctx.send(f'Successfully reloaded {extension}')
    except Exception as e:
        return await ctx.send(e)


for cog in cogs:
    bot.load_extension(cog)

bot.run(token)
