# In python, what's the most efficient way to combine 3 dicts and to sort by one of the dict's keys?
sorted(itertools.chain(list1.itervalues(), list2.itervalues(),
    list3.itervalues()), key=operator.itemgetter('timestamp'))
