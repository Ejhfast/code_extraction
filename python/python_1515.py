# Python - automating MySQL index: passing parameter
updateIndexMySQLQuery = """UPDATE %s
SET numberID=%%s WHERE numberID=%%s;""" % (tableName,)
