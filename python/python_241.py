# get site name from a URL in python
&gt;&gt;&gt; from urllib.parse import urlparse
 &gt;&gt;&gt; urlparse('http://www.cwi.nl:80/%7Eguido/Python.html').hostname
 'www.cwi.nl'
