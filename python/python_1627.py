# getting list without k'th element efficiently and non-destructively
l = [('a', 1), ('b', 2), ('c', 3)]
k = 1
l_without_num = l[:k] + l[(k + 1):]
