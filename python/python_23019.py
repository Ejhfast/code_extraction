# Unable to update Multiple cloums in a sql database table using pyodbc
cursor.execute("update Gps_table set longitude=?,latitude=? where gps_id=1", s1, s2)
