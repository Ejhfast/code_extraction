# Python regular expression that replaces test before a particular pattern
&gt;&gt;&gt; s = re.search(r".*\/(app.*)", "/home/python/app/index.html")
&gt;&gt;&gt; s.groups()[0]
'app/index.html'
