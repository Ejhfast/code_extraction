# How to find all indexes of a list that are empty in Python
&gt;&gt;&gt; mylist  = [[1,2,3,4], [] , [1,2,3,4] , []]
&gt;&gt;&gt; [i for i,x in enumerate(mylist) if not x]
[1, 3]
