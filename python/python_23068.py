# Summing up numbers in a defaultdict(list)
sum(td.seconds for sublist in d.itervalues() for td in sublist)
