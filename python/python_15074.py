# List comprehension for flatteing values from dicts from list
&gt;&gt;&gt; lst = [{'a': 1, 'b': 2, 'c': 3}, {'a': 4, 'b': 5, 'c': 6}]
&gt;&gt;&gt; [dct[i] for dct in lst for i in ('b', 'c')]
[2, 3, 5, 6]
