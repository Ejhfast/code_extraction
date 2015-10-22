# List of open browser tabs programmatically
&gt;&gt;&gt; from appscript import *
&gt;&gt;&gt; map(lambda x: x.title(), app('Google Chrome').windows[0].tabs())
[u'Stack Overflow', u'Google']
