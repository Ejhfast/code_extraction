# Group list by values
values = set(map(lambda x:x[1], list))
newlist = [[y[0] for y in list if y[1]==x] for x in values]
