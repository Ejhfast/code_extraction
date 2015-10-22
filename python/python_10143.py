# Select records from mysql table one by one - dynamic table with more records continuously being written
i = 0
while True:
    # your usual select here, but with "and MyIndexColumn = %d' % (i,)
