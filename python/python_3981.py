# Python: Expanding List of Class Objects
for row in table:
    print '{0} - {1} - {2}'.format(*[x.name for x in row])
