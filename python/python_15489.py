# python: sort table (list of lists) according to specific ordered list (and other options)
order_of_3rd = [3,0,1,2]
My_table.sort(key=lambda a: (a[0], order_of_3rd.index(a[2])))
