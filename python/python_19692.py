# python 2.7.5+ split list ['a', 'xxx yyy zzz'] into list ['a', 'xxx', 'yyy', 'zzz'] how?
&gt;&gt;&gt; [word for s in L for word in s.split()]
['a', 'xxx', 'yyy', 'zzz']
