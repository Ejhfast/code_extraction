# execute *.sql file with python MySQLdb
for line in open(PATH_TO_FILE):
    cursor.execute(line)
