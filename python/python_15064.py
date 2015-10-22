# How to find first instance of HTML comment starting with <!-- ? (Python)
itertools.ifilter(lambda x:x.startswith('&lt;!--'), open('test')).next()
