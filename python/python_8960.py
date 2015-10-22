# (<class 'sqlite3.OperationalError'>, OperationalError('unrecognized token: ":"',))
sql = "INSERT INTO warrent(link, content) values (\'{0}\', \'{1}\')".format(url,page)
self.curs.execute(sql)
