# sqlite3.OperationalError: near "REFERENCES": syntax error - foreign key creating
db.execute("create table if not exists table2 (names text,my_id integer, FOREIGN KEY(my_id) REFERENCES maintable (id))")
