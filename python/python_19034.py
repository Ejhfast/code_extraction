# how to pop right most(lowest value) item from dictionary?
item = min(dic, key=dic.get)
del dic[item]
