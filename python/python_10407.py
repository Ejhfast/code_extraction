# How to escape a pipe ( | ) symbol for url_encode in python
&gt;&gt;&gt; u = urlencode(params)
&gt;&gt;&gt; u.replace('%7C', '|')
'p=1+2+3+4+5%266&amp;l=ab|cd|ef'
