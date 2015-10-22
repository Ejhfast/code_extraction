# Find the two longest strings from a list || or the second longest list in PYTHON
&gt;&gt;&gt; lst = ['hello', 'blah', 'boo', 'braininess']
&gt;&gt;&gt; heapq.nlargest(2, lst, key=len)
['braininess', 'hello']
