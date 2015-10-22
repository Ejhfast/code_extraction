# Finding permuations and combinations using Python
&gt;&gt;&gt; import itertools
&gt;&gt;&gt; list(itertools.product('ab', repeat=3))
[('a', 'a', 'a'), ('a', 'a', 'b'), ('a', 'b', 'a'), ('a', 'b', 'b'), ('b', 'a', 'a'), ('b', 'a', 'b'), ('b', 'b', 'a'), ('b', 'b', 'b')]
