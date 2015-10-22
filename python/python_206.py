# How do I do what strtok() does in C, in Python?
A = '1, 2,,3,4  '
B = [int(x) for x in A.split(',') if x.strip()]
