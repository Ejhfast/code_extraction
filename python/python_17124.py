# Return all values when a condition value is NULL
query = 'SELECT * FROM table1 WHERE id = COALESCE(%s,id)'
