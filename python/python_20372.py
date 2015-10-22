# How to convert List in to Dictionary in python?
&gt;&gt;&gt; list1 = ["a:b","x:y","s:e","w:x"]
&gt;&gt;&gt; dict(elem.split(':') for elem in list1)
{'a': 'b', 'x': 'y', 's': 'e', 'w': 'x'}
