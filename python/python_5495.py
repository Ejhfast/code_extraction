# Encode file path properly using python
&gt;&gt;&gt; from urllib import pathname2url
&gt;&gt;&gt; pathname2url('foo, bar.mp3')
'foo%2C%20bar.mp3'
