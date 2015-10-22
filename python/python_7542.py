# Using append() on transient anonymous lists inside of a list comprehension in Python
&gt;&gt;&gt; mylist = [['A;B', 'C'], ['D;E', 'F']]
&gt;&gt;&gt; [first.split(';') + [second] for first, second in mylist]
[['A', 'B', 'C'], ['D', 'E', 'F']]
