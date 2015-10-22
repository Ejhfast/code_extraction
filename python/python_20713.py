# How to sort in python based on two parameters but with different orders
&gt;&gt;&gt; sorted(st, key=lambda x: (x[1]*-1,x[0]))
[('andrew', 14, 15), ('zach', 14, 12), ('jane', 12, 10)]
&gt;&gt;&gt;
