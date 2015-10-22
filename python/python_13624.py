# MongoEngine & serverStatus
db = Document._get_db()
client_count = db.command("serverStatus")["connections"]['current'] - 1
