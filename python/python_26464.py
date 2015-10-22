# breaking a list in to lists in python?
your_list = [[int(j) for j in i.split()] for i in ' '.join(data).split('&lt;&gt;')]
