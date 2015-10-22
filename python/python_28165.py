# Python Dynamic Query on Strings
db.execute("SELECT count(*) from table where field = %s", [val])
