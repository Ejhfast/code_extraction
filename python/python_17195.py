# Printing an list with hex elements
&gt;&gt;&gt; a_list = range(4)
&gt;&gt;&gt; print '[{}]'.format(', '.join(hex(x) for x in a_list))
[0x0, 0x1, 0x2, 0x3]
