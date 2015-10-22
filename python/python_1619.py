# In Python, how do I split a string and keep the separators?
&gt;&gt;&gt; re.split('(\W)', 'foo/bar spam\neggs')
['foo', '/', 'bar', ' ', 'spam', '\n', 'eggs']
