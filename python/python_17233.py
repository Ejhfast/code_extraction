# Separating integers from a string properly (no regex)
&gt;&gt;&gt; s = '34 ch33se 34e8 3.4'
&gt;&gt;&gt; map(int, filter(None, ''.join(map(lambda c: (c.isdigit() and c or ' '), s)).split(' ')))
[34, 33, 34, 8, 3, 4]
