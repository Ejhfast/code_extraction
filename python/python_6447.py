# pysqlite, save database, and open it later
c.execute("SELECT * FROM mytable")
for row in c:
    #process row
