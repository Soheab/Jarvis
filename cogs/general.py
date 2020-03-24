import discord
import os
import random
import sys
import traceback
from discord.ext import commands


class WelcomingCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_member_join(self, member):
        channel = self.bot.get_channel(689959642947780733)
        messages = ['One step out of place, and into the cock and ball torture chamber you go.',
                    'Oh great. Now you came here to steal my eggs to? Well, guess what, I hired attack chickens! Try me now...',
                    'Watch your step here before you get licked on your arm',
                    'Welp we had a good run boys, time to reset the server now that this monster joined.',
                    'Can you not?',
                    'Ah yes, the degenerate']
        if channel is not None:
            await channel.send(f'{member.mention} has descended to the Cave. {random.choice(messages)}')

    @commands.command()
    async def latency(self, ctx):
        await ctx.send(f'The current latency is: {self.bot.latency}')


class Assistance(commands.MinimalHelpCommand):
    def get_command_signature(self, command):
        return '{0.clean_prefix}{1.qualified_name} {1.signature}'.format(self, command)


def setup(bot):
    bot.add_cog(WelcomingCog(bot))
