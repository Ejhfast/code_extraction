# Python: Split String into list of lists of lists
V = [[map(int, j.split()) for j in i.split(',')] for i in s.split(';')]
