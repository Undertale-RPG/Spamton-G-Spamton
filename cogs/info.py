import disnake
from disnake.ext import commands


class Info(commands.Cog):
	def __init__(self, bot):
		self.bot = bot
	
	@commands.slash_command(description="shows server info")
	@commands.cooldown(1, 12, commands.BucketType.user)
	async def server(self, inter):
		em = disnake.Embed(
			title="Server Info",
			color=0x3EB58B
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

	@commands.slash_command(description="List of all server roles")
	@commands.cooldown(1, 12, commands.BucketType.user)
	async def roles(self, inter):
		guild_roles = []
		for role in inter.guild.roles:
			if role.is_bot_managed() == False:
				guild_roles.append(role)
			else:
				pass
		guild_roles.sort(reverse=True)
		roles = "".join(f"• {role.mention}`({len(role.members)} members)`\n" for role in guild_roles)
		em = disnake.Embed(
			title="List of all our roles",
			color=0x3EB58B,
			description=roles
		)
		await inter.send(embed=em)

	@commands.slash_command(description="shows info on a role")
	@commands.cooldown(1, 12, commands.BucketType.user)
	async def role(self, inter, role: disnake.Role):
		em = disnake.Embed(
			title="Role info",
			color=role.color
		)
		em.set_thumbnail(url=role.icon)
		em.add_field(name="Name", value=f"```{role.name}```")
		em.add_field(name="Color", value=f"```{role.color}```")
		em.add_field(name="Created at", value=f"```{role.created_at.ctime()}```", inline=False)

		await inter.send(embed=em)

	@commands.slash_command(description="see userinfo")
	@commands.cooldown(1, 12, commands.BucketType.user)
	async def member(self, inter, member: disnake.User = None):
		if member == None:
			member = inter.author

		user = await self.bot.fetch_user(member.id)
		em = disnake.Embed(
			title="Member info",
			color=member.color
		)
		em.set_thumbnail(url=member.display_avatar)
		em.set_image(url=user.banner)
		em.add_field(name="Name",value=f"```{member.display_name}({member})```")
		em.add_field(name="Bot?", value=f"```{member.bot}```")
		em.add_field(name="ID", value=f"```{member.id}```", inline=False)
		em.add_field(name="Joined discord", value=f"```{member.created_at.ctime()}```", inline=False)

		await inter.send(embed=em)

def setup(bot):
	bot.add_cog(Info(bot))