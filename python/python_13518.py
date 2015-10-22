# more efficient use of itertools.groupby()
[(sum(1 for _ in v), int(k)) for k,v in groupby(str(1223444556))]
