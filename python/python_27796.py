# Change order of elements in a list
&gt;&gt;&gt; [', '.join(reversed(name.split(', '))) for name in names]
['John, Snow', 'Ariya, Stark', 'Myrcella, Baratheon']
