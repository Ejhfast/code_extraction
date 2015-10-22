# Using regular expression to catch phrases in Python
&gt;&gt;&gt; regex = re.compile("Who created (.*?)\?", re.I)
&gt;&gt;&gt; regex.search("Who created Lord of the Rings?").groups()[0]
'Lord of the Rings'
