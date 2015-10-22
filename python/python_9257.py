# Joining every four strings in a list
&gt;&gt;&gt; L = ['Ww','Aa','Bb','Cc','ww','AA','BB','CC']
&gt;&gt;&gt; [''.join(x) for x in zip(*[iter(L)] * 4)]
['WwAaBbCc', 'wwAABBCC']
