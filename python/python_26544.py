# How do i sort a dictionary by value that has tuples as values
In [1]: sorted(a.items(), key=lambda e: (-e[1][0], +e[1][1]))
Out[1]: [('John', (18, 19)), ('Alex', (18, 22)), ('Jim', (5, 8)), ('Maria', (5, 11))]
