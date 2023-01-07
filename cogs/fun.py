import disnake
import random
from disnake.ext import commands

class Fun(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.slash_command(description="flip a coin!")
    @commands.cooldown(1, 12, commands.BucketType.user)
    async def coin(self, inter):
        choice = random.choice(["Head","Tails"])
        await inter.send(choice)

    @commands.slash_command(description="play rps")
    @commands.cooldown(1, 12, commands.BucketType.user)
    async def rps(self, inter, choice: str = commands.Param(choices=["Rock", "Paper", "Scissors"])):
        botchoice = random.choice(["Rock", "Paper", "Scissors"])
        await inter.send(f"You choose: **{choice}**\nI choose: **{botchoice}**")

def setup(bot):
	bot.add_cog(Fun(bot))