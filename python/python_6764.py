# creating a list with 2 entries for each element of an iterator
data = [1,10,100]
itertools.chain(*((x,log10(x)) for x in data))
