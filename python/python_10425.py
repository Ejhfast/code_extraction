# How to remove the first and last item in a list?
&gt;&gt;&gt; L = ['Q 0006 005C 0078 0030 0030 0033 0034 ONE_OF 0002 ']
&gt;&gt;&gt; [' '.join(el.split()[1:-1]) for el in L]
['0006 005C 0078 0030 0030 0033 0034 ONE_OF']
