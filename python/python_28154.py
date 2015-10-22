# error in python mysql where clause
cursor.execute("""SELECT pass FROM tablename1 where name='%s'""", (first_name, ))
