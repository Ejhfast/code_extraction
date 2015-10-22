# string to integer function in python
&gt;&gt;&gt; t = '12 23 apples banana 5'
&gt;&gt;&gt; [int(x) for x in t.split() if x.isdecimal()]
[12, 23, 5]
