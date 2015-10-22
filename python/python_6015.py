# Python MySQLdb unique records, ignore errors
for string in self.FinalMailsArray:
    c.execute("""INSERT IGNORE INTO table (email) VALUES(%s) """,(string))
