# loop through two list and extend one list by a value in the other list
&gt;&gt;&gt; [x + [y] for x, y in zip(list1, list2)]
[['a', 'a', 1], ['b', 'b', 2], ['c', 'c', 3]]
