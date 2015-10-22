# Creating a list comprehension to find orthogonal neighbours in 2D list
[(i,j) for i,j in ((a-1,b), (a+1,b), (a,b-1), (a,b+1)) if 0&lt;=i&lt;MAXX and 0&lt;=j&lt;MAXy and X[i][j] is not None ]
