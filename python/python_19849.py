# Python: SQL query results to table
Stuff = []
for row in Data:
    Stuff.append([i for i in [row['day'], float(row['a1']), float(row['a2']), float(row['a3'])]]);
