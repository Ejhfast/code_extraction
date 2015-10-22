# Length-wise-sorted list but, same length in alphabetical-order in a step
&gt;&gt;&gt; x.sort(key=lambda item: (len(item), item))
&gt;&gt;&gt; x
['a', 'b', 'c', 'aa', 'ab', 'ba', 'aaa']
