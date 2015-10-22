# How can I make re.findall('a.*c', 'abcbc') match abc instead of abcbc
&gt;&gt;&gt; re.findall('a.*?c', 'abcbc')
['abc']
