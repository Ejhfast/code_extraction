# How can I get a value that's inside parentheses in a string in Python?
&gt;&gt;&gt; a = '2(3.4)'
&gt;&gt;&gt; a[a.index("(") + 1:a.rindex(")")]
'3.4'
