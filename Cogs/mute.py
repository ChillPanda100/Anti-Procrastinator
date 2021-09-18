from main import *
from discord.ext import commands
from replit import db
from pytz import timezone
from datetime import datetime, timedelta
import asyncio
import Embed
import Check

tasking = []

timezones = {
	"EST": "US/EASTERN",
	"PST": "US/PACIFIC",
	"MST": "US/MOUNTAIN",
	"GMT": "Etc/GMT",
	"CT": "US/CENTRAL",
	"HST": "US/HAWAII"
}

async def check_time(self, ctx, guild):
	tasking.append(guild)
	await self.client.wait_until_ready()
	while True:
		if not Check.check_entity(f"{ctx.author.id + ctx.guild.id} time"):
			break
		# Retrieves the timezone out of the three provided arguments
		set_timezone = db[f"{ctx.author.id + ctx.guild.id} time"].split()[2].upper()
		author_role_ids = db[str(ctx.author.id) + " " + str(ctx.guild.id)]
		server_role = ctx.guild.get_role(db[str(ctx.guild.id)])
		excluded_timezone = db[f"{ctx.author.id + ctx.guild.id} time"].split()
		for k, v in timezones.items():
			tz = timezone(timezones[k])
			current_time = datetime.now(tz)
			official_time = f"{excluded_timezone[0]} {excluded_timezone[1]}"
			# Formatting for the time (Example: 2:06 PM)
			current_time = current_time.strftime("%-I:%M %p")

			if k == set_timezone and official_time == current_time:
				for id in author_role_ids.value:
					user_role = ctx.guild.get_role(id)
					await ctx.author.add_roles(user_role)
				await ctx.author.remove_roles(server_role)
				embed_var = Embed.embed("Unmuted!", "You are now unmuted and can continue chatting in the server.")
				await ctx.author.send(embed=embed_var)

				# Deletes the user from the database
				del db[f"{ctx.author.id + ctx.guild.id} time"]
				del db[str(ctx.author.id) + " " + str(ctx.guild.id)]
				break
	
		await asyncio.sleep(63 - datetime.utcnow().second)

class events(commands.Cog):
	def __init__(self, client):
		self.client = client
	
	@commands.command()
	async def mute(self, ctx, *args):
		first_argument = args[0]
		second_argument = args[1]
		third_argument = args[2]
		
		db[str(ctx.author.id) + " " + str(ctx.guild.id)] = []

		# Checks if a role was set for the server
		if not Check.check_entity(str(ctx.guild.id)):
			embed_var = Embed.embed("Role not set!", "A role has not been set for your server! Contact an admin to fix this.")
			await ctx.send(embed=embed_var)
			return

		# Removing semicolon from first argument to see if a valid time has been entered
		check_valid_time = args[0].replace(":", "")

		# Checks if the amount of arguments given is correct
		if len(args) < 3:
			print("Not enough arguments")
			embed_var = Embed.embed("Not enough arguments!", "Please enter in a valid amount of arguments.")
			await ctx.send(embed=embed_var)
			return
		
		# Checks if a valid time was given
		if int(check_valid_time) > 1259 or int(check_valid_time) < 100:
			embed_var = Embed.embed("Invalid time given!", "Please enter a valid time (Do not use military time).")
			await ctx.send(embed=embed_var)
			return 
		
		# Checks if AM or PM was given
		if second_argument and second_argument.upper() != "PM" and second_argument.upper()!= "AM":
			embed_var = Embed.embed("AM or PM not given!", "Please enter the time you want to be muted followed by AM or PM and the timezone.")
			await ctx.send(embed=embed_var)
			return 
		
		# Checks if a semicolon is in the time given AND is in a correct place
		if first_argument[1] != ":" and first_argument[2] != ":":
			embed_var = Embed.embed("Invalid time given!", "Please enter a valid time with a semicolon in the necessary spot.")
			await ctx.send(embed=embed_var)
			return
		
		# Makes sure that the third argument is a valid timezone
		if third_argument and third_argument.upper() not in timezones:
			embed_var = Embed.embed("Invalid timezone given!", "Please enter a valid timezone. To get a list of the valid timezones, please use #timezones.")
			await ctx.send(embed=embed_var)
			return 
		
		# Retrieves the role from the database
		role = ctx.guild.get_role(db[str(ctx.guild.id)])

		# Each "Role" corresponds with an "id" and a "name", it will store all of the user's roles into the database (excluding @everyone) and then proceed to remove their roles
		for Role in ctx.author.roles:
			if Role.name != "@everyone" and Role.name != role:
				db[str(ctx.author.id) + " " + str(ctx.guild.id)].append(Role.id)
				await ctx.author.remove_roles(ctx.guild.get_role(Role.id))
		
		await ctx.author.add_roles(role)

		db[f"{ctx.author.id + ctx.guild.id} time"] = f"{first_argument} {second_argument} {third_argument}"

		embed_var = Embed.embed("Muted successfully!", "You will now be muted until the time you provided.")
		await ctx.author.send(embed=embed_var)
		if not str(ctx.guild.id) in tasking:
			self.client.loop.create_task(check_time(self, ctx, str(ctx.guild.id)))
		print(db[str(ctx.author.id) + " " + str(ctx.guild.id)])
		print(db[f"{ctx.author.id + ctx.guild.id} time"])

	@commands.command(aliases=["timezone", "tz"])
	async def timezones(self, ctx):
		embed_var = Embed.embed("List of available timezones", "``EST``: US/EASTERN \n``PST``: US/PACIFIC \n ``MST``: US/Mountain \n ``GMT``: Etc/GMT \n ``CT``: US/CENTRAL \n ``HST``: US/HAWAII")
		await ctx.send(embed_var)

def setup(client):
	client.add_cog(events(client))
