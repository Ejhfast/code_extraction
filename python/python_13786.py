# Is there a simple way to convert a 2d list of floats into a 2d list of tuples in python?
&gt;&gt;&gt; l = [[0.1, 0.2], [1.1, 1.2]]
&gt;&gt;&gt; [[(0, val) for val in elem] for elem in l]
[[(0, 0.1), (0, 0.2)], [(0, 1.1), (0, 1.2)]]
