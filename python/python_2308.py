# sort a list of percentages
b =['52.5%', '62.4%', '91.8%', '21.5%']
b.sort(key = lambda a: float(a[:-1]))
