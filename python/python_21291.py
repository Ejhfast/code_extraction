# Upload values from Python list to MySql using selfwritten function
query = "INSERT INTO phone_db ({column}) VALUES (%s)".format(column = insertitem)
args = (what,)
cursor.execute(query,args)
