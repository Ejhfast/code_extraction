# How to split a multistring in python?
&gt;&gt;&gt; s = "the quick brown fox\x00jumped over the lazy\00programmer\00\00"
&gt;&gt;&gt; filter(None, s.split('\x00'))
['the quick brown fox', 'jumped over the lazy', 'programmer']
