# clumsy comprehension cleanup
dct = {row[0]:[float(x) for x in row[1:]] for row in pat_mat}
