# How do I convert a list of ascii values to a string in python?
&gt;&gt;&gt; L = [104, 101, 108, 108, 111, 44, 32, 119, 111, 114, 108, 100]
&gt;&gt;&gt; ''.join(chr(i) for i in L)
'hello, world'
