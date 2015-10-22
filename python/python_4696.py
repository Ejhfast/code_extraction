# Is there a function in Python which generates all the strings of length n over a given alphabet?
&gt;&gt;&gt; [''.join(i) for i in itertools.product("ab",repeat=4)]
['aaaa', 'aaab', 'aaba', 'aabb', 'abaa', 'abab', 'abba', 'abbb', 'baaa', 'baab', 'baba', 'babb', 'bbaa', 'bbab', 'bbba', 'bbbb']
