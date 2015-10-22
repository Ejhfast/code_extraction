# What's the best python idiom for grouping a list of items into groups of a specific max size?
l = [1,2,3,4,5,6,7]
n = 5
newlist = [l[i:i+n] for i in range(0,len(l),n)]
