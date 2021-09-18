from flask import Flask
from threading import Thread

bot = Flask("")

@bot.route('/')
def home():
	return "Bot is online"

def run():
	bot.run(host="0.0.0.0", port=8080)

def keep_alive():
	thread = Thread(target=run)
	thread.start()
