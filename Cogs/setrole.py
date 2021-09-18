import discord
from discord.ext import commands
from replit import db
import Embed

async def prerequisites(self, ctx, args):
	# Checks if user setting the role is an admin
	if not ctx.message.author.guild_permissions.administrator:
		embed_var = Embed.embed("Not an admin", "You must be an admin to set a role!")
		print("Access denied")
		await ctx.send(embed=embed_var)
		return False
	
	# Makes sure that an argument is given
	if not args:
		embed_var = Embed.embed("No argument given", "Please enter a valid role ID")
		print("No argument given")
		await ctx.send(embed=embed_var)
		return False
	
	# Checks if the ID given is a valid role in the server
	if not discord.utils.get(ctx.message.guild.roles, id=int(args)):
		embed_var = Embed.embed("Invalid role ID", "Please enter a valid role ID!")
		print("Invalid role")
		await ctx.send(embed=embed_var)
		return False

	# Role given is added to the database
	db[str(ctx.guild.id)] = int(args)

	return str(ctx.guild.id)
	
class events(commands.Cog):
	def __init__(self, client):
		self.client = client
	
	@commands.command()
	async def setrole(self, ctx, args):
		prereq = await prerequisites(self, ctx, args)
		print(prereq)
		# Checks if all the requirements were met
		if not prereq:
			return

		embed_var = Embed.embed("Role successfully set!", "Your role has been set.")
		await ctx.send(embed=embed_var)

def setup(client):
	client.add_cog(events(client))
