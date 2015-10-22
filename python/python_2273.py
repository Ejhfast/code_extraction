# Is there a neater way to get the first occurrence of something?
&gt;&gt;&gt; lista = ['a', 'b', 'foo', 'c', 'd', 'e', 'bar']
&gt;&gt;&gt; next(i for i in lista if len(i) &gt; 2)
'foo'
