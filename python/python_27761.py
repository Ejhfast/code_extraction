# Non nested for loops in a single line for creating list in python
&gt;&gt;&gt; [[-1, y] for y in range(-1, 2)] + [[0, 1], [[1, z] for z in range(1, -2, -1)], [0, -1]]
[[-1, -1], [-1, 0], [-1, 1], [0, 1], [[1, 1], [1, 0], [1, -1]], [0, -1]]
