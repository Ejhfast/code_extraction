# How to sort a list by checking values in a sublist in python?
&gt;&gt;&gt; data = [['a',[10]], ['b',[1]], ['c',[5,10]], ['d',[5,1,-10]], ['e',[5,1,-1]]
&gt;&gt;&gt; sorted(data, reverse = True, key = lambda pair: pair[1])
[['a', [10]], ['c', [5, 10]], ['e', [5, 1, -1]], ['d', [5, 1, -10]], ['b', [1]]]
