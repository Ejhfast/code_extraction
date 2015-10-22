# Printing values in row order from dictionary/ list
print([v for r in (row for row in zip(*l[1:])) for v in r])
#['B', 'C', 'F', 'C', 'B', 'E', 'B', 'D', 'A', 'C', 'B', 'C', 'C', 'C', 'B', 'B', 'A', 'D', 'B', 'F', 'A', 'C', 'B', 'F', 'F', 'A', 'F']
