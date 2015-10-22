# How should I prevent abuse when using web.py's web.database?
results = db.query("SELECT * FROM users WHERE id=$id", vars={'id':10})
