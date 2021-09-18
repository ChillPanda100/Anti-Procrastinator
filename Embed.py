import discord

# Hex code for red
color_embed = 0xFF0000

def embed(header, desc):

	# The arguments needed for the embed
	embed_var = discord.Embed(title = header, description = desc, color = color_embed) 
	
	return embed_var
