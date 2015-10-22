# Update 2D numpy array values
v[0:5:2,0:5:2] += v[0:5:2,1:6:2]    # even rows
v[1:5:2,1:5:2] += v[1:5:2,2:6:2]    # odd rows
