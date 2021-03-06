from discord.ext import commands
from main import *
import Embed

class events(commands.Cog):
	def __init__(self, client):
		self.client = client
	
	@commands.command()
	async def help(self, ctx):
		embed_var = Embed.embed("Help Section", "``#mute``: Mute yourself for a certain amount of time. Example: #mute 4:52 PM EST\n ``#instructions``: Learn how to use the bot.\n ``#timezones``: Get a list of all the valid timezones.\n ``#setrole``: Set a role for the server (Admin only).\n ``#github``: Link to GitHub repository.\n ``#credits``: Displays the credits and everyone involved.")
		embed_var.set_footer(text="Made with Discord.py")
		await ctx.send(embed=embed_var)
	
	@commands.command()
	async def credits(self, ctx):
		developer_one = await client.fetch_user(702690873024053309)
		developer_two = await client.fetch_user(882795835371450499)
		developer_three = await client.fetch_user(771153822994530354)
		embed_var = Embed.embed("Credits", f"Anti-Procrastinator was created by {developer_one}, {developer_two}, and {developer_three}")
		embed_var.set_footer(text="Made with Discord.py")
		await ctx.send(embed=embed_var)
	
	@commands.command()
	async def instructions(self, ctx):
		embed_var = Embed.embed("Instructions", "``For admins``: Use the ``#setrole`` command to set a role (Make sure the role is isolated to a channel) that will be given to the users when muted. Additionally, move the \"Anti-Procrastinator\" role to the very top of the role hierarchy if possible. \n\n ``For users``: Use the ``#mute`` command and enter the time you want to be muted, followed by ``AM/PM`` and the timezone of your choice (Use #timezones to get a list of all the available timezones).")
		await ctx.send(embed=embed_var)
	
	@commands.command()
	async def github(self, ctx):
		embed_var = Embed.embed("GitHub Repository", "``Link``: https://github.com/ChillPanda100/Anti-Procrastinator")
		await ctx.send(embed=embed_var)
	
def setup(client):
	client.add_cog(events(client))
