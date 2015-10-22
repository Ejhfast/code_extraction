# Python Convert Unicode-Hex utf-8 strings to Unicode strings
&gt;&gt;&gt; s = u'Gaga\xe2\x80\x99s'
&gt;&gt;&gt; s.encode('latin-1').decode('utf8')
u'Gaga\u2019s'
