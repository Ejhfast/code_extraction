# mysql_info() equivalent in Python
conn = mysql.connector.connect(...)
result =  conn.cmd_query("LOAD DATA LOCAL INFILE query")
print (result['info_msg'])
