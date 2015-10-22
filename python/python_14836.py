# Two 'for' loops at once in python
for i, j in zip(range(linecount - 1, -1, -1), range(linecount, -1, -1)):
    print i, j
