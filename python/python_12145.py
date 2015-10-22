# Python - regular expressions - find every word except in tags
re.compile(r'&lt;[^&gt;]+&gt;').sub('', string).split()
