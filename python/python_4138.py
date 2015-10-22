# What is the simplest way to swap char in a string with Python?
&gt;&gt;&gt; s = 'badcfe'
&gt;&gt;&gt; ''.join([ s[x:x+2][::-1] for x in range(0, len(s), 2) ])
'abcdef'
