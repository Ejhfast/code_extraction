# how to replace specific word in a sentence with python
&gt;&gt;&gt; idx = s.find('hello') + len('hello')
&gt;&gt;&gt; s[:idx] + s[idx:].replace('hello', '')
'hello this is  stackoverflow '
