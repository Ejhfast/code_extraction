# return column names from pyodbc execute() statement
columns = [column[0] for column in cursor.description]
