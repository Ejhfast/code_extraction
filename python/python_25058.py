# How does one print a Unicode character code in Python?
&gt;&gt;&gt; s = u'\u0103'
&gt;&gt;&gt; print s.encode('raw_unicode_escape')
\u0103
