from replit import db
def check_entity(entity):
	try:
		db[str(entity)]
		return True
	except:
		return False
