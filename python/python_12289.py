# Python: How can I take a list of lists, convert every element into strings, and return the list of lists?
&gt;&gt;&gt; l = [[11, 2, 3, 5], [5, 3, 74, 1, 90]]
&gt;&gt;&gt; [[str(j) for j in i] for i in l]
[['11', '2', '3', '5'], ['5', '3', '74', '1', '90']]
