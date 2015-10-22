# how to safely generate a SQL LIKE statement using python db-api
sql='SELECT x FROM myTable WHERE x LIKE %s'
args=[beginningOfString+'%']
cursor.execute(sql,args)
