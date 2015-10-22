# How to get the name of a regex named capturing group?
&gt;&gt;&gt; match = re.match("(?P&lt;letter&gt;A)", "A")
&gt;&gt;&gt; match.groupdict()
{'letter': 'A'}
