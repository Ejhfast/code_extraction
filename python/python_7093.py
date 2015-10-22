# Looping Through Nested List - Convert from String to Float
&gt;&gt;&gt; benchmark = [[1, 2, 3, 4], [5, 6, 7, 8]]
&gt;&gt;&gt; [[float(col) if i == 2 else col for i, col in enumerate(row)] for row in benchmark]
[[1, 2, 3.0, 4], [5, 6, 7.0, 8]]
