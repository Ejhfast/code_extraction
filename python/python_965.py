# pygresql - insert and return serial
sql = "insert into job_runners (hostname) values ('localhost') returning id"
rv = dbconn.query(sql)
id = rv.dictresult()[0]['id']
