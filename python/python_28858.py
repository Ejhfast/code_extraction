# Selecting rows depending on conditions for multiple columns
&gt;&gt;&gt; test_array[np.where(np.all(test_array[:,[0,3]]==[1,5],axis=1))]
array([[1, 2, 3, 5]])
