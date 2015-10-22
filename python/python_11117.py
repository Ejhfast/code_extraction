# Join a list of strings in python and wrap each string in quotation marks
&gt;&gt;&gt; words = ['hello', 'world', 'you', 'look', 'nice']
&gt;&gt;&gt; ', '.join('"{0}"'.format(w) for w in words)
'"hello", "world", "you", "look", "nice"'
