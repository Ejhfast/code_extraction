# Using a Python dict for a SQL INSERT statement
qmarks = ', '.join('?' * len(myDict))
qry = "Insert Into Table (%s) Values (%s)" % (qmarks, qmarks)
cursor.execute(qry, myDict.keys() + myDict.values())
