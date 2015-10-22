# Jython, Query multiple columns dynamically
columns = ['column1', 'column2', 'column3', 'column4', 'column5']
results = statement.executeQuery("select %s from %s where column_id = '%s'" % (",".join(columns), table, id))
