# How to find the length of a leading sequence in a string?
&gt;&gt;&gt; F = lambda x:len(x)-len(x.lstrip(' '))
&gt;&gt;&gt; F(' ' * 5 + 'a')
5
