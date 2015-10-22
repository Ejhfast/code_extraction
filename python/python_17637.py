# ProgrammingError: (1064, 'You have an error in your SQL syntax; check the manual that corresponds to your MySQL server version for the right syntax
self.cursor.execute("UPDATE urls SET state=%d,content='%s' WHERE url='%s'"%(state,self.conn.escape_string(content),url))
