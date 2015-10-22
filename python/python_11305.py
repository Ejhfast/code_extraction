# Generate arrays that contain every combination of elements from an array
&gt;&gt;&gt; from itertools import combinations
&gt;&gt;&gt; list(combinations('ABCD', 2))
[('A', 'B'), ('A', 'C'), ('A', 'D'), ('B', 'C'), ('B', 'D'), ('C', 'D')]
