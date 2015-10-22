# Python: Add data to first CSV column
for row in r:
    w.writerow(('US', row[0], row[3]))
