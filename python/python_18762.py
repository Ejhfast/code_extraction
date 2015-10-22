# Truncate a decimal value in Python
&gt;&gt; before_dec, after_dec = str(d).split('.')
&gt;&gt; float('.'.join((before_dec, after_dec[0:2])))
0.98
