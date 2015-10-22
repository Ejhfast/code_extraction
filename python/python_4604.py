# python list comprehension unzipping multiple returns
a, b = zip(*[func(i,j) for i, j in zip(x,y)])
