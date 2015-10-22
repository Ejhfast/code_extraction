# User-readable file format for python list of lists
In [105]: my_list = [1, 'the name of the set', [[1, 'data1', 'data2'],[2,'data3','data4']]]
In [106]: my_list == json.loads(json.dumps(my_list))
Out[106]: True
