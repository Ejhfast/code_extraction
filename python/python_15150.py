# How do you decode an ascii string in python?
&gt;&gt;&gt; a = rb"\x3cdiv\x3e"
&gt;&gt;&gt; a.decode('unicode_escape')
'&lt;div&gt;'
