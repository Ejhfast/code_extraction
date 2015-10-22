# Python: Get items that follow a specified element of a list
&gt;&gt;&gt; a = ['ONE', 'TWO', 'SEVEN', 'TWELVE', 'ONE', 'SEVEN']
&gt;&gt;&gt; [a[x+1] if x+1 &lt; len(a) else None for x in range(len(a)) if a[x] == 'ONE']
['TWO', 'SEVEN']
