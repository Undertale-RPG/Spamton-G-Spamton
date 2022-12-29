import disnake
from disnake.ext import commands
import datetime

class Help(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.slash_command(description="a complete view of the bot's features and commands.")
    @commands.cooldown(1, 12, commands.BucketType.user)
    async def help(self, inter):
        """Info on how to use the bot and it's commands.""" 
        em = disnake.Embed(
            title = "📜 | Help Menu!",
            color = 0x3EB58B,
            timestamp = datetime.datetime.now()
        )
        em.set_thumbnail(url=self.bot.user.avatar.url)
        forbid = ["Events", "Errors"]   
        for cog in self.bot.cogs:
            cog = self.bot.get_cog(cog)
            if cog.qualified_name in forbid:
                continue    
            cmds = cog.get_slash_commands()
            commands_per = "".join(f" `{command.name}` • " for command in cmds)
            em.add_field(name=cog.qualified_name, value=f"• {commands_per} \n\n", inline=False)      
        await inter.send(inter.author.mention, embed=em)

    @commands.slash_command(description="Change the settings of this server.")
    @commands.cooldown(1, 12, commands.BucketType.user)
    async def settings(self, inter):
        em = disnake.Embed(
            title=f"<:Settings:1057790028396384396> {inter.guild.name} Settings",
            color=0x3EB58B
        )
        em.add_field(name="Logs channel", value="None")
        em.add_field(name="Welcome channel", value="None")
        em.add_field(name="Leave channel", value="None")
        await inter.send(embed=em)

def setup(bot):
	bot.add_cog(Help(bot))