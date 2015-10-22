# Python: Inserting list of tuples in SQL Database and add an auto-incrementing id field
curs.execute('INSERT INTO test(POI, Address, Phone, Website) VALUES(?, ?, ?, ?)',var)
