# How to strip double spaces and leave new lines? Python
&gt;&gt;&gt; text = '   foo\nbar      spam'
&gt;&gt;&gt; '\n'.join(' '.join(line.split()) for line in text.split('\n'))
'foo\nbar spam'
