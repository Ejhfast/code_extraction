# Convert python list with None values to numpy array with nan values
&gt;&gt;&gt; my_list = [3, 5, 6, None, 6, None]
&gt;&gt;&gt; np.array(my_list, dtype=np.float)
array([  3.,   5.,   6.,  nan,   6.,  nan])
