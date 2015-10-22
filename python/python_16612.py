# Create a word replacement dictionary from list of tuples
&gt;&gt;&gt; word_dict = {'et': ['horse','dog'], 'ft': ['horses','dogs']}
&gt;&gt;&gt; dict(word_dict.values())
{'horses': 'dogs', 'horse': 'dog'}
