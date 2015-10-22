# Update list of dictionaries elementwise in Python
map(lambda (i,v) : A[i].update(v), enumerate(map((lambda i: {'x':i['x'] + 1}), A)))
