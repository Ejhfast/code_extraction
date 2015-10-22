# How do I send a query string in post request in Python using pipe delimiters?
&gt;&gt;&gt; data = {'string': username + '|' + password}
&gt;&gt;&gt; r = requests.post(url, data=data)
