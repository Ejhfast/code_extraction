# split elements of a list in python
&gt;&gt;&gt; l = ['element1\t0238.94', 'element2\t2.3904', 'element3\t0139847']
&gt;&gt;&gt; [i.split('\t', 1)[0] for i in l]
['element1', 'element2', 'element3']
