# How to interfere some text in a html link string in python
from BeautifulSoup import BeautifulSoup
soup = BeautifulSoup('&lt;a href="path/tomyhtml/foo.html"&gt;foo&lt;/a&gt;')
soup.a["title"] = "Some cool title"
