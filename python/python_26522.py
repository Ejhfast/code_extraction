# Python Cleaner way to get all substrings in a string
&gt;&gt;&gt; w="Shum"
&gt;&gt;&gt; [w[:c] for c in range(len(w),0,-1)]
['Shum', 'Shu', 'Sh', 'S']
