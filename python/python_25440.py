# How to sort ANY list in Python 2.7 in DESCENDING order?
&gt;&gt;&gt; lst = [[1,2,3], [2,3,4], [4,5,6]]
&gt;&gt;&gt; sorted([sorted(sublst, reverse=True) for sublst in lst], reverse=True)
[[6, 5, 4], [4, 3, 2], [3, 2, 1]]
