# Python - converting wide-char strings from a binary file to Python unicode strings
&gt;&gt;&gt; data = 'S\x00e\x00r\x00i\x00e\x00s\x00'
&gt;&gt;&gt; data.decode('utf-16')
u'Series'
