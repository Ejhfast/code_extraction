# How to convert unicode string like u'\\u4f60\\u4f60' to u'\u4f60\u4f60' in Python?
&gt;&gt;&gt; u'\\u4f60\\u4f60'.decode('unicode_escape')
u'\u4f60\u4f60'
