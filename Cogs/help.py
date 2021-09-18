from discord.ext import commands
import Embed

class events(commands.Cog):
	def __init__(self, client):
		self.client = client
	
	@commands.command()
	async def help(self, ctx):
		embed_var = Embed.embed("Help Section", "``#mute``: Mute yourself for a certain amount of time. Example: #mute 4:52 PM\n ``#timezones``: Get a list of all the valid timezones.\n ``#setrole``: Set a role for the server (Admin only)\n``#credits``: Displays the credits and everyone involved.")
		embed_var.set_footer(text="Made with Discord.py")
		await ctx.send(embed=embed_var)
	
	@commands.command()
	async def credits(self, ctx):
		embed_var = Embed.embed("Credits", "Anti-Procrastinator was created by ShyguyIV#6970, fisherman#2033, and ChillPanda#5842")
		embed_var.set_footer(text="Made with Discord.py")
		await ctx.send(embed=embed_var)
	
	@commands.command()
	async def instructions(self, ctx):
		embed_var = Embed.embed("Instructions" "``For admins``: Use the ``#setrole`` command to set a role (Make sure the role is isolated to a channel) that will be given to the users when muted. \n ``For users``: Use the ``#mute`` command and enter the time you want to be muted, followed by ``AM/PM`` and the timezone of your choice (Use #timezones to get a list of all the available timezones).")
		await ctx.send(embed=embed_var)
	
def setup(client):
	client.add_cog(events(client))
