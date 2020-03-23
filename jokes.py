import discord
from discord.ext import commands
import os
import random
import sys, traceback

class ComedicCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        
    @commands.Cog.listener()
    async def on_ready(self):
        print('The Comedic Specs for Jarvis is online')
    
    @commands.command()
    async def legocity(self, ctx, arg1, arg2):
        await ctx.send('{} has fallen into {} in Lego City! **Hey!**'.format(arg1, arg2))

    @commands.command()
    async def jojoke(self, ctx):
        responses = ['You fool, you fell for it! THUNDER CROSS SPLIT ATTACK!',
                 "I don't know, how many loaves of bread ave you eaten in your entire life?", 
                 "NIGERUNDAYO!!!",
                 "Yare yare daze...",
                 "20 Meter Radius Emerald Splash!",
                 "No one can just deflect the Emerald Splash!",
                 "Za Warudo!",
                 "Road rolla da!", 
                 "What did you say about my hair?!?1!1?", 
                 "Bites Za Dusto!",
                 "I just want to live a quiet life.",
                 "I, Jarvis the Bot, have a dream!",
                 "*7 Page Muda intensifies*",
                 "All that remains in this world are the results.",
                 "Wha- Wha- Wha- Wha- Wha- Wha- Wha- Wha- Wha- Wha-"]
        await ctx.send(f"{random.choice(responses)}")

    @commands.command()
    @commands.is_nsfw()
    async def sending(self, ctx):
        channel = self.bot.get_channel(381963689470984203)
        await ctx.channel.send('please kids, when you are giving a hand job to george clooney, remember to stick you finger in his mouth. that gets him hard instantly')
    
    @commands.command()
    async def emote(self, ctx):
        emotes = ['\U0001f595',
                  '\U0001f914',
                  '\U00002b50',
                  '\U0001f4a9']
        await ctx.send(f'{random.choice(emotes)}')

    @commands.command()
    async def dongsize(self, ctx, member=None):
        sizes = ['8D',
                 '8=D',
                 '8==D',
                 '8===D',
                 '8====D',
                 '8=====D',
                 '8======D',
                 '\U0001f90f \U0001f346',
                 '8=======D',
                 '8========D',
                 '8=========D',
                 '8==========D',
                 '8===========D',
                 '8============D',
                 '8=============D',
                 '8==============D',
                 '8===============D',
                 '8================D',
                 '8=================D']           
        if member is None:
            member = ctx.author
        await ctx.send(f'\U0001f346 {member} has this dong size: {random.choice(sizes)}')
    
    @commands.command(name='EightBall', aliases=['8ball'])
    async def eightball(self, ctx, *, question):
        responses = ['It is certain.',
                 'Definetly',
                 "Yeah, it's gonna happen",
                 "Don't try to do it",
                 "You better watch out",
                 "U w0t.",
                 "I don't have an answer right now.",
                 "You have a better chance of success than I do.",
                 "That's gonna be a no from me, dawg.",
                 "You're future looks dimmer than a basement light.",
                 "You are going to succeed. And by that I mean your level of success will be equal to the Virtual Boy",
                 "Looks like your dream will come true, Giorno",
                 "Error 404: Ball machine br0k",
                 "I don't have an answer yet, come back with better internet",
                 "Yes'nt.",
                 "Sorry, Dio Brando stopped time so I can't give a reply yet",
                 "n0 U"]
        await ctx.send(f'\U0001f3b1 Question: {question}\nAnswer: {random.choice(responses)}')

def setup(bot):
    bot.add_cog(ComedicCog(bot))