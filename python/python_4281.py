# Creating a dictionary from two iterables and consuming both of them
dict(itertools.izip_longest(l, x))
# {1: 'a', 2: 'b', 3: 'c', 4: None, 5: None}
