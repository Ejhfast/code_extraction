# single list comprehension to unpack nested dictionary
&gt;&gt;&gt; [i for j in a.values() for i in j.values()]
['c aw', 'b aw', 'c2 aw', 'b2 aw']
