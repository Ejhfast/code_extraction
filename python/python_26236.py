# Trying to append a list with immutable list of chars [Python]
for x_ in  range(0, 10):
    string[2] = x_
    lisMonthData.append(string[:]) # slice [:] to create copy of entire list
