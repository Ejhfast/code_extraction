# How to make a list to be a list in a list
&gt;&gt;&gt; a = ['NO YES NO NO', 'YES YES NO YES', 'NO NO YES NO', ]
&gt;&gt;&gt; [s.split() for s in a]
[['NO', 'YES', 'NO', 'NO'], ['YES', 'YES', 'NO', 'YES'], ['NO', 'NO', 'YES', 'NO']]
