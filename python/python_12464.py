# mysql query getting different results in mysql-python
cur.execute("""select * from table where sub_date %s '%s' order by sub_date asc limit %s""" % (oper, date, limit))
