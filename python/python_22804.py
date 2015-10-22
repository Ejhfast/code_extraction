# Insert unicode value into sqlite from python code
sql = "insert into "+tableNameForSheet+" ("+columnNamesCSV+") values (?,?,?,?)"
parameters = [1, u'cust01', u'addr01  strasse 48908', "2131234213"]
cursor.execute(sql, parameters)
