# Remove String spaces with regular expression
&gt;&gt;&gt; re.sub(r'^\s+|\s+$', '', ' hello world ')
'hello world'
