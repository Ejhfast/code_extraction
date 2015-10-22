# Create two tables in sqlite3 database in Python
for ele in my_data_2:
    c.execute('''INSERT INTO MY_TABLE_2 VALUES(?,?,?)''',ele)
