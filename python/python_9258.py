# How can i pass configuration variable values into the pyodbc connect command?
self.db = pyodbc.connect('driver={%s};server=%s;database=%s;uid=%s;pwd=%s' % ( driver, server, db, user, password ) )
