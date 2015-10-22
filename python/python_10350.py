# Python - Fast Way to Remove Duplicates in This List?
&gt;&gt;&gt; a = [["hello", "hi"], ["hello", "hi"], ["how", "what"], ["hello", "hi"], ["how", "what"]]
&gt;&gt;&gt; set(map(tuple, a))
set([('how', 'what'), ('hello', 'hi')])
