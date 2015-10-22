# How do you dynamically identify unknown delimiters in a data file?
&gt;&gt;&gt; l = "big long list of space separated words"
&gt;&gt;&gt; re.split(r'[ ,|;"]+', l)
['big', 'long', 'list', 'of', 'space', 'separated', 'words']
