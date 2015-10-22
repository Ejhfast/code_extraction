# Reconstructing absolute urls from relative urls on a page
&gt;&gt;&gt; from urlparse import urljoin
&gt;&gt;&gt; urljoin('http://mysite.com/foo/bar/x.html', '../../images/img.png')
'http://mysite.com/images/img.png'
