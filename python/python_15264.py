# How to speed up iteration over part of a numpy array
big_3d_arr = some 100x100x100 array
where_to_operate_arr = big_3d_arr &lt; 500 # or whatever your condition is
big_3d_arr[where_to_operate_arr] = do_something(big_3d_arr[where_to_operate_arr])
