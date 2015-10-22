# Printing a list justified with format
li = [2, 3, 5, 7, 11]
print ('{:&gt;12}'*len(li)).format(*li)
        2           3           5           7          11
