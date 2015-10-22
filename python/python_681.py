# PYTHON: Update MULTIPLE COLUMNS with python variables
cursor.execute("UPDATE table_name SET field1=%s ... field10=%s WHERE id=%s", (var1,... var10, id))
