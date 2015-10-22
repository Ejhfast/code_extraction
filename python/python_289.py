# Sorting dictionary keys in python
&gt;&gt;&gt; mydict = {'a':1,'b':3,'c':2}
&gt;&gt;&gt; sorted(mydict, key=lambda key: mydict[key])
['a', 'c', 'b']
