# How to turn multiple lists into a list of sublists where each sublist is made up of the same index items across all lists?
&gt;&gt;&gt; [list(x) for x in zip(lsta, lstb, lstc)]
[['a', 'a', 'a'], ['b', 'b', 'b'], ['c', 'c', 'c'], ['d', 'd', 'd']]
&gt;&gt;&gt;
