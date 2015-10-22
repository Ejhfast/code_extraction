# How to get datatypes of specific fields of an Access database using pyodbc?
# columns in table x
for row in cursor.columns(table='x'):
    print row.column_name
