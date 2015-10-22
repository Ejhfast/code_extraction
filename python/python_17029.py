# Performing arithmetic operation on string list
&gt;&gt;&gt; s = 'a=(10100*10)+(-1289201*20)+(12312312*100)'
&gt;&gt;&gt; index = s.find('=') + 1
&gt;&gt;&gt; eval(s[index:])
