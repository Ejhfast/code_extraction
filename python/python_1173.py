# Why does an assignment for double-sliced numpy arrays not work?
a[numpy.where(a==1)[0][1:]] = 3
