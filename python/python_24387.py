# Python 3: list of 2 elements into dictionary
&gt;&gt;&gt; a = [('John', 'first@email.com'), ('John', 'second@email.com'), ('Jack', 'third@email.com')]
&gt;&gt;&gt; [dict([('sender', x[0]), ('email',x[1])]) for x in a]
[{'sender': 'John', 'email': 'first@email.com'}, {'sender': 'John', 'email': 'second@email.com'}, {'sender': 'Jack', 'email': 'third@email.com'}]
