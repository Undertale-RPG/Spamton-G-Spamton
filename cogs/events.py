import disnake
from disnake.ext import commands
from utility.utils import ConsoleColors

class Events(commands.Cog):
	def __init__(self, bot):
		self.bot = bot

	@commands.Cog.listener()
	async def on_ready(self):
		print(f"{ConsoleColors.GREEN}Acount: {self.bot.user}")
		print(f"{ConsoleColors.GREEN}Id: {self.bot.user.id}")
		print(f"{ConsoleColors.GREEN}Guilds: {len(self.bot.guilds)}")
		print(f"{ConsoleColors.GREEN}Users: {len(self.bot.users)}")

	@commands.Cog.listener()
	async def on_guild_join(self, guild):
		print(f"{ConsoleColors.YELLOW}➕ Joined \"{guild.name}\"")
		for channel in guild.text_channels:
			if channel.permissions_for(guild.me).send_messages:
				await channel.send("Hello!, Thanks for adding me! You can use the **/help** To learn how the bot works!")
				break

def setup(bot):
	bot.add_cog(Events(bot))