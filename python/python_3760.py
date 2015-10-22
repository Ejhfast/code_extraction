# Select column names in a table using PyODBC
# columns in table x
for row in cursor.columns(table='x'):
    print row.column_name
