# Python accessing cell with column name dynamically obtained
for row in rows:
    id = ''.join([getattr(row, col) for col in columns])
