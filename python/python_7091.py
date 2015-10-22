# Twisted, MySQLdb and (2006, 'MySQL server has gone away') using Twisted adbapi
self.pool = adbapi.ConnectionPool("MySQLdb", self.parms['host'], self.parms['username'], self.parms['password'], self.parms['database'], cp_reconnect=True)
