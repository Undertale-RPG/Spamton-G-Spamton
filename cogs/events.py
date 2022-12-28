import disnake
from disnake.ext import commands, tasks

class Events(commands.Cog):
	def __init__(self, bot):
		self.bot = bot

	@commands.Cog.listener()
	async def on_ready(self):
		print(f"logged in as {self.bot.user}")
		print(f"id: {self.bot.user.id}")
		print(f"guilds: {len(self.bot.guilds)}")

	@commands.Cog.listener()
	async def on_guild_join(self, guild):
		print(f"➕ Joined \"{guild.name}\"")
		for channel in guild.text_channels:
			if channel.permissions_for(guild.me).send_messages:
				await channel.send("Hello!, Thanks for adding me! You can use the **/help** To learn how the bot works!")
				break

def setup(bot):
	bot.add_cog(Events(bot))