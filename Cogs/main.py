import discord
import os
import discord.ext
import keep_alive
from discord.ext import commands
from discord.ext.commands import CommandNotFound

client = discord.Client()
client = commands.Bot(help_command = None, command_prefix = "#")

@client.event
async def on_ready():
	keep_alive.keep_alive()
	print("Bot is online")
	stat = discord.Game("#help")

	# Displays the bot's status as "Playing #help"
	await client.change_presence(status=discord.Status.online, activity=stat)

# If an incorrect command is used it will be ignored in the terminal
@client.event
async def on_command_error(ctx, error):
	if isinstance(error, CommandNotFound):
		return

for file in os.listdir("./Cogs"):
	# Loads all files in the Cogs folder with the .py extension
	if file.endswith(".py"):
		client.load_extension(f"Cogs.{file[:-3]}")
		print(f"{file[:-3]}.py has been loaded")

# Retrieves token
client.run(os.getenv("Token"))
