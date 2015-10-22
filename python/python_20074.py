# Extract values from list and make tuples
&gt;&gt;&gt; [(list[i-1], list[i]) for i in range(1, len(list))]
[('S', 'B'), ('B', 'E'), ('E', 'D'), ('D', 'F'), ('F', 'G')]
