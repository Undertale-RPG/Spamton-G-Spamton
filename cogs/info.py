import disnake
from disnake.ext import commands


class Info(commands.Cog):
	def __init__(self, bot):
		self.bot = bot
	
	@commands.slash_command()
	@commands.cooldown(1, 12, commands.BucketType.user)
	async def server(self, inter):
		em = disnake.Embed(
			title="Server Info",
			color=0x5bb95d
		)
		em.set_thumbnail(url=inter.guild.icon)
		em.add_field(name="👑Owner", value=f"```{inter.guild.owner}```")
		em.add_field(name="👪Members", value=f"```{inter.guild.member_count}```")
		em.add_field(name="🔖Roles", value=f"```{len(inter.guild.roles)}```")
		em.add_field(name="🗃️Categories", value=f"```{len(inter.guild.categories)}```")
		em.add_field(name="📚Text channels", value=f"```{len(inter.guild.text_channels)}```")
		em.add_field(name="🙊Voice channels", value=f"```{len(inter.guild.voice_channels)}```")
		em.add_field(name="💥Creation date", value=f"```{inter.guild.created_at.ctime()}```", inline=False)

		await inter.send(embed=em)

	@commands.slash_command()
	@commands.cooldown(1, 12, commands.BucketType.user)
	async def roles(self, inter):
		guild_roles = []
		for role in inter.guild.roles:
			if role.is_bot_managed() == False:
				guild_roles.append(role)
			else:
				pass
		roles = "".join(f"• {role.mention}`({len(role.members)} members)`\n" for role in guild_roles)
		em = disnake.Embed(
			title="List of all our roles",
			color=0x5bb95d,
			description=roles
		)
		await inter.send(embed=em)

	@commands.slash_command()
	async def emojis(self, inter):
		emojis = "".join(f":{emoji.name}: " for emoji in inter.guild.emojis)
		await inter.send(emojis)

def setup(bot):
	bot.add_cog(Info(bot))