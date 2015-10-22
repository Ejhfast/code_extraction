# Python: MySQLdb: Error: 1064 "You have an error in your SQL syntax."
header_string = ('number_one','number_two','number_three')
values = (1,2,3)
cursor.execute("""INSERT INTO my_table (%s,%s,%s) VALUES (%s,%s,%s)""", (header_string+values))
