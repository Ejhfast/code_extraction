# Find all occurences of an element in a matrix in Python
&gt;&gt;&gt; my_list = [[1,2,3,1, 3], [1,3,2]]
&gt;&gt;&gt; [(i,j) for i,x in enumerate(my_list) for j,y in enumerate(x) if y == 3]
[(0, 2), (0, 4), (1, 1)]
