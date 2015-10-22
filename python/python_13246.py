# Inserting JSON data to sqlite - OperationalError: unrecognized token "{"
sqlString=company['name']+","+simplejson.dumps(info)
cur.execute("INSERT INTO companyInfo VALUES (?)", (sqlString, ))
