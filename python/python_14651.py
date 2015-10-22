# Using pymssql to insert datetime object into SQL Server
cursor.execute("INSERT INTO MyTable
                VALUES(1, 'Having Trouble', '" + str(datetime.datetime.now()) + "')
")
