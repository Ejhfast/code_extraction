# merge two lists in python - but sort them during merge
all_res = sorted(list(fq) + list(sq), key = lambda x: (x[-1], x[0]))
