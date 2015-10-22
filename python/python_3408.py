# How to copy a variable number of elements in a list to a uniform list and store in MySQL using Python the most efficient way?
for line in mylistings:
    out = line + [None] * (4 - len(line)) # pad the list with None to 4 elements
    cursor.execute("INSERT INTO LoadData VALUES (%s, %s, %s, %s)", out)
