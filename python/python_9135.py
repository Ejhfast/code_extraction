# create new list with duplicates of list in list - python
list1 = [ ['node1', 'pathA'], ['node2', 'pathA'], ['node3', 'pathB'], ['node4', 'pathC'], ['node5', 'pathA'] ]
result = [x for x in list1 if [y[1] for y in list1].count(x[1]) &gt; 1]
