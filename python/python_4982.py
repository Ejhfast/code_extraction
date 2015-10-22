# How to turn a string of letters into 3 letter words in Python 2.7.1
&gt;&gt;&gt; a = "aaabbbcccdddeeefffggg"
&gt;&gt;&gt; [a[i:i+3] for i in range(0, len(a), 3)]
['aaa', 'bbb', 'ccc', 'ddd', 'eee', 'fff', 'ggg']
