# Delete multiple rows in MYSQL with info from python list
id_list = ['abc', 'def', 'ghi']
query_string = "delete from test where id in (%s)" % ','.join(['?'] * len(id_list))
cursor.execute(query_string, id_list)
