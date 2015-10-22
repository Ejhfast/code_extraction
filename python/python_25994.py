# a function that chages the structure of a python list
&gt;&gt;&gt; my_list = [['A B C','D E F'],['1 2 3 ', '4 5 6 ']]
&gt;&gt;&gt; map(lambda x:x.split(), map(" ".join, my_list))
[['A', 'B', 'C', 'D', 'E', 'F'], ['1', '2', '3', '4', '5', '6']]
