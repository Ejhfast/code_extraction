# Find max length of each column in a list of lists
[max(len(str(x)) for x in line) for line in zip(*foo)]
