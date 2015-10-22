# How to insert strings with pipe symbol in sqlite
s.execute('INSERT INTO mytable (col_name) VALUES (?);', ("a|b",))
