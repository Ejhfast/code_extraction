# Python Convert IP to octal adress
&gt;&gt;&gt; ip = '127.0.0.1'
&gt;&gt;&gt; print '.'.join(format(int(x), '04o') for x in ip.split('.'))
0177.0000.0000.0001
