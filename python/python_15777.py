# Pyodbc query string quote escaping
cursor.execute("SELECT x from y where Name = ?", (namepar,))
