# Most elegant way to modify Python list elements inplace
for row in table:
    row[1:] = [int(c) for c in row[1:]]
