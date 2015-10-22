# I how to intersect a range of columns between two horizontal list?
set_b = set(list_b)
result = [x for x in list_a if (x[1], x[2]) in set_b]
